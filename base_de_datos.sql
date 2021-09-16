-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 15-11-2020 a las 04:25:11
-- Versión del servidor: 5.7.31
-- Versión de PHP: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `flask`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

DROP TABLE IF EXISTS `categoria`;
CREATE TABLE IF NOT EXISTS `categoria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) COLLATE latin1_spanish_ci NOT NULL,
  `Descripcion` varchar(100) COLLATE latin1_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;


-- STORED PROCEDURES


-- CATEGORIAS
DELIMITER //
CREATE PROCEDURE sp_buscar_lista_categoria()
BEGIN
	SELECT * FROM categoria;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_buscar_categoria(IN id_cat INT)
BEGIN
	SELECT * FROM categoria
        WHERE id = id_cat;
END//
DELIMITER ;


DELIMITER //
CREATE PROCEDURE sp_insertar_categoria(OUT id_cat INT(11), 
        IN nombre varchar(50),
        descripcion varchar(100))
BEGIN
	INSERT INTO categoria VALUES(null, 
            nombre,
            descripcion);

    COMMIT;

    SELECT MAX(id) INTO id_cat
    FROM categoria;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_editar_categoria(IN id_cat INT(11), 
        nombre_cat varchar(50),
        descripcion_cat varchar(100))
BEGIN
	UPDATE categoria SET 
            nombre = nombre_cat,
            descripcion = descripcion_cat
        WHERE id = id_cat;

    COMMIT;
END//
DELIMITER ;


DELIMITER //
CREATE PROCEDURE sp_borrar_categoria(IN id_cat INT(11))
BEGIN
	DELETE FROM categoria WHERE id = id_cat;

    COMMIT;
END//
DELIMITER ;