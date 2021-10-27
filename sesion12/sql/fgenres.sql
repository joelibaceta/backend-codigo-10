CREATE FUNCTION `fgenres`(id INT) 
    RETURNS varchar(100) CHARSET utf8mb3
    DETERMINISTIC
BEGIN
	DECLARE done INT DEFAULT FALSE;
	DECLARE str_genres VARCHAR(100) DEFAULT "";	
    DECLARE t_title VARCHAR(45);
    DECLARE gid INT;

	DECLARE cur_genres CURSOR FOR SELECT idGenre FROM moviegenre WHERE idMovie = id;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
	OPEN cur_genres;
    
    genres_loop: LOOP
		FETCH cur_genres INTO gid;
		IF done THEN
			LEAVE genres_loop;
		END IF;
		SELECT Title INTO t_title FROM genre WHERE idGenre = gid;
		SET str_genres = CONCAT(str_genres, " ", t_title);
    END LOOP;
    
	RETURN str_genres;
END