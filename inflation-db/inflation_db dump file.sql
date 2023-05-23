-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.7.31 - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             12.4.0.6659
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for inflation_db
CREATE DATABASE IF NOT EXISTS `inflation_db` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `inflation_db`;

-- Dumping structure for table inflation_db.analysis
CREATE TABLE IF NOT EXISTS `analysis` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) NOT NULL DEFAULT '0',
  `description` varchar(100) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

-- Dumping data for table inflation_db.analysis: 12 rows
/*!40000 ALTER TABLE `analysis` DISABLE KEYS */;
REPLACE INTO `analysis` (`id`, `date`, `description`) VALUES
	(1, '2018-May', 'Sample analysis description'),
	(2, '2018-Mar', 'Sample analysis 2'),
	(3, '2019-Mar', 'Sample Analysis 3'),
	(4, '2019-Jul', 'Sample Analysis 5'),
	(5, '2018-Dec', 'Sample Analysis 7'),
	(6, '2018-Nov', 'Sample analysis 9'),
	(7, '2018-Oct', 'Sample analysis 10'),
	(8, '2019-Oct', 'Sample analysis 11'),
	(9, '2019-Aug', 'Sample Analysis 12'),
	(10, '2019-Jun', 'Sample Analysis 13'),
	(11, '2018-Feb', 'Sample Analysis 115'),
	(12, '2018-Jun', 'Sample Analysis 116');
/*!40000 ALTER TABLE `analysis` ENABLE KEYS */;

-- Dumping structure for table inflation_db.cpi
CREATE TABLE IF NOT EXISTS `cpi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) DEFAULT NULL,
  `cpi` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

-- Dumping data for table inflation_db.cpi: 24 rows
/*!40000 ALTER TABLE `cpi` DISABLE KEYS */;
REPLACE INTO `cpi` (`id`, `date`, `cpi`) VALUES
	(1, '2018-Jan', '248.385774'),
	(2, '2018-Feb', '249.5152666'),
	(3, '2018-Mar', '249.6724188'),
	(4, '2018-Apr', '250.308381'),
	(5, '2018-May', '251.0600444'),
	(6, '2018-Jun', '251.6144154'),
	(7, '2018-Jul', '252.000842'),
	(8, '2018-Aug', '252.2923545'),
	(9, '2018-Sep', '252.8020806'),
	(10, '2018-Oct', '252.9980926'),
	(11, '2018-Nov', '253.1825478'),
	(12, '2018-Dec', '253.0806074'),
	(13, '2019-Jan', '252.8327514'),
	(14, '2019-Feb', '252.6120839'),
	(15, '2019-Mar', '253.1429956'),
	(16, '2019-Apr', '253.9957689'),
	(17, '2019-May', '254.7508031'),
	(18, '2019-Jun', '255.4311057'),
	(19, '2019-Jul', '255.8949236'),
	(20, '2019-Aug', '256.3054068'),
	(21, '2019-Sep', '256.5939942'),
	(22, '2019-Oct', '256.8563644'),
	(23, '2019-Nov', '257.1042863'),
	(24, '2019-Dec', '255.7682666');
/*!40000 ALTER TABLE `cpi` ENABLE KEYS */;

-- Dumping structure for table inflation_db.inflation
CREATE TABLE IF NOT EXISTS `inflation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) NOT NULL DEFAULT '0',
  `rate` varchar(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

-- Dumping data for table inflation_db.inflation: 24 rows
/*!40000 ALTER TABLE `inflation` DISABLE KEYS */;
REPLACE INTO `inflation` (`id`, `date`, `rate`) VALUES
	(1, '2018-Jan', '0.755'),
	(2, '2018-Feb', '0.454'),
	(3, '2018-Mar', '0.062'),
	(4, '2018-Apr', '0.254'),
	(5, '2018-May', '0.300'),
	(6, '2018-Jun', '0.220'),
	(7, '2018-Jul', '0.153'),
	(8, '2018-Aug', '0.115'),
	(9, '2018-Sep', '0.202'),
	(10, '2018-Oct', '0.077'),
	(11, '2018-Nov', '0.072'),
	(12, '2018-Dec', '-0.040'),
	(13, '2019-Jan', '-0.097'),
	(14, '2019-Feb', '-0.087'),
	(15, '2019-Mar', '0.210'),
	(16, '2019-Apr', '0.336'),
	(17, '2019-May', '0.297'),
	(18, '2019-Jun', '0.267'),
	(19, '2019-Jul', '0.181'),
	(20, '2019-Aug', '0.160'),
	(21, '2019-Sep', '0.112'),
	(22, '2019-Oct', '0.102'),
	(23, '2019-Nov', '0.096'),
	(24, '2019-Dec', '-0.519');
/*!40000 ALTER TABLE `inflation` ENABLE KEYS */;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
