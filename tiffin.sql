-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 12, 2024 at 02:23 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `tiffin`
--

-- --------------------------------------------------------

--
-- Table structure for table `assign`
--

CREATE TABLE IF NOT EXISTS `assign` (
  `ssid` int(10) NOT NULL AUTO_INCREMENT,
  `ocid` int(10) NOT NULL,
  `sid` int(10) NOT NULL,
  PRIMARY KEY (`ssid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `assign`
--

INSERT INTO `assign` (`ssid`, `ocid`, `sid`) VALUES
(1, 1, 7),
(2, 1, 7);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_group`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_group_permissions`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=19 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_user`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_30a071c9_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_user_groups`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_user_user_permissions`
--


-- --------------------------------------------------------

--
-- Table structure for table `canteen`
--

CREATE TABLE IF NOT EXISTS `canteen` (
  `cnid` int(10) NOT NULL AUTO_INCREMENT,
  `cname` varchar(50) NOT NULL,
  `addr` varchar(100) NOT NULL,
  `city` varchar(50) NOT NULL,
  `district` varchar(40) NOT NULL,
  `pin` int(10) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `license` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,
  `amt` int(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`cnid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `canteen`
--

INSERT INTO `canteen` (`cnid`, `cname`, `addr`, `city`, `district`, `pin`, `phone`, `license`, `type`, `amt`, `email`) VALUES
(1, 'aryas', 'aryas hotel', 'Adoor', 'pathanamthitta', 232323, '1234567890', 'ff43333', '', 0, 'aryas@gmail.com'),
(3, 'asd', 'sdsd', 'Adoor', 'pathanamthitta', 123456, '1332343445', 'f23344', 'Vegetarian', 50, 'aa@gmail.com'),
(4, 'Bismi', 'Bismi hotel', 'Adoor', 'pathanamthitta', 756566, '4555555555', 'g5656565655', '', 0, 'bismi@gmail.com'),
(5, 'saravanas', 'saranavas hotel', 'Alappuzha', 'Alappuzha', 676655, '9876565656', 'Rh77565', 'Non-veg/veg', 50, 'saravanas@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_5151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_1c5f563_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `django_admin_log`
--


-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-02-28 06:39:32'),
(2, 'auth', '0001_initial', '2022-02-28 06:39:32'),
(3, 'admin', '0001_initial', '2022-02-28 06:39:32'),
(4, 'contenttypes', '0002_remove_content_type_name', '2022-02-28 06:39:32'),
(5, 'auth', '0002_alter_permission_name_max_length', '2022-02-28 06:39:32'),
(6, 'auth', '0003_alter_user_email_max_length', '2022-02-28 06:39:32'),
(7, 'auth', '0004_alter_user_username_opts', '2022-02-28 06:39:32'),
(8, 'auth', '0005_alter_user_last_login_null', '2022-02-28 06:39:32'),
(9, 'auth', '0006_require_contenttypes_0002', '2022-02-28 06:39:32'),
(10, 'sessions', '0001_initial', '2022-02-28 06:39:32');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('19737jvecwgoyrmlewxk9hovvihfpadt', 'N2ZmOTA1OGQzOWI0ZWY5NzcwYmE1NWQ5ODJjZTVhMTBmNDhmNWU4NTp7InR5cGUiOiJ1c2VyIiwiaWQiOjR9', '2022-11-21 07:34:17'),
('28kotfuwgebuulldiu609ifo7rlfncmx', 'YWIyODYxYzExOWZkNDA2ODZiYWU2ODQ0ZWEyOTNlZmMxNjJkZWJiZTp7InR5cGUiOiJhZG1pbiIsImlkIjoxfQ==', '2022-11-20 20:05:59'),
('29if2eyu78fzjy6370bapwiuh98q7w7n', 'ZGI3ZjVkZmJiODBmZGFmYjJiZDhkYmE3NmNmNmE2ZjdiY2VkODU1ODp7InR5cGUiOiJ1c2VyIiwiaWQiOjF9', '2022-04-23 16:34:16'),
('29wimv1t6kcmq5ags0drzgffwum1abig', 'eyJ1aWQiOjEsInV0eXBlIjoiY2FudGVlbiJ9:1rbv7k:Ysevv0WSUCihgXiehIujaLW5lCoPbvNC7Z-YpMmUtwM', '2024-03-04 04:19:24'),
('2ga2x0lgeul3f3jmq7y3o8j42hf3k6zz', 'ZGI3ZjVkZmJiODBmZGFmYjJiZDhkYmE3NmNmNmE2ZjdiY2VkODU1ODp7InR5cGUiOiJ1c2VyIiwiaWQiOjF9', '2022-04-24 15:08:28'),
('31vyi74mt1uldqag9h5ybg1wl6wemp27', 'NzM0MGNlNDEyMGMzODU0MzQzYjcxMWNlMTMzNmIwOTJkMWJjYmIxNDp7InR5cGUiOiJ1c2VyIiwiZW1haWwiOiJyZWV0aHVzaGFqaUBnbWFpbC5jb20iLCJpZCI6MX0=', '2022-04-23 05:42:43'),
('50xeiq65meam6e6y64q7acq2r91e5c28', 'eyJ1aWQiOjEsInV0eXBlIjoidXNlciJ9:1ptsbt:6PJ0DECYWHLN0BzKFTM9hc8OYqaswDR4ePwqRAZE8Dg', '2023-05-16 16:12:13'),
('63emwbn31nqkxu5rass6le9tar832up5', 'eyJ1aWQiOjEsInV0eXBlIjoidXNlciJ9:1py7yC:6WUgfjx42iAORWpghkwhRjWxF3E7GRaDNyeyuI_nfFo', '2023-05-28 09:24:48'),
('6ufrpxfatkjwgfgwp1r4d47ta8qylgpd', 'eyJ1aWQiOjEsInV0eXBlIjoidXNlciJ9:1puPOW:Dz_wywXugm_7XlGcefJkpY1977GnKBDvJm4LM4nGUfM', '2023-05-18 03:12:36'),
('6wpszqwey0em55su9vbhecbr4kznjmi2', 'eyJ1aWQiOjEsInV0eXBlIjoidXNlciIsInN0YXR1cyI6ImFwcHJvdmVkIn0:1rdShd:8hPU4vEWQmqa4F_HRi-4QehuVjKqchmRs2aNReaMdTA', '2024-03-08 10:22:49'),
('783hk250hu3ab54hhosk84us2ljmhtw5', 'YWIyODYxYzExOWZkNDA2ODZiYWU2ODQ0ZWEyOTNlZmMxNjJkZWJiZTp7InR5cGUiOiJhZG1pbiIsImlkIjoxfQ==', '2022-10-23 16:33:39'),
('7e8g1apy5dj6y29pj186kz9gcd4edjr2', 'eyJ1aWQiOjEsInV0eXBlIjoidXNlciIsInN0YXR1cyI6IiJ9:1rjchP:tsqSpxCazWGaZ6gabHuwAUbjtUKsiMgGPuoNyWfgAtA', '2024-03-25 10:16:03'),
('9stcvahc0q61ala5q20558sshqby1m8i', 'Mjg2ZjFiZjJmZWJlMzhlNmZjOThlZWIzMmI3NDE3YjQyOGI2ZjU2YTp7InR5cGUiOiJidWlsZGVyIiwiZW1haWwiOjF9', '2022-03-30 14:45:03'),
('b58fvauzd38xn2uodj9qyed5aum2tsan', 'eyJ1aWQiOjIsInV0eXBlIjoidXNlciIsInN0YXR1cyI6IiJ9:1rhTbE:7LGBwulZcaz-_PTUCR92r48Y7AHv44m2SCqQFhZ4grE', '2024-03-19 12:08:48'),
('c1dwdyttjlpkby76tmb7ypduk972xx54', 'eyJ1aWQiOjEsInV0eXBlIjoidXNlciJ9:1pzhdq:Yu8FM4ARlQRHYEPFPZ9EGeR0B1DqT4CGB67qW6eIPOc', '2023-06-01 17:42:18'),
('c629696y9dmdnkck7dca8w3dhg3t7prv', 'N2ZmOTA1OGQzOWI0ZWY5NzcwYmE1NWQ5ODJjZTVhMTBmNDhmNWU4NTp7InR5cGUiOiJ1c2VyIiwiaWQiOjR9', '2022-11-14 12:53:43'),
('ckpppm7gasnw2q8eyijfyghdtuoiiad6', 'eyJ1aWQiOjIsInV0eXBlIjoidXNlciIsInN0YXR1cyI6IiJ9:1rgHtx:-7LXVN4gz7BFrViWRCbsViFtIcvIgWmqx7GQSRs_I1c', '2024-03-16 05:27:13'),
('j1g6qx2dvi5t394a84hjp5fxxgf943vz', 'eyJ1aWQiOjIsInV0eXBlIjoidXNlciIsInN0YXR1cyI6IiJ9:1rfZqV:qkFjKQ2RLsOGdLmm5hC5mg5l80vUOZ51QdrberaFiIE', '2024-03-14 06:24:43'),
('kixcuakh7cx0rqv8a68axg5sly58jl25', 'eyJ1aWQiOjEsInV0eXBlIjoidXNlciJ9:1ovXDS:o4rAr0tY62A4tKKJwl8HL4Y4besW9kdeUVP5WIdbYQs', '2022-12-01 05:13:34'),
('l3en68gouea3k4kj8e82l1j4azgizjjm', 'eyJ1aWQiOjUsInV0eXBlIjoiY2FudGVlbiIsInN0YXR1cyI6ImFwcHJvdmVkIn0:1rirFZ:IUhhE9SYWQxW0_2YV1SeZRbrxRPX9T2XStBOXY76S54', '2024-03-23 07:36:09'),
('pvtblbwngoq056dyk43nz68vpcda0lbs', 'eyJ1aWQiOjIsInV0eXBlIjoidXNlciIsInN0YXR1cyI6IiJ9:1rg5HK:Y_rYTSki1mQsjtNVTExEPajZDPf9Wzh7Bf5wwv-Ksts', '2024-03-15 15:58:30'),
('qupq6i83w1qgqgwcl7kmx1stvnkrql78', 'N2ZmOTA1OGQzOWI0ZWY5NzcwYmE1NWQ5ODJjZTVhMTBmNDhmNWU4NTp7InR5cGUiOiJ1c2VyIiwiaWQiOjR9', '2022-11-21 06:51:04'),
('rk113xdeway6zrqyij6d47tfbnmpg5s0', 'N2ZmOTA1OGQzOWI0ZWY5NzcwYmE1NWQ5ODJjZTVhMTBmNDhmNWU4NTp7InR5cGUiOiJ1c2VyIiwiaWQiOjR9', '2022-11-21 04:29:45'),
('ruda6ve46lm7trr9m2qty3vwygmms8sl', 'YWIyODYxYzExOWZkNDA2ODZiYWU2ODQ0ZWEyOTNlZmMxNjJkZWJiZTp7InR5cGUiOiJhZG1pbiIsImlkIjoxfQ==', '2022-11-21 07:47:30'),
('sceoazvlj29xsus3vvmxhzhpjp1v6zml', 'eyJ1aWQiOjEsInV0eXBlIjoidXNlciJ9:1pyrke:_v-eq0uskinEUe_k1FThRcCzkXySx2lvVedRlggmCNQ', '2023-05-30 10:17:52'),
('ssyuhy2jndw4hbmw8jyh7xhd250b3tjz', 'eyJ1aWQiOjUsInV0eXBlIjoiY2FudGVlbiIsInN0YXR1cyI6ImFwcHJvdmVkIn0:1rh626:_jhRT4vp1hn14p2fzn8PUr_1mVRKRyMyPOWIXeNTgBE', '2024-03-18 10:58:58'),
('wfmszz9pidle9htjx7u6dywphlan8h0t', 'eyJ1aWQiOjAsInV0eXBlIjoiYWRtaW4ifQ:1puQGy:cszh9adoFPOnEjnboayMEephhxzRjFYl4r8cAhD7BJ4', '2023-05-18 04:08:52'),
('y7r1dzx455w2qtytbpixtmczgz75haxx', 'eyJ1aWQiOjEsInV0eXBlIjoidXNlciJ9:1rXD3E:gCs9jthZ2-LCXEHM9LR_3iVDMsDFFWctNIuS6-zfHVA', '2024-02-20 04:27:16'),
('zncj4alnj7ulrpdn1l8667ahnjuugsyo', 'YWIyODYxYzExOWZkNDA2ODZiYWU2ODQ0ZWEyOTNlZmMxNjJkZWJiZTp7InR5cGUiOiJhZG1pbiIsImlkIjoxfQ==', '2022-11-10 09:22:47');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE IF NOT EXISTS `feedback` (
  `fid` int(10) NOT NULL AUTO_INCREMENT,
  `cid` int(10) NOT NULL,
  `date` date NOT NULL,
  `Feedback` varchar(100) NOT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `feedback`
--


-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `lid` int(10) NOT NULL AUTO_INCREMENT,
  `uid` int(10) NOT NULL,
  `uname` varchar(50) NOT NULL,
  `upass` varchar(50) NOT NULL,
  `utype` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=18 ;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`lid`, `uid`, `uname`, `upass`, `utype`, `status`) VALUES
(1, 0, 'admin', 'admin', 'admin', ''),
(2, 1, 'alfi@gmail.com', 'alfi', 'user', ''),
(3, 1, 'aryas@gmail.com', 'aryas', 'canteen', 'approved'),
(4, 1, 'anju@gmail.com', 'anju', 'staff', ''),
(6, 2, 'k@gmail.com', '123', 'canteen', 'approved'),
(7, 3, 'malu@gmail.com', 'malu', 'staff', ''),
(8, 4, 'malu@gmail.com', 'malu', 'staff', 'Rejected'),
(10, 2, 'ammu@gmail.com', 'ammu', 'user', ''),
(11, 3, 'aa@gmail.com', '123', 'canteen', 'approved'),
(12, 6, 'athira@gmail.com', 'athira', 'staff', ''),
(13, 3, 'anjana@gmail.com', 'anjana', 'user', ''),
(14, 4, 'bismi@gmail.com', 'bismi', 'canteen', 'Rejected'),
(15, 5, 'saravanas@gmail.com', '123', 'canteen', 'approved'),
(16, 7, 'manu@gmail.com', 'manu', 'staff', ''),
(17, 1, 'alfi@gmail.com', 'alfi', 'user', '');

-- --------------------------------------------------------

--
-- Table structure for table `menu`
--

CREATE TABLE IF NOT EXISTS `menu` (
  `mid` int(10) NOT NULL AUTO_INCREMENT,
  `cnid` int(10) NOT NULL,
  `dish` varchar(50) NOT NULL,
  `dtype` varchar(50) NOT NULL,
  `category` varchar(50) NOT NULL,
  `details` varchar(100) NOT NULL,
  `amt` int(10) NOT NULL,
  PRIMARY KEY (`mid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `menu`
--

INSERT INTO `menu` (`mid`, `cnid`, `dish`, `dtype`, `category`, `details`, `amt`) VALUES
(1, 1, 'chappathi and veg curry', 'Breakfast', 'veg', 'nice', 40),
(2, 1, 'Biriyani', 'Lunch', 'Non-Veg', 'good', 100),
(3, 3, 'meals', 'Lunch', 'veg', 'good', 50),
(4, 3, 'chappathi', 'Breakfast', 'veg', 'dfdf', 40);

-- --------------------------------------------------------

--
-- Table structure for table `orderc`
--

CREATE TABLE IF NOT EXISTS `orderc` (
  `ocid` int(10) NOT NULL AUTO_INCREMENT,
  `cid` int(10) NOT NULL,
  `date` date NOT NULL,
  `cnid` int(10) NOT NULL,
  `dtype` varchar(100) NOT NULL,
  `address1` varchar(500) NOT NULL,
  `address2` varchar(500) NOT NULL,
  `address3` varchar(300) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`ocid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `orderc`
--

INSERT INTO `orderc` (`ocid`, `cid`, `date`, `cnid`, `dtype`, `address1`, `address2`, `address3`, `status`) VALUES
(1, 1, '2024-03-10', 5, 'Breakfast,Lunch,Dinner', 'alfiya villa,adoor,Pathanamthitta,691234', 'Strato Infotech,town plaza building,adoor p.o,6789', 'alfiya villa,adoor,Pathanamthitta,691234', 'assigned');

-- --------------------------------------------------------

--
-- Table structure for table `payc`
--

CREATE TABLE IF NOT EXISTS `payc` (
  `pcid` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(10) NOT NULL,
  `cnid` int(10) NOT NULL,
  `date` date NOT NULL,
  `month` int(10) NOT NULL,
  `amount` int(10) NOT NULL,
  PRIMARY KEY (`pcid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `payc`
--


-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE IF NOT EXISTS `payment` (
  `pid` int(10) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `cnid` int(11) NOT NULL,
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `edate` date NOT NULL,
  `amt` int(10) NOT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`pid`, `uid`, `cnid`, `fname`, `lname`, `edate`, `amt`) VALUES
(1, 1, 5, 'Alfiya', 'Nizam', '2024-04-06', 1000),
(2, 1, 5, 'Alfi', 's', '2024-04-06', 1000);

-- --------------------------------------------------------

--
-- Table structure for table `request`
--

CREATE TABLE IF NOT EXISTS `request` (
  `rqid` int(10) NOT NULL AUTO_INCREMENT,
  `rqdate` date NOT NULL,
  `cnid` int(10) NOT NULL,
  `cid` int(10) NOT NULL,
  `status` varchar(40) NOT NULL,
  `pstatus` varchar(50) NOT NULL,
  PRIMARY KEY (`rqid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `request`
--

INSERT INTO `request` (`rqid`, `rqdate`, `cnid`, `cid`, `status`, `pstatus`) VALUES
(1, '2024-03-11', 5, 1, 'Approved', 'advpaid');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE IF NOT EXISTS `staff` (
  `sid` int(10) NOT NULL AUTO_INCREMENT,
  `sname` varchar(50) NOT NULL,
  `adr` varchar(100) NOT NULL,
  `district` varchar(50) NOT NULL,
  `pin` int(10) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `dob` date NOT NULL,
  `doj` date NOT NULL,
  `cnid` int(10) NOT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`sid`, `sname`, `adr`, `district`, `pin`, `phone`, `email`, `gender`, `dob`, `doj`, `cnid`) VALUES
(1, 'Anju', 'anju villa', 'pathanamthitta', 453535, '2324234343', 'anju@gmail.com', 'Male', '1997-06-23', '2024-01-01', 1),
(4, 'Malu', 'malu villa', 'Alappuzha', 235555, '6566777777', 'malu@gmail.com', 'Male', '2000-05-08', '2023-01-01', 2),
(6, 'athira', 'athiraffff', 'Alappuzha', 234556, '9987878677', 'athira@gmail.com', 'Male', '2000-02-13', '2024-02-01', 3),
(7, 'Manu', 'Manu villa', 'Alappuzha', 665676, '5767454665', 'manu@gmail.com', 'Male', '2000-03-09', '2023-03-01', 5);

-- --------------------------------------------------------

--
-- Table structure for table `timetable`
--

CREATE TABLE IF NOT EXISTS `timetable` (
  `did` int(10) NOT NULL AUTO_INCREMENT,
  `cnid` int(10) NOT NULL,
  `day` varchar(50) NOT NULL,
  `breakfast` varchar(50) NOT NULL,
  `lunch` varchar(50) NOT NULL,
  `dinner` varchar(50) NOT NULL,
  PRIMARY KEY (`did`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=15 ;

--
-- Dumping data for table `timetable`
--

INSERT INTO `timetable` (`did`, `cnid`, `day`, `breakfast`, `lunch`, `dinner`) VALUES
(1, 3, 'Monday', 'appam', 'meals', 'chappathi'),
(2, 3, 'Tuesday', 'uppumav', 'meals', 'rice and curry'),
(3, 3, 'Wednesday', 'dosha', 'meals', 'chappathi'),
(4, 3, 'Thursday', 'idli', 'meals', 'rice and curry'),
(5, 3, 'Friday', 'putt and kadala', 'meals', 'chappathi.'),
(6, 3, 'Saturday', 'uppumav', 'rice and curry', 'chappathi'),
(7, 3, 'sunday', 'porotta', 'veg biriyani', 'chappathi'),
(8, 5, 'Monday', 'appam', 'meals', 'chappathi'),
(9, 5, 'Tuesday', 'uppumav', 'rice and curry', 'chappathi'),
(10, 5, 'Wednesday', 'dosha', 'meals', 'chappathi.'),
(11, 5, 'Thursday', 'idli', 'meals', 'rice and curry'),
(12, 5, 'Friday', 'putt and kadala', 'meals', 'rice and curry'),
(13, 5, 'Saturday', 'appam', 'meals', 'chappathi.'),
(14, 5, 'sunday', 'porotta', 'Chicken biriyani', 'chappathi');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `cid` int(10) NOT NULL AUTO_INCREMENT,
  `cname` varchar(50) NOT NULL,
  `adr` varchar(50) NOT NULL,
  `office` varchar(50) NOT NULL,
  `phn` varchar(10) NOT NULL,
  `em` varchar(100) NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`cid`, `cname`, `adr`, `office`, `phn`, `em`) VALUES
(1, 'Alfiya', 'alfiya villa,adoor,Pathanamthitta,691234', 'Strato Infotech,town plaza building,adoor p.o,6789', '9767886553', 'alfi@gmail.com');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissions_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_group_permissions_ibfk_2` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_ibfk_1` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permissions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_ibfk_2` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `django_admin_log_ibfk_2` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);
