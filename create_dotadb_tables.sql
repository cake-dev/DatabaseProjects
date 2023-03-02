CREATE SCHEMA `dota`;

CREATE TABLE `dota`.`TEAM` (
  `team_id` int PRIMARY KEY AUTO_INCREMENT,
  `team_name` varchar(255),
  `team_region` varchar(255),
  `team_winnings` int
);

CREATE TABLE `dota`.`PLAYER` (
  `player_id` int PRIMARY KEY AUTO_INCREMENT,
  `player_name` varchar(255),
  `player_country` varchar(255),
  `player_rank` int,
  `team_id` int
);

CREATE TABLE `dota`.`MATCH` (
  `match_id` int PRIMARY KEY AUTO_INCREMENT,
  `match_winner` int,
  `match_duration` int,
  `match_date` datetime,
  `tournament_id` int
);

CREATE TABLE `dota`.`TOURNAMENT` (
  `t_id` int PRIMARY KEY AUTO_INCREMENT,
  `t_name` varchar(255),
  `t_date` datetime,
  `t_prize` int,
  `t_winner` int
);

CREATE TABLE `dota`.`GAME_PERFORMANCE` (
  `gameplay_id` int PRIMARY KEY AUTO_INCREMENT,
  `g_kills` int,
  `g_deaths` int,
  `g_assists` int,
  `g_xpm` int,
  `g_gpm` int,
  `g_last_hits` int,
  `g_win` int,
  `player_id` int,
  `match_id` int,
  `hero_id` int
);

CREATE TABLE `dota`.`HERO` (
  `hero_id` int PRIMARY KEY AUTO_INCREMENT,
  `h_name` varchar(255),
  `h_main_stat` varchar(255),
  `str_base` int,
  `str_gain` float,
  `str_30` float,
  `agi_base` int,
  `agi_gain` float,
  `agi_30` float,
  `int_base` int,
  `int_gain` float,
  `int_30` float,
  `attack_type` varchar(255),
  `attack_range` int,
  `damage_base` int,
  `armor_base` int,
  `move_speed_base` int,
  `turn_rate` float
);

CREATE TABLE `dota`.`PLAYER_TEAM_HISTORY` (
  `player_id` int,
  `team_id` int,
  `join_date` datetime
);

CREATE TABLE `dota`.`TEAM_MATCH` (
  `match_id` int,
  `team1_id` int,
  `team2_id` int
);

ALTER TABLE `dota`.`PLAYER` ADD FOREIGN KEY (`team_id`) REFERENCES `dota`.`TEAM` (`team_id`);

ALTER TABLE `dota`.`MATCH` ADD FOREIGN KEY (`tournament_id`) REFERENCES `dota`.`TOURNAMENT` (`t_id`);

ALTER TABLE `dota`.`GAME_PERFORMANCE` ADD FOREIGN KEY (`player_id`) REFERENCES `dota`.`PLAYER` (`player_id`);

ALTER TABLE `dota`.`GAME_PERFORMANCE` ADD FOREIGN KEY (`match_id`) REFERENCES `dota`.`MATCH` (`match_id`);

ALTER TABLE `dota`.`GAME_PERFORMANCE` ADD FOREIGN KEY (`hero_id`) REFERENCES `dota`.`HERO` (`hero_id`);

ALTER TABLE `dota`.`PLAYER_TEAM_HISTORY` ADD FOREIGN KEY (`player_id`) REFERENCES `dota`.`PLAYER` (`player_id`);

ALTER TABLE `dota`.`TEAM_MATCH` ADD FOREIGN KEY (`match_id`) REFERENCES `dota`.`MATCH` (`match_id`);

ALTER TABLE `dota`.`TEAM_MATCH` ADD FOREIGN KEY (`team1_id`) REFERENCES `dota`.`TEAM` (`team_id`);

ALTER TABLE `dota`.`TEAM_MATCH` ADD FOREIGN KEY (`team2_id`) REFERENCES `dota`.`TEAM` (`team_id`);
