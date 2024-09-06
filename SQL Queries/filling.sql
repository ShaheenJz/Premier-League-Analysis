CREATE OR REPLACE FUNCTION loopall(startyear INT, endyear INT)
RETURNS void AS $$


DECLARE
    teamname text;
	team_cursor CURSOR (y INT) FOR SELECT DISTINCT home_team AS team FROM match WHERE season = y;
	i int;
	
BEGIN
	-- Loop through start year to end year
	FOR i IN startyear..endyear LOOP 
    
		-- Open the cursor
    	OPEN team_cursor(i);
    	
    	-- Fetch each team name from the cursor and call the populate function
    	LOOP
        	FETCH team_cursor INTO teamname;
			
			--Condition for ending loop
        	EXIT WHEN NOT FOUND;
        
        	-- Call the populate function for the current team name
        	PERFORM populate(teamname, i);
    	
		END LOOP;
    
    	-- Close the cursor
    	CLOSE team_cursor;

--End year loop
	END LOOP;

END;

$$ LANGUAGE plpgsql;

--SELECT loopall(1994,2023);

--SELECT * FROM performance;
