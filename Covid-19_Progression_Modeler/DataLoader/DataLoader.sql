
CREATE DATABASE IF NOT EXISTS `DataLoader` ;


USE `DataLoader`;

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

) engine=InnoDB;

CREATE TABLE IF NOT EXISTS `Regions` (
  `NomRegion` varchar(50) DEFAULT "NULL" PRIMARY KEY,
  `Nbre_Cas` int(5) NOT NULL DEFAULT 0,
  `id_regions` int NOT NULL
  
) engine=InnoDB;
INSERT INTO `Regions` VALUES ("DAKAR",0,5) ;
INSERT INTO `Regions` VALUES ("DIOURBEL",0,6) ;
INSERT INTO `Regions` VALUES ("FATICK",0,14) ;
INSERT INTO `Regions` VALUES ("KEDOUGOU",0,1) ;
INSERT INTO `Regions` VALUES ("KAFFRINE",0,13) ;
INSERT INTO `Regions` VALUES ("KAOLACK",0,3) ;
INSERT INTO `Regions` VALUES ("KOLDA",0,12) ;
INSERT INTO `Regions` VALUES ("LOUGA",0,7) ;
INSERT INTO `Regions` VALUES ("MATAM",0,8) ;
INSERT INTO `Regions` VALUES ("SEDHIOU",0,11) ;
INSERT INTO `Regions` VALUES ("SAINT-LOUIS",0,9) ;
INSERT INTO `Regions` VALUES ("TAMBACOUNDA",0,2) ;
INSERT INTO `Regions` VALUES ("THIES",0,4) ;
INSERT INTO `Regions` VALUES ("ZIGUINCHOR",0,10) ;

