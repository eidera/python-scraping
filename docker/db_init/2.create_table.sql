use scraped;
SET NAMES utf8mb4;

CREATE TABLE IF NOT EXISTS `results` (
  `url` VARCHAR(191) NOT NULL,
  `html` TEXT NULL,
  `scraped_at` DATETIME NULL,
  PRIMARY KEY (`url`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;
