USE mydb;

INSERT INTO categoria (nombre) VALUES ("Autos");
INSERT INTO categoria (nombre) VALUES ("Motos");
INSERT INTO categoria (nombre) VALUES ("Aereoplanos");
INSERT INTO categoria (nombre) VALUES ("Barcos");

INSERT INTO marca (nombre) VALUES ("Bugati");
INSERT INTO marca (nombre) VALUES ("Lamborghini");
INSERT INTO marca (nombre) VALUES ("Audi");

INSERT INTO producto 
(nombre, fechProduccion, precio, descripcion, idcategoria, idmarca)
VALUES
("Beyron Rojo", "2019-03-12", 100000.0, "Full Equipo", 1, 1);

INSERT INTO producto 
(nombre, fechProduccion, precio, descripcion, idcategoria, idmarca)
VALUES
("Aventador Negro", "2020-03-12", 140000.0, "Timon a la derecha", 1, 2);

INSERT INTO producto 
(nombre, fechProduccion, precio, descripcion, idcategoria, idmarca)
VALUES
("Audi R8 Blanco", "2021-03-12", 80000.0, "Full Equipo", 1, 3);



SELECT p.idproducto, p.nombre, p.precio, c.nombre AS categoria, m.nombre AS marca
FROM producto AS p
LEFT JOIN categoria AS c
ON p.idcategoria = c.idcategoria
LEFT JOIN marca as m
ON p.idmarca = m.idmarca


UPDATE mydb.categoria
SET nombre = "Embarcaciones"
WHERE idcategoria = 3;

DELETE FROM mydb.categoria
WHERE idcategoria = 3

INSERT INTO producto 
(nombre, fechProduccion, precio, descripcion, idcategoria)
VALUES
("Rolls Royce Phantom", "2021-03-12", 100000.0, "Full Equipo", 1);




