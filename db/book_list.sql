-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 25, 2024 at 02:30 PM
-- Server version: 10.6.14-MariaDB
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `book_list`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `name` varchar(255) DEFAULT NULL,
  `id` int(10) NOT NULL,
  `isbn` varchar(13) DEFAULT NULL,
  `authors` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `number_of_pages` int(11) DEFAULT NULL,
  `publisher` varchar(255) DEFAULT NULL,
  `release_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`name`, `id`, `isbn`, `authors`, `country`, `number_of_pages`, `publisher`, `release_date`) VALUES
('Book_101', 1, 'ISBN955922340', 'Autho0', 'Us', 50, 'Publisher_ade', '0000-00-00'),
('Book_101', 2, 'ISBN955922340', 'Autho0', 'Us', 50, 'Publisher_ade', '0000-00-00'),
('Book_3', 3, 'ISBN594016631', 'Author_8416', 'UK', 353, 'Publisher_7532', '2023-07-23'),
('Book_4', 4, 'ISBN741889656', 'Author_6257', 'Canada', 369, 'Publisher_4834', '2017-03-07'),
('Book_5', 5, 'ISBN427350131', 'Author_4562', 'Canada', 363, 'Publisher_1382', '2021-08-05'),
('Book_6', 6, 'ISBN559578677', 'Author_659', 'UK', 78, 'Publisher_3287', '2016-10-20'),
('Book_7', 7, 'ISBN199201733', 'Author_2930', 'Canada', 279, 'Publisher_6887', '2010-12-28'),
('Book_8', 8, 'ISBN078190236', 'Author_4747', 'USA', 186, 'Publisher_9444', '2022-12-13'),
('Book_9', 9, 'ISBN978532366', 'Author_6249', 'USA', 85, 'Publisher_7867', '2020-04-29'),
('Book_10', 10, 'ISBN458668894', 'Author_8204', 'Canada', 135, 'Publisher_6749', '2022-05-04'),
('Book_101', 11, 'ISBN955922344', 'Author_2000', 'Us', 500, 'Publisher_ade', '0000-00-00'),
('Book_101', 12, 'ISBN955922344', 'Author_2000', 'Us', 500, 'Publisher_ade', '0000-00-00'),
('Book_101', 13, 'ISBN955922344', 'Author_2000', 'Us', 500, 'Publisher_ade', '0000-00-00'),
('Book_101', 14, 'ISBN955922344', 'Author_2000', 'Us', 500, 'Publisher_ade', '0000-00-00'),
('Book_101', 15, 'ISBN955922344', 'Author_2000', 'Us', 500, 'Publisher_ade', '0000-00-00'),
('Book_101', 16, 'ISBN955922340', 'Autho0', 'Us', 50, 'Publisher_ade', '0000-00-00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
