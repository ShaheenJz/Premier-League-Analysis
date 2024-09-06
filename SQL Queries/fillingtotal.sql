DO $$
DECLARE
teamname text;
team_cursor CURSOR FOR SELECT DISTINCT home_team AS team FROM match;

BEGIN
OPEN team_cursor;

LOOP
        	FETCH team_cursor INTO teamname;
			
			--Condition for ending loop
        	EXIT WHEN NOT FOUND;
        
        	-- Call the populate function for the current team name
        	PERFORM filltotal(teamname);
    	
		END LOOP;
CLOSE team_cursor;

END;

$$ LANGUAGE plpgsql;
