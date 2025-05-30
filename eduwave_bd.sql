-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: eduwave_bd
-- ------------------------------------------------------
-- Server version	8.0.30

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
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add ambiente',6,'add_ambiente'),(22,'Can change ambiente',6,'change_ambiente'),(23,'Can delete ambiente',6,'delete_ambiente'),(24,'Can view ambiente',6,'view_ambiente'),(25,'Can add categoria',7,'add_categoria'),(26,'Can change categoria',7,'change_categoria'),(27,'Can delete categoria',7,'delete_categoria'),(28,'Can view categoria',7,'view_categoria'),(29,'Can add municipio',8,'add_municipio'),(30,'Can change municipio',8,'change_municipio'),(31,'Can delete municipio',8,'delete_municipio'),(32,'Can view municipio',8,'view_municipio'),(33,'Can add programa formacion',9,'add_programaformacion'),(34,'Can change programa formacion',9,'change_programaformacion'),(35,'Can delete programa formacion',9,'delete_programaformacion'),(36,'Can view programa formacion',9,'view_programaformacion'),(37,'Can add regional',10,'add_regional'),(38,'Can change regional',10,'change_regional'),(39,'Can delete regional',10,'delete_regional'),(40,'Can view regional',10,'view_regional'),(41,'Can add rol',11,'add_rol'),(42,'Can change rol',11,'change_rol'),(43,'Can delete rol',11,'delete_rol'),(44,'Can view rol',11,'view_rol'),(45,'Can add tipo ambiente',12,'add_tipoambiente'),(46,'Can change tipo ambiente',12,'change_tipoambiente'),(47,'Can delete tipo ambiente',12,'delete_tipoambiente'),(48,'Can view tipo ambiente',12,'view_tipoambiente'),(49,'Can add tipo novedad',13,'add_tiponovedad'),(50,'Can change tipo novedad',13,'change_tiponovedad'),(51,'Can delete tipo novedad',13,'delete_tiponovedad'),(52,'Can view tipo novedad',13,'view_tiponovedad'),(53,'Can add inventario',14,'add_inventario'),(54,'Can change inventario',14,'change_inventario'),(55,'Can delete inventario',14,'delete_inventario'),(56,'Can view inventario',14,'view_inventario'),(57,'Can add centro formacion',15,'add_centroformacion'),(58,'Can change centro formacion',15,'change_centroformacion'),(59,'Can delete centro formacion',15,'delete_centroformacion'),(60,'Can view centro formacion',15,'view_centroformacion'),(61,'Can add ficha',16,'add_ficha'),(62,'Can change ficha',16,'change_ficha'),(63,'Can delete ficha',16,'delete_ficha'),(64,'Can view ficha',16,'view_ficha'),(65,'Can add red',17,'add_red'),(66,'Can change red',17,'change_red'),(67,'Can delete red',17,'delete_red'),(68,'Can view red',17,'view_red'),(69,'Can add sede',18,'add_sede'),(70,'Can change sede',18,'change_sede'),(71,'Can delete sede',18,'delete_sede'),(72,'Can view sede',18,'view_sede'),(73,'Can add sub categoria',19,'add_subcategoria'),(74,'Can change sub categoria',19,'change_subcategoria'),(75,'Can delete sub categoria',19,'delete_subcategoria'),(76,'Can view sub categoria',19,'view_subcategoria'),(77,'Can add Usuario',20,'add_usuario'),(78,'Can change Usuario',20,'change_usuario'),(79,'Can delete Usuario',20,'delete_usuario'),(80,'Can view Usuario',20,'view_usuario'),(81,'Can add novedad',21,'add_novedad'),(82,'Can change novedad',21,'change_novedad'),(83,'Can delete novedad',21,'delete_novedad'),(84,'Can view novedad',21,'view_novedad');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
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
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_Eduwave_app_usuario_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_Eduwave_app_usuario_id` FOREIGN KEY (`user_id`) REFERENCES `eduwave_app_usuario` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(6,'Eduwave_app','ambiente'),(7,'Eduwave_app','categoria'),(15,'Eduwave_app','centroformacion'),(16,'Eduwave_app','ficha'),(14,'Eduwave_app','inventario'),(8,'Eduwave_app','municipio'),(21,'Eduwave_app','novedad'),(9,'Eduwave_app','programaformacion'),(17,'Eduwave_app','red'),(10,'Eduwave_app','regional'),(11,'Eduwave_app','rol'),(18,'Eduwave_app','sede'),(19,'Eduwave_app','subcategoria'),(12,'Eduwave_app','tipoambiente'),(13,'Eduwave_app','tiponovedad'),(20,'Eduwave_app','usuario'),(5,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-04-19 17:36:39.988256'),(2,'contenttypes','0002_remove_content_type_name','2025-04-19 17:36:40.694842'),(3,'auth','0001_initial','2025-04-19 17:36:41.770861'),(4,'auth','0002_alter_permission_name_max_length','2025-04-19 17:36:41.939554'),(5,'auth','0003_alter_user_email_max_length','2025-04-19 17:36:41.970605'),(6,'auth','0004_alter_user_username_opts','2025-04-19 17:36:41.995946'),(7,'auth','0005_alter_user_last_login_null','2025-04-19 17:36:42.029894'),(8,'auth','0006_require_contenttypes_0002','2025-04-19 17:36:42.052014'),(9,'auth','0007_alter_validators_add_error_messages','2025-04-19 17:36:42.087300'),(10,'auth','0008_alter_user_username_max_length','2025-04-19 17:36:42.112609'),(11,'auth','0009_alter_user_last_name_max_length','2025-04-19 17:36:42.145444'),(12,'auth','0010_alter_group_name_max_length','2025-04-19 17:36:42.193866'),(13,'auth','0011_update_proxy_permissions','2025-04-19 17:36:42.229602'),(14,'auth','0012_alter_user_first_name_max_length','2025-04-19 17:36:42.253697'),(15,'Eduwave_app','0001_initial','2025-04-19 17:36:50.535174'),(16,'admin','0001_initial','2025-04-19 17:36:51.135633'),(17,'admin','0002_logentry_remove_auto_add','2025-04-19 17:36:51.169613'),(18,'admin','0003_logentry_add_action_flag_choices','2025-04-19 17:36:51.194322'),(19,'sessions','0001_initial','2025-04-19 17:36:51.390413'),(20,'Eduwave_app','0002_usuario_centro','2025-04-20 03:08:49.711832'),(21,'Eduwave_app','0003_alter_usuario_tipo_doc','2025-04-20 03:08:49.811835'),(22,'Eduwave_app','0004_remove_usuario_ficha_usuario_ficha','2025-04-20 03:08:52.253609'),(23,'Eduwave_app','0005_rename_ficha_usuario_fichas','2025-04-20 03:08:52.336108'),(24,'Eduwave_app','0006_alter_inventario_categoria','2025-04-20 04:35:53.200970'),(25,'Eduwave_app','0007_novedad_inventario','2025-04-20 05:02:18.512220'),(26,'Eduwave_app','0008_alter_novedad_inventario','2025-04-20 05:36:15.664897'),(27,'Eduwave_app','0009_alter_novedad_inventario','2025-04-20 05:41:40.388566');
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
INSERT INTO `django_session` VALUES ('2uwqj510rm3hhuktulg7xnyq5u4737re','.eJxVjMEOwiAQRP-FsyHSBbp49O43EFi2UjWQlPZk_Hdp0oMeZ96beQsftjX7rfHi5yQuAsTpt4uBnlx2kB6h3KukWtZljnJX5EGbvNXEr-vh_h3k0HJfGzs50G5wPEVURIPRaFUCVBxHpB4iousCK7IaKHFXzgzWjAqcCeLzBcmHNwg:1u6PkG:3dIBIImG0W-URRgOR_xV6pVF9w9GuP8rvp5OWPqXqPU','2025-05-04 08:09:44.762975'),('6j12jn0t3xpcluisq1pynjvq7gyivb88','.eJxVjDsOwjAQBe_iGlnxd72U9Jwh2l07OIAcKZ8KcXeIlALaNzPvpXra1tpvS5n7MauzMur0uzHJo7Qd5Du126Rlaus8st4VfdBFX6dcnpfD_TuotNRvzZ23jMVFYGJvkBhksMkIhSH4HMW6LnXgEEA4oE_JRiQMKI4pO1DvD9-cN4A:1u6L7h:x8BouuINAB2gAVXJXrqORQzu4kUcVwGeTSAgG7zl5Ms','2025-05-04 03:13:37.962369'),('hue81992bwkuoy3j9h42cwkgykpgp8nk','.eJxVjDsOwjAQRO_iGln-O6akzxmstXeDA8iW4qRC3J1ESgHdaN6bebMI21ri1mmJM7IrM-zy2yXIT6oHwAfUe-O51XWZEz8UftLOx4b0up3u30GBXva1xUFPIliYFHnQwivMzqBSPnkj0x6El9JrIA1Cu5AtBbCBEJzKacjs8wXV0DfI:1u6aQA:hnG2y8VKyotTN05v32RDm4bAP_NS_4IarRk6OC8PK68','2025-05-04 19:33:42.718721'),('s42n2z007iymeg8hhxw3y2rpxotwylwv','.eJxVjDsOwjAQBe_iGlnxd72U9Jwh2l07OIAcKZ8KcXeIlALaNzPvpXra1tpvS5n7MauzMur0uzHJo7Qd5Du126Rlaus8st4VfdBFX6dcnpfD_TuotNRvzZ23jMVFYGJvkBhksMkIhSH4HMW6LnXgEEA4oE_JRiQMKI4pO1DvD9-cN4A:1u6QG9:9tnjMnKzwfPXAtO7n9wTSgB0zM0ltYwBnpwyF_5_OeY','2025-05-04 08:42:41.196875'),('w8h6v4dq01m401ocm2jknz60mnlap88t','.eJxVjDsOwjAQBe_iGlnxd72U9Jwh2l07OIAcKZ8KcXeIlALaNzPvpXra1tpvS5n7MauzMur0uzHJo7Qd5Du126Rlaus8st4VfdBFX6dcnpfD_TuotNRvzZ23jMVFYGJvkBhksMkIhSH4HMW6LnXgEEA4oE_JRiQMKI4pO1DvD9-cN4A:1u6RCy:2HdCWm4rXxVUM25L17vOLEyeAmoXATJ4eiaY_6rb-w8','2025-05-04 09:43:28.815764'),('yisknf7gf6va44369gltnimuc503x45g','.eJxVjDsOwjAQRO_iGln-O6akzxmstXeDA8iW4qRC3J1ESgHdaN6bebMI21ri1mmJM7IrM-zy2yXIT6oHwAfUe-O51XWZEz8UftLOx4b0up3u30GBXva1xUFPIliYFHnQwivMzqBSPnkj0x6El9JrIA1Cu5AtBbCBEJzKacjs8wXV0DfI:1u6aQA:hnG2y8VKyotTN05v32RDm4bAP_NS_4IarRk6OC8PK68','2025-05-04 19:33:42.677721');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eduwave_app_ambiente`
--

DROP TABLE IF EXISTS `eduwave_app_ambiente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eduwave_app_ambiente` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `numero_ambiente` varchar(100) NOT NULL,
  `estado` varchar(1) NOT NULL,
  `sede_id` bigint NOT NULL,
  `tipo_ambiente_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `numero_ambiente` (`numero_ambiente`),
  KEY `Eduwave_app_ambiente_sede_id_a7133c2b_fk_Eduwave_app_sede_id` (`sede_id`),
  KEY `Eduwave_app_ambiente_tipo_ambiente_id_6ed7481d_fk_Eduwave_a` (`tipo_ambiente_id`),
  CONSTRAINT `Eduwave_app_ambiente_sede_id_a7133c2b_fk_Eduwave_app_sede_id` FOREIGN KEY (`sede_id`) REFERENCES `eduwave_app_sede` (`id`),
  CONSTRAINT `Eduwave_app_ambiente_tipo_ambiente_id_6ed7481d_fk_Eduwave_a` FOREIGN KEY (`tipo_ambiente_id`) REFERENCES `eduwave_app_tipoambiente` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eduwave_app_ambiente`
--

LOCK TABLES `eduwave_app_ambiente` WRITE;
/*!40000 ALTER TABLE `eduwave_app_ambiente` DISABLE KEYS */;
INSERT INTO `eduwave_app_ambiente` VALUES (1,'101','A',3,1),(3,'101 T','N',1,2),(4,'201','A',2,1),(5,'202','A',2,3);
/*!40000 ALTER TABLE `eduwave_app_ambiente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eduwave_app_categoria`
--

DROP TABLE IF EXISTS `eduwave_app_categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eduwave_app_categoria` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eduwave_app_categoria`
--

LOCK TABLES `eduwave_app_categoria` WRITE;
/*!40000 ALTER TABLE `eduwave_app_categoria` DISABLE KEYS */;
INSERT INTO `eduwave_app_categoria` VALUES (3,'Electronicos'),(1,'Infraestructura'),(2,'Muebles'),(6,'Objetos Deportivos');
/*!40000 ALTER TABLE `eduwave_app_categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eduwave_app_centroformacion`
--

DROP TABLE IF EXISTS `eduwave_app_centroformacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eduwave_app_centroformacion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `codigo` varchar(10) NOT NULL,
  `nombre` varchar(300) NOT NULL,
  `direccion` varchar(300) NOT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  `municipio_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `codigo` (`codigo`),
  KEY `Eduwave_app_centrofo_municipio_id_de7afac2_fk_Eduwave_a` (`municipio_id`),
  CONSTRAINT `Eduwave_app_centrofo_municipio_id_de7afac2_fk_Eduwave_a` FOREIGN KEY (`municipio_id`) REFERENCES `eduwave_app_municipio` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eduwave_app_centroformacion`
--

LOCK TABLES `eduwave_app_centroformacion` WRITE;
/*!40000 ALTER TABLE `eduwave_app_centroformacion` DISABLE KEYS */;
INSERT INTO `eduwave_app_centroformacion` VALUES (1,'1234','Centro Industrial y de Desarrollo Empresarial','Calle 13 # 10-45','3101234567',1),(2,'01','CENFETEC-Centro de Formaci├│n Empresarial y Tecnol├│gica,','Carrera 19 #65','2341233213',3),(3,'02','Centro Agropecuario La Granja','Carrera 5 #155','3208187271',5);
/*!40000 ALTER TABLE `eduwave_app_centroformacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eduwave_app_ficha`
--

DROP TABLE IF EXISTS `eduwave_app_ficha`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eduwave_app_ficha` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `num_ficha` varchar(45) NOT NULL,
  `programa_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `num_ficha` (`num_ficha`),
  KEY `Eduwave_app_ficha_programa_id_74664022_fk_Eduwave_a` (`programa_id`),
  CONSTRAINT `Eduwave_app_ficha_programa_id_74664022_fk_Eduwave_a` FOREIGN KEY (`programa_id`) REFERENCES `eduwave_app_programaformacion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eduwave_app_ficha`
--

LOCK TABLES `eduwave_app_ficha` WRITE;
/*!40000 ALTER TABLE `eduwave_app_ficha` DISABLE KEYS */;
INSERT INTO `eduwave_app_ficha` VALUES (1,'2902290',1),(2,'2902291',2),(3,'28889033',3);
/*!40000 ALTER TABLE `eduwave_app_ficha` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eduwave_app_inventario`
--

DROP TABLE IF EXISTS `eduwave_app_inventario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eduwave_app_inventario` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `codigo` varchar(40) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `fecha_adquisicion` date NOT NULL,
  `num_placa_almacen` varchar(45) NOT NULL,
  `precio_compra` decimal(20,2) NOT NULL,
  `estado` varchar(1) NOT NULL,
  `ambiente_id` bigint DEFAULT NULL,
  `categoria_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `codigo` (`codigo`),
  KEY `Eduwave_app_inventar_ambiente_id_d30b97b9_fk_Eduwave_a` (`ambiente_id`),
  KEY `Eduwave_app_inventar_categoria_id_54602a12_fk_Eduwave_a` (`categoria_id`),
  CONSTRAINT `Eduwave_app_inventar_ambiente_id_d30b97b9_fk_Eduwave_a` FOREIGN KEY (`ambiente_id`) REFERENCES `eduwave_app_ambiente` (`id`),
  CONSTRAINT `Eduwave_app_inventar_categoria_id_54602a12_fk_Eduwave_a` FOREIGN KEY (`categoria_id`) REFERENCES `eduwave_app_subcategoria` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eduwave_app_inventario`
--

LOCK TABLES `eduwave_app_inventario` WRITE;
/*!40000 ALTER TABLE `eduwave_app_inventario` DISABLE KEYS */;
INSERT INTO `eduwave_app_inventario` VALUES (1,'123','Dell','Computador negro','2025-04-18','111111',140.00,'A',1,6),(2,'1','Pared','Pared','2025-04-19','12',150.00,'A',1,1),(3,'12312','Balon','Balon de Balonecsto','2025-04-09','12311',90.00,'A',3,8),(4,'45235126','Computador de Lizeth','Computador negro','2025-04-09','5251',8000.00,'A',4,6);
/*!40000 ALTER TABLE `eduwave_app_inventario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eduwave_app_municipio`
--

DROP TABLE IF EXISTS `eduwave_app_municipio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eduwave_app_municipio` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `codigo_DANE` varchar(20) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `regional_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `codigo_DANE` (`codigo_DANE`),
  KEY `Eduwave_app_municipi_regional_id_d7ef5979_fk_Eduwave_a` (`regional_id`),
  CONSTRAINT `Eduwave_app_municipi_regional_id_d7ef5979_fk_Eduwave_a` FOREIGN KEY (`regional_id`) REFERENCES `eduwave_app_regional` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eduwave_app_municipio`
--

LOCK TABLES `eduwave_app_municipio` WRITE;
/*!40000 ALTER TABLE `eduwave_app_municipio` DISABLE KEYS */;
INSERT INTO `eduwave_app_municipio` VALUES (1,'25599','Soacha',1),(2,'01','Bogot├í',1),(3,'03','Chaparral',2),(5,'02','Ibagu├®',2);
/*!40000 ALTER TABLE `eduwave_app_municipio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eduwave_app_novedad`
--

DROP TABLE IF EXISTS `eduwave_app_novedad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eduwave_app_novedad` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(450) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `evidencia` varchar(100) DEFAULT NULL,
  `estado` varchar(1) NOT NULL,
  `tipo_falta` varchar(10) DEFAULT NULL,
  `ambiente_id` bigint DEFAULT NULL,
  `tipo_novedad_id` bigint NOT NULL,
  `creado_por_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Eduwave_app_novedad_ambiente_id_32740797_fk_Eduwave_a` (`ambiente_id`),
  KEY `Eduwave_app_novedad_tipo_novedad_id_e881807e_fk_Eduwave_a` (`tipo_novedad_id`),
  KEY `Eduwave_app_novedad_creado_por_id_21ea4bd9_fk_Eduwave_a` (`creado_por_id`),
  CONSTRAINT `Eduwave_app_novedad_ambiente_id_32740797_fk_Eduwave_a` FOREIGN KEY (`ambiente_id`) REFERENCES `eduwave_app_ambiente` (`id`),
  CONSTRAINT `Eduwave_app_novedad_creado_por_id_21ea4bd9_fk_Eduwave_a` FOREIGN KEY (`creado_por_id`) REFERENCES `eduwave_app_usuario` (`id`),
  CONSTRAINT `Eduwave_app_novedad_tipo_novedad_id_e881807e_fk_Eduwave_a` FOREIGN KEY (`tipo_novedad_id`) REFERENCES `eduwave_app_tiponovedad` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eduwave_app_novedad`
--

LOCK TABLES `eduwave_app_novedad` WRITE;
/*!40000 ALTER TABLE `eduwave_app_novedad` DISABLE KEYS */;
INSERT INTO `eduwave_app_novedad` VALUES (1,'La Se├▒orita Danna no ha entregado los ultimos 20 trabajos del trimestre','2025-04-20 04:55:52.438571','evidencias/Captura_de_pantalla_2025-01-24_191842.png','P','Grave',NULL,1,1),(2,'La se├▒orita Danna falt├│ durante todo el trimestre','2025-04-20 04:57:57.839864','evidencias/Captura_de_pantalla_2025-01-24_191842_yueMdU6.png','P','Leve',NULL,2,1),(3,'Ariana Le falt├│ el respeto a Robinson','2025-04-20 04:58:46.941545','evidencias/Captura_de_pantalla_2025-01-24_191842_RjhJotX.png','P','Gravisima',NULL,2,1),(4,'Se cay├│ el piso','2025-04-20 06:45:41.286701','','A','',3,3,1),(5,'Se cay├│ la pared','2025-04-20 07:09:31.879904','','P','',1,3,3),(6,'Se├▒ora','2025-04-20 07:46:43.891459','','P','',5,3,3),(7,'Ariana Pao Pao','2025-04-20 08:57:34.411272','','P','Gravisima',NULL,2,1),(8,'Prueba de listado','2025-04-20 09:39:06.187528','','P','',5,3,7);
/*!40000 ALTER TABLE `eduwave_app_novedad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eduwave_app_novedad_inventario`
--

DROP TABLE IF EXISTS `eduwave_app_novedad_inventario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eduwave_app_novedad_inventario` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `novedad_id` bigint NOT NULL,
  `inventario_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Eduwave_app_novedad_inve_novedad_id_inventario_id_c3cf75f5_uniq` (`novedad_id`,`inventario_id`),
  KEY `Eduwave_app_novedad__inventario_id_6aae0db7_fk_Eduwave_a` (`inventario_id`),
  CONSTRAINT `Eduwave_app_novedad__inventario_id_6aae0db7_fk_Eduwave_a` FOREIGN KEY (`inventario_id`) REFERENCES `eduwave_app_inventario` (`id`),
  CONSTRAINT `Eduwave_app_novedad__novedad_id_ca8a89be_fk_Eduwave_a` FOREIGN KEY (`novedad_id`) REFERENCES `eduwave_app_novedad` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eduwave_app_novedad_inventario`
--

LOCK TABLES `eduwave_app_novedad_inventario` WRITE;
/*!40000 ALTER TABLE `eduwave_app_novedad_inventario` DISABLE KEYS */;
INSERT INTO `eduwave_app_novedad_inventario` VALUES (1,4,2),(2,5,2),(3,6,2),(4,8,4);
/*!40000 ALTER TABLE `eduwave_app_novedad_inventario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eduwave_app_novedad_usuarios`
--

DROP TABLE IF EXISTS `eduwave_app_novedad_usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eduwave_app_novedad_usuarios` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `novedad_id` bigint NOT NULL,
  `usuario_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Eduwave_app_novedad_usuarios_novedad_id_usuario_id_0d8aa4d3_uniq` (`novedad_id`,`usuario_id`),
  KEY `Eduwave_app_novedad__usuario_id_c5229cd9_fk_Eduwave_a` (`usuario_id`),
  CONSTRAINT `Eduwave_app_novedad__novedad_id_e3ede7c1_fk_Eduwave_a` FOREIGN KEY (`novedad_id`) REFERENCES `eduwave_app_novedad` (`id`),
  CONSTRAINT `Eduwave_app_novedad__usuario_id_c5229cd9_fk_Eduwave_a` FOREIGN KEY (`usuario_id`) REFERENCES `eduwave_app_usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eduwave_app_novedad_usuarios`
--

LOCK TABLES `eduwave_app_novedad_usuarios` WRITE;
/*!40000 ALTER TABLE `eduwave_app_novedad_usuarios` DISABLE KEYS */;
INSERT INTO `eduwave_app_novedad_usuarios` VALUES (1,1,6),(5,3,2),(4,7,2);
/*!40000 ALTER TABLE `eduwave_app_novedad_usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eduwave_app_programaformacion`
--

DROP TABLE IF EXISTS `eduwave_app_programaformacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eduwave_app_programaformacion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `modalidad` varchar(1) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `red_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  KEY `Eduwave_app_programa_red_id_d22238be_fk_Eduwave_a` (`red_id`),
  CONSTRAINT `Eduwave_app_programa_red_id_d22238be_fk_Eduwave_a` FOREIGN KEY (`red_id`) REFERENCES `eduwave_app_red` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eduwave_app_programaformacion`
--

LOCK TABLES `eduwave_app_programaformacion` WRITE;
/*!40000 ALTER TABLE `eduwave_app_programaformacion` DISABLE KEYS */;
INSERT INTO `eduwave_app_programaformacion` VALUES (1,'P','ADSO-An├ílisis y Desarrollo De Software',1),(2,'P','Producci├│n multimedia',1),(3,'P','Plantas y hierbas',2);
/*!40000 ALTER TABLE `eduwave_app_programaformacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eduwave_app_red`
--

DROP TABLE IF EXISTS `eduwave_app_red`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eduwave_app_red` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `centro_formacion_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  KEY `Eduwave_app_red_centro_formacion_id_505e9349_fk_Eduwave_a` (`centro_formacion_id`),
  CONSTRAINT `Eduwave_app_red_centro_formacion_id_505e9349_fk_Eduwave_a` FOREIGN KEY (`centro_formacion_id`) REFERENCES `eduwave_app_centroformacion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eduwave_app_red`
--

LOCK TABLES `eduwave_app_red` WRITE;
/*!40000 ALTER TABLE `eduwave_app_red` DISABLE KEYS */;
INSERT INTO `eduwave_app_red` VALUES (1,'TICS',1),(2,'Agricultura',3);
/*!40000 ALTER TABLE `eduwave_app_red` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eduwave_app_regional`
--

DROP TABLE IF EXISTS `eduwave_app_regional`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eduwave_app_regional` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `codigo` varchar(2) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `codigo` (`codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eduwave_app_regional`
--

LOCK TABLES `eduwave_app_regional` WRITE;
/*!40000 ALTER TABLE `eduwave_app_regional` DISABLE KEYS */;
INSERT INTO `eduwave_app_regional` VALUES (1,'01','Cundinamarca'),(2,'02','Tolima');
/*!40000 ALTER TABLE `eduwave_app_regional` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eduwave_app_rol`
--

DROP TABLE IF EXISTS `eduwave_app_rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eduwave_app_rol` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `codigo` varchar(10) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `codigo` (`codigo`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eduwave_app_rol`
--

LOCK TABLES `eduwave_app_rol` WRITE;
/*!40000 ALTER TABLE `eduwave_app_rol` DISABLE KEYS */;
INSERT INTO `eduwave_app_rol` VALUES (1,'ADS','Administrador del Sistema','Usted es el admin'),(2,'APD','Aprendiz','Usted es un aprendiz'),(3,'INS','Instructor','Usted es el instructor'),(4,'ADE','Administrador De Edificios','Ed'),(5,'COO','Coordinador','Usted es el coordinador');
/*!40000 ALTER TABLE `eduwave_app_rol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eduwave_app_sede`
--

DROP TABLE IF EXISTS `eduwave_app_sede`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eduwave_app_sede` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `codigo` varchar(100) NOT NULL,
  `nombre` varchar(300) NOT NULL,
  `direccion` varchar(300) NOT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  `centro_formacion_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `codigo` (`codigo`),
  KEY `Eduwave_app_sede_centro_formacion_id_26fcb6ce_fk_Eduwave_a` (`centro_formacion_id`),
  CONSTRAINT `Eduwave_app_sede_centro_formacion_id_26fcb6ce_fk_Eduwave_a` FOREIGN KEY (`centro_formacion_id`) REFERENCES `eduwave_app_centroformacion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eduwave_app_sede`
--

LOCK TABLES `eduwave_app_sede` WRITE;
/*!40000 ALTER TABLE `eduwave_app_sede` DISABLE KEYS */;
INSERT INTO `eduwave_app_sede` VALUES (1,'01','Tecno Parque Cazuca','Calle 19','3208187272',1),(2,'02','Chicoral','Carrera 16 #15','3208187272',3),(3,'03','Sede-Ciudad verde','Calle 20','3208187233',1);
/*!40000 ALTER TABLE `eduwave_app_sede` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eduwave_app_subcategoria`
--

DROP TABLE IF EXISTS `eduwave_app_subcategoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eduwave_app_subcategoria` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `categoria_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Eduwave_app_subcateg_categoria_id_3e9088f9_fk_Eduwave_a` (`categoria_id`),
  CONSTRAINT `Eduwave_app_subcateg_categoria_id_3e9088f9_fk_Eduwave_a` FOREIGN KEY (`categoria_id`) REFERENCES `eduwave_app_categoria` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eduwave_app_subcategoria`
--

LOCK TABLES `eduwave_app_subcategoria` WRITE;
/*!40000 ALTER TABLE `eduwave_app_subcategoria` DISABLE KEYS */;
INSERT INTO `eduwave_app_subcategoria` VALUES (1,'Pared',1),(2,'Piso',1),(3,'Techo',1),(4,'silla',2),(5,'Mesa',2),(6,'Computador',3),(7,'Televisor',3),(8,'Balon',6);
/*!40000 ALTER TABLE `eduwave_app_subcategoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eduwave_app_tipoambiente`
--

DROP TABLE IF EXISTS `eduwave_app_tipoambiente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eduwave_app_tipoambiente` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(300) NOT NULL,
  `descripcion` varchar(450) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eduwave_app_tipoambiente`
--

LOCK TABLES `eduwave_app_tipoambiente` WRITE;
/*!40000 ALTER TABLE `eduwave_app_tipoambiente` DISABLE KEYS */;
INSERT INTO `eduwave_app_tipoambiente` VALUES (1,'Tecnologico','Tecnologico'),(2,'Deportivo','Deporte'),(3,'Salud','Area de  salud');
/*!40000 ALTER TABLE `eduwave_app_tipoambiente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eduwave_app_tiponovedad`
--

DROP TABLE IF EXISTS `eduwave_app_tiponovedad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eduwave_app_tiponovedad` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eduwave_app_tiponovedad`
--

LOCK TABLES `eduwave_app_tiponovedad` WRITE;
/*!40000 ALTER TABLE `eduwave_app_tiponovedad` DISABLE KEYS */;
INSERT INTO `eduwave_app_tiponovedad` VALUES (1,'Acad├®mica'),(3,'Ambiente'),(2,'Disciplinaria');
/*!40000 ALTER TABLE `eduwave_app_tiponovedad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eduwave_app_usuario`
--

DROP TABLE IF EXISTS `eduwave_app_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eduwave_app_usuario` (
  `id` bigint NOT NULL AUTO_INCREMENT,
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
  `tipo_doc` varchar(3) NOT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  `numero_doc` varchar(30) NOT NULL,
  `rol_id` bigint NOT NULL,
  `centro_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `numero_doc` (`numero_doc`),
  KEY `Eduwave_app_usuario_rol_id_d3f763f9_fk_Eduwave_app_rol_id` (`rol_id`),
  KEY `Eduwave_app_usuario_centro_id_72a897dc_fk_Eduwave_a` (`centro_id`),
  CONSTRAINT `Eduwave_app_usuario_centro_id_72a897dc_fk_Eduwave_a` FOREIGN KEY (`centro_id`) REFERENCES `eduwave_app_centroformacion` (`id`),
  CONSTRAINT `Eduwave_app_usuario_rol_id_d3f763f9_fk_Eduwave_app_rol_id` FOREIGN KEY (`rol_id`) REFERENCES `eduwave_app_rol` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eduwave_app_usuario`
--

LOCK TABLES `eduwave_app_usuario` WRITE;
/*!40000 ALTER TABLE `eduwave_app_usuario` DISABLE KEYS */;
INSERT INTO `eduwave_app_usuario` VALUES (1,'pbkdf2_sha256$870000$4epcu3DaJRzPwIT3iSyKO0$ovU8fsE4VLbQH4gUWZzATY/XxWVeToLvfddGugnU4/s=','2025-04-20 09:43:28.791352',0,'Robinson','Robinson',' Chaguala','chagualarobinson4@gmail.com',0,1,'2025-04-20 03:13:27.906292','CC','3208187277','1023374642',1,1),(2,'pbkdf2_sha256$870000$mkFuDzE53vcwZSQM7OhvBW$TYFFKl6bVBK61cUus8J13rlhPIRmwiDYUMbSZ/m6hF8=','2025-04-20 08:54:57.772855',0,'Ariana','Ariana','Luz','asdas@gmail.com',0,1,'2025-04-20 03:22:45.411479','TI','3208187271','1023374648',2,1),(3,'pbkdf2_sha256$870000$DYXN6A1KX20fnGuCNEgsej$x6jmNqNWMQmuv0lHHI2lknudktNlgM4I2UNGK/pCy9M=','2025-04-20 09:35:07.987911',0,'Michael','Michael','Quecano','michael@gmail.com',0,1,'2025-04-20 03:36:16.767326','CC','3208187272','1023374643',4,1),(4,'pbkdf2_sha256$870000$TJKlH8ki4EAg4YtiDX5diT$t8jWzYs59pJnRo/hdpmzqwzC1cRDeVJ1KJMggKiRKtQ=','2025-04-20 19:33:42.652439',0,'Luisa','Luisa','Campos','luisa@gmail.com',0,1,'2025-04-20 03:39:37.430351','CC','3208187274','1023374644',5,1),(5,'pbkdf2_sha256$870000$JjxhlnTYeFfeprROHeuGQa$nfAkey7ahHmSlOJliQIOP3DBI6zaafVREBDXagx7wSg=','2025-04-20 09:27:02.455777',0,'Lizeth','Lizeth','Diutama','Lizeth@gmail.com',0,1,'2025-04-20 03:47:48.442772','CC','3208187275','1023374645',3,1),(6,'pbkdf2_sha256$870000$2yGeSM2LXsHy3e7x8BLHw3$oHtrBFU7QdL2xjlacDCQzbHtWERxrMcxiR6bVi/r+zU=',NULL,0,'Danna','Danna','Ayala','danna@gmail.com',0,1,'2025-04-20 04:48:27.511152','CC','3208187279','1023374649',2,3),(7,'pbkdf2_sha256$870000$PbkgqkEGfv458oQFcsYz48$6Kj68PVP4e/yg46PSC6djKHVYr8QZ56cJXiZDITOulA=','2025-04-20 09:37:54.189557',0,'Emili','Emili','Chaguala','Emili@gmail.com',0,1,'2025-04-20 09:37:49.520906','CC','3208187279','1023374639',1,3);
/*!40000 ALTER TABLE `eduwave_app_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eduwave_app_usuario_fichas`
--

DROP TABLE IF EXISTS `eduwave_app_usuario_fichas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eduwave_app_usuario_fichas` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usuario_id` bigint NOT NULL,
  `ficha_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Eduwave_app_usuario_ficha_usuario_id_ficha_id_489004ea_uniq` (`usuario_id`,`ficha_id`),
  KEY `Eduwave_app_usuario__ficha_id_352a4ada_fk_Eduwave_a` (`ficha_id`),
  CONSTRAINT `Eduwave_app_usuario__ficha_id_352a4ada_fk_Eduwave_a` FOREIGN KEY (`ficha_id`) REFERENCES `eduwave_app_ficha` (`id`),
  CONSTRAINT `Eduwave_app_usuario__usuario_id_7116259a_fk_Eduwave_a` FOREIGN KEY (`usuario_id`) REFERENCES `eduwave_app_usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eduwave_app_usuario_fichas`
--

LOCK TABLES `eduwave_app_usuario_fichas` WRITE;
/*!40000 ALTER TABLE `eduwave_app_usuario_fichas` DISABLE KEYS */;
INSERT INTO `eduwave_app_usuario_fichas` VALUES (1,2,2),(2,5,1),(3,5,2),(4,6,3);
/*!40000 ALTER TABLE `eduwave_app_usuario_fichas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eduwave_app_usuario_groups`
--

DROP TABLE IF EXISTS `eduwave_app_usuario_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eduwave_app_usuario_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usuario_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Eduwave_app_usuario_groups_usuario_id_group_id_271d9722_uniq` (`usuario_id`,`group_id`),
  KEY `Eduwave_app_usuario_groups_group_id_64e6fe1c_fk_auth_group_id` (`group_id`),
  CONSTRAINT `Eduwave_app_usuario__usuario_id_78db1f4e_fk_Eduwave_a` FOREIGN KEY (`usuario_id`) REFERENCES `eduwave_app_usuario` (`id`),
  CONSTRAINT `Eduwave_app_usuario_groups_group_id_64e6fe1c_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eduwave_app_usuario_groups`
--

LOCK TABLES `eduwave_app_usuario_groups` WRITE;
/*!40000 ALTER TABLE `eduwave_app_usuario_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `eduwave_app_usuario_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eduwave_app_usuario_user_permissions`
--

DROP TABLE IF EXISTS `eduwave_app_usuario_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eduwave_app_usuario_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usuario_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Eduwave_app_usuario_user_usuario_id_permission_id_07cf8219_uniq` (`usuario_id`,`permission_id`),
  KEY `Eduwave_app_usuario__permission_id_c02a8ca2_fk_auth_perm` (`permission_id`),
  CONSTRAINT `Eduwave_app_usuario__permission_id_c02a8ca2_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `Eduwave_app_usuario__usuario_id_8e639f07_fk_Eduwave_a` FOREIGN KEY (`usuario_id`) REFERENCES `eduwave_app_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eduwave_app_usuario_user_permissions`
--

LOCK TABLES `eduwave_app_usuario_user_permissions` WRITE;
/*!40000 ALTER TABLE `eduwave_app_usuario_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `eduwave_app_usuario_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-20 22:41:37
