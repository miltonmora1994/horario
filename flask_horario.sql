-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: calendario_flask
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `asistencias`
--

DROP TABLE IF EXISTS `asistencias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `asistencias` (
  `id_asistencia` int NOT NULL AUTO_INCREMENT,
  `fecha_asistencia` date NOT NULL,
  `hora_inicio_asistencia` time NOT NULL,
  `hora_fin_asistencia` time NOT NULL,
  `espacio_id` int NOT NULL,
  PRIMARY KEY (`id_asistencia`),
  KEY `espacio_id_idx` (`espacio_id`),
  CONSTRAINT `espacio_id` FOREIGN KEY (`espacio_id`) REFERENCES `espacios` (`id_espacio`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asistencias`
--

LOCK TABLES `asistencias` WRITE;
/*!40000 ALTER TABLE `asistencias` DISABLE KEYS */;
INSERT INTO `asistencias` VALUES (1,'2021-04-29','03:20:00','04:20:00',1),(2,'2021-04-30','13:57:00','14:57:00',3),(4,'2021-05-01','11:34:00','11:35:00',5);
/*!40000 ALTER TABLE `asistencias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `asistencias_estudiantes`
--

DROP TABLE IF EXISTS `asistencias_estudiantes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `asistencias_estudiantes` (
  `id_asistencias_estudiantes` int NOT NULL AUTO_INCREMENT,
  `estudiante_id` int NOT NULL,
  `asistencia_id` int NOT NULL,
  `estudiante_asistencia` tinyint DEFAULT '0',
  PRIMARY KEY (`id_asistencias_estudiantes`),
  KEY `estudiante_id_idx` (`estudiante_id`),
  KEY `asistencia_id_idx` (`asistencia_id`),
  CONSTRAINT `asistencia_id` FOREIGN KEY (`asistencia_id`) REFERENCES `asistencias` (`id_asistencia`),
  CONSTRAINT `estudiante_id` FOREIGN KEY (`estudiante_id`) REFERENCES `estudiantes` (`id_estudiante`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asistencias_estudiantes`
--

LOCK TABLES `asistencias_estudiantes` WRITE;
/*!40000 ALTER TABLE `asistencias_estudiantes` DISABLE KEYS */;
INSERT INTO `asistencias_estudiantes` VALUES (11,9,2,1),(12,10,2,1),(13,11,2,1);
/*!40000 ALTER TABLE `asistencias_estudiantes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `espacios`
--

DROP TABLE IF EXISTS `espacios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `espacios` (
  `id_espacio` int NOT NULL AUTO_INCREMENT,
  `nombre_espacio` varchar(45) NOT NULL,
  `semestre_espacio` int NOT NULL,
  PRIMARY KEY (`id_espacio`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `espacios`
--

LOCK TABLES `espacios` WRITE;
/*!40000 ALTER TABLE `espacios` DISABLE KEYS */;
INSERT INTO `espacios` VALUES (1,'bases de datos 2',4),(3,'inteligencias artificial',1),(5,'ia',3),(7,'test',6);
/*!40000 ALTER TABLE `espacios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estudiantes`
--

DROP TABLE IF EXISTS `estudiantes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estudiantes` (
  `id_estudiante` int NOT NULL AUTO_INCREMENT,
  `identificacion_estudiante` varchar(45) NOT NULL,
  `nombres_estudiante` varchar(45) NOT NULL,
  `apellidos_estudiante` varchar(45) NOT NULL,
  `telefono_estudiante` int NOT NULL,
  `email_estudiante` varchar(45) NOT NULL,
  `semestre_estudiante` int NOT NULL,
  PRIMARY KEY (`id_estudiante`),
  UNIQUE KEY `identificacion_estudiante_UNIQUE` (`identificacion_estudiante`),
  UNIQUE KEY `email_estudiante_UNIQUE` (`email_estudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estudiantes`
--

LOCK TABLES `estudiantes` WRITE;
/*!40000 ALTER TABLE `estudiantes` DISABLE KEYS */;
INSERT INTO `estudiantes` VALUES (1,'123','pepito','perez',1213123890,'pepe@gmail',4),(6,'1234','luis','guzman',1234567890,'luis@mail.com',4),(8,'1','adriana','lopez',1000000001,'adriana@mail.com',1),(9,'2','amelia','ortiz',1000000002,'amelia@mail.com',1),(10,'12','alexander','burbano',1000000003,'alex@mail.com',1),(11,'21','viviana','aguilar',1000000004,'vivi@mail.com',1);
/*!40000 ALTER TABLE `estudiantes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-30 14:36:08
