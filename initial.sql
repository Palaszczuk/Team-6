-- -----------------------------------------------------
-- Schema django
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `django` DEFAULT CHARACTER SET utf8 ;
USE `django` ;

GRANT USAGE ON *.* TO 'userdjango'@'%';

GRANT ALL PRIVILEGES ON *.* TO 'userdjango'@'%';