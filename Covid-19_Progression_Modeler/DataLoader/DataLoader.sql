--Création de la base de donnée DataLoader
CREATE DATABASE IF NOT EXISTS `DataLoader`;

--Utilisation de la base de donnée DataLoader
USE `DataLoader`;

--Création de la table Communiques
CREATE TABLE IF NOT EXISTS `Communiques` (
  `id_communique` int(5) PRIMARY KEY,
  `date` varchar(50) DEFAULT "NULL",
  `nb_test` int(5) NOT NULL DEFAULT 0,
  `nb_nv_cas` int(5) NOT NULL DEFAULT 0,
  `nb_cas_contact` int(5) NOT NULL DEFAULT 0,
  `nb_cas_communautaire` int(5) NOT NULL DEFAULT 0,
  `nb_gueris` int(5) NOT NULL DEFAULT 0,
  `nb_deces` int(5) NOT NULL DEFAULT 0,
  `date_extraction`varchar(10)  DEFAULT NULL

);

--Création de la table Regions
CREATE TABLE IF NOT EXISTS `Regions` (
  `NomRegion` varchar(50) DEFAULT "NULL" PRIMARY KEY,
  `Nbre_Cas` int(5) NOT NULL DEFAULT 0
  
);

--Insertion de valeur dans la table Region
INSERT INTO `Regions` VALUES ("DAKAR",0);
INSERT INTO `Regions` VALUES ("DIOURBEL",0);
INSERT INTO `Regions` VALUES ("FATICK",0);
INSERT INTO `Regions` VALUES ("KEDOUGOU",0);
INSERT INTO `Regions` VALUES ("KAFFRINE",0);
INSERT INTO `Regions` VALUES ("KAOLACK",0);
INSERT INTO `Regions` VALUES ("KOLDA",0);
INSERT INTO `Regions` VALUES ("LOUGA",0);
INSERT INTO `Regions` VALUES ("MATAM",0);
INSERT INTO `Regions` VALUES ("SEDHIOU",0);
INSERT INTO `Regions` VALUES ("SAINT-LOUIS",0);
INSERT INTO `Regions` VALUES ("TAMBACOUNDA",0);
INSERT INTO `Regions` VALUES ("THIES",0);
INSERT INTO `Regions` VALUES ("ZIGUINCHOR",0);