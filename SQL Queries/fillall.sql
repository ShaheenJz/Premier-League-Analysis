DELETE FROM performance1994;

CREATE or REPLACE FUNCTION populate(teamname text)
RETURNS void AS $$

BEGIN
 
	INSERT INTO performance1994(team,home_wins, 
					    home_draws, home_losses, 
						home_gd, away_wins, away_draws,
						away_losses, away_gd)
						 
	SELECT
	teamname as team,
	count(*) filter(where home_team = teamname and winner = 'H') as home_wins,
	count(*) filter(where home_team = teamname and winner = 'D') as home_draws,
	count(*) filter(where home_team = teamname and winner = 'A') as home_losses,
	SUM(home_goals) FILTER (WHERE home_team = teamname) - SUM(away_goals) FILTER (WHERE home_team = teamname) AS home_gd,
	count(*) filter(where away_team = teamname and winner = 'A') as away_wins,
	count(*) filter(where away_team = teamname and winner = 'D') as away_draws,
	count(*) filter(where away_team = teamname and winner = 'H') as away_losses,
	SUM(away_goals) FILTER (WHERE away_team = teamname) - SUM(home_goals) FILTER (WHERE away_team = teamname) AS home_gd

	from match where season = 1994;

	RAISE NOTICE 'Data for team % inserted into performance1994', teamname;
					 
END;
$$ LANGUAGE plpgsql;

DO $$
DECLARE
teamname text;
team_cursor CURSOR FOR SELECT DISTINCT team FROM (select home_team as team FROM match WHERE season = 1994) AS teams;

BEGIN
	OPEN team_cursor;

	LOOP
		FETCH team_cursor INTO teamname;
		EXIT WHEN NOT FOUND;
		
		PERFORM populate(teamname);
	END LOOP;
	
CLOSE team_cursor;
END $$;
						
select * from performance1994 ORDER BY home_wins DESC;
