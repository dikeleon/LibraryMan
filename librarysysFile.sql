-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- ------------------------------------------------------
-- Creating the main user of the software
-- ------------------------------------------------------
CREATE USER 'LibMan'@'localhost' IDENTIFIED BY 'libman23';
GRANT ALL ON *.* TO 'LibMan'@'localhost' WITH GRANT OPTION;

-- -----------------------------------------------------
-- Schema librarysys
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema librarysys
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `librarysys` DEFAULT CHARACTER SET utf8 ;
USE `librarysys` ;

-- -----------------------------------------------------
-- Table `librarysys`.`students`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `librarysys`.`students` (
  `id_students` INT NOT NULL AUTO_INCREMENT COMMENT 'this is the students table',
  `name` VARCHAR(60) NOT NULL,
  `gender` VARCHAR(9) NULL,
  `class` VARCHAR(60) NULL,
  `dob` DOUBLE NULL,
  `photo` LONGTEXT NULL,
  PRIMARY KEY (`id_students`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `librarysys`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `librarysys`.`books` (
  `id_books` INT NOT NULL AUTO_INCREMENT,
  `id_students` INT NOT NULL,
  `bk_titles` LONGTEXT NULL,
  `doi` DOUBLE NULL,
  `duedate` DOUBLE NULL,
  PRIMARY KEY (`id_books`),
  INDEX `id_students_idx` (`id_students` ASC),
  CONSTRAINT `id_students`
    FOREIGN KEY (`id_students`)
    REFERENCES `librarysys`.`students` (`id_students`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `librarysys`.`configs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `librarysys`.`configs` (
  `id_admin` INT NOT NULL AUTO_INCREMENT,
  `libname` VARCHAR(75) NULL,
  `liblogo` LONGTEXT NULL,
  `graceperiod` INT NULL,
  PRIMARY KEY (`id_admin`))
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
