-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 06, 2021 at 10:39 AM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blood_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `bld_login`
--

CREATE TABLE `bld_login` (
  `bl_id` int(11) NOT NULL,
  `bl_user` varchar(250) NOT NULL,
  `bl_pass` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bld_login`
--

INSERT INTO `bld_login` (`bl_id`, `bl_user`, `bl_pass`) VALUES
(1, 'admin', 'admin'),
(2, 'ayana', 'ayana'),
(3, 'amal', 'amal'),
(4, 'anet', 'anet'),
(5, 'maria', 'maria'),
(6, 'surya', 'surya'),
(7, 'rahim', 'rahim'),
(8, 'sara', 'sara'),
(9, 'malu', 'malu'),
(10, 'suraj', 'suraj'),
(11, 'arathy', 'arthy'),
(14, 'manu', 'manu'),
(15, 'maneesha', 'maneesha');

-- --------------------------------------------------------

--
-- Table structure for table `bld_register`
--

CREATE TABLE `bld_register` (
  `reg_id` int(11) NOT NULL,
  `reg_name` varchar(250) NOT NULL,
  `reg_age` int(11) NOT NULL,
  `reg_sex` char(50) NOT NULL,
  `reg_mobile` bigint(20) DEFAULT NULL,
  `reg_bloodgrp` varchar(50) NOT NULL,
  `reg_rh` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bld_register`
--

INSERT INTO `bld_register` (`reg_id`, `reg_name`, `reg_age`, `reg_sex`, `reg_mobile`, `reg_bloodgrp`, `reg_rh`) VALUES
(20, 'Ayana Roy', 23, 'Female', 9747232208, 'B', 'B+'),
(21, 'Amal TA', 25, 'Male', 9526045036, 'AB', 'AB-'),
(22, 'Anet Mary', 24, 'Female', 8080808080, 'B', 'B-'),
(23, 'Maria John', 29, 'Female', 9012345678, 'A', 'A+'),
(24, 'Surya TK', 45, 'Male', 8765432190, 'O', 'O-'),
(25, 'Rahim Sahid', 56, 'Male', 8767676789, 'O', 'O-'),
(26, 'Sara Tom', 46, 'Female', 8097654789, 'B', 'B-'),
(27, 'Malu AK', 34, 'Male', 9876542390, 'AB', 'AB-'),
(28, 'Suraj ss', 34, 'Male', 9867456789, 'B', 'B-'),
(29, 'Arathy Ann', 19, 'Female', 9747234567, 'AB', 'AB-'),
(32, 'Manu jj', 23, 'Male', 5678904523, 'O', 'O-'),
(34, 'Maneesha', 20, 'Female', 9747234569, 'A', 'A-');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bld_login`
--
ALTER TABLE `bld_login`
  ADD PRIMARY KEY (`bl_id`),
  ADD UNIQUE KEY `bl_user` (`bl_user`),
  ADD UNIQUE KEY `bl_pass` (`bl_pass`);

--
-- Indexes for table `bld_register`
--
ALTER TABLE `bld_register`
  ADD PRIMARY KEY (`reg_id`),
  ADD UNIQUE KEY `reg_mobile` (`reg_mobile`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bld_login`
--
ALTER TABLE `bld_login`
  MODIFY `bl_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `bld_register`
--
ALTER TABLE `bld_register`
  MODIFY `reg_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
