INSERT INTO movie
(`Title`, `Plot`, `Year`, `Length`, `Director`, `BackgroundImage`,
`CoverImage`, `MainColor`)
VALUES 
("Bright", "Set in a world where fantasy creatures live side by side with humans. A human cop is forced to work with an Orc to find a weapon everyone is prepared to kill for.",
2017, 117, "David Ayer", 
"https://occ-0-2433-448.1.nflxso.net/art/cd5c9/3e192edf2027c536e25bb5d3b6ac93ced77cd5c9.jpg",
"https://movieplayer.net-cdn.it/t/images/2017/12/20/bright_jpg_191x283_crop_q85.jpg",
"#0d0d0c")

INSERT INTO `genre` (`Title`) VALUES ("Action");
INSERT INTO `genre` (`Title`) VALUES ("Crime");
INSERT INTO `genre` (`Title`) VALUES ("Fantasy");
INSERT INTO `genre` (`Title`) VALUES ("Aventure");
INSERT INTO `genre` (`Title`) VALUES ("Sci-Fy");

INSERT INTO `moviegenre` (`idMovie`, `idGenre`)
VALUES (1,1);

INSERT INTO `moviegenre` (`idMovie`, `idGenre`)
VALUES (1,2);

INSERT INTO `moviegenre` (`idMovie`, `idGenre`)
VALUES (1,3);
