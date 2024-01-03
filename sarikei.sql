-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 03, 2024 at 02:31 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student_registeration_form`
--

-- --------------------------------------------------------

--
-- Table structure for table `sarikei`
--

CREATE TABLE `sarikei` (
  `student_full_name` text NOT NULL,
  `student_year` int(1) NOT NULL,
  `student_adress` varchar(100) NOT NULL,
  `student_gender` text NOT NULL,
  `parent_full_name` text NOT NULL,
  `parent_email` varchar(50) NOT NULL,
  `student_set` varchar(5) NOT NULL,
  `student_pack_quantity` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sarikei`
--

INSERT INTO `sarikei` (`student_full_name`, `student_year`, `student_adress`, `student_gender`, `parent_full_name`, `parent_email`, `student_set`, `student_pack_quantity`) VALUES
('Luzman Al Thaqif Bin Narzaruddin', 6, 'No.1, Flat Sungai Rejang, Jalan Repok, 96100, Sari', 'Male', 'Narzaruddin Bin Kiprawi', 'deden.ayah@gmail.com', 'Set 2', 9),
('Adam Iskandar Bin Zulkarnine', 1, 'No.28, Lorong Gugusan Alam, 7/22, Bandar Puncak Alam, 42300, Kuala Selangor, Selangor', 'Male', 'Zulkarnine', 'ayahadam@gmail.com', 'Set 2', 3),
('Huda Binti Narzarudin', 5, 'No.2, Flat Sungai Terusan, Jalan Repok, 96100, Sarikei, Sarawak', 'Female', 'narzarudin Kiprawi', 'narza.hensem@gmail.com', 'Set 2', 5),
('Nur Cahya Binti Akkimi', 3, 'No.4, Flat Sungai Kemena, Jalan Repok, 96100, Sarikei, Sarawak', 'Female', 'Akkimi Bin Razi', 'akkimibusiness@gmail.com', 'Set 3', 10);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
