CREATE DATABASE pyapp;

USE pyapp;

CREATE TABLE `compteur` (
	`compteur` INT unsigned NOT NULL DEFAULT '0'
) ENGINE=InnoDB;

INSERT INTO pyapp.compteur VALUES (1);