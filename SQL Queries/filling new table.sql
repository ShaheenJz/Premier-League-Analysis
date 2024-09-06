INSERT INTO performance1993 (team, season, home_wins, 
						 home_draws, home_losses, 
						 home_gd, away_wins, away_draws,
						 away_losses, away_gd)
						 
Select 

'Arsenal' as team, 1993 as season, 
count(*) filter(where home_team = 'Arsenal' and winner = 'H') as home_wins,
count(*) filter(where home_team = 'Arsenal' and winner = 'D') as home_draws,
count(*) filter(where home_team = 'Arsenal' and winner = 'A') as home_losses,
SUM(home_goals) FILTER (WHERE home_team = 'Arsenal') - SUM(away_goals) FILTER (WHERE home_team = 'Arsenal') AS home_gd,
count(*) filter(where away_team = 'Arsenal' and winner = 'A') as away_wins,
count(*) filter(where away_team = 'Arsenal' and winner = 'D') as away_draws,
count(*) filter(where away_team = 'Arsenal' and winner = 'H') as away_losses,
SUM(away_goals) FILTER (WHERE away_team = 'Arsenal') - SUM(home_goals) FILTER (WHERE away_team = 'Arsenal') AS home_gd

from match where season = 1993;

select * from performance1993;
						 

