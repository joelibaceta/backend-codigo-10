CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `movies`.`carterlera` AS
    SELECT 
        `movies`.`movie`.`idMovie` AS `idMovie`,
        `movies`.`movie`.`Title` AS `Title`,
        `movies`.`movie`.`Year` AS `Year`,
        `movies`.`movie`.`Length` AS `Length`,
        `movies`.`movie`.`Director` AS `Director`,
        `movies`.`movie`.`BackgroundImage` AS `BackgroundImage`,
        `movies`.`movie`.`CoverImage` AS `CoverImage`,
        `movies`.`movie`.`MainColor` AS `MainColor`,
        `movies`.`fgenres`(`movies`.`movie`.`idMovie`) AS `Genres`
    FROM
        `movies`.`movie`
    ORDER BY `movies`.`movie`.`Year` DESC , `movies`.`movie`.`Title`