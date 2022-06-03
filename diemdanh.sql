-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 31, 2022 at 06:05 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.3.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `diemdanh`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_customuser'),
(22, 'Can change user', 6, 'change_customuser'),
(23, 'Can delete user', 6, 'delete_customuser'),
(24, 'Can view user', 6, 'view_customuser'),
(25, 'Can add giang vien', 7, 'add_giangvien'),
(26, 'Can change giang vien', 7, 'change_giangvien'),
(27, 'Can delete giang vien', 7, 'delete_giangvien'),
(28, 'Can view giang vien', 7, 'view_giangvien'),
(29, 'Can add khoa', 8, 'add_khoa'),
(30, 'Can change khoa', 8, 'change_khoa'),
(31, 'Can delete khoa', 8, 'delete_khoa'),
(32, 'Can view khoa', 8, 'view_khoa'),
(33, 'Can add mon hoc', 9, 'add_monhoc'),
(34, 'Can change mon hoc', 9, 'change_monhoc'),
(35, 'Can delete mon hoc', 9, 'delete_monhoc'),
(36, 'Can view mon hoc', 9, 'view_monhoc'),
(37, 'Can add sinh vien', 10, 'add_sinhvien'),
(38, 'Can change sinh vien', 10, 'change_sinhvien'),
(39, 'Can delete sinh vien', 10, 'delete_sinhvien'),
(40, 'Can view sinh vien', 10, 'view_sinhvien'),
(41, 'Can add vector dac trung', 11, 'add_vectordactrung'),
(42, 'Can change vector dac trung', 11, 'change_vectordactrung'),
(43, 'Can delete vector dac trung', 11, 'delete_vectordactrung'),
(44, 'Can view vector dac trung', 11, 'view_vectordactrung'),
(45, 'Can add lop hoc phan', 12, 'add_lophocphan'),
(46, 'Can change lop hoc phan', 12, 'change_lophocphan'),
(47, 'Can delete lop hoc phan', 12, 'delete_lophocphan'),
(48, 'Can view lop hoc phan', 12, 'view_lophocphan'),
(49, 'Can add diem danh', 13, 'add_diemdanh'),
(50, 'Can change diem danh', 13, 'change_diemdanh'),
(51, 'Can delete diem danh', 13, 'delete_diemdanh'),
(52, 'Can view diem danh', 13, 'view_diemdanh'),
(53, 'Can add anh nhan dien', 14, 'add_anhnhandien'),
(54, 'Can change anh nhan dien', 14, 'change_anhnhandien'),
(55, 'Can delete anh nhan dien', 14, 'delete_anhnhandien'),
(56, 'Can view anh nhan dien', 14, 'view_anhnhandien'),
(57, 'Can add admin hod', 15, 'add_adminhod'),
(58, 'Can change admin hod', 15, 'change_adminhod'),
(59, 'Can delete admin hod', 15, 'delete_adminhod'),
(60, 'Can view admin hod', 15, 'view_adminhod');

-- --------------------------------------------------------

--
-- Table structure for table `base_adminhod`
--

CREATE TABLE `base_adminhod` (
  `id` int(11) NOT NULL,
  `admin_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `base_anhnhandien`
--

CREATE TABLE `base_anhnhandien` (
  `id` int(11) NOT NULL,
  `embeddings` longtext NOT NULL,
  `sinhvien_id` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `base_customuser`
--

CREATE TABLE `base_customuser` (
  `id` bigint(20) NOT NULL,
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
  `user_type` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `base_customuser_groups`
--

CREATE TABLE `base_customuser_groups` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `base_customuser_user_permissions`
--

CREATE TABLE `base_customuser_user_permissions` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `base_diemdanh`
--

CREATE TABLE `base_diemdanh` (
  `id` int(11) NOT NULL,
  `buoi_1` tinyint(1) NOT NULL,
  `buoi_2` tinyint(1) NOT NULL,
  `buoi_3` tinyint(1) NOT NULL,
  `buoi_4` tinyint(1) NOT NULL,
  `buoi_5` tinyint(1) NOT NULL,
  `buoi_6` tinyint(1) NOT NULL,
  `buoi_7` tinyint(1) NOT NULL,
  `buoi_8` tinyint(1) NOT NULL,
  `buoi_9` tinyint(1) NOT NULL,
  `buoi_10` tinyint(1) NOT NULL,
  `buoi_11` tinyint(1) NOT NULL,
  `buoi_12` tinyint(1) NOT NULL,
  `buoi_13` tinyint(1) NOT NULL,
  `buoi_14` tinyint(1) NOT NULL,
  `buoi_15` tinyint(1) NOT NULL,
  `lophocphan_id` varchar(20) NOT NULL,
  `sinhvien_id` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_diemdanh`
--

INSERT INTO `base_diemdanh` (`id`, `buoi_1`, `buoi_2`, `buoi_3`, `buoi_4`, `buoi_5`, `buoi_6`, `buoi_7`, `buoi_8`, `buoi_9`, `buoi_10`, `buoi_11`, `buoi_12`, `buoi_13`, `buoi_14`, `buoi_15`, `lophocphan_id`, `sinhvien_id`) VALUES
(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '1', '102190267'),
(2, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, '1', '102190281');

-- --------------------------------------------------------

--
-- Table structure for table `base_giangvien`
--

CREATE TABLE `base_giangvien` (
  `id` varchar(10) NOT NULL,
  `gioitinh` varchar(3) NOT NULL,
  `khoa_id` varchar(10) DEFAULT NULL,
  `user_type_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_giangvien`
--

INSERT INTO `base_giangvien` (`id`, `gioitinh`, `khoa_id`, `user_type_id`) VALUES
('1', 'Nu', 'K01', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `base_khoa`
--

CREATE TABLE `base_khoa` (
  `id` varchar(10) NOT NULL,
  `tenkhoa` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_khoa`
--

INSERT INTO `base_khoa` (`id`, `tenkhoa`) VALUES
('K01', 'Công nghệ thông tin');

-- --------------------------------------------------------

--
-- Table structure for table `base_lophocphan`
--

CREATE TABLE `base_lophocphan` (
  `id` varchar(20) NOT NULL,
  `ten_lophp` varchar(255) NOT NULL,
  `kyhoc` varchar(255) NOT NULL,
  `giangvien_id` varchar(10) NOT NULL,
  `mon_id` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_lophocphan`
--

INSERT INTO `base_lophocphan` (`id`, `ten_lophp`, `kyhoc`, `giangvien_id`, `mon_id`) VALUES
('1', 'Xác suất thống kê', 'I/2021-2022', '1', '1');

-- --------------------------------------------------------

--
-- Table structure for table `base_monhoc`
--

CREATE TABLE `base_monhoc` (
  `id` varchar(20) NOT NULL,
  `ten_mon` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_monhoc`
--

INSERT INTO `base_monhoc` (`id`, `ten_mon`) VALUES
('1', 'Xác suất thống kê');

-- --------------------------------------------------------

--
-- Table structure for table `base_sinhvien`
--

CREATE TABLE `base_sinhvien` (
  `id` varchar(10) NOT NULL,
  `ten_sv` varchar(128) NOT NULL,
  `gioitinh` varchar(3) NOT NULL,
  `anhthe` longtext DEFAULT NULL,
  `khoa_id` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_sinhvien`
--

INSERT INTO `base_sinhvien` (`id`, `ten_sv`, `gioitinh`, `anhthe`, `khoa_id`) VALUES
('102190057', 'Trương Quang Định', 'Nam', NULL, 'K01'),
('102190086', 'Huỳnh Phú Quý', 'Nam', NULL, NULL),
('102190267', 'Nguyễn Thị Quỳnh Hương', 'F', NULL, 'K01'),
('102190281', 'Ông Nguyễn Uyên Nhi', 'F', NULL, 'K01');

-- --------------------------------------------------------

--
-- Table structure for table `base_vectordactrung`
--

CREATE TABLE `base_vectordactrung` (
  `id` int(11) NOT NULL,
  `vector_dt` longtext NOT NULL,
  `sinhvien_id` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_vectordactrung`
--

INSERT INTO `base_vectordactrung` (`id`, `vector_dt`, `sinhvien_id`) VALUES
(39, '-0.07466856//0.054760657//-0.11898182//0.004770991//-0.026411679//0.04672527//0.023708899//-0.020877574//-0.057982128//0.11964642//-0.0085530775//-0.029388625//0.027733723//0.0027169308//-0.10380839//-0.10220529//-0.078408234//-0.06787571//-0.07373386//0.021842044//-0.05539342//-0.13076548//0.026163174//0.0139188925//0.13287075//-0.154736//0.016279979//0.20288946//-0.0018595848//-0.14031579//0.027970327//0.14267968//-0.011060642//0.104132324//0.011953219//-0.117849246//-0.007547372//0.005621134//-0.17717488//0.035054136//-0.089411154//-0.06902364//0.01483383//-0.04800626//0.036304016//0.07719033//-0.17585732//0.06883892//-0.034147628//-0.06159316//0.10287405//0.026321668//0.045111567//-0.06041746//0.0056654965//-0.12163711//-0.1487068//0.096640944//-0.105143145//0.016788885//-0.0109601775//-0.13369048//-0.06304797//-0.033078536//-0.111501925//-0.0968059//0.0953885//0.09031895//0.01759608//0.084518395//-0.002175323//0.00891685//-0.040421538//-0.064744614//0.055420734//-0.088341735//0.15554003//-0.013686491//-0.016177028//-0.109225586//0.03807677//0.009790166//0.017951647//-0.11556002//-0.0009882012//0.061984167//0.0027705003//-0.025564024//-0.0065017296//0.044099554//-0.057795156//-0.0095729//-0.18823656//-0.048627384//-0.03051646//-0.015627295//-0.0741372//-0.19581026//0.032678254//-0.07704086//0.08298041//0.053167425//-0.13583164//-0.17923822//-0.011901852//0.0064259097//0.035795536//0.049785204//-0.029154044//0.21396038//0.0013275677//0.1290672//-0.019751642//-0.023323132//-0.078751095//-0.022286126//0.0012564798//-0.15518215//0.054800723//-0.001349029//-0.09422988//-0.1287683//-0.13335143//0.052869905//-0.0076976432//-0.100870065//0.0897843//0.16172607//', '102190281'),
(40, '-0.08279744//0.05147478//-0.11049533//-0.008197809//-0.074111864//0.02676411//0.040306203//-0.00021061761//-0.019829802//0.10005121//-0.016531346//-0.02883025//0.010389743//0.0066323886//-0.010083402//-0.109709084//-0.084954664//-0.11155846//-0.0105669955//0.0353441//-0.015022693//-0.09653259//0.039690036//0.09579586//0.120565355//-0.084477775//0.041745383//0.22194509//0.097709954//-0.120144546//-0.0052418066//0.10762052//-0.012228075//0.0033380548//-0.02563571//-0.024922773//-0.0040828995//-0.008069212//-0.281256//0.06366903//-0.12368234//-0.037439793//0.05757593//-0.011206164//0.017532315//0.040000875//-0.2377601//-7.973107e-05//0.045303542//-0.08234701//-0.012497751//0.025537936//0.038312//-0.077546366//0.040184118//-0.121080525//-0.082960784//0.099118404//-0.06919969//0.0061314367//0.013375775//-0.14351267//-0.0403374//-0.078268215//-0.1325026//-0.08206536//0.03556211//0.08259851//0.100282736//0.079571225//-0.021584183//0.07679773//-0.028249452//-0.15001807//0.042083234//-0.06695171//0.07700785//0.009848384//0.030079897//-0.0626907//0.042640522//-0.030287787//-0.031419028//-0.024246423//0.05411503//0.041072533//-0.03560837//0.0012811861//-0.010261921//-0.06003096//-0.13849466//0.06742667//-0.22782932//-0.059317317//0.0022124466//0.041760806//-0.048157472//-0.16646393//0.09271776//-0.05716923//0.05087098//0.1827792//-0.16521257//-0.18139918//-0.008646881//0.029798185//0.11004713//0.022300504//0.034563616//0.18690534//0.023446444//0.07545084//-0.038230356//-0.008883671//-0.10684603//0.06171019//-0.040145878//-0.08826646//0.059480652//0.014760995//-0.14106867//-0.07979275//-0.13674966//-0.056980938//-0.017490998//-0.005188186//0.056087837//0.14197047//', '102190281'),
(41, '-0.08556157//0.017740678//-0.116883144//-0.012233244//-0.042649303//0.01990909//0.053816035//0.029428327//-0.03755816//0.11046338//0.003291999//-0.06238459//0.004428783//0.013723515//-0.0031085429//-0.07052586//-0.09383051//-0.11268407//-0.06141057//0.05088579//-0.018767025//-0.111694306//0.07429308//0.12214368//0.0884397//-0.024152223//0.04084121//0.20123537//0.08514315//-0.099636056//-0.047404304//0.08847213//-0.025030952//0.06512704//0.017763212//-0.07539336//0.035771016//0.011312865//-0.25438577//0.055579513//-0.08476275//-0.03919285//0.114909224//-0.055902284//0.020192457//0.032728747//-0.16498677//0.022294473//-0.015884485//-0.0824158//0.03875322//-0.001223279//0.115825586//-0.051305987//0.034255642//-0.14953814//-0.08748988//0.004638024//-0.07351586//-0.03529618//0.00938832//-0.13072908//-0.08422718//-0.06016791//-0.12962711//-0.11873848//0.12682562//0.1445382//0.051647257//0.16072239//-0.019449754//0.08390305//-0.036438394//-0.14573824//0.025636569//-0.030992795//0.064716116//0.03987104//-0.039247844//-0.13921168//0.07630058//0.0026105987//-0.013105007//-0.021086741//0.02715461//0.0071204063//-0.02521443//-0.051486976//-0.047129855//-0.06450245//-0.12822847//0.049175657//-0.10897352//-0.060254477//-0.08719476//0.0013497218//-0.031779233//-0.17332885//0.033688784//-0.006928238//0.032586876//0.14211023//-0.1111764//-0.13514969//0.023912027//0.07641862//0.119838536//0.017819285//0.0251497//0.16288733//-0.03607503//0.043673888//0.011468173//0.024097798//-0.11364614//0.10322173//-0.026187422//-0.15052757//0.03690055//-0.012737543//-0.14966153//-0.16346106//-0.099201724//-0.04161256//-0.02336762//-0.038798526//0.07847333//0.12476207//', '102190281'),
(42, '-0.13190891//-0.010172175//-0.1293159//-0.06921753//0.01580401//0.024952918//-0.06610385//-0.05489763//-0.09828578//0.14607827//-0.042928293//0.041122608//0.00407327//0.082029566//-0.053908736//-0.038835347//-0.07067764//-0.072919056//-0.05226839//0.06598534//-0.07991612//-0.04803873//-0.011218888//0.04137855//0.15724283//-0.10437578//0.0025100566//0.30363744//0.034978762//-0.03210001//0.06623552//0.012364739//-0.043925274//0.10206267//0.014441106//-0.048008032//0.009081884//-0.020169858//-0.15450922//0.068343475//-0.06465007//0.0027575076//0.084802754//0.006787799//0.03950991//0.060619105//-0.21074624//0.10579056//-0.0017426376//-0.12999158//-0.02037526//0.05295123//0.0394832//0.035326667//-0.046021935//-0.117104955//-0.10292756//0.12561488//-0.08150781//-0.036846906//0.042835593//-0.13887288//-0.13516958//-0.0469524//-0.07066698//-0.15627645//0.10568997//0.1339009//0.08394694//0.03931572//-0.031062996//0.07316412//0.05288119//-0.1268787//0.056785602//-0.12416027//0.0853851//0.016691739//-0.037022445//-0.033468045//0.025235295//0.008484054//0.019131357//0.010485708//-0.04909156//0.05247758//-0.023032282//-0.07322848//0.01596841//-0.035959046//-0.11791732//-0.049950182//-0.18809216//-0.010128066//-0.030040538//0.04208487//-0.00948981//-0.100769304//0.025174318//-0.013100117//0.06805231//-0.032999966//-0.1806785//-0.15562248//0.07153377//0.012622507//0.06720388//0.12482191//0.028360212//0.22819465//-0.0020863677//0.1389978//-0.0032884025//-0.036878567//-0.08020321//-0.020715084//0.037526563//-0.09119044//0.06414517//-0.0031659494//-0.10942987//-0.11416228//-0.12936346//0.03700546//0.04243202//-0.010914674//0.13726969//0.1438954//', '102190281'),
(43, '-0.14855656//0.060368408//-0.10535314//-0.022715766//-0.08489545//0.064976834//-0.043591555//-0.012014106//0.058633994//-0.056361776//0.14619237//-0.012355435//0.01756801//0.06453435//-0.13887286//-0.15491287//-0.15021989//-0.006611187//-0.04934343//0.053921156//-0.03620444//-0.16699241//0.026381535//0.113116294//0.18876332//-0.124093145//-0.019862348//0.1081543//-0.0052009127//-0.032272115//-0.0089497715//0.2599659//0.0011315754//0.010469244//-0.023055548//-0.1352974//-0.06832292//-0.12242245//-0.20539717//0.0063255914//-0.09072736//-0.012818656//0.04906896//-0.038145363//0.047899473//-0.07745377//-0.13218585//-0.07411582//-0.0057725925//-0.055975445//0.043511316//0.034772374//-0.009739285//-0.08512405//-0.07891261//0.015067074//-0.068518564//0.049616307//-0.18725735//-0.07603179//-0.01045345//-0.1823831//-0.043791946//-0.035260953//-0.05651595//-0.13705738//0.022729553//0.12724622//-0.034716614//0.0034595935//-0.011208909//0.03535588//0.0073603755//-0.028929925//-0.0136826495//-0.046224903//0.09580853//-0.039825004//0.11132185//-0.16482452//0.037675973//-0.054155365//-0.014555797//-0.18982467//-0.009055163//0.047056735//-0.039699174//-0.013777152//-0.000179475//0.027653255//-0.02469013//0.017863005//-0.09867602//-0.025001071//-0.01468529//-0.044880718//0.06024849//-0.1540839//-0.010028876//-0.09150532//0.08135772//0.120788984//-0.037115864//-0.15973847//-0.05371644//-0.010738401//0.059026036//0.009541038//-0.029258614//0.10424485//0.05196394//0.09322151//-0.04385705//0.0002506276//-0.09553839//0.017782373//0.0068738502//-0.013374526//-0.048776828//0.043678332//-0.16053973//-0.14596562//-0.15690935//-0.010821638//-0.083737805//0.01061677//0.046621483//0.0928745//', '102190281');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(15, 'base', 'adminhod'),
(14, 'base', 'anhnhandien'),
(6, 'base', 'customuser'),
(13, 'base', 'diemdanh'),
(7, 'base', 'giangvien'),
(8, 'base', 'khoa'),
(12, 'base', 'lophocphan'),
(9, 'base', 'monhoc'),
(10, 'base', 'sinhvien'),
(11, 'base', 'vectordactrung'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-05-05 13:30:08.346600'),
(2, 'contenttypes', '0002_remove_content_type_name', '2022-05-05 13:30:08.434357'),
(3, 'auth', '0001_initial', '2022-05-05 13:30:08.815316'),
(4, 'auth', '0002_alter_permission_name_max_length', '2022-05-05 13:30:08.905265'),
(5, 'auth', '0003_alter_user_email_max_length', '2022-05-05 13:30:08.918220'),
(6, 'auth', '0004_alter_user_username_opts', '2022-05-05 13:30:08.929672'),
(7, 'auth', '0005_alter_user_last_login_null', '2022-05-05 13:30:08.941806'),
(8, 'auth', '0006_require_contenttypes_0002', '2022-05-05 13:30:08.948606'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2022-05-05 13:30:08.958386'),
(10, 'auth', '0008_alter_user_username_max_length', '2022-05-05 13:30:08.970383'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2022-05-05 13:30:08.982107'),
(12, 'auth', '0010_alter_group_name_max_length', '2022-05-05 13:30:09.004351'),
(13, 'auth', '0011_update_proxy_permissions', '2022-05-05 13:30:09.017338'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2022-05-05 13:30:09.027352'),
(15, 'base', '0001_initial', '2022-05-05 13:30:10.582432'),
(16, 'admin', '0001_initial', '2022-05-05 13:30:10.758334'),
(17, 'admin', '0002_logentry_remove_auto_add', '2022-05-05 13:30:10.771679'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2022-05-05 13:30:10.787596'),
(19, 'sessions', '0001_initial', '2022-05-05 13:30:10.839860');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `base_adminhod`
--
ALTER TABLE `base_adminhod`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `admin_id` (`admin_id`);

--
-- Indexes for table `base_anhnhandien`
--
ALTER TABLE `base_anhnhandien`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_anhnhandien_sinhvien_id_1d0b47fe_fk_base_sinhvien_id` (`sinhvien_id`);

--
-- Indexes for table `base_customuser`
--
ALTER TABLE `base_customuser`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `base_customuser_groups`
--
ALTER TABLE `base_customuser_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `base_customuser_groups_customuser_id_group_id_d4e28d0b_uniq` (`customuser_id`,`group_id`),
  ADD KEY `base_customuser_groups_group_id_d1822349_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `base_customuser_user_permissions`
--
ALTER TABLE `base_customuser_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `base_customuser_user_per_customuser_id_permission_90414b11_uniq` (`customuser_id`,`permission_id`),
  ADD KEY `base_customuser_user_permission_id_e62eddd3_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `base_diemdanh`
--
ALTER TABLE `base_diemdanh`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_diemdanh_lophocphan_id_e1278deb_fk_base_lophocphan_id` (`lophocphan_id`),
  ADD KEY `base_diemdanh_sinhvien_id_62b1f6b9_fk_base_sinhvien_id` (`sinhvien_id`);

--
-- Indexes for table `base_giangvien`
--
ALTER TABLE `base_giangvien`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_type_id` (`user_type_id`),
  ADD KEY `base_giangvien_khoa_id_a6228803_fk_base_khoa_id` (`khoa_id`);

--
-- Indexes for table `base_khoa`
--
ALTER TABLE `base_khoa`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `base_lophocphan`
--
ALTER TABLE `base_lophocphan`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_lophocphan_giangvien_id_7979c118_fk_base_giangvien_id` (`giangvien_id`),
  ADD KEY `base_lophocphan_mon_id_817e3550_fk_base_monhoc_id` (`mon_id`);

--
-- Indexes for table `base_monhoc`
--
ALTER TABLE `base_monhoc`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `base_sinhvien`
--
ALTER TABLE `base_sinhvien`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_sinhvien_khoa_id_d617bb57_fk_base_khoa_id` (`khoa_id`);

--
-- Indexes for table `base_vectordactrung`
--
ALTER TABLE `base_vectordactrung`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_vectordactrung_sinhvien_id_4c5787ef_fk_base_sinhvien_id` (`sinhvien_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_base_customuser_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `base_adminhod`
--
ALTER TABLE `base_adminhod`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `base_anhnhandien`
--
ALTER TABLE `base_anhnhandien`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `base_customuser`
--
ALTER TABLE `base_customuser`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `base_customuser_groups`
--
ALTER TABLE `base_customuser_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `base_customuser_user_permissions`
--
ALTER TABLE `base_customuser_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `base_diemdanh`
--
ALTER TABLE `base_diemdanh`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `base_vectordactrung`
--
ALTER TABLE `base_vectordactrung`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `base_adminhod`
--
ALTER TABLE `base_adminhod`
  ADD CONSTRAINT `base_adminhod_admin_id_88ea4c3b_fk_base_customuser_id` FOREIGN KEY (`admin_id`) REFERENCES `base_customuser` (`id`);

--
-- Constraints for table `base_anhnhandien`
--
ALTER TABLE `base_anhnhandien`
  ADD CONSTRAINT `base_anhnhandien_sinhvien_id_1d0b47fe_fk_base_sinhvien_id` FOREIGN KEY (`sinhvien_id`) REFERENCES `base_sinhvien` (`id`);

--
-- Constraints for table `base_customuser_groups`
--
ALTER TABLE `base_customuser_groups`
  ADD CONSTRAINT `base_customuser_grou_customuser_id_04d7166b_fk_base_cust` FOREIGN KEY (`customuser_id`) REFERENCES `base_customuser` (`id`),
  ADD CONSTRAINT `base_customuser_groups_group_id_d1822349_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `base_customuser_user_permissions`
--
ALTER TABLE `base_customuser_user_permissions`
  ADD CONSTRAINT `base_customuser_user_customuser_id_4f46199a_fk_base_cust` FOREIGN KEY (`customuser_id`) REFERENCES `base_customuser` (`id`),
  ADD CONSTRAINT `base_customuser_user_permission_id_e62eddd3_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `base_diemdanh`
--
ALTER TABLE `base_diemdanh`
  ADD CONSTRAINT `base_diemdanh_lophocphan_id_e1278deb_fk_base_lophocphan_id` FOREIGN KEY (`lophocphan_id`) REFERENCES `base_lophocphan` (`id`),
  ADD CONSTRAINT `base_diemdanh_sinhvien_id_62b1f6b9_fk_base_sinhvien_id` FOREIGN KEY (`sinhvien_id`) REFERENCES `base_sinhvien` (`id`);

--
-- Constraints for table `base_giangvien`
--
ALTER TABLE `base_giangvien`
  ADD CONSTRAINT `base_giangvien_khoa_id_a6228803_fk_base_khoa_id` FOREIGN KEY (`khoa_id`) REFERENCES `base_khoa` (`id`),
  ADD CONSTRAINT `base_giangvien_user_type_id_afa74937_fk_base_customuser_id` FOREIGN KEY (`user_type_id`) REFERENCES `base_customuser` (`id`);

--
-- Constraints for table `base_lophocphan`
--
ALTER TABLE `base_lophocphan`
  ADD CONSTRAINT `base_lophocphan_giangvien_id_7979c118_fk_base_giangvien_id` FOREIGN KEY (`giangvien_id`) REFERENCES `base_giangvien` (`id`),
  ADD CONSTRAINT `base_lophocphan_mon_id_817e3550_fk_base_monhoc_id` FOREIGN KEY (`mon_id`) REFERENCES `base_monhoc` (`id`);

--
-- Constraints for table `base_sinhvien`
--
ALTER TABLE `base_sinhvien`
  ADD CONSTRAINT `base_sinhvien_khoa_id_d617bb57_fk_base_khoa_id` FOREIGN KEY (`khoa_id`) REFERENCES `base_khoa` (`id`);

--
-- Constraints for table `base_vectordactrung`
--
ALTER TABLE `base_vectordactrung`
  ADD CONSTRAINT `base_vectordactrung_sinhvien_id_4c5787ef_fk_base_sinhvien_id` FOREIGN KEY (`sinhvien_id`) REFERENCES `base_sinhvien` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_base_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `base_customuser` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
