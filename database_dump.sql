-- MySQL dump 10.13  Distrib 8.0.39, for Linux (x86_64)
--
-- Host: localhost    Database: mkenyaisaak
-- ------------------------------------------------------
-- Server version	8.0.39-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add booking',7,'add_booking'),(26,'Can change booking',7,'change_booking'),(27,'Can delete booking',7,'delete_booking'),(28,'Can view booking',7,'view_booking'),(29,'Can add event',8,'add_event'),(30,'Can change event',8,'change_event'),(31,'Can delete event',8,'delete_event'),(32,'Can view event',8,'view_event'),(33,'Can add ticket type',9,'add_tickettype'),(34,'Can change ticket type',9,'change_tickettype'),(35,'Can delete ticket type',9,'delete_tickettype'),(36,'Can view ticket type',9,'view_tickettype'),(37,'Can add ticket',10,'add_ticket'),(38,'Can change ticket',10,'change_ticket'),(39,'Can delete ticket',10,'delete_ticket'),(40,'Can view ticket',10,'view_ticket'),(41,'Can add social post',11,'add_socialpost'),(42,'Can change social post',11,'change_socialpost'),(43,'Can delete social post',11,'delete_socialpost'),(44,'Can view social post',11,'view_socialpost'),(45,'Can add Social Profile',12,'add_socialprofile'),(46,'Can change Social Profile',12,'change_socialprofile'),(47,'Can delete Social Profile',12,'delete_socialprofile'),(48,'Can view Social Profile',12,'view_socialprofile'),(49,'Can add Social Media Channel',13,'add_socialmediachannel'),(50,'Can change Social Media Channel',13,'change_socialmediachannel'),(51,'Can delete Social Media Channel',13,'delete_socialmediachannel'),(52,'Can view Social Media Channel',13,'view_socialmediachannel'),(53,'Can add performance',14,'add_performance'),(54,'Can change performance',14,'change_performance'),(55,'Can delete performance',14,'delete_performance'),(56,'Can view performance',14,'view_performance');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$1000000$vXmU7TWebKzu9QXSzcZWC9$o+lmb6O0VpUG3yMTWz9X50/ebRdqsrzu76OOq7U3k18=',NULL,1,'admin','','','admin@example.com',1,1,'2025-11-24 11:49:32.423252'),(2,'pbkdf2_sha256$1000000$FFqk5wdC9vAGTjCt7mmIaB$XrQ1otbFcN6BtCkq5Mx1iuPtw4RaY9c8QtdiJpHpqIU=','2026-01-13 15:28:16.564887',1,'christiano','','','christianokwena@gmail.com',1,1,'2025-11-24 11:53:08.382021'),(3,'pbkdf2_sha256$1000000$SKJClHtl5TuPX2FEiuvvi9$93OR0yQNVq/lJjlOAl6vr1m/ZtHiSRyXICpFlt8eg/8=','2025-12-13 10:24:52.258909',0,'mkenya','Mkenya','Isaak','nafeelkenya@gmail.com',1,1,'2025-12-13 10:06:45.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2025-11-24 12:55:28.365963','1','WAKENYAAA!',1,'[{\"added\": {}}]',8,2),(2,'2025-11-24 12:56:55.799127','1','WAKENYAAA!',2,'[{\"added\": {\"name\": \"ticket type\", \"object\": \"WAKENYAAA! - VIP\"}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"WAKENYAAA! - Family of 4\"}}]',8,2),(3,'2025-11-24 15:02:59.356486','1','YouTube - 2025-11-24',1,'[{\"added\": {}}]',11,2),(4,'2025-11-24 15:41:28.394605','1','WAKENYAAA!',2,'[{\"changed\": {\"fields\": [\"Payment till number\", \"Payment instructions\"]}}]',8,2),(5,'2025-11-24 15:43:57.938521','1','WAKENYAAA!',2,'[{\"changed\": {\"fields\": [\"Payment instructions\"]}}]',8,2),(6,'2025-11-28 19:03:22.696715','4','Facebook - https://web.facebook.com/seven7miIlion/?_rdc=1&_rdr',2,'[{\"changed\": {\"fields\": [\"Profile url\"]}}]',12,2),(7,'2025-11-28 19:04:06.819364','1','TikTok - https://www.tiktok.com/@mkenya7million',2,'[]',12,2),(8,'2025-11-28 19:04:43.581798','3','YouTube - https://www.youtube.com/@mkenya7million',2,'[{\"changed\": {\"fields\": [\"Profile url\"]}}]',12,2),(9,'2025-11-28 19:06:07.326235','2','TikTok - 2025-11-28',1,'[{\"added\": {}}]',11,2),(10,'2025-11-28 19:08:22.874689','2','TikTok - 2025-11-28',2,'[{\"changed\": {\"fields\": [\"Embed code\"]}}]',11,2),(11,'2025-11-28 19:12:26.274858','3','YouTube - 2025-11-28',1,'[{\"added\": {}}]',11,2),(12,'2025-11-28 19:36:18.758875','4','TikTok - 2025-11-28',1,'[{\"added\": {}}]',11,2),(13,'2025-11-28 19:47:43.988070','5','TikTok - 2025-11-28',1,'[{\"added\": {}}]',11,2),(14,'2025-11-28 19:51:21.305541','6','TikTok - 2025-11-28',1,'[{\"added\": {}}]',11,2),(15,'2025-11-28 19:52:45.934807','7','TikTok - 2025-11-28',1,'[{\"added\": {}}]',11,2),(16,'2025-11-28 20:08:04.099577','1','YouTube - 2025-11-24',3,'',11,2),(17,'2025-11-29 05:33:38.451218','1','WAKENYAAA!',2,'[{\"changed\": {\"fields\": [\"Description\"]}}]',8,2),(18,'2025-12-01 08:18:25.466571','1','WAKENYAAA!',2,'[{\"added\": {\"name\": \"ticket type\", \"object\": \"WAKENYAAA! - testing only\"}}]',8,2),(19,'2025-12-01 09:20:59.332573','1','WAKENYAAA!',2,'[{\"changed\": {\"fields\": [\"Notification email\"]}}]',8,2),(20,'2025-12-01 14:33:52.092656','1','WAKENYAAA!',2,'[{\"changed\": {\"fields\": [\"Poster\"]}}]',8,2),(21,'2025-12-01 14:34:14.122574','1','WAKENYAAA!',2,'[{\"deleted\": {\"name\": \"ticket type\", \"object\": \"WAKENYAAA! - testing only\"}}]',8,2),(22,'2025-12-01 14:34:38.828541','1','WAKENYAAA!',2,'[]',8,2),(23,'2025-12-01 14:36:36.959513','1','WAKENYAAA!',2,'[{\"changed\": {\"fields\": [\"Poster\"]}}]',8,2),(24,'2025-12-05 14:57:11.578379','8','TikTok - 2025-12-05',1,'[{\"added\": {}}]',11,2),(25,'2025-12-05 14:58:35.685062','8','TikTok - 2025-12-05',2,'[]',11,2),(26,'2025-12-05 14:58:43.112907','9','TikTok - 2025-12-05',1,'[{\"added\": {}}]',11,2),(27,'2025-12-05 14:59:11.129890','10','TikTok - 2025-12-05',1,'[{\"added\": {}}]',11,2),(28,'2025-12-05 15:01:24.776095','11','TikTok - 2025-12-05',1,'[{\"added\": {}}]',11,2),(29,'2025-12-13 10:06:45.613182','3','mkenya',1,'[{\"added\": {}}]',4,2),(30,'2025-12-13 10:08:09.904615','3','mkenya',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\", \"Staff status\"]}}]',4,2),(31,'2025-12-17 09:38:30.859078','12','TikTok - 2025-12-17',1,'[{\"added\": {}}]',11,2),(32,'2025-12-17 09:40:18.163114','13','TikTok - 2025-12-17',1,'[{\"added\": {}}]',11,2),(33,'2025-12-17 09:42:23.850279','14','TikTok - 2025-12-17',1,'[{\"added\": {}}]',11,2),(34,'2025-12-17 09:53:20.466801','14','TikTok - 2025-12-17',2,'[]',11,2);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'events','booking'),(8,'events','event'),(14,'events','performance'),(10,'events','ticket'),(9,'events','tickettype'),(6,'sessions','session'),(13,'socials','socialmediachannel'),(11,'socials','socialpost'),(12,'socials','socialprofile');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-11-24 11:48:43.993123'),(2,'auth','0001_initial','2025-11-24 11:48:49.773535'),(3,'admin','0001_initial','2025-11-24 11:48:51.212431'),(4,'admin','0002_logentry_remove_auto_add','2025-11-24 11:48:51.437126'),(5,'admin','0003_logentry_add_action_flag_choices','2025-11-24 11:48:51.669744'),(6,'contenttypes','0002_remove_content_type_name','2025-11-24 11:48:53.023581'),(7,'auth','0002_alter_permission_name_max_length','2025-11-24 11:48:53.520345'),(8,'auth','0003_alter_user_email_max_length','2025-11-24 11:48:53.969428'),(9,'auth','0004_alter_user_username_opts','2025-11-24 11:48:54.189507'),(10,'auth','0005_alter_user_last_login_null','2025-11-24 11:48:54.674268'),(11,'auth','0006_require_contenttypes_0002','2025-11-24 11:48:54.885457'),(12,'auth','0007_alter_validators_add_error_messages','2025-11-24 11:48:55.096401'),(13,'auth','0008_alter_user_username_max_length','2025-11-24 11:48:55.618514'),(14,'auth','0009_alter_user_last_name_max_length','2025-11-24 11:48:56.094473'),(15,'auth','0010_alter_group_name_max_length','2025-11-24 11:48:56.547490'),(16,'auth','0011_update_proxy_permissions','2025-11-24 11:48:57.637816'),(17,'auth','0012_alter_user_first_name_max_length','2025-11-24 11:48:58.442702'),(18,'events','0001_initial','2025-11-24 11:49:01.380733'),(19,'sessions','0001_initial','2025-11-24 11:49:02.264516'),(20,'socials','0001_initial','2025-11-24 11:49:02.730405'),(21,'events','0002_event_payment_account_number_and_more','2025-11-24 15:21:17.438333'),(22,'socials','0002_socialprofile_alter_socialpost_platform','2025-11-24 16:46:42.656771'),(23,'socials','0003_socialpost_embed_code','2025-11-28 17:41:20.233340'),(24,'socials','0004_socialpost_author_socialpost_comment_count_and_more','2025-11-28 19:45:26.197749'),(25,'socials','0005_alter_socialpost_embed_code','2025-11-28 19:50:52.014696'),(26,'socials','0006_socialmediachannel','2025-11-28 20:01:40.420384'),(27,'events','0003_booking_mpesa_receipt_number','2025-12-01 08:36:06.602445'),(28,'events','0004_event_notification_email','2025-12-01 08:48:34.280494'),(29,'events','0005_booking_mpesa_transaction_date','2025-12-01 10:31:57.118097'),(30,'events','0006_performance','2025-12-10 19:15:23.284158'),(31,'events','0007_performance_notes','2025-12-10 19:37:06.295575');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0s2z3apkhahyidv7koc8jxyuwo57yt0o','.eJxVjEEOwiAQAP-yZ0MWaFno0btvILBQqRpISnsy_t006UGvM5N5gw_7Vvze8-qXBBMouPyyGPiZ6yHSI9R7E9zqti5RHIk4bRe3lvLrerZ_gxJ6gQmITWCK1pFETRbHOTtmYu3IaXQJaVA5Sj0PWiqOkgidNmxotArZSPh8AcX7NpI:1vV2c4:jxCVQ4F7INxXT24sDfvosDRdM2iNjX-JWzceAmNstf4','2025-12-29 07:03:20.461302'),('14ghwnmxboacyjbev8we74b3pta8m1nf','.eJxVjEEOwiAQRe_C2pCBaRlw6d4zEBioVA0kpV0Z765NutDtf-_9l_BhW4vfel78nMRZaHH63WLgR647SPdQb01yq-syR7kr8qBdXlvKz8vh_h2U0Mu3JjaBKVpHCpAsjFN2zMToyCG4BDToHBVOAyrNURGBQ8OGRquBjRLvD8X7NpI:1vfgJU:29FgiUrocyqH2ur0tI5QKzKnvM6OCV2b_-it6H4uxNA','2026-01-27 15:28:08.419659'),('2vtyjfy139z30j3soube7hmvb8h2gr6l','.eJxVjEEOwiAQRe_C2pCBaRlw6d4zEBioVA0kpV0Z765NutDtf-_9l_BhW4vfel78nMRZaHH63WLgR647SPdQb01yq-syR7kr8qBdXlvKz8vh_h2U0Mu3JjaBKVpHCpAsjFN2zMToyCG4BDToHBVOAyrNURGBQ8OGRquBjRLvD8X7NpI:1vPzwk:ko_WBmOu-WQksWdyGmG7Moe4ojhLutr3wirCEaKHhTQ','2025-12-15 09:11:50.076952'),('5tqmr82yoj45ksp5j51lz87gk5a6ksvi','.eJxVjEEOwiAQAP-yZ0MWaFno0btvILBQqRpISnsy_t006UGvM5N5gw_7Vvze8-qXBBMouPyyGPiZ6yHSI9R7E9zqti5RHIk4bRe3lvLrerZ_gxJ6gQmITWCK1pFETRbHOTtmYu3IaXQJaVA5Sj0PWiqOkgidNmxotArZSPh8AcX7NpI:1vP3je:yKHnTXtTzYn-FZeNjFlzO2CFGRmrVmkxeNrGpXcf2Aw','2025-12-12 19:02:26.610524'),('6zba1o89c1khtydlkr763g6xl5y9cwti','.eJxVjEEOwiAQRe_C2pCBaRlw6d4zEBioVA0kpV0Z765NutDtf-_9l_BhW4vfel78nMRZaHH63WLgR647SPdQb01yq-syR7kr8qBdXlvKz8vh_h2U0Mu3JjaBKVpHCpAsjFN2zMToyCG4BDToHBVOAyrNURGBQ8OGRquBjRLvD8X7NpI:1vfgJc:JLOHDZfcW1pvocpeRVdAAWv__H46f-QBkMsJNUsQnTI','2026-01-27 15:28:16.570396'),('a9btbdj9scb4825h7qa4s9xusbejlskx','.eJxVjEEOwiAQAP-yZ0MWaFno0btvILBQqRpISnsy_t006UGvM5N5gw_7Vvze8-qXBBMouPyyGPiZ6yHSI9R7E9zqti5RHIk4bRe3lvLrerZ_gxJ6gQmITWCK1pFETRbHOTtmYu3IaXQJaVA5Sj0PWiqOkgidNmxotArZSPh8AcX7NpI:1vTQSJ:fol3NXORiK3A_Dn1juvbq65_oTKm7y3_eugDML2oY6c','2025-12-24 20:06:35.759310'),('dpavyq9tlxrvim9fo8irgpqevz4mlir6','.eJxVjEEOwiAQRe_C2pCBaRlw6d4zEBioVA0kpV0Z765NutDtf-_9l_BhW4vfel78nMRZaHH63WLgR647SPdQb01yq-syR7kr8qBdXlvKz8vh_h2U0Mu3JjaBKVpHCpAsjFN2zMToyCG4BDToHBVOAyrNURGBQ8OGRquBjRLvD8X7NpI:1vfgJZ:tZZglFzBdMBiAZWb8hyJHdyHYrY_TtYhgC2vshLiquE','2026-01-27 15:28:13.486051'),('gdsd0gg8ez6r5g3cwbbvvvh79utcgll5','.eJxVjEEOwiAQRe_C2hAHygAu3fcMhOmAVA0kpV0Z765NutDtf-_9lwhxW0vYelrCzOIitDj9bhSnR6o74HustyanVtdlJrkr8qBdjo3T83q4fwcl9vKtVTLJANhMxiNbpgE1M3hF7owQPfpMGi1nBOMIfHYO3WCAk49gSIn3B9fGN2M:1vUMo0:-NSt6SUT1GckF-68JCtw84J9xqVx0_Td0ZYIuHkSiMY','2025-12-27 10:24:52.264090'),('hq978qnliqrddyoemzmxw02235kx1ur3','.eJxVjEEOwiAQRe_C2pCBaRlw6d4zEBioVA0kpV0Z765NutDtf-_9l_BhW4vfel78nMRZaHH63WLgR647SPdQb01yq-syR7kr8qBdXlvKz8vh_h2U0Mu3JjaBKVpHCpAsjFN2zMToyCG4BDToHBVOAyrNURGBQ8OGRquBjRLvD8X7NpI:1vV1vu:HWQemHQmwM2ygodpL-ogg0umulv7-DCWEaPArKodbaw','2025-12-29 06:19:46.370382'),('jwe7xc3rq857qofy6nkabai5xl2mp93c','.eJxVjEEOwiAQAP-yZ0MWaFno0btvILBQqRpISnsy_t006UGvM5N5gw_7Vvze8-qXBBMouPyyGPiZ6yHSI9R7E9zqti5RHIk4bRe3lvLrerZ_gxJ6gQmITWCK1pFETRbHOTtmYu3IaXQJaVA5Sj0PWiqOkgidNmxotArZSPh8AcX7NpI:1vTQJv:eIx8ulNWsLed5FbGlHo_ocQ4GcjskfohyF_wGH9gaew','2025-12-24 19:57:55.215845'),('m2r0wikb83n5jrjqe2qbjbmpcrhokaan','.eJxVjEEOwiAQRe_C2pCBaRlw6d4zEBioVA0kpV0Z765NutDtf-_9l_BhW4vfel78nMRZaHH63WLgR647SPdQb01yq-syR7kr8qBdXlvKz8vh_h2U0Mu3JjaBKVpHCpAsjFN2zMToyCG4BDToHBVOAyrNURGBQ8OGRquBjRLvD8X7NpI:1vfgIS:JfNP8L8SqVKLcghA7ZT5-_v7ztpk7lyCpF48ZsL2ejo','2026-01-27 15:27:04.133781'),('p8p91ed8abx3ilwm8m4glrmw6qys34o2','.eJxVjEEOwiAQRe_C2pCBaRlw6d4zEBioVA0kpV0Z765NutDtf-_9l_BhW4vfel78nMRZaHH63WLgR647SPdQb01yq-syR7kr8qBdXlvKz8vh_h2U0Mu3JjaBKVpHCpAsjFN2zMToyCG4BDToHBVOAyrNURGBQ8OGRquBjRLvD8X7NpI:1vfgJE:qOqnfhFBL2bI7lAOxeYmB3AuGoS5hs21GQac65jWxK0','2026-01-27 15:27:52.275326'),('qsca5miwulvw3d2dg0kerxcuidxos5nq','.eJxVjEEOwiAQRe_C2pCBaRlw6d4zEBioVA0kpV0Z765NutDtf-_9l_BhW4vfel78nMRZaHH63WLgR647SPdQb01yq-syR7kr8qBdXlvKz8vh_h2U0Mu3JjaBKVpHCpAsjFN2zMToyCG4BDToHBVOAyrNURGBQ8OGRquBjRLvD8X7NpI:1vNYzk:0mUkEdpvKJyyYcSeZJ9pkthwjUHgTAhIZP_iCOpSnGQ','2025-12-08 16:00:52.546620'),('tu9ws0m2busl1m4jpf6vleun4jtc8dqr','.eJxVjEEOwiAQRe_C2pCBaRlw6d4zEBioVA0kpV0Z765NutDtf-_9l_BhW4vfel78nMRZaHH63WLgR647SPdQb01yq-syR7kr8qBdXlvKz8vh_h2U0Mu3JjaBKVpHCpAsjFN2zMToyCG4BDToHBVOAyrNURGBQ8OGRquBjRLvD8X7NpI:1vfgJX:B5U83flPVRcZvXzzC0eatgU6CT9IJhQF_wslST4dZH0','2026-01-27 15:28:11.209137'),('tyrj6k0h3j10oxmczjkwcza194w3rsd5','.eJxVjEEOwiAQRe_C2pCBaRlw6d4zEBioVA0kpV0Z765NutDtf-_9l_BhW4vfel78nMRZaHH63WLgR647SPdQb01yq-syR7kr8qBdXlvKz8vh_h2U0Mu3JjaBKVpHCpAsjFN2zMToyCG4BDToHBVOAyrNURGBQ8OGRquBjRLvD8X7NpI:1vVivx:-E9h0Hj76lkV8Jdcikuon6x2HVHlp0sQ1fGwk5s3LCU','2025-12-31 04:14:41.187541'),('v7wqjkvlhhmvklfabh6rskjbyffxmnmm','.eJxVjEEOwiAQRe_C2pCBaRlw6d4zEBioVA0kpV0Z765NutDtf-_9l_BhW4vfel78nMRZaHH63WLgR647SPdQb01yq-syR7kr8qBdXlvKz8vh_h2U0Mu3JjaBKVpHCpAsjFN2zMToyCG4BDToHBVOAyrNURGBQ8OGRquBjRLvD8X7NpI:1vfgJY:3oe6onGzpaiXDRh-U0HzbHiwL2dkV1F1jA0trPX-DaM','2026-01-27 15:28:12.619421'),('vz2qw6ht1a2woyjfimr56b7udaxw67y9','.eJxVjEEOwiAQAP-yZ0MWaFno0btvILBQqRpISnsy_t006UGvM5N5gw_7Vvze8-qXBBMouPyyGPiZ6yHSI9R7E9zqti5RHIk4bRe3lvLrerZ_gxJ6gQmITWCK1pFETRbHOTtmYu3IaXQJaVA5Sj0PWiqOkgidNmxotArZSPh8AcX7NpI:1vNW3V:XU-V6j67L_F3G1jj-LI3PwPwArSw5-eX_unb9-iKntU','2025-12-08 12:52:33.302831'),('zwj0n3txn628fpqthbvvvjo57g2mb2zw','.eJxVjEEOwiAQRe_C2pCBaRlw6d4zEBioVA0kpV0Z765NutDtf-_9l_BhW4vfel78nMRZaHH63WLgR647SPdQb01yq-syR7kr8qBdXlvKz8vh_h2U0Mu3JjaBKVpHCpAsjFN2zMToyCG4BDToHBVOAyrNURGBQ8OGRquBjRLvD8X7NpI:1vRXDz:FpG45JRle7sCG4EQAQRYxlbxBktVxp2Kcm9wlWYgfdM','2025-12-19 14:55:59.330390');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `events_booking`
--

DROP TABLE IF EXISTS `events_booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `events_booking` (
  `id` char(32) NOT NULL,
  `customer_name` varchar(200) DEFAULT NULL,
  `customer_email` varchar(254) DEFAULT NULL,
  `customer_phone` varchar(20) NOT NULL,
  `total_amount` decimal(10,2) NOT NULL,
  `payment_status` varchar(20) NOT NULL,
  `payment_reference` varchar(100) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `mpesa_receipt_number` varchar(100) DEFAULT NULL,
  `mpesa_transaction_date` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events_booking`
--

LOCK TABLES `events_booking` WRITE;
/*!40000 ALTER TABLE `events_booking` DISABLE KEYS */;
INSERT INTO `events_booking` VALUES ('048033b79f654e3897e08b46b0fabbd1','Mark Simiyu','nyongesamarks@gmail.com','0712949307',4000.00,'FAILED','ws_CO_08122025174421217712949307','2025-12-08 14:44:19.988814','2025-12-08 14:44:50.132696',NULL,NULL),('0579dd776cb040d4b6b2c461c4813a59','Isaac Ongere','anyoloisaac35@gmail.com','0791258513',1000.00,'PENDING',NULL,'2025-11-24 16:12:38.723814','2025-11-24 16:12:38.723878',NULL,NULL),('079386fa3a9945c1a81cd62bf0e84090','Elkanah','onyakwama@gmail.com','0721986074',1000.00,'FAILED','ws_CO_02122025191954253721986074','2025-12-02 16:19:52.981469','2025-12-02 16:20:04.587903',NULL,NULL),('07a80967d79741bfb9a4adecf06c6192','Isaac Ongere','anyoloisaac35@gmail.com','0791258513',1000.00,'PENDING',NULL,'2025-11-24 16:08:59.244695','2025-11-24 16:08:59.244736',NULL,NULL),('0870ab6ae25646e9bf14ef307e786c66','Dominic Orina','orinadominic21@gmail.com','0707407160',40000.00,'FAILED','ws_CO_12122025210127462707407160','2025-12-12 18:01:25.693296','2025-12-12 18:01:30.937746',NULL,NULL),('0eef88e8c6434c5dac0189f0efbd9e32','ISAAC SICHEI','','0798149948',5.00,'PAID','ws_CO_01122025124551317798149948','2025-12-01 09:45:49.411993','2025-12-01 09:46:06.715463',NULL,NULL),('1530f0f2fb344f1baa112bcc9beb284f','Peter Wafula','pnyaranga@gmail.com','0715434417',5000.00,'PAID','ws_CO_15122025100246002715434417','2025-12-15 07:02:44.430926','2025-12-15 07:03:06.070571','TLF3S146IT','20251215100305'),('1c1268a1d4ef4e40ab17df424d025121','Beldina','bellah2namisi@gmail.com','0769581816',1000.00,'PENDING',NULL,'2025-11-29 09:59:21.430540','2025-11-29 09:59:21.430691',NULL,NULL),('22075fef910e49c5a1458307410a1493','Wycliffe Nyaosi','','+254717955093',2000.00,'FAILED','ws_CO_19122025101434061717955093','2025-12-19 07:14:33.250098','2025-12-19 07:14:52.815835',NULL,NULL),('27bb4f46c76a47e289a5c54babaa2407','Mutamaywa','','0719114173',40000.00,'FAILED','ws_CO_04122025134008864719114173','2025-12-04 10:40:06.723794','2025-12-04 10:40:15.504001',NULL,NULL),('2d07fae86b08408582c8ef1108f3cabb','Newton kulundu','','0792585422',1000.00,'FAILED','ws_CO_08122025140853382792585422','2025-12-08 11:08:51.420751','2025-12-08 11:09:10.922622',NULL,NULL),('2d9538747e524e33929f999c8d4344e1','Moses Kibonei','','0722144559',1000.00,'PAID','ws_CO_15122025094514892722144559','2025-12-15 06:45:12.504657','2025-12-15 06:45:26.142814','TLF39158UU','20251215094525'),('3502c56ad31e43318ed10eecb4fa0705','Hillary muyip','','0748381552',5000.00,'FAILED','ws_CO_10122025041530613748381552','2025-12-10 01:15:28.634989','2025-12-10 01:15:41.193141',NULL,NULL),('3512b6dab0ee48158e087ad00cca8d0c','Natalie Iyadi','','0112967333',1000.00,'PAID','ws_CO_19122025105211963112967333','2025-12-19 07:52:10.094334','2025-12-19 07:52:22.880580','TLJ7T1DWYC','20251219105221'),('3dce2d850407483581575345cae2c527','Ezra Keter','','0712690459',1000.00,'FAILED','ws_CO_06122025103454830712690459','2025-12-06 07:34:52.754057','2025-12-06 07:35:05.614029',NULL,NULL),('3e3ee31b3d3b4f3aa0b99dbde7c8586b','MOOGI DUKE','mariariamoogi@gmail.com','0705953716',1000.00,'FAILED','ws_CO_04122025222458580705953716','2025-12-04 19:24:56.896686','2025-12-04 19:25:10.481668',NULL,NULL),('4a52a61d06364ebd82963229291bf9ca','','','0792340223',1000.00,'PENDING',NULL,'2025-11-30 08:59:19.771080','2025-11-30 08:59:19.771170',NULL,NULL),('4aee465898e44f99bb7bd8950e92976b','','','0722243459',10000.00,'PENDING',NULL,'2025-11-24 15:32:17.180388','2025-11-24 15:32:17.180452',NULL,NULL),('5199fb1a04fb4e8196151df7d3642b26','','','0722243459',5.00,'PAID','ws_CO_01122025113823622722243459','2025-12-01 08:38:21.411555','2025-12-01 08:38:35.424450',NULL,NULL),('526f370deb8044b0b6830718a5608eed','victor','','0713068665',1000.00,'FAILED','ws_CO_13012026173636067713068665','2026-01-13 14:36:35.199930','2026-01-13 14:36:48.469856',NULL,NULL),('575df03784d749a79ea702a603f1315e','Catalan jason','kibet1339@gmail.com','0745283412',6000.00,'PENDING','ws_CO_13122025094730765745283412','2025-12-13 06:47:28.692317','2025-12-13 06:47:31.095938',NULL,NULL),('57cd2da2e6ee479ba73b33b28edc9b83','Hillary Chewen','hillarychewen@gmail.com','0724845059',1000.00,'FAILED','ws_CO_04122025183027089724845059','2025-12-04 15:30:26.270620','2025-12-04 15:30:38.716652',NULL,NULL),('5aef5c114d154ea49745405bfaa19e83','Isaac Ongere','anyoloisaac35@gmail.com','0791258513',1000.00,'FAILED','ws_CO_09122025182057815791258513','2025-12-09 15:20:55.961740','2025-12-09 15:21:26.098627',NULL,NULL),('647297be0f194817b34c7aabd1b9b035','','','0798149948',1000.00,'PENDING',NULL,'2025-11-28 14:01:34.569787','2025-11-28 14:01:34.569908',NULL,NULL),('64b8c2c0a72042de9e16d514b5d59ee5','kris','','0722243459',5.00,'PAID','ws_CO_01122025132021648722243459','2025-12-01 10:20:20.066726','2025-12-01 10:20:36.700216',NULL,NULL),('69fc92eec4cf497d84629012506ca291','Susan achieng okoth','suzyachie@gmail.com','0725610518',7000.00,'PAID','ws_CO_18122025100134701725610518','2025-12-18 07:01:32.238849','2025-12-18 07:01:49.403154','TLION1GBZ5','20251218100148'),('6bcf658a12994ac7957efbd9d0c77f6c','Isaac Ongere','anyoloisaac35@gmail.com','0791258513',1000.00,'FAILED','ws_CO_01122025223452241791258513','2025-12-01 19:34:51.081242','2025-12-01 19:35:11.737343',NULL,NULL),('6cc0ab143d41431bb32a70df4ddc091e','ISAAC SICHEI','mkenyasevenmillion@gmail.com','0798149948',5.00,'PAID','ws_CO_01122025163655650798149948','2025-12-01 13:36:54.219674','2025-12-01 13:37:05.454298','TL12JBRX0F','20251201163704'),('70fa27f6df2d4a60b7e560a17e698497','Denis Mwangi muhoro','dennismuhoro11@gmail.com','0757286782',1000.00,'FAILED','ws_CO_04122025151236419757286782','2025-12-04 12:12:34.681121','2025-12-04 12:12:55.115144',NULL,NULL),('7404a5806300489fb2cb1825edccf95e','Mutamaywa','','0719114173',40000.00,'FAILED','ws_CO_04122025133953218719114173','2025-12-04 10:39:51.702449','2025-12-04 10:40:03.416396',NULL,NULL),('7bc51c117ed9478580783b4927d79c0b','Wycliffe Nyatika','nyaosi2012@gmail.com','0717955093',2000.00,'PAID','ws_CO_20122025080439517717955093','2025-12-20 05:04:37.601995','2025-12-20 05:04:48.961597','TLKKX1MKWU','20251220080448'),('7cf49c3684df44d58e3a6bd7b085df98','ISAAC SICHEI','','0798149948',5.00,'PAID','ws_CO_01122025162949500798149948','2025-12-01 13:29:48.159090','2025-12-01 13:30:03.172357','TL12JBRWVN','20251201163002'),('80daf0540360403a81c6598f81bebc1b','Amos Kiplagat','','0727320793',25.00,'FAILED','ws_CO_01122025163305981727320793','2025-12-01 13:33:04.432639','2025-12-01 13:33:20.865152',NULL,NULL),('8192f92cf1054c7897380add40605782','Allan kiprono','kipchumbaa8@gmail.com','0724437029',1000.00,'PAID','ws_CO_08122025223623968724437029','2025-12-08 19:36:21.904932','2025-12-08 19:36:47.852870','TL8150GL75','20251208223637'),('86959793e2d6461cb8e8d309c7e48dbd','christiano','','0722243459',9000.00,'FAILED','ws_CO_02122025111433632722243459','2025-12-02 08:14:31.803739','2025-12-02 08:14:56.318979',NULL,NULL),('878677bc191a489b841b4e6102b99612','kris','','0712345678',4000.00,'PENDING',NULL,'2025-11-24 15:25:03.244160','2025-11-24 15:25:03.244227',NULL,NULL),('87d9ed88f8e34684a53e3e2b5b80f390','Nelson 6','ndiwanelson@gmail.com','0723417771',4000.00,'FAILED','ws_CO_09122025075252528723417771','2025-12-09 04:52:50.496694','2025-12-09 04:53:05.255360',NULL,NULL),('8dfffd180a8540188b9a0e35b54a6342','Victor','kiragavavictor@gmail.com','0793534053',1000.00,'FAILED','ws_CO_05122025161231588793534053','2025-12-05 13:12:29.459254','2025-12-05 13:12:45.698478',NULL,NULL),('8ec7c6ae36f14bcdacc4b593073a2230','Kk','','0736572685',40000.00,'FAILED','ws_CO_08122025075844160736572685','2025-12-08 04:58:43.066146','2025-12-08 04:58:50.630431',NULL,NULL),('93b92f7906734d15b99be314f3877a4e','','','0723013325',1000.00,'PENDING',NULL,'2025-11-24 16:08:15.791067','2025-11-24 16:08:15.791153',NULL,NULL),('9ac44b6abc9644edb1d82afc9cee97d0','Brinton burare sokoli','brintonsokoli178@gmail.com','0745090917',1000.00,'PAID','ws_CO_07122025082639514745090917','2025-12-07 05:26:37.869787','2025-12-07 05:27:07.155886','TL74E0GSUC','20251207082701'),('9e87dbfe07cc4d1f8bd3cb1a67c12277','Amos Amdany','dobnet11@gmail.com','+254726895631',3000.00,'FAILED','ws_CO_09122025112932169726895631','2025-12-09 08:29:30.946023','2025-12-09 08:29:42.069256',NULL,NULL),('9e974cc7250f431895bfba870b6b5853','Allan kiprono','kipchumbaa8@gmail.com','0724437029',1000.00,'FAILED','ws_CO_08122025223626888724437029','2025-12-08 19:36:24.900734','2025-12-08 19:36:29.984446',NULL,NULL),('a3ca9957622f400ea1f5405f87a52625','Christiano kwena','','0722243459',5.00,'PAID','ws_CO_01122025162905051722243459','2025-12-01 13:29:03.761946','2025-12-01 13:29:18.852947','TL1OKBPYR3','20251201162918'),('a4f140d4c942440daeebd9ef7ed1dfb3','Ian muge simiyu','Iansimiyu490@gmail.com','0748410659',10000.00,'FAILED','ws_CO_02122025141110658748410659','2025-12-02 11:11:08.867758','2025-12-02 11:11:24.863991',NULL,NULL),('a8daf121416f4df39ff9a925b1a44119','Christiano','','0722243459',5.00,'PENDING','ws_CO_01122025111850171722243459','2025-12-01 08:18:49.030007','2025-12-01 08:18:51.553478',NULL,NULL),('accf19c8e9d74d56bc5fe45a139f3b31','','','0798149948',1000.00,'PENDING',NULL,'2025-11-24 16:14:39.565585','2025-11-24 16:14:39.565878',NULL,NULL),('acef42bd6d0e46e1a4347cddbc3fe7fc','Kitunguru kevin','','0726128079',10.00,'PAID','ws_CO_01122025163000464726128079','2025-12-01 13:29:58.532187','2025-12-01 13:30:24.347741','TL1BBBO58S','20251201163023'),('ae69403ee07b444aacbed058ff979b1d','ONESS DAKTARI','ookothokumu@yahoo.com','0725662159',7000.00,'FAILED','ws_CO_17122025173655483725662159','2025-12-17 14:36:53.471489','2025-12-17 14:36:58.610121',NULL,NULL),('af951aeac32449fb9858e934df7b7c53','christiano kwena','christianokwena@gmail.com','0722243459',5.00,'PAID','ws_CO_01122025161744115722243459','2025-12-01 13:17:43.240025','2025-12-01 13:17:54.644819','TL1OKBPVMJ','20251201161753'),('bd31990fafdf48e3bd7ab67006b31ad8','christiano','','0722243459',5.00,'PAID','ws_CO_01122025120842202722243459','2025-12-01 09:08:41.347686','2025-12-01 09:08:55.120566',NULL,NULL),('c047aae1f1af47128036d2b1ce2f7f6d','Suleiman Simiyu','','0796683342',1000.00,'FAILED','ws_CO_11122025071124366796683342','2025-12-11 04:11:23.462524','2025-12-11 04:11:28.131697',NULL,NULL),('c1c708b63df943409e4dc9659bd8c5b0','','','0798149948',1000.00,'PENDING',NULL,'2025-11-29 09:58:12.695885','2025-11-29 09:58:12.695955',NULL,NULL),('c29ec0f261d24766b995ad06fcf4f199','Hillary muyip','','0748381552',35000.00,'FAILED','ws_CO_10122025041549752748381552','2025-12-10 01:15:47.953873','2025-12-10 01:15:57.368625',NULL,NULL),('c2f672f39516455c813ddd219e537eba','','','0722243459',13000.00,'PENDING',NULL,'2025-11-24 15:38:09.553988','2025-11-24 15:38:09.554094',NULL,NULL),('c40fac48f8904aad97953cd0ededf7eb','Filson Engineering Services','tonnykiptoh8@gmail.com','0798309636',1000.00,'FAILED','ws_CO_13122025082105706798309636','2025-12-13 05:21:03.705870','2025-12-13 05:21:33.606805',NULL,NULL),('c4bd0f5bc54548f29de8bd7d62e5dea4','Walter','ulumawalter@gmail.com','0702257335',40000.00,'FAILED','ws_CO_10122025222547297702257335','2025-12-10 19:25:46.360850','2025-12-10 19:26:03.089384',NULL,NULL),('c73ac4aa477a40f7979f1f973cddb58c','Stephen Biki','kimutaibiki@gmail.com','+254727402384',2000.00,'FAILED','ws_CO_04122025134919424727402384','2025-12-04 10:49:17.813864','2025-12-04 10:49:29.374057',NULL,NULL),('cf29a78914134bba88936da0cb9ba09d','Nelson 6','ndiwanelson@gmail.com','0723417771',4000.00,'FAILED','ws_CO_09122025075308480723417771','2025-12-09 04:53:06.995460','2025-12-09 04:53:18.521872',NULL,NULL),('d35cfb0d856d4ab7b5d6798c5b5da4e7','Chris','','0722243459',2000.00,'FAILED','ws_CO_15122025132114307722243459','2025-12-15 10:21:13.025547','2025-12-15 10:21:43.700359',NULL,NULL),('d37bf9c3400a4418bc2d7060f5eadfb8','LABAN','','0743799931',12000.00,'FAILED','ws_CO_04122025131740042743799931','2025-12-04 10:17:38.663883','2025-12-04 10:17:54.479765',NULL,NULL),('d511410dd79944298ea270c38edaf1da','Nyatika','nyaosi2012@gmail.com','0706609916',1000.00,'FAILED','ws_CO_12122025223526392706609916','2025-12-12 19:35:25.168566','2025-12-12 19:35:30.814450',NULL,NULL),('d6780895370f41b49b506ec06972ebf8','Aristurchus','johnmusieve@gmail.com','0703571967',1000.00,'FAILED','ws_CO_18122025113018502703571967','2025-12-18 08:30:16.932968','2025-12-18 08:30:30.883752',NULL,NULL),('e700b666362b49698991e51281e72f44','christiano kwena','christianokwena@gmail.com','0722243459',5.00,'PAID','ws_CO_01122025141333519722243459','2025-12-01 11:13:31.682758','2025-12-01 12:13:40.536206','TL1OKBPHJR','20251201141343'),('e9f53e5543114ddb8da2b27bbcb2c03f','','','0722243459',1000.00,'PENDING',NULL,'2025-11-24 15:39:45.112853','2025-11-24 15:39:45.112892',NULL,NULL),('f161413577c74a0283e743c8b210bb00','Catalan jason','kibet1339@gmail.com','0745283412',6000.00,'FAILED','ws_CO_13122025094733073745283412','2025-12-13 06:47:31.519336','2025-12-13 06:47:36.299676',NULL,NULL),('f882891388c94889adc84d5652ddb539','Christiano','christianokwena@gmail.com','0722243459',5.00,'PAID','ws_CO_01122025122239589722243459','2025-12-01 09:22:38.004846','2025-12-01 09:22:57.931126',NULL,NULL),('fe788345713340a7bdd6a93dae05b52d','Isaac Ongere','anyoloisaac35@gmail.com','0791258513',1000.00,'PENDING',NULL,'2025-11-24 16:11:54.571896','2025-11-24 16:11:54.571946',NULL,NULL);
/*!40000 ALTER TABLE `events_booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `events_event`
--

DROP TABLE IF EXISTS `events_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `events_event` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `poster` varchar(100) NOT NULL,
  `date` datetime(6) NOT NULL,
  `venue` varchar(200) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `marketing_qr_code` varchar(100) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `payment_account_number` varchar(50) DEFAULT NULL,
  `payment_instructions` longtext,
  `payment_till_number` varchar(20) DEFAULT NULL,
  `notification_email` varchar(254) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events_event`
--

LOCK TABLES `events_event` WRITE;
/*!40000 ALTER TABLE `events_event` DISABLE KEYS */;
INSERT INTO `events_event` VALUES (1,'WAKENYAAA!','13 years of clean content experience. \r\n2000 Kenyans.\r\nONE venue.\r\nGates open 10am , Show starts 2pm.','event_posters/poster_new_vSf2YNp.jpeg','2025-12-20 10:00:00.000000','Kitale School',1,'','2025-11-24 12:55:28.150520','2025-12-01 14:36:36.956572',NULL,'mPesa Till name: Nafeel Kenya','5692342','christianokwena@gmail.com');
/*!40000 ALTER TABLE `events_event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `events_performance`
--

DROP TABLE IF EXISTS `events_performance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `events_performance` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `category` varchar(20) NOT NULL,
  `number_of_performers` int unsigned NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `event_id` bigint NOT NULL,
  `notes` longtext,
  PRIMARY KEY (`id`),
  KEY `events_performance_event_id_a4e03d97_fk_events_event_id` (`event_id`),
  CONSTRAINT `events_performance_event_id_a4e03d97_fk_events_event_id` FOREIGN KEY (`event_id`) REFERENCES `events_event` (`id`),
  CONSTRAINT `events_performance_chk_1` CHECK ((`number_of_performers` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events_performance`
--

LOCK TABLES `events_performance` WRITE;
/*!40000 ALTER TABLE `events_performance` DISABLE KEYS */;
INSERT INTO `events_performance` VALUES (1,'anon','COMEDY',3,'0833324389','2025-12-10 19:42:09.333628','2025-12-10 19:42:09.333697',1,'none'),(2,'Mode de hyper','DANCE',1,'0106097124','2025-12-11 11:33:50.156147','2025-12-11 11:33:50.156214',1,''),(3,'Pastor\'s Kids','OTHER',2,'0723 513460','2025-12-11 11:37:52.165520','2025-12-11 11:37:52.165597',1,'Podcast set'),(4,'KWIRYONDET','SONG',1,'0707283363','2025-12-11 12:00:56.396072','2025-12-11 12:00:56.396172',1,''),(5,'Mattycitty music','SONG',1,'0715059317','2025-12-11 12:04:02.568054','2025-12-11 12:04:02.568143',1,''),(6,'Caster pal Tamland','SONG',2,'254701059673','2025-12-11 12:11:56.705663','2025-12-11 12:11:56.705745',1,'Together we shine and we support each other'),(7,'Curtail kyzle','SONG',1,'0795517926','2025-12-11 12:29:42.976408','2025-12-11 12:29:42.976524',1,'YouTube channel support..'),(8,'Mode de hyper','DANCE',1,'0106097124','2025-12-11 12:29:44.564488','2025-12-11 12:29:44.564597',1,''),(9,'Kronic Mkaliwao','SONG',1,'0757452252','2025-12-11 12:30:31.541661','2025-12-11 12:30:31.541693',1,''),(10,'Tribe 26','SONG',3,'0757321457','2025-12-11 12:53:43.818606','2025-12-11 12:53:43.818645',1,''),(11,'Ibrahim 003','COMEDY',1,'0718465375','2025-12-11 12:55:35.781436','2025-12-11 12:55:35.781503',1,''),(12,'Nifty zydeco','SONG',2,'0748381552','2025-12-11 13:24:05.913646','2025-12-11 13:24:05.913879',1,'I take this opportunity first to thank God for this far, I met mkenya at talanta awards 2024 and I was inspired to work with you.so I will appreciate this opportunity that you will give me on 20th to show case also my work. Thankfully from Nifty Zydeco.'),(13,'Nifty zydeco','SONG',2,'0748381552','2025-12-11 13:24:12.444371','2025-12-11 13:24:12.444450',1,'I take this opportunity first to thank God for this far, I met mkenya at talanta awards 2024 and I was inspired to work with you.so I will appreciate this opportunity that you will give me on 20th to show case also my work. Thankfully from Nifty Zydeco.'),(14,'Nifty Zydeco','SONG',2,'0748381552','2025-12-11 13:31:04.863896','2025-12-11 13:31:04.863938',1,'First I take this opportunity to thank God for this far, I\'m really happy at this moment for this coming opportunity of show casing my talent at wakenya@10\r\nI remember meeting mkenya @2024talanta awards and I was happy for the meet up so I will appreciate for this opportunity. Much appreciated\r\nFrom Nifty Zydeco.'),(15,'Jay fightah','SONG',1,'0795506965','2025-12-11 13:50:34.784782','2025-12-11 13:50:34.784862',1,''),(16,'Jay fightah','SONG',1,'0795506965','2025-12-11 13:51:00.133685','2025-12-11 13:51:00.133728',1,''),(17,'Jay fightah','SONG',1,'0795506965','2025-12-11 13:51:34.775589','2025-12-11 13:51:34.775646',1,''),(18,'Simiyu comedian','COMEDY',1,'0798546789','2025-12-11 14:37:11.942155','2025-12-11 14:37:11.942273',1,''),(19,'Castraph jani','SONG',1,'0768695921','2025-12-11 14:50:18.039289','2025-12-11 14:50:18.039453',1,'Humble for the show'),(20,'De magnet','SONG',1,'0743445247','2025-12-11 15:54:54.723876','2025-12-11 15:54:54.724001',1,''),(21,'Warriors dance crew','DANCE',10,'0705528672','2025-12-11 18:56:01.129716','2025-12-11 18:56:01.129804',1,''),(22,'WARRIORS DANCE CREW','DANCE',10,'0705528672','2025-12-11 19:40:54.552280','2025-12-11 19:40:54.552390',1,'Dance for live songs presentations'),(23,'Kobby creed.','SONG',1,'0707378922','2025-12-12 09:53:16.945143','2025-12-12 09:53:16.945227',1,''),(24,'Kobby Creed','SONG',1,'0707378922','2025-12-12 09:54:18.987363','2025-12-12 09:54:18.987522',1,''),(25,'Yung Dilla','SONG',2,'0705719756','2025-12-12 20:03:16.961478','2025-12-12 20:03:16.961582',1,''),(26,'Dan Keyz','SONG',1,'0741792891','2025-12-12 23:25:31.259769','2025-12-12 23:25:31.259939',1,'I would like to perform atleast 2 songs'),(27,'Loker Junior Bramo','SONG',2,'0786967341','2025-12-13 07:28:51.363748','2025-12-13 07:28:51.363996',1,''),(28,'Nijoh the dj','OTHER',10,'+254714401640','2025-12-13 10:43:19.021391','2025-12-13 10:43:19.021466',1,''),(29,'Wasafi','DANCE',5,'0768208258','2025-12-13 10:43:45.164697','2025-12-13 10:43:45.164750',1,''),(30,'Bakule Cherongos','OTHER',1,'0718902349','2025-12-13 10:57:19.873832','2025-12-13 10:57:19.873926',1,'Special appearance as an MC/Hypeman'),(31,'Mjukuu Wa Timona','COMEDY',2,'0714874757','2025-12-13 10:58:46.263229','2025-12-13 10:58:46.263273',1,''),(32,'Adduh official','SONG',1,'0727801871','2025-12-13 11:04:45.250071','2025-12-13 11:04:45.250143',1,''),(33,'Sabaot lady','SONG',1,'0706223124','2025-12-13 11:44:45.947460','2025-12-13 11:44:45.947597',1,''),(34,'Princess Chepkemei','SONG',1,'0715454708','2025-12-13 12:27:16.863116','2025-12-13 12:27:16.863254',1,''),(35,'Sharlyne','DANCE',2,'0769969648','2025-12-13 12:33:50.392498','2025-12-13 12:33:50.392561',1,''),(36,'Wex Brown official','SONG',1,'0791361470','2025-12-13 12:39:45.934573','2025-12-13 12:39:45.934684',1,'Kindly connect with known artist for a collaboration'),(37,'Wex Brown official','SONG',1,'0791361470','2025-12-13 12:40:15.273254','2025-12-13 12:40:15.273353',1,'Kindly connect with known artist for a collaboration'),(38,'Jay fightah','SONG',1,'0795506965','2025-12-13 12:48:08.872997','2025-12-13 12:48:08.873072',1,''),(39,'Mercy Wambalaba Cheptapkaa','SONG',1,'0707602694','2025-12-13 13:30:34.289774','2025-12-13 13:30:34.289830',1,''),(40,'Mercy Wambalaba Cheptapkaa','SONG',1,'0707602694','2025-12-13 13:30:34.878965','2025-12-13 13:30:34.879056',1,''),(41,'Bloodyboyz 🙂','SONG',7164760,'0716476021','2025-12-13 14:21:23.111860','2025-12-13 14:21:23.111922',1,'God is better'),(42,'Bloodyboyz 🙂 bondanation','SONG',3,'0716476021','2025-12-13 14:23:14.786904','2025-12-13 14:23:14.787016',1,'God is better'),(43,'Bloodyboyz','SONG',3,'0716476021','2025-12-13 14:34:55.985322','2025-12-13 14:34:55.985464',1,'Dril instruments and trap'),(44,'Moureen Tarus','SONG',1,'0706229324','2025-12-13 15:22:57.580111','2025-12-13 15:22:57.580264',1,'Wellcome to my album launch\r\nMoureen Tarus YouTube channel\r\nFacebook moureen chemtai\r\nYouTube moureen Tarus.'),(45,'Jamesh Otieno','COMEDY',1,'0705952443','2025-12-13 16:12:08.708263','2025-12-13 16:12:08.708378',1,''),(46,'Jamesh Otieno','COMEDY',1,'0705952443','2025-12-13 16:12:53.836389','2025-12-13 16:12:53.836463',1,''),(47,'Rising star','SONG',4,'0712776689','2025-12-13 17:15:37.714643','2025-12-13 17:15:37.714711',1,''),(48,'Mud minds','OTHER',3,'0790373316','2025-12-13 17:22:55.688123','2025-12-13 17:22:55.688240',1,''),(49,'Mud minds','COMEDY',3,'0798287886','2025-12-13 17:23:51.870620','2025-12-13 17:23:51.870721',1,''),(50,'Mud minds','COMEDY',3,'0798287886','2025-12-13 17:23:52.388037','2025-12-13 17:23:52.388142',1,''),(51,'SHALDON NAMASAKA WABWILE','COMEDY',1,'0729411053','2025-12-13 17:32:59.737472','2025-12-13 17:32:59.737527',1,''),(52,'Joseph Akonya','SONG',1,'0707743546','2025-12-13 18:29:22.048280','2025-12-13 18:29:22.048357',1,''),(53,'Santae Tv','COMEDY',2,'0717873950','2025-12-13 20:13:02.925921','2025-12-13 20:13:02.925998',1,''),(54,'Mike Kamau AKA Ndezy africa','SONG',1,'0796330247','2025-12-14 08:15:36.564377','2025-12-14 08:15:36.564487',1,''),(55,'Mike Kamau AKA Ndezy africa','SONG',1,'0796330247','2025-12-14 08:16:21.969820','2025-12-14 08:16:21.969910',1,''),(56,'Bram Simiyu','SONG',1,'0707691986','2025-12-14 14:13:36.165856','2025-12-14 14:13:36.165986',1,''),(57,'KOBBY CREED KC','SONG',1,'0707378922','2025-12-14 14:59:08.782394','2025-12-14 14:59:08.782477',1,''),(58,'KOBBY CREED KC','SONG',1,'0707378922','2025-12-14 14:59:14.002848','2025-12-14 14:59:14.002935',1,''),(59,'KOBBY CREED KC','SONG',1,'0707378922','2025-12-14 14:59:14.566742','2025-12-14 14:59:14.566798',1,''),(60,'KOBBY CREED KC','SONG',1,'0707378922','2025-12-14 14:59:15.782435','2025-12-14 14:59:15.782485',1,''),(61,'KOBBY CREED KC','SONG',1,'0707378922','2025-12-14 14:59:16.271546','2025-12-14 14:59:16.271587',1,''),(62,'KOBBY CREED KC','SONG',1,'0707378922','2025-12-14 14:59:17.206340','2025-12-14 14:59:17.206387',1,''),(63,'Mama msani','SONG',3,'0748931384','2025-12-15 08:11:53.921828','2025-12-15 08:11:53.922066',1,''),(64,'GTl lucii','SONG',1,'0724281285','2025-12-15 08:36:54.604168','2025-12-15 08:36:54.604378',1,''),(65,'Elias Kinyua','SONG',2,'0746959490','2025-12-17 08:00:36.909419','2025-12-17 08:00:36.909474',1,'Gospel songs'),(66,'Carlosmoi','COMEDY',3,'0743391766','2025-12-17 08:02:58.678266','2025-12-17 08:02:58.678307',1,'');
/*!40000 ALTER TABLE `events_performance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `events_ticket`
--

DROP TABLE IF EXISTS `events_ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `events_ticket` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `ticket_code` varchar(8) NOT NULL,
  `qr_code` varchar(100) DEFAULT NULL,
  `checked_in_at_gate1` datetime(6) DEFAULT NULL,
  `checked_in_at_gate2` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `booking_id` char(32) NOT NULL,
  `ticket_type_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ticket_code` (`ticket_code`),
  KEY `events_ticket_booking_id_82b963b0_fk_events_booking_id` (`booking_id`),
  KEY `events_ticket_ticket_type_id_6a59a96c_fk_events_tickettype_id` (`ticket_type_id`),
  CONSTRAINT `events_ticket_booking_id_82b963b0_fk_events_booking_id` FOREIGN KEY (`booking_id`) REFERENCES `events_booking` (`id`),
  CONSTRAINT `events_ticket_ticket_type_id_6a59a96c_fk_events_tickettype_id` FOREIGN KEY (`ticket_type_id`) REFERENCES `events_tickettype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=262 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events_ticket`
--

LOCK TABLES `events_ticket` WRITE;
/*!40000 ALTER TABLE `events_ticket` DISABLE KEYS */;
INSERT INTO `events_ticket` VALUES (1,'D578ED9C','',NULL,NULL,'2025-11-24 15:25:03.450551','878677bc191a489b841b4e6102b99612',1),(2,'224EA728','',NULL,NULL,'2025-11-24 15:25:03.734498','878677bc191a489b841b4e6102b99612',2),(3,'EC541A50','',NULL,NULL,'2025-11-24 15:32:17.396580','4aee465898e44f99bb7bd8950e92976b',1),(4,'D16993FE','',NULL,NULL,'2025-11-24 15:32:17.592832','4aee465898e44f99bb7bd8950e92976b',2),(5,'76B3CA8B','',NULL,NULL,'2025-11-24 15:32:17.799662','4aee465898e44f99bb7bd8950e92976b',2),(6,'7BFB2B86','',NULL,NULL,'2025-11-24 15:32:18.034834','4aee465898e44f99bb7bd8950e92976b',2),(7,'7EEA6339','',NULL,NULL,'2025-11-24 15:38:09.768832','c2f672f39516455c813ddd219e537eba',1),(8,'A69C8E40','',NULL,NULL,'2025-11-24 15:38:09.971265','c2f672f39516455c813ddd219e537eba',1),(9,'02BBB8AC','',NULL,NULL,'2025-11-24 15:38:10.191347','c2f672f39516455c813ddd219e537eba',1),(10,'69918E61','',NULL,NULL,'2025-11-24 15:38:10.384130','c2f672f39516455c813ddd219e537eba',1),(11,'17F33DE2','',NULL,NULL,'2025-11-24 15:38:10.587091','c2f672f39516455c813ddd219e537eba',1),(12,'E226195A','',NULL,NULL,'2025-11-24 15:38:10.791343','c2f672f39516455c813ddd219e537eba',1),(13,'1C77E9CB','',NULL,NULL,'2025-11-24 15:38:11.016346','c2f672f39516455c813ddd219e537eba',1),(14,'BC1DDF23','',NULL,NULL,'2025-11-24 15:38:11.241356','c2f672f39516455c813ddd219e537eba',1),(15,'44288032','',NULL,NULL,'2025-11-24 15:38:11.459481','c2f672f39516455c813ddd219e537eba',1),(16,'A8F109AE','',NULL,NULL,'2025-11-24 15:38:11.662893','c2f672f39516455c813ddd219e537eba',1),(17,'B7253CE8','',NULL,NULL,'2025-11-24 15:38:11.869190','c2f672f39516455c813ddd219e537eba',2),(18,'6390678A','',NULL,NULL,'2025-11-24 15:39:45.326663','e9f53e5543114ddb8da2b27bbcb2c03f',1),(19,'3C33755E','',NULL,NULL,'2025-11-24 16:08:15.801089','93b92f7906734d15b99be314f3877a4e',1),(20,'4F2D831B','',NULL,NULL,'2025-11-24 16:08:59.251725','07a80967d79741bfb9a4adecf06c6192',1),(21,'8688B8F8','',NULL,NULL,'2025-11-24 16:11:54.577830','fe788345713340a7bdd6a93dae05b52d',1),(22,'5ABFEF9C','',NULL,NULL,'2025-11-24 16:12:38.731726','0579dd776cb040d4b6b2c461c4813a59',1),(23,'8BF29A63','',NULL,NULL,'2025-11-24 16:14:39.577066','accf19c8e9d74d56bc5fe45a139f3b31',1),(24,'5F9D83D8','',NULL,NULL,'2025-11-28 14:01:34.586309','647297be0f194817b34c7aabd1b9b035',1),(25,'575C2FB7','',NULL,NULL,'2025-11-29 09:58:12.708277','c1c708b63df943409e4dc9659bd8c5b0',1),(26,'91EF478B','',NULL,NULL,'2025-11-29 09:59:21.441667','1c1268a1d4ef4e40ab17df424d025121',1),(27,'37DC5D2B','',NULL,NULL,'2025-11-30 08:59:19.785646','4a52a61d06364ebd82963229291bf9ca',1),(48,'6B0C6FE5','',NULL,NULL,'2025-12-01 19:34:51.088960','6bcf658a12994ac7957efbd9d0c77f6c',1),(49,'37481479','',NULL,NULL,'2025-12-02 08:14:31.811732','86959793e2d6461cb8e8d309c7e48dbd',2),(50,'CBE704A7','',NULL,NULL,'2025-12-02 08:14:31.817443','86959793e2d6461cb8e8d309c7e48dbd',2),(51,'3A8F359F','',NULL,NULL,'2025-12-02 08:14:31.820450','86959793e2d6461cb8e8d309c7e48dbd',2),(52,'F97A716B','',NULL,NULL,'2025-12-02 11:11:08.915583','a4f140d4c942440daeebd9ef7ed1dfb3',1),(53,'E487AB21','',NULL,NULL,'2025-12-02 11:11:08.922320','a4f140d4c942440daeebd9ef7ed1dfb3',1),(54,'F831ED23','',NULL,NULL,'2025-12-02 11:11:08.934082','a4f140d4c942440daeebd9ef7ed1dfb3',1),(55,'52290293','',NULL,NULL,'2025-12-02 11:11:08.937769','a4f140d4c942440daeebd9ef7ed1dfb3',1),(56,'A5F8C498','',NULL,NULL,'2025-12-02 11:11:08.943274','a4f140d4c942440daeebd9ef7ed1dfb3',1),(57,'6A1E9B0F','',NULL,NULL,'2025-12-02 11:11:08.947037','a4f140d4c942440daeebd9ef7ed1dfb3',1),(58,'236DF693','',NULL,NULL,'2025-12-02 11:11:08.951057','a4f140d4c942440daeebd9ef7ed1dfb3',1),(59,'4A097ADD','',NULL,NULL,'2025-12-02 11:11:08.954568','a4f140d4c942440daeebd9ef7ed1dfb3',1),(60,'7D489ACB','',NULL,NULL,'2025-12-02 11:11:08.960532','a4f140d4c942440daeebd9ef7ed1dfb3',1),(61,'DF92BE41','',NULL,NULL,'2025-12-02 11:11:08.964613','a4f140d4c942440daeebd9ef7ed1dfb3',1),(62,'8F864EF3','',NULL,NULL,'2025-12-02 16:19:52.990468','079386fa3a9945c1a81cd62bf0e84090',1),(63,'37887808','',NULL,NULL,'2025-12-04 10:17:38.672792','d37bf9c3400a4418bc2d7060f5eadfb8',2),(64,'64F3D068','',NULL,NULL,'2025-12-04 10:17:38.676513','d37bf9c3400a4418bc2d7060f5eadfb8',2),(65,'55067FE2','',NULL,NULL,'2025-12-04 10:17:38.679010','d37bf9c3400a4418bc2d7060f5eadfb8',2),(66,'419966CB','',NULL,NULL,'2025-12-04 10:17:38.682050','d37bf9c3400a4418bc2d7060f5eadfb8',2),(67,'FD2C664C','',NULL,NULL,'2025-12-04 10:39:51.710211','7404a5806300489fb2cb1825edccf95e',1),(68,'E493338B','',NULL,NULL,'2025-12-04 10:39:51.726163','7404a5806300489fb2cb1825edccf95e',1),(69,'C89513BF','',NULL,NULL,'2025-12-04 10:39:51.729543','7404a5806300489fb2cb1825edccf95e',1),(70,'D5F2F09F','',NULL,NULL,'2025-12-04 10:39:51.731767','7404a5806300489fb2cb1825edccf95e',1),(71,'46420B8D','',NULL,NULL,'2025-12-04 10:39:51.737547','7404a5806300489fb2cb1825edccf95e',1),(72,'C4B1EEDC','',NULL,NULL,'2025-12-04 10:39:51.742611','7404a5806300489fb2cb1825edccf95e',1),(73,'A95BAC67','',NULL,NULL,'2025-12-04 10:39:51.748695','7404a5806300489fb2cb1825edccf95e',1),(74,'15BE4431','',NULL,NULL,'2025-12-04 10:39:51.752325','7404a5806300489fb2cb1825edccf95e',1),(75,'F4D85579','',NULL,NULL,'2025-12-04 10:39:51.756142','7404a5806300489fb2cb1825edccf95e',1),(76,'B8C9E91D','',NULL,NULL,'2025-12-04 10:39:51.759084','7404a5806300489fb2cb1825edccf95e',1),(77,'70E0FC27','',NULL,NULL,'2025-12-04 10:39:51.761422','7404a5806300489fb2cb1825edccf95e',2),(78,'3DB4FF26','',NULL,NULL,'2025-12-04 10:39:51.764971','7404a5806300489fb2cb1825edccf95e',2),(79,'E7D42114','',NULL,NULL,'2025-12-04 10:39:51.767621','7404a5806300489fb2cb1825edccf95e',2),(80,'8F9ADE67','',NULL,NULL,'2025-12-04 10:39:51.770422','7404a5806300489fb2cb1825edccf95e',2),(81,'8D579B57','',NULL,NULL,'2025-12-04 10:39:51.773621','7404a5806300489fb2cb1825edccf95e',2),(82,'18BADA9B','',NULL,NULL,'2025-12-04 10:39:51.776247','7404a5806300489fb2cb1825edccf95e',2),(83,'5E487400','',NULL,NULL,'2025-12-04 10:39:51.779107','7404a5806300489fb2cb1825edccf95e',2),(84,'2839D07E','',NULL,NULL,'2025-12-04 10:39:51.782840','7404a5806300489fb2cb1825edccf95e',2),(85,'5AFAECEE','',NULL,NULL,'2025-12-04 10:39:51.785770','7404a5806300489fb2cb1825edccf95e',2),(86,'6964BF02','',NULL,NULL,'2025-12-04 10:39:51.789525','7404a5806300489fb2cb1825edccf95e',2),(87,'235B9DEF','',NULL,NULL,'2025-12-04 10:40:06.731233','27bb4f46c76a47e289a5c54babaa2407',1),(88,'D8440357','',NULL,NULL,'2025-12-04 10:40:06.735453','27bb4f46c76a47e289a5c54babaa2407',1),(89,'A6603FD5','',NULL,NULL,'2025-12-04 10:40:06.739614','27bb4f46c76a47e289a5c54babaa2407',1),(90,'95F09366','',NULL,NULL,'2025-12-04 10:40:06.743395','27bb4f46c76a47e289a5c54babaa2407',1),(91,'8F52AA7A','',NULL,NULL,'2025-12-04 10:40:06.747803','27bb4f46c76a47e289a5c54babaa2407',1),(92,'985DFCDE','',NULL,NULL,'2025-12-04 10:40:06.750608','27bb4f46c76a47e289a5c54babaa2407',1),(93,'2E1E41B0','',NULL,NULL,'2025-12-04 10:40:06.753858','27bb4f46c76a47e289a5c54babaa2407',1),(94,'49D0AA3A','',NULL,NULL,'2025-12-04 10:40:06.758031','27bb4f46c76a47e289a5c54babaa2407',1),(95,'1EC1D67C','',NULL,NULL,'2025-12-04 10:40:06.761453','27bb4f46c76a47e289a5c54babaa2407',1),(96,'A87C77DD','',NULL,NULL,'2025-12-04 10:40:06.765970','27bb4f46c76a47e289a5c54babaa2407',1),(97,'3384A756','',NULL,NULL,'2025-12-04 10:40:06.769505','27bb4f46c76a47e289a5c54babaa2407',2),(98,'3EC980A9','',NULL,NULL,'2025-12-04 10:40:06.772651','27bb4f46c76a47e289a5c54babaa2407',2),(99,'ED6781F8','',NULL,NULL,'2025-12-04 10:40:06.778395','27bb4f46c76a47e289a5c54babaa2407',2),(100,'56ED60BC','',NULL,NULL,'2025-12-04 10:40:06.785100','27bb4f46c76a47e289a5c54babaa2407',2),(101,'401971BE','',NULL,NULL,'2025-12-04 10:40:06.790604','27bb4f46c76a47e289a5c54babaa2407',2),(102,'25EAB7B2','',NULL,NULL,'2025-12-04 10:40:06.802192','27bb4f46c76a47e289a5c54babaa2407',2),(103,'EAC407BF','',NULL,NULL,'2025-12-04 10:40:06.808211','27bb4f46c76a47e289a5c54babaa2407',2),(104,'294DD585','',NULL,NULL,'2025-12-04 10:40:06.814996','27bb4f46c76a47e289a5c54babaa2407',2),(105,'688AAD02','',NULL,NULL,'2025-12-04 10:40:06.820070','27bb4f46c76a47e289a5c54babaa2407',2),(106,'E31A7AD5','',NULL,NULL,'2025-12-04 10:40:06.828828','27bb4f46c76a47e289a5c54babaa2407',2),(107,'3C45E72D','',NULL,NULL,'2025-12-04 10:49:17.820461','c73ac4aa477a40f7979f1f973cddb58c',1),(108,'F71C781C','',NULL,NULL,'2025-12-04 10:49:17.825188','c73ac4aa477a40f7979f1f973cddb58c',1),(109,'D6BCA483','',NULL,NULL,'2025-12-04 12:12:34.688383','70fa27f6df2d4a60b7e560a17e698497',1),(110,'892FFD75','',NULL,NULL,'2025-12-04 15:30:26.284703','57cd2da2e6ee479ba73b33b28edc9b83',1),(111,'5591BA5E','',NULL,NULL,'2025-12-04 19:24:56.903456','3e3ee31b3d3b4f3aa0b99dbde7c8586b',1),(112,'4055B275','',NULL,NULL,'2025-12-05 13:12:29.471145','8dfffd180a8540188b9a0e35b54a6342',1),(113,'B96818C2','',NULL,NULL,'2025-12-06 07:34:52.764762','3dce2d850407483581575345cae2c527',1),(114,'D875ECB4','ticket_qrs/qr_D875ECB4.png',NULL,NULL,'2025-12-07 05:26:37.888859','9ac44b6abc9644edb1d82afc9cee97d0',1),(115,'BAA4AB51','',NULL,NULL,'2025-12-08 04:58:43.083094','8ec7c6ae36f14bcdacc4b593073a2230',1),(116,'8A6E9887','',NULL,NULL,'2025-12-08 04:58:43.089796','8ec7c6ae36f14bcdacc4b593073a2230',1),(117,'3804E0C9','',NULL,NULL,'2025-12-08 04:58:43.097682','8ec7c6ae36f14bcdacc4b593073a2230',1),(118,'3B59A389','',NULL,NULL,'2025-12-08 04:58:43.108172','8ec7c6ae36f14bcdacc4b593073a2230',1),(119,'53D1ED6A','',NULL,NULL,'2025-12-08 04:58:43.112268','8ec7c6ae36f14bcdacc4b593073a2230',1),(120,'879E5313','',NULL,NULL,'2025-12-08 04:58:43.116829','8ec7c6ae36f14bcdacc4b593073a2230',1),(121,'9F197A04','',NULL,NULL,'2025-12-08 04:58:43.121056','8ec7c6ae36f14bcdacc4b593073a2230',1),(122,'8A735A91','',NULL,NULL,'2025-12-08 04:58:43.125465','8ec7c6ae36f14bcdacc4b593073a2230',1),(123,'B28A0641','',NULL,NULL,'2025-12-08 04:58:43.130973','8ec7c6ae36f14bcdacc4b593073a2230',1),(124,'900A44FD','',NULL,NULL,'2025-12-08 04:58:43.137498','8ec7c6ae36f14bcdacc4b593073a2230',1),(125,'F176313E','',NULL,NULL,'2025-12-08 04:58:43.156050','8ec7c6ae36f14bcdacc4b593073a2230',2),(126,'8AFABDBB','',NULL,NULL,'2025-12-08 04:58:43.161091','8ec7c6ae36f14bcdacc4b593073a2230',2),(127,'1859B46D','',NULL,NULL,'2025-12-08 04:58:43.164916','8ec7c6ae36f14bcdacc4b593073a2230',2),(128,'2C68A9D5','',NULL,NULL,'2025-12-08 04:58:43.172173','8ec7c6ae36f14bcdacc4b593073a2230',2),(129,'C4EE4438','',NULL,NULL,'2025-12-08 04:58:43.176052','8ec7c6ae36f14bcdacc4b593073a2230',2),(130,'2ACC48C3','',NULL,NULL,'2025-12-08 04:58:43.181726','8ec7c6ae36f14bcdacc4b593073a2230',2),(131,'D41AA075','',NULL,NULL,'2025-12-08 04:58:43.188036','8ec7c6ae36f14bcdacc4b593073a2230',2),(132,'37BE7768','',NULL,NULL,'2025-12-08 04:58:43.191676','8ec7c6ae36f14bcdacc4b593073a2230',2),(133,'F8E2FAE5','',NULL,NULL,'2025-12-08 04:58:43.195365','8ec7c6ae36f14bcdacc4b593073a2230',2),(134,'F5E97160','',NULL,NULL,'2025-12-08 04:58:43.198851','8ec7c6ae36f14bcdacc4b593073a2230',2),(135,'37CB5F0C','',NULL,NULL,'2025-12-08 11:08:51.430055','2d07fae86b08408582c8ef1108f3cabb',1),(137,'2E042949','',NULL,NULL,'2025-12-08 14:44:19.997353','048033b79f654e3897e08b46b0fabbd1',1),(138,'6FF76876','',NULL,NULL,'2025-12-08 14:44:20.005324','048033b79f654e3897e08b46b0fabbd1',2),(139,'7A9084D8','ticket_qrs/qr_7A9084D8.png',NULL,NULL,'2025-12-08 19:36:21.912800','8192f92cf1054c7897380add40605782',1),(140,'86514B02','',NULL,NULL,'2025-12-08 19:36:24.907832','9e974cc7250f431895bfba870b6b5853',1),(141,'8FC4C2B3','',NULL,NULL,'2025-12-09 04:52:50.503648','87d9ed88f8e34684a53e3e2b5b80f390',1),(142,'60F4ED4F','',NULL,NULL,'2025-12-09 04:52:50.509129','87d9ed88f8e34684a53e3e2b5b80f390',2),(143,'8BB25ADC','',NULL,NULL,'2025-12-09 04:53:07.001484','cf29a78914134bba88936da0cb9ba09d',1),(144,'AB090B54','',NULL,NULL,'2025-12-09 04:53:07.006540','cf29a78914134bba88936da0cb9ba09d',2),(145,'71B2D0E5','',NULL,NULL,'2025-12-09 08:29:30.953812','9e87dbfe07cc4d1f8bd3cb1a67c12277',2),(146,'61AA9151','',NULL,NULL,'2025-12-09 15:20:55.973647','5aef5c114d154ea49745405bfaa19e83',1),(147,'A24C18A9','',NULL,NULL,'2025-12-10 01:15:28.640420','3502c56ad31e43318ed10eecb4fa0705',1),(148,'77DF1B0F','',NULL,NULL,'2025-12-10 01:15:28.644072','3502c56ad31e43318ed10eecb4fa0705',1),(149,'FB6C0992','',NULL,NULL,'2025-12-10 01:15:28.646896','3502c56ad31e43318ed10eecb4fa0705',1),(150,'6450BC21','',NULL,NULL,'2025-12-10 01:15:28.649709','3502c56ad31e43318ed10eecb4fa0705',1),(151,'67A7D012','',NULL,NULL,'2025-12-10 01:15:28.652654','3502c56ad31e43318ed10eecb4fa0705',1),(152,'EB22069F','',NULL,NULL,'2025-12-10 01:15:47.958305','c29ec0f261d24766b995ad06fcf4f199',1),(153,'A69C59AA','',NULL,NULL,'2025-12-10 01:15:47.963025','c29ec0f261d24766b995ad06fcf4f199',1),(154,'31135F8F','',NULL,NULL,'2025-12-10 01:15:47.967056','c29ec0f261d24766b995ad06fcf4f199',1),(155,'A9243829','',NULL,NULL,'2025-12-10 01:15:47.970131','c29ec0f261d24766b995ad06fcf4f199',1),(156,'F73EECBC','',NULL,NULL,'2025-12-10 01:15:47.973068','c29ec0f261d24766b995ad06fcf4f199',1),(157,'47364D83','',NULL,NULL,'2025-12-10 01:15:47.976497','c29ec0f261d24766b995ad06fcf4f199',2),(158,'5555E338','',NULL,NULL,'2025-12-10 01:15:47.979441','c29ec0f261d24766b995ad06fcf4f199',2),(159,'EDABAEA0','',NULL,NULL,'2025-12-10 01:15:47.982004','c29ec0f261d24766b995ad06fcf4f199',2),(160,'B4725A40','',NULL,NULL,'2025-12-10 01:15:47.984124','c29ec0f261d24766b995ad06fcf4f199',2),(161,'3F5CA358','',NULL,NULL,'2025-12-10 01:15:47.987202','c29ec0f261d24766b995ad06fcf4f199',2),(162,'908B53F9','',NULL,NULL,'2025-12-10 01:15:47.989414','c29ec0f261d24766b995ad06fcf4f199',2),(163,'51024563','',NULL,NULL,'2025-12-10 01:15:47.991357','c29ec0f261d24766b995ad06fcf4f199',2),(164,'C34CAA06','',NULL,NULL,'2025-12-10 01:15:47.994840','c29ec0f261d24766b995ad06fcf4f199',2),(165,'36C76360','',NULL,NULL,'2025-12-10 01:15:47.998599','c29ec0f261d24766b995ad06fcf4f199',2),(166,'CB63ACBF','',NULL,NULL,'2025-12-10 01:15:48.002359','c29ec0f261d24766b995ad06fcf4f199',2),(167,'3CAC6CA8','',NULL,NULL,'2025-12-10 19:25:46.369294','c4bd0f5bc54548f29de8bd7d62e5dea4',1),(168,'9DEAF6A1','',NULL,NULL,'2025-12-10 19:25:46.374164','c4bd0f5bc54548f29de8bd7d62e5dea4',1),(169,'0290C724','',NULL,NULL,'2025-12-10 19:25:46.378399','c4bd0f5bc54548f29de8bd7d62e5dea4',1),(170,'3BA3AD26','',NULL,NULL,'2025-12-10 19:25:46.382659','c4bd0f5bc54548f29de8bd7d62e5dea4',1),(171,'EC76A94D','',NULL,NULL,'2025-12-10 19:25:46.388548','c4bd0f5bc54548f29de8bd7d62e5dea4',1),(172,'F33B54F0','',NULL,NULL,'2025-12-10 19:25:46.403509','c4bd0f5bc54548f29de8bd7d62e5dea4',1),(173,'4C6E9594','',NULL,NULL,'2025-12-10 19:25:46.408672','c4bd0f5bc54548f29de8bd7d62e5dea4',1),(174,'C1E4D135','',NULL,NULL,'2025-12-10 19:25:46.412046','c4bd0f5bc54548f29de8bd7d62e5dea4',1),(175,'9CBC91B3','',NULL,NULL,'2025-12-10 19:25:46.416110','c4bd0f5bc54548f29de8bd7d62e5dea4',1),(176,'6D5F940E','',NULL,NULL,'2025-12-10 19:25:46.420820','c4bd0f5bc54548f29de8bd7d62e5dea4',1),(177,'8759BA58','',NULL,NULL,'2025-12-10 19:25:46.425256','c4bd0f5bc54548f29de8bd7d62e5dea4',2),(178,'783DF4A0','',NULL,NULL,'2025-12-10 19:25:46.429749','c4bd0f5bc54548f29de8bd7d62e5dea4',2),(179,'3779B2AC','',NULL,NULL,'2025-12-10 19:25:46.434650','c4bd0f5bc54548f29de8bd7d62e5dea4',2),(180,'6F59115E','',NULL,NULL,'2025-12-10 19:25:46.438286','c4bd0f5bc54548f29de8bd7d62e5dea4',2),(181,'E677E028','',NULL,NULL,'2025-12-10 19:25:46.441234','c4bd0f5bc54548f29de8bd7d62e5dea4',2),(182,'8FB24B81','',NULL,NULL,'2025-12-10 19:25:46.446246','c4bd0f5bc54548f29de8bd7d62e5dea4',2),(183,'50CC34A4','',NULL,NULL,'2025-12-10 19:25:46.449248','c4bd0f5bc54548f29de8bd7d62e5dea4',2),(184,'6CCE85B9','',NULL,NULL,'2025-12-10 19:25:46.454082','c4bd0f5bc54548f29de8bd7d62e5dea4',2),(185,'71ACE574','',NULL,NULL,'2025-12-10 19:25:46.460356','c4bd0f5bc54548f29de8bd7d62e5dea4',2),(186,'874FE380','',NULL,NULL,'2025-12-10 19:25:46.465774','c4bd0f5bc54548f29de8bd7d62e5dea4',2),(187,'5C41D0C3','',NULL,NULL,'2025-12-11 04:11:23.469289','c047aae1f1af47128036d2b1ce2f7f6d',1),(188,'62918FC0','',NULL,NULL,'2025-12-12 18:01:25.699812','0870ab6ae25646e9bf14ef307e786c66',1),(189,'C5952E75','',NULL,NULL,'2025-12-12 18:01:25.704604','0870ab6ae25646e9bf14ef307e786c66',1),(190,'E9117416','',NULL,NULL,'2025-12-12 18:01:25.707602','0870ab6ae25646e9bf14ef307e786c66',1),(191,'5C070CCF','',NULL,NULL,'2025-12-12 18:01:25.710346','0870ab6ae25646e9bf14ef307e786c66',1),(192,'D8A222D2','',NULL,NULL,'2025-12-12 18:01:25.712813','0870ab6ae25646e9bf14ef307e786c66',1),(193,'BC8BD72F','',NULL,NULL,'2025-12-12 18:01:25.715707','0870ab6ae25646e9bf14ef307e786c66',1),(194,'7AC6F782','',NULL,NULL,'2025-12-12 18:01:25.718301','0870ab6ae25646e9bf14ef307e786c66',1),(195,'4EB816FD','',NULL,NULL,'2025-12-12 18:01:25.721788','0870ab6ae25646e9bf14ef307e786c66',1),(196,'BEF01FC2','',NULL,NULL,'2025-12-12 18:01:25.723913','0870ab6ae25646e9bf14ef307e786c66',1),(197,'D5FBC45A','',NULL,NULL,'2025-12-12 18:01:25.726198','0870ab6ae25646e9bf14ef307e786c66',1),(198,'6278B385','',NULL,NULL,'2025-12-12 18:01:25.741715','0870ab6ae25646e9bf14ef307e786c66',2),(199,'C8DB2FB9','',NULL,NULL,'2025-12-12 18:01:25.743863','0870ab6ae25646e9bf14ef307e786c66',2),(200,'BAFEAB00','',NULL,NULL,'2025-12-12 18:01:25.747128','0870ab6ae25646e9bf14ef307e786c66',2),(201,'C91F47A7','',NULL,NULL,'2025-12-12 18:01:25.750128','0870ab6ae25646e9bf14ef307e786c66',2),(202,'257D8E86','',NULL,NULL,'2025-12-12 18:01:25.752226','0870ab6ae25646e9bf14ef307e786c66',2),(203,'EBE0C959','',NULL,NULL,'2025-12-12 18:01:25.755406','0870ab6ae25646e9bf14ef307e786c66',2),(204,'12505BA1','',NULL,NULL,'2025-12-12 18:01:25.758073','0870ab6ae25646e9bf14ef307e786c66',2),(205,'861549C6','',NULL,NULL,'2025-12-12 18:01:25.759926','0870ab6ae25646e9bf14ef307e786c66',2),(206,'CDBA0E9D','',NULL,NULL,'2025-12-12 18:01:25.762314','0870ab6ae25646e9bf14ef307e786c66',2),(207,'D7AD041D','',NULL,NULL,'2025-12-12 18:01:25.767443','0870ab6ae25646e9bf14ef307e786c66',2),(208,'0F8DCFF6','',NULL,NULL,'2025-12-12 19:35:25.177931','d511410dd79944298ea270c38edaf1da',1),(209,'F202CE4A','',NULL,NULL,'2025-12-13 05:21:03.717485','c40fac48f8904aad97953cd0ededf7eb',1),(210,'D0081FAF','',NULL,NULL,'2025-12-13 06:47:28.703852','575df03784d749a79ea702a603f1315e',2),(211,'2D312F1E','',NULL,NULL,'2025-12-13 06:47:28.708290','575df03784d749a79ea702a603f1315e',2),(212,'DFA5EEF6','',NULL,NULL,'2025-12-13 06:47:31.524764','f161413577c74a0283e743c8b210bb00',2),(213,'AF374235','',NULL,NULL,'2025-12-13 06:47:31.530379','f161413577c74a0283e743c8b210bb00',2),(218,'41F5742E','ticket_qrs/qr_41F5742E.png',NULL,NULL,'2025-12-15 06:45:12.514742','2d9538747e524e33929f999c8d4344e1',1),(234,'D10D930B','ticket_qrs/qr_D10D930B.png',NULL,NULL,'2025-12-15 07:02:44.439391','1530f0f2fb344f1baa112bcc9beb284f',1),(235,'2C962944','ticket_qrs/qr_2C962944.png',NULL,NULL,'2025-12-15 07:02:44.446453','1530f0f2fb344f1baa112bcc9beb284f',1),(236,'3D4B3081','ticket_qrs/qr_3D4B3081.png',NULL,NULL,'2025-12-15 07:02:44.461468','1530f0f2fb344f1baa112bcc9beb284f',1),(237,'F0E76DC7','ticket_qrs/qr_F0E76DC7.png',NULL,NULL,'2025-12-15 07:02:44.465814','1530f0f2fb344f1baa112bcc9beb284f',1),(238,'3F7C06F8','ticket_qrs/qr_3F7C06F8.png',NULL,NULL,'2025-12-15 07:02:44.470590','1530f0f2fb344f1baa112bcc9beb284f',1),(239,'B3D76000','',NULL,NULL,'2025-12-15 10:21:13.034056','d35cfb0d856d4ab7b5d6798c5b5da4e7',1),(240,'197DA90A','',NULL,NULL,'2025-12-15 10:21:13.038930','d35cfb0d856d4ab7b5d6798c5b5da4e7',1),(241,'265D0B36','',NULL,NULL,'2025-12-17 14:36:53.479003','ae69403ee07b444aacbed058ff979b1d',1),(242,'617ECD86','',NULL,NULL,'2025-12-17 14:36:53.484814','ae69403ee07b444aacbed058ff979b1d',1),(243,'0A4DDEF4','',NULL,NULL,'2025-12-17 14:36:53.488774','ae69403ee07b444aacbed058ff979b1d',1),(244,'6939AAAC','',NULL,NULL,'2025-12-17 14:36:53.493933','ae69403ee07b444aacbed058ff979b1d',1),(245,'7A731801','',NULL,NULL,'2025-12-17 14:36:53.497948','ae69403ee07b444aacbed058ff979b1d',1),(246,'8D6168B6','',NULL,NULL,'2025-12-17 14:36:53.502976','ae69403ee07b444aacbed058ff979b1d',1),(247,'A4AC8AD3','',NULL,NULL,'2025-12-17 14:36:53.506992','ae69403ee07b444aacbed058ff979b1d',1),(248,'B983AC30','ticket_qrs/qr_B983AC30.png',NULL,NULL,'2025-12-18 07:01:32.258829','69fc92eec4cf497d84629012506ca291',1),(249,'27FB8107','ticket_qrs/qr_27FB8107.png',NULL,NULL,'2025-12-18 07:01:32.266017','69fc92eec4cf497d84629012506ca291',1),(250,'19DEF3BD','ticket_qrs/qr_19DEF3BD.png',NULL,NULL,'2025-12-18 07:01:32.272969','69fc92eec4cf497d84629012506ca291',1),(251,'A2525339','ticket_qrs/qr_A2525339.png',NULL,NULL,'2025-12-18 07:01:32.278689','69fc92eec4cf497d84629012506ca291',1),(252,'D63CF8AE','ticket_qrs/qr_D63CF8AE.png',NULL,NULL,'2025-12-18 07:01:32.286222','69fc92eec4cf497d84629012506ca291',1),(253,'3D128D41','ticket_qrs/qr_3D128D41.png',NULL,NULL,'2025-12-18 07:01:32.292344','69fc92eec4cf497d84629012506ca291',1),(254,'29F95006','ticket_qrs/qr_29F95006.png',NULL,NULL,'2025-12-18 07:01:32.297222','69fc92eec4cf497d84629012506ca291',1),(255,'4E580403','',NULL,NULL,'2025-12-18 08:30:16.942964','d6780895370f41b49b506ec06972ebf8',1),(256,'4F8AD47C','',NULL,NULL,'2025-12-19 07:14:33.260468','22075fef910e49c5a1458307410a1493',1),(257,'24B801B6','',NULL,NULL,'2025-12-19 07:14:33.273738','22075fef910e49c5a1458307410a1493',1),(258,'40A57814','ticket_qrs/qr_40A57814.png',NULL,NULL,'2025-12-19 07:52:10.105450','3512b6dab0ee48158e087ad00cca8d0c',1),(259,'444C878D','ticket_qrs/qr_444C878D.png',NULL,NULL,'2025-12-20 05:04:37.609060','7bc51c117ed9478580783b4927d79c0b',1),(260,'3CB86A93','ticket_qrs/qr_3CB86A93.png',NULL,NULL,'2025-12-20 05:04:37.612282','7bc51c117ed9478580783b4927d79c0b',1),(261,'C5090079','',NULL,NULL,'2026-01-13 14:36:35.207783','526f370deb8044b0b6830718a5608eed',1);
/*!40000 ALTER TABLE `events_ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `events_tickettype`
--

DROP TABLE IF EXISTS `events_tickettype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `events_tickettype` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `quantity_available` int unsigned NOT NULL,
  `event_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `events_tickettype_event_id_9ef8a4b2_fk_events_event_id` (`event_id`),
  CONSTRAINT `events_tickettype_event_id_9ef8a4b2_fk_events_event_id` FOREIGN KEY (`event_id`) REFERENCES `events_event` (`id`),
  CONSTRAINT `events_tickettype_chk_1` CHECK ((`quantity_available` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events_tickettype`
--

LOCK TABLES `events_tickettype` WRITE;
/*!40000 ALTER TABLE `events_tickettype` DISABLE KEYS */;
INSERT INTO `events_tickettype` VALUES (1,'VIP',1000.00,2000,1),(2,'Family of 4',3000.00,2000,1);
/*!40000 ALTER TABLE `events_tickettype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `socials_socialmediachannel`
--

DROP TABLE IF EXISTS `socials_socialmediachannel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `socials_socialmediachannel` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `platform` varchar(20) NOT NULL,
  `channel_url` varchar(200) NOT NULL,
  `channel_identifier` varchar(200) NOT NULL,
  `display_name` varchar(200) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `last_sync` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `channel_identifier` (`channel_identifier`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `socials_socialmediachannel`
--

LOCK TABLES `socials_socialmediachannel` WRITE;
/*!40000 ALTER TABLE `socials_socialmediachannel` DISABLE KEYS */;
/*!40000 ALTER TABLE `socials_socialmediachannel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `socials_socialpost`
--

DROP TABLE IF EXISTS `socials_socialpost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `socials_socialpost` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `platform` varchar(20) NOT NULL,
  `url` varchar(200) NOT NULL,
  `caption` longtext NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `embed_code` longtext NOT NULL DEFAULT (_utf8mb3''),
  `author` varchar(200) NOT NULL,
  `comment_count` bigint NOT NULL,
  `like_count` bigint NOT NULL,
  `published_date` datetime(6) DEFAULT NULL,
  `title` varchar(500) NOT NULL,
  `view_count` bigint NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `socials_socialpost`
--

LOCK TABLES `socials_socialpost` WRITE;
/*!40000 ALTER TABLE `socials_socialpost` DISABLE KEYS */;
INSERT INTO `socials_socialpost` VALUES (2,'TIKTOK','https://www.tiktok.com/@mkenya7million/video/7198423948625825030','',1,'2025-11-28 19:06:07.119872','2025-11-28 19:08:22.668312','<blockquote class=\"tiktok-embed\" cite=\"https://www.tiktok.com/@mkenya7million/video/7198423948625825030\" data-video-id=\"7198423948625825030\" style=\"max-width: 605px;min-width: 325px;\" > <section> <a target=\"_blank\" title=\"@mkenya7million\" href=\"https://www.tiktok.com/@mkenya7million?refer=embed\">@mkenya7million</a> <p>Gone are the days</p> <a target=\"_blank\" title=\"♬ original sound - Mkenya Isaak 7Million\" href=\"https://www.tiktok.com/music/original-sound-7198424017135815430?refer=embed\">♬ original sound - Mkenya Isaak 7Million</a> </section> </blockquote> <script async src=\"https://www.tiktok.com/embed.js\"></script>','',0,0,NULL,'',0),(3,'YOUTUBE','https://www.youtube.com/watch?v=DIABNWgSS8k','',1,'2025-11-28 19:12:26.083725','2025-11-28 19:12:26.083789','<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/DIABNWgSS8k?si=U49uXYIxNdMANflt\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe>','',0,0,NULL,'',0),(4,'TIKTOK','https://www.tiktok.com/@mkenya7million/video/7577005078809267512','',1,'2025-11-28 19:36:18.549636','2025-11-28 19:36:18.549667','<blockquote class=\"tiktok-embed\" cite=\"https://www.tiktok.com/@mkenya7million/video/7577005078809267512\" data-video-id=\"7577005078809267512\" style=\"max-width: 605px; min-width: 325px;\"> <section> <a target=\"_blank\" href=\"https://www.tiktok.com/@mkenya7million/video/7577005078809267512\"></a> </section> </blockquote> <script async src=\"https://www.tiktok.com/embed.js\"></script>','',0,0,NULL,'',0),(5,'TIKTOK','https://www.tiktok.com/@mkenya7million/video/7576539802594462988','',1,'2025-11-28 19:47:43.783415','2025-11-28 19:47:43.783444','<div class=\"tiktok-embed-container\" style=\"position: relative; width: 100%; padding-top: 177.78%; /* 9:16 aspect ratio */ height: 0;\"><blockquote class=\"tiktok-embed\" cite=\"https://www.tiktok.com/@mkenya7million/video/7576539802594462988\" data-video-id=\"7576539802594462988\" style=\"position: absolute; top: 0; left: 0; width: 100%; height: 100%; max-width: 300px; margin: 0 auto;\"> <section> <a target=\"_blank\" href=\"https://www.tiktok.com/@mkenya7million/video/7576539802594462988\"></a> </section> </blockquote></div><script async src=\"https://www.tiktok.com/embed.js\"></script>','',0,0,NULL,'',0),(6,'TIKTOK','https://www.tiktok.com/@mkenya7million/photo/7576379887859158283','',1,'2025-11-28 19:51:20.879332','2025-11-28 19:51:20.879376','<div class=\"tiktok-embed-container\" style=\"position: relative; width: 100%; padding-top: 177.78%; /* 9:16 aspect ratio */ height: 0;\"><blockquote class=\"tiktok-embed\" cite=\"https://www.tiktok.com/@mkenya7million/photo/7576379887859158283\" data-video-id=\"7576379887859158283\" style=\"position: absolute; top: 0; left: 0; width: 100%; height: 100%; max-width: 300px; margin: 0 auto;\"> <section> <a target=\"_blank\" href=\"https://www.tiktok.com/@mkenya7million/photo/7576379887859158283\"></a> </section> </blockquote></div><script async src=\"https://www.tiktok.com/embed.js\"></script>','',0,0,NULL,'',0),(7,'TIKTOK','https://www.tiktok.com/@mkenya7million/photo/7577798005818969355','',1,'2025-11-28 19:52:45.677531','2025-11-28 19:52:45.677591','<div class=\"tiktok-embed-container\" style=\"position: relative; width: 100%; padding-top: 177.78%; /* 9:16 aspect ratio */ height: 0;\"><blockquote class=\"tiktok-embed\" cite=\"https://www.tiktok.com/@mkenya7million/photo/7577798005818969355\" data-video-id=\"7577798005818969355\" style=\"position: absolute; top: 0; left: 0; width: 100%; height: 100%; max-width: 300px; margin: 0 auto;\"> <section> <a target=\"_blank\" href=\"https://www.tiktok.com/@mkenya7million/photo/7577798005818969355\"></a> </section> </blockquote></div><script async src=\"https://www.tiktok.com/embed.js\"></script>','',0,0,NULL,'',0),(8,'TIKTOK','https://www.tiktok.com/@mkenya7million/video/7579570015834361144','',1,'2025-12-05 14:57:11.576043','2025-12-05 14:58:35.680536','<div class=\"tiktok-embed-container\" style=\"position: relative; width: 100%; padding-top: 177.78%; /* 9:16 aspect ratio */ height: 0;\"><blockquote class=\"tiktok-embed\" cite=\"https://www.tiktok.com/@mkenya7million/video/7579570015834361144\" data-video-id=\"7579570015834361144\" style=\"position: absolute; top: 0; left: 0; width: 100%; height: 100%; max-width: 300px; margin: 0 auto;\"> <section> <a target=\"_blank\" href=\"https://www.tiktok.com/@mkenya7million/video/7579570015834361144\"></a> </section> </blockquote></div><script async src=\"https://www.tiktok.com/embed.js\"></script>','',0,0,NULL,'',0),(9,'TIKTOK','https://www.tiktok.com/@mkenya7million/video/7580223485738224908','',1,'2025-12-05 14:58:43.108494','2025-12-05 14:58:43.108545','<div class=\"tiktok-embed-container\" style=\"position: relative; width: 100%; padding-top: 177.78%; /* 9:16 aspect ratio */ height: 0;\"><blockquote class=\"tiktok-embed\" cite=\"https://www.tiktok.com/@mkenya7million/video/7580223485738224908\" data-video-id=\"7580223485738224908\" style=\"position: absolute; top: 0; left: 0; width: 100%; height: 100%; max-width: 300px; margin: 0 auto;\"> <section> <a target=\"_blank\" href=\"https://www.tiktok.com/@mkenya7million/video/7580223485738224908\"></a> </section> </blockquote></div><script async src=\"https://www.tiktok.com/embed.js\"></script>','',0,0,NULL,'',0),(10,'TIKTOK','https://www.tiktok.com/@mkenya7million/photo/7580247092451446027','',1,'2025-12-05 14:59:11.126661','2025-12-05 14:59:11.126728','<div class=\"tiktok-embed-container\" style=\"position: relative; width: 100%; padding-top: 177.78%; /* 9:16 aspect ratio */ height: 0;\"><blockquote class=\"tiktok-embed\" cite=\"https://www.tiktok.com/@mkenya7million/photo/7580247092451446027\" data-video-id=\"7580247092451446027\" style=\"position: absolute; top: 0; left: 0; width: 100%; height: 100%; max-width: 300px; margin: 0 auto;\"> <section> <a target=\"_blank\" href=\"https://www.tiktok.com/@mkenya7million/photo/7580247092451446027\"></a> </section> </blockquote></div><script async src=\"https://www.tiktok.com/embed.js\"></script>','',0,0,NULL,'',0),(11,'TIKTOK','https://www.tiktok.com/@mkenya7million/video/7579301354515025163','',1,'2025-12-05 15:01:24.773184','2025-12-05 15:01:24.773287','<div class=\"tiktok-embed-container\" style=\"position: relative; width: 100%; padding-top: 177.78%; /* 9:16 aspect ratio */ height: 0;\"><blockquote class=\"tiktok-embed\" cite=\"https://www.tiktok.com/@mkenya7million/video/7579301354515025163\" data-video-id=\"7579301354515025163\" style=\"position: absolute; top: 0; left: 0; width: 100%; height: 100%; max-width: 300px; margin: 0 auto;\"> <section> <a target=\"_blank\" href=\"https://www.tiktok.com/@mkenya7million/video/7579301354515025163\"></a> </section> </blockquote></div><script async src=\"https://www.tiktok.com/embed.js\"></script>','',0,0,NULL,'',0),(12,'TIKTOK','https://www.tiktok.com/@mkenya7million/photo/7584571107617918219?is_from_webapp=1&sender_device=pc','The Unsuccessful Recruit\r\nPerforming live on state at WAKENYAA! 20th Dec 2025 mkenyaisaak.co.ke',1,'2025-12-17 09:38:30.847027','2025-12-17 09:38:30.847065','<div class=\"tiktok-embed-container\" style=\"position: relative; width: 100%; padding-top: 177.78%; /* 9:16 aspect ratio */ height: 0;\"><blockquote class=\"tiktok-embed\" cite=\"https://www.tiktok.com/@mkenya7million/photo/7584571107617918219?is_from_webapp=1&sender_device=pc\" data-video-id=\"7584571107617918219\" style=\"position: absolute; top: 0; left: 0; width: 100%; height: 100%; max-width: 300px; margin: 0 auto;\"> <section> <a target=\"_blank\" href=\"https://www.tiktok.com/@mkenya7million/photo/7584571107617918219?is_from_webapp=1&sender_device=pc\"></a> </section> </blockquote></div><script async src=\"https://www.tiktok.com/embed.js\"></script>','',0,0,NULL,'',0),(13,'TIKTOK','https://www.tiktok.com/@mkenya7million/photo/7584018532275408140?is_from_webapp=1&sender_device=pc','KataKala - official butchery at WAKENYAA! 20th Dec 2025. Buy tickets mkenyaisaak.co.ke',1,'2025-12-17 09:40:18.158263','2025-12-17 09:40:18.158338','<div class=\"tiktok-embed-container\" style=\"position: relative; width: 100%; padding-top: 177.78%; /* 9:16 aspect ratio */ height: 0;\"><blockquote class=\"tiktok-embed\" cite=\"https://www.tiktok.com/@mkenya7million/photo/7584018532275408140?is_from_webapp=1&sender_device=pc\" data-video-id=\"7584018532275408140\" style=\"position: absolute; top: 0; left: 0; width: 100%; height: 100%; max-width: 300px; margin: 0 auto;\"> <section> <a target=\"_blank\" href=\"https://www.tiktok.com/@mkenya7million/photo/7584018532275408140?is_from_webapp=1&sender_device=pc\"></a> </section> </blockquote></div><script async src=\"https://www.tiktok.com/embed.js\"></script>','',0,0,NULL,'',0),(14,'TIKTOK','https://www.tiktok.com/@mkenya7million/photo/7583948861568339212?is_from_webapp=1&sender_device=pc','Karibu sana FKF chairman to WAKENYAAA! 20th Dec 2025.',1,'2025-12-17 09:42:23.848460','2025-12-17 09:53:20.456925','<div class=\"tiktok-embed-container\" style=\"position: relative; width: 100%; padding-top: 177.78%; /* 9:16 aspect ratio */ height: 0;\"><blockquote class=\"tiktok-embed\" cite=\"https://www.tiktok.com/@mkenya7million/photo/7583948861568339212?is_from_webapp=1&sender_device=pc\" data-video-id=\"7583948861568339212\" style=\"position: absolute; top: 0; left: 0; width: 100%; height: 100%; max-width: 300px; margin: 0 auto;\"> <section> <a target=\"_blank\" href=\"https://www.tiktok.com/@mkenya7million/photo/7583948861568339212?is_from_webapp=1&sender_device=pc\"></a> </section> </blockquote></div><script async src=\"https://www.tiktok.com/embed.js\"></script>','',0,0,NULL,'',0);
/*!40000 ALTER TABLE `socials_socialpost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `socials_socialprofile`
--

DROP TABLE IF EXISTS `socials_socialprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `socials_socialprofile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `platform` varchar(20) NOT NULL,
  `profile_url` varchar(200) NOT NULL,
  `display_name` varchar(100) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `platform` (`platform`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `socials_socialprofile`
--

LOCK TABLES `socials_socialprofile` WRITE;
/*!40000 ALTER TABLE `socials_socialprofile` DISABLE KEYS */;
INSERT INTO `socials_socialprofile` VALUES (1,'TIKTOK','https://www.tiktok.com/@mkenya7million','@mkenya7million',1,'2025-11-25 03:51:30.500853','2025-11-28 19:04:06.626428'),(2,'INSTAGRAM','https://www.instagram.com/mkenyaisaak/','@mkenyaisaak',1,'2025-11-25 03:51:31.513702','2025-11-25 03:51:31.513763'),(3,'YOUTUBE','https://www.youtube.com/@mkenya7million','Mkenya Isaak 7Million',1,'2025-11-25 03:51:32.508808','2025-11-28 19:04:43.305520'),(4,'FACEBOOK','https://web.facebook.com/seven7miIlion/?_rdc=1&_rdr','Mkenya Isaak 7Million',1,'2025-11-25 03:51:33.529703','2025-11-28 19:03:22.503328');
/*!40000 ALTER TABLE `socials_socialprofile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-02-18  5:02:12
