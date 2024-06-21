CREATE DATABASE IF NOT EXISTS pokebuildmaker;
USE pokebuildmaker;

CREATE TABLE IF NOT EXISTS USER (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(20) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL,
    profile_picture VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS POKEMON (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pokedex_id INT(4) NOT NULL,
    level INT(3) NOT NULL,
    name VARCHAR(12),
    ability_1 VARCHAR(30) NOT NULL,
    ability_2 VARCHAR(30),
    ability_3 VARCHAR(30),
    ability_4 VARCHAR(30),
    owner_id INT NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES USER(id)
);

CREATE TABLE IF NOT EXISTS BUILDS (
    id INT AUTO_INCREMENT PRIMARY KEY,
<<<<<<< HEAD
    build_name VARCHAR(32) NOT NULL,
<<<<<<< HEAD
    pokemon_id_1 INT NOT NULL,
=======
    build_name VARCHAR(12) NOT NULL,
    pokemon_id_1 INT,
>>>>>>> Frontend-formulario_añadir_pokemon
=======
    pokemon_id_1 INT,
>>>>>>> Frontend-delete_pokemon
    pokemon_id_2 INT,
    pokemon_id_3 INT,
    pokemon_id_4 INT,
    pokemon_id_5 INT,
    pokemon_id_6 INT,
    timestamp DATETIME NOT NULL,
    owner_id INT NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES USER(id)
);

INSERT INTO USER (username, password, email, profile_picture) VALUES
('user1', 'password1', 'email1@gmail.com', 'profile_picture1.png'),
('user2', 'password2', 'email2@gmail.com', 'profile_picture2.png'),
('user3', 'password3', 'email3@gmail.com', 'profile_picture3.png'),
('user4', 'password4', 'email4@gmail.com', 'profile_picture4.png'),
('user5', 'password5', 'email5@gmail.com', 'profile_picture5.png'),
('user6', 'password6', 'email6@gmail.com', 'profile_picture6.png'),
('user7', 'password7', 'email7@gmail.com', 'profile_picture7.png'),
('user8', 'password8', 'email8@gmail.com', 'profile_picture8.png'),
('user9', 'password9', 'email9@gmail.com', 'profile_picture9.png'),
('user10', 'password10', 'email10@gmail.com', 'profile_picture10.png'),
('user11', 'password11', 'email11@gmail.com', 'profile_picture11.png'),
('user12', 'password12', 'email12@gmail.com', 'profile_picture12.png');

INSERT INTO POKEMON (pokedex_id, level, name, ability_1, ability_2, ability_3, ability_4, owner_id) VALUES
(6,   9, 'Charizard', 'Blaze', 'Solar Power', 'None', 'None', 1),
(25,  13, 'Pikachu', 'Static', 'None', 'None', 'None', 1),
(1,   10, 'Bulbasaur', 'Overgrow', 'Chlorophyll', 'None', 'None', 1),
(4,   22, 'Charmander', 'Blaze', 'Solar Power', 'None', 'None', 1),
(7,   10, 'Squirtle', 'Torrent', 'Rain Dish', 'None', 'None', 1),
(10,  33, 'Caterpie', 'Shield Dust', 'Run Away', 'None', 'None', 1),
(13,  10, 'Weedle', 'Shield Dust', 'Run Away', 'None', 'None', 1),
(16,  14, 'Pidgey', 'Keen Eye', 'Tangled Feet', 'Big Pecks', 'None', 1),
(19,  10, 'Rattata', 'Run Away', 'Guts', 'Hustle', 'None', 1),
(23,  10, 'Ekans', 'Intimidate', 'Shed Skin', 'Unnerve', 'None', 1),
(27,  10, 'Sandshrew', 'Sand Veil', 'Sand Rush', 'None', 'None', 2),
(29,  10, 'Nidoran♀', 'Poison Point', 'Rivalry', 'Hustle', 'None', 2),
(32,  10, 'Nidoran♂', 'Poison Point', 'Rivalry', 'Hustle', 'None', 2),
(37,  10, 'Vulpix', 'Flash Fire', 'Drought', 'None', 'None', 2),
(39,  10, 'Jigglypuff', 'Cute Charm', 'Competitive', 'Friend Guard', 'None', 2),
(43,  10, 'Oddish', 'Chlorophyll', 'Run Away', 'None', 'None', 2),
(48,  10, 'Venonat', 'Compound Eyes', 'Tinted Lens', 'Run Away', 'None', 2),
(52,  10, 'Meowth', 'Pickup', 'Technician', 'Unnerve', 'None', 2),
(54,  10 , 'Psyduck', 'Damp', 'Cloud Nine', 'Swift Swim', 'None', 2),
(58,  10, 'Growlithe', 'Intimidate', 'Flash Fire', 'Justified', 'None', 2),
(60,  10, 'Poliwag', 'Water Absorb', 'Damp', 'Swift Swim', 'None', 3),
(63,  10, 'Abra', 'Synchronize', 'Inner Focus', 'Magic Guard', 'None', 3),
(66,  10, 'Machop', 'Guts', 'No Guard', 'Steadfast', 'None', 3),
(69,  10, 'Bellsprout', 'Chlorophyll', 'Gluttony', 'None', 'None', 3),
(74,  10, 'Geodude', 'Rock Head', 'Sturdy', 'Sand Veil', 'None', 3),
(77,  10, 'Ponyta', 'Run Away', 'Flash Fire', 'Flame Body', 'None', 3),
(79,  10, 'Slowpoke', 'Oblivious', 'Own Tempo', 'Regenerator', 'None', 3),
(81,  10, 'Magnemite', 'Magnet Pull', 'Sturdy', 'Analytic', 'None', 3),
(84,  10, 'Doduo', 'Run Away', 'Early Bird', 'Tangled Feet', 'None', 3),
(86,  10, 'Seel', 'Thick Fat', 'Hydration', 'Ice Body', 'None', 3),
(90,  10, 'Shellder', 'Shell Armor', 'Skill Link', 'Overcoat', 'None', 3),
(92,  10, 'Gastly', 'Levitate', 'None', 'None', 'None', 3),
(94,  10, 'Gengar', 'Levitate', 'Cursed Body', 'None', 'None', 3),
(96,  10, 'Drowzee', 'Insomnia', 'Forewarn', 'Inner Focus', 'None', 3),
(98,  10, 'Krabby', 'Hyper Cutter', 'Shell Armor', 'Sheer Force', 'None', 3),
(100, 10, 'Voltorb', 'Soundproof', 'Static', 'Aftermath', 'None', 4),
(102, 10, 'Exeggcute', 'Chlorophyll', 'Harvest', 'None', 'None', 4),
(104, 10, 'Cubone', 'Rock Head', 'Lightning Rod', 'Battle Armor', 'None', 4),
(108, 10, 'Lickitung', 'Own Tempo', 'Oblivious', 'Cloud Nine', 'None', 4),
(109, 10, 'Koffing', 'Levitate', 'None', 'None', 'None', 4),
(111, 10, 'Rhyhorn', 'Lightning Rod', 'Rock Head', 'Reckless', 'None', 4),
(116, 10, 'Horsea', 'Swift Swim', 'Sniper', 'Damp', 'None', 4),
(118, 10, 'Goldeen', 'Swift Swim', 'Water Veil', 'Lightning Rod', 'None', 4),
(120, 10, 'Staryu', 'Illuminate', 'Natural Cure', 'Analytic', 'None', 4),
(129, 10, 'Magikarp', 'Swift Swim', 'Rattled', 'None', 'None', 4),
(133, 10, 'Eevee', 'Run Away', 'Adaptability', 'Anticipation', 'None', 4),
(138, 10, 'Omanyte', 'Swift Swim', 'Shell Armor', 'Weak Armor', 'None', 4),
(140, 10, 'Kabuto', 'Swift Swim', 'Battle Armor', 'Weak Armor', 'None', 4),
(147, 10, 'Dratini', 'Shed Skin', 'Marvel Scale', 'None', 'None', 4),
(152, 10, 'Chikorita', 'Overgrow', 'Leaf Guard', 'None', 'None', 4),
(155, 10, 'Cyndaquil', 'Blaze', 'Flash Fire', 'None', 'None', 5),
(158, 10, 'Totodile', 'Torrent', 'Sheer Force', 'None', 'None', 5),
(161, 10, 'Sentret', 'Run Away', 'Keen Eye', 'Frisk', 'None', 5),
(163, 10, 'Hoothoot', 'Insomnia', 'Keen Eye', 'Tinted Lens', 'None', 5),
(165, 10, 'Ledyba', 'Swarm', 'Early Bird', 'Rattled', 'None', 5),
(167, 10, 'Spinarak', 'Swarm', 'Insomnia', 'Sniper', 'None', 5),
(170, 10, 'Chinchou', 'Volt Absorb', 'Illuminate', 'Water Absorb', 'None', 5),
(177, 10, 'Natu', 'Synchronize', 'Early Bird', 'Magic Bounce', 'None', 5),
(179, 10, 'Mareep', 'Static', 'Plus', 'None', 'None', 5),
(183, 10, 'Marill', 'Thick Fat', 'Huge Power', 'Sap Sipper', 'None', 5),
(187, 10, 'Hoppip', 'Chlorophyll', 'Leaf Guard', 'Infiltrator', 'None', 5),
(190, 10, 'Aipom', 'Run Away', 'Pickup', 'Skill Link', 'None', 5),
(193, 10, 'Yanma', 'Speed Boost', 'Compound Eyes', 'Frisk', 'None', 5),
(198, 10, 'Murkrow', 'Insomnia', 'Super Luck', 'Prankster', 'None', 5),
(200, 10, 'Misdreavus', 'Levitate', 'None', 'None', 'None', 5),
(203, 10, 'Girafarig', 'Inner Focus', 'Early Bird', 'Sap Sipper', 'None', 6),
(206, 10, 'Dunsparce', 'Serene Grace', 'Run Away', 'Rattled', 'None', 6),
(209, 10, 'Snubbull', 'Intimidate', 'Run Away', 'Rattled', 'None', 6),
(211, 10, 'Qwilfish', 'Poison Point', 'Swift Swim', 'Intimidate', 'None', 6),
(213, 10, 'Shuckle', 'Sturdy', 'Gluttony', 'Contrary', 'None', 6),
(215, 10, 'Sneasel', 'Inner Focus', 'Keen Eye', 'Pickpocket', 'None', 6),
(218, 10, 'Slugma', 'Magma Armor', 'Flame Body', 'Weak Armor', 'None', 6),
(220, 10, 'Swinub', 'Oblivious', 'Snow Cloak', 'Thick Fat', 'None', 6),
(223, 10, 'Remoraid', 'Hustle', 'Sniper', 'Moody', 'None', 6),
(226, 10, 'Mantine', 'Swift Swim', 'Water Absorb', 'Water Veil', 'None', 6),
(228, 10, 'Houndour', 'Early Bird', 'Flash Fire', 'Unnerve', 'None', 6),
(231, 10, 'Phanpy', 'Pickup', 'Sand Veil', 'None', 'None', 6),
(234, 10, 'Stantler', 'Intimidate', 'Frisk', 'Sap Sipper', 'None', 6),
(236, 10, 'Tyrogue', 'Guts', 'Steadfast', 'Vital Spirit', 'None', 6),
(239, 10, 'Elekid', 'Static', 'Vital Spirit', 'None', 'None', 6),
(241, 10, 'Miltank', 'Thick Fat', 'Scrappy', 'Sap Sipper', 'None', 7),
(246, 10, 'Larvitar', 'Guts', 'Sand Veil', 'None', 'None', 7),
(252, 10, 'Treecko', 'Overgrow', 'Unburden', 'None', 'None', 7),
(255, 10, 'Torchic', 'Blaze', 'Speed Boost', 'None', 'None', 7),
(258, 10, 'Mudkip', 'Torrent', 'Damp', 'None', 'None', 7),
(261, 10, 'Poochyena', 'Run Away', 'Quick Feet', 'Rattled', 'None', 7),
(263, 10, 'Zigzagoon', 'Pickup', 'Gluttony', 'Quick Feet', 'None', 7),
(265, 10, 'Wurmple', 'Shield Dust', 'Run Away', 'None', 'None', 7),
(270, 10, 'Lotad', 'Swift Swim', 'Rain Dish', 'Own Tempo', 'None', 7),
(273, 10, 'Seedot', 'Chlorophyll', 'Early Bird', 'Pickpocket', 'None', 7),
(276, 10, 'Taillow', 'Guts', 'Scrappy', 'None', 'None', 7),
(278, 10, 'Wingull', 'Keen Eye', 'Hydration', 'Rain Dish', 'None', 7),
(280, 10, 'Ralts', 'Synchronize', 'Trace', 'Telepathy', 'None', 7),
(283, 10, 'Surskit', 'Swift Swim', 'Rain Dish', 'None', 'None', 7),
(285, 10, 'Shroomish', 'Effect Spore', 'Poison Heal', 'Quick Feet', 'None', 7),
(287, 10, 'Slakoth', 'Truant', 'None', 'None', 'None', 8),
(290, 10, 'Nincada', 'Compound Eyes', 'Run Away', 'None', 'None', 8),
(293, 10, 'Whismur', 'Soundproof', 'Rattled', 'None', 'None', 8),
(296, 10, 'Makuhita', 'Thick Fat', 'Guts', 'Sheer Force', 'None', 8),
(299, 10, 'Nosepass', 'Sturdy', 'Magnet Pull', 'Sand Force', 'None', 8),
(302, 10, 'Sableye', 'Keen Eye', 'Stall', 'Prankster', 'None', 8),
(304, 10, 'Aron', 'Sturdy', 'Rock Head', 'Heavy Metal', 'None', 8),
(307, 10, 'Meditite', 'Pure Power', 'Telepathy', 'None', 'None', 8),
(309, 10, 'Electrike', 'Static', 'Lightning Rod', 'Minus', 'None', 8),
(311, 10, 'Plusle', 'Plus', 'None', 'None', 'None', 8),
(313, 10, 'Volbeat', 'Illuminate', 'Swarm', 'Prankster', 'None', 8),
(316, 10, 'Gulpin', 'Liquid Ooze', 'Sticky Hold', 'Gluttony', 'None', 8),
(318, 10, 'Carvanha', 'Rough Skin', 'Speed Boost', 'None', 'None', 8),
(320, 10, 'Wailmer', 'Water Veil', 'Oblivious', 'Pressure', 'None', 8),
(322, 10, 'Numel', 'Oblivious', 'Simple', 'Own Tempo', 'None', 8),
(324, 10, 'Torkoal', 'White Smoke', 'Drought', 'Shell Armor', 'None', 9),
(327, 10, 'Spinda', 'Own Tempo', 'Tangled Feet', 'Contrary', 'None', 9),
(331, 10, 'Cacnea', 'Sand Veil', 'Water Absorb', 'None', 'None', 9),
(333, 10, 'Swablu', 'Natural Cure', 'Cloud Nine', 'None', 'None', 9),
(335, 10, 'Zangoose', 'Immunity', 'Toxic Boost', 'None', 'None', 9),
(337, 10, 'Lunatone', 'Levitate', 'None', 'None', 'None', 9),
(339, 10, 'Barboach', 'Oblivious', 'Anticipation', 'Hydration', 'None', 9),
(341, 10, 'Corphish', 'Hyper Cutter', 'Shell Armor', 'Adaptability', 'None', 9),
(343, 10, 'Baltoy', 'Levitate', 'None', 'None', 'None', 9),
(345, 10, 'Lileep', 'Suction Cups', 'Storm Drain', 'None', 'None', 9),
(347, 10, 'Anorith', 'Battle Armor', 'Swift Swim', 'None', 'None', 9),
(349, 10, 'Feebas', 'Swift Swim', 'Oblivious', 'Adaptability', 'None', 9),
(351, 10, 'Castform', 'Forecast', 'None', 'None', 'None', 9),
(353, 10, 'Shuppet', 'Insomnia', 'Frisk', 'Cursed Body', 'None', 9),
(355, 10, 'Duskull', 'Levitate', 'Frisk', 'None', 'None', 9),
(357, 10, 'Tropius', 'Chlorophyll', 'Solar Power', 'Harvest', 'None', 9),
(359, 10, 'Absol', 'Pressure', 'Super Luck', 'Justified', 'None', 9),
(361, 10, 'Snorunt', 'Inner Focus', 'Ice Body', 'Moody', 'None', 9),
(363, 10, 'Spheal', 'Thick Fat', 'Ice Body', 'Oblivious', 'None', 9),
(366, 10, 'Clamperl', 'Shell Armor', 'Rattled', 'None', 'None', 9),
(369, 10, 'Relicanth', 'Swift Swim', 'Rock Head', 'Sturdy', 'None', 9),
(371, 10, 'Bagon', 'Rock Head', 'Sheer Force', 'None', 'None', 10),
(374, 10, 'Beldum', 'Clear Body', 'None', 'None', 'None', 10),
(377, 10, 'Regirock', 'Clear Body', 'None', 'None', 'None', 10),
(379, 10, 'Registeel', 'Clear Body', 'None', 'None', 'None', 10),
(381, 10, 'Latios', 'Levitate', 'None', 'None', 'None', 10),
(383, 10, 'Groudon', 'Drought', 'None', 'None', 'None', 10),
(385, 10, 'Jirachi', 'Serene Grace', 'None', 'None', 'None', 10),
(387, 10, 'Turtwig', 'Overgrow', 'Shell Armor', 'None', 'None', 10),
(390, 10, 'Chimchar', 'Blaze', 'Iron Fist', 'None', 'None', 10),
(393, 10, 'Piplup', 'Torrent', 'Defiant', 'None', 'None', 10),
(396, 10, 'Starly', 'Keen Eye', 'Reckless', 'None', 'None', 10),
(399, 10, 'Bidoof', 'Simple', 'Unaware', 'Moody', 'None', 10),
(401, 10, 'Kricketot', 'Shed Skin', 'Run Away', 'None', 'None', 11),
(403, 10, 'Shinx', 'Rivalry', 'Intimidate', 'Guts', 'None', 11),
(406, 10, 'Budew', 'Natural Cure', 'Poison Point', 'Leaf Guard', 'None', 11),
(408, 10, 'Cranidos', 'Mold Breaker', 'Sheer Force', 'None', 'None', 11),
(410, 10, 'Shieldon', 'Sturdy', 'Soundproof', 'None', 'None', 11),
(412, 10, 'Burmy', 'Shed Skin', 'None', 'None', 'None', 11),
(414, 10, 'Mothim', 'Swarm', 'Tinted Lens', 'None', 'None', 11),
(416, 10, 'Vespiquen', 'Pressure', 'Unnerve', 'None', 'None', 11),
(418, 10, 'Buizel', 'Swift Swim', 'Water Veil', 'None', 'None', 11),
(420, 10, 'Cherubi', 'Chlorophyll', 'None', 'None', 'None', 11),
(422, 10, 'Shellos', 'Sticky Hold', 'Storm Drain', 'Sand Force', 'None', 11),
(425, 10, 'Drifloon', 'Aftermath', 'Unburden', 'Flare Boost', 'None', 11),
(427, 10, 'Buneary', 'Run Away', 'Klutz', 'Limber', 'None', 11),
(429, 10, 'Mismagius', 'Levitate', 'None', 'None', 'None', 11),
(431, 10, 'Glameow', 'Limber', 'Own Tempo', 'Keen Eye', 'None', 11),
(433, 10, 'Chingling', 'Levitate', 'None', 'None', 'None', 11),
(435, 10, 'Skuntank', 'Stench', 'Aftermath', 'Keen Eye', 'None', 11),
(437, 10, 'Bronzor', 'Levitate', 'Heatproof', 'Heavy Metal', 'None', 11),
(439, 10, 'Mime Jr.', 'Soundproof', 'Filter', 'Technician', 'None', 11),
(441, 10, 'Chatot', 'Keen Eye', 'Tangled Feet', 'Big Pecks', 'None', 11),
(443, 10, 'Gible', 'Sand Veil', 'Rough Skin', 'None', 'None', 11),
(445, 10, 'Garchomp', 'Sand Veil', 'None', 'None', 'None', 11),
(447, 10, 'Riolu', 'Steadfast', 'Inner Focus', 'Prankster', 'None', 11),
(449, 10, 'Hippopotas', 'Sand Stream', 'Sand Force', 'None', 'None', 12),
(451, 10, 'Skorupi', 'Battle Armor', 'Sniper', 'Keen Eye', 'None', 12),
(453, 10, 'Croagunk', 'Anticipation', 'Dry Skin', 'Poison Touch', 'None', 12),
(455, 10, 'Carnivine', 'Levitate', 'None', 'None', 'None', 12),
(457, 10, 'Lumineon', 'Swift Swim', 'Storm Drain', 'None', 'None', 12),
(459, 10, 'Snover', 'Snow Warning', 'Soundproof', 'None', 'None', 12),
(461, 10, 'Weavile', 'Pressure', 'Pickpocket', 'None', 'None', 12),
(463, 10, 'Lickilicky', 'Own Tempo', 'Oblivious', 'Cloud Nine', 'None', 12),
(465, 10, 'Tangrowth', 'Chlorophyll', 'Leaf Guard', 'Regenerator', 'None', 12),
(467, 10, 'Magmortar', 'Flame Body', 'Vital Spirit', 'None', 'None', 12),
(469, 10, 'Yanmega', 'Speed Boost', 'Tinted Lens', 'Frisk', 'None', 12),
(471, 10, 'Glaceon', 'Snow Cloak', 'Ice Body', 'None', 'None', 12),
(473, 10, 'Mamoswine', 'Oblivious', 'Snow Cloak', 'Thick Fat', 'None', 12),
(475, 10, 'Gallade', 'Steadfast', 'Justified', 'None', 'None', 12),
(477, 10, 'Dusknoir', 'Pressure', 'Frisk', 'None', 'None', 12),
(479, 10, 'Rotom', 'Levitate', 'None', 'None', 'None', 1),
(481, 10, 'Mesprit', 'Levitate', 'None', 'None', 'None', 1),
(483, 10, 'Dialga', 'Pressure', 'Telepathy', 'None', 'None', 1),
(485, 10, 'Heatran', 'Flash Fire', 'Flame Body', 'None', 'None', 1),
(487, 10, 'Giratina', 'Pressure', 'Telepathy', 'None', 'None', 2),
(489, 10, 'Phione', 'Hydration', 'None', 'None', 'None', 2),
(491, 10, 'Darkrai', 'Bad Dreams', 'None', 'None', 'None', 2),
(493, 10, 'Arceus', 'Multitype', 'None', 'None', 'None', 2),
(495, 10, 'Snivy', 'Overgrow', 'Contrary', 'None', 'None', 3),
(498, 10, 'Tepig', 'Blaze', 'Thick Fat', 'None', 'None', 3),
(501, 10, 'Oshawott', 'Torrent', 'Shell Armor', 'None', 'None', 3),
(504, 10, 'Patrat', 'Run Away', 'Keen Eye', 'Analytic', 'None', 3),
(506, 10, 'Lillipup', 'Vital Spirit', 'Pickup', 'Run Away', 'None', 4),
(509, 10, 'Purrloin', 'Limber', 'Unburden', 'Prankster', 'None', 4),
(511, 10, 'Pansage', 'Gluttony', 'Overgrow', 'None', 'None', 4),
(513, 10, 'Pansear', 'Gluttony', 'Blaze', 'None', 'None', 4),
(515, 10, 'Panpour', 'Gluttony', 'Torrent', 'None', 'None', 5),
(517, 10, 'Munna', 'Forewarn', 'Synchronize', 'Telepathy', 'None', 5),
(519, 10, 'Pidove', 'Big Pecks', 'Super Luck', 'Rivalry', 'None', 5),
(522, 10, 'Blitzle', 'Lightning Rod', 'Motor Drive', 'Sap Sipper', 'None', 5),
(524, 10, 'Roggenrola', 'Sturdy', 'Weak Armor', 'Sand Force', 'None', 6),
(527, 10, 'Woobat', 'Unaware', 'Klutz', 'Simple', 'None', 6),
(529, 10, 'Drilbur', 'Sand Rush', 'Sand Force', 'Mold Breaker', 'None', 6),
(531, 10, 'Audino', 'Healer', 'Regenerator', 'Klutz', 'None', 6),
(533, 10, 'Gurdurr', 'Guts', 'Sheer Force', 'Iron Fist', 'None', 6),
(535, 10, 'Tympole', 'Swift Swim', 'Hydration', 'Water Absorb', 'None', 6),
(537, 10, 'Seismitoad', 'Swift Swim', 'Poison Touch', 'Water Absorb', 'None', 6),
(539, 10, 'Sawk', 'Sturdy', 'Inner Focus', 'Mold Breaker', 'None', 6),
(541, 10, 'Swadloon', 'Leaf Guard', 'Chlorophyll', 'Overcoat', 'None', 8),
(543, 10, 'Venipede', 'Poison Point', 'Swarm', 'Speed Boost', 'None', 8),
(545, 10, 'Scolipede', 'Poison Point', 'Swarm', 'Speed Boost', 'None', 8),
(547, 10, 'Whimsicott', 'Prankster', 'Infiltrator', 'Chlorophyll', 'None', 8),
(549, 10, 'Lilligant', 'Chlorophyll', 'Own Tempo', 'Leaf Guard', 'None', 8),
(551, 10, 'Sandile', 'Intimidate', 'Moxie', 'Anger Point', 'None', 8),
(553, 10, 'Krokorok', 'Intimidate', 'Moxie', 'Anger Point', 'None', 8),
(557, 10, 'Dwebble', 'Sturdy', 'Shell Armor', 'Weak Armor', 'None', 8),
(559, 10, 'Scraggy', 'Shed Skin', 'Moxie', 'Intimidate', 'None', 10),
(561, 10, 'Sigilyph', 'Wonder Skin', 'Magic Guard', 'Tinted Lens', 'None', 10),
(563, 10, 'Cofagrigus', 'Mummy', 'None', 'None', 'None', 10),
(565, 10, 'Carracosta', 'Solid Rock', 'Sturdy', 'Swift Swim', 'None', 10),
(567, 10, 'Archeops', 'Defeatist', 'None', 'None', 'None', 11),
(569, 10, 'Garbodor', 'Stench', 'Weak Armor', 'Aftermath', 'None', 11),
(571, 10, 'Zoroark', 'Illusion', 'None', 'None', 'None', 11),
(573, 10, 'Cinccino', 'Cute Charm', 'Technician', 'Skill Link', 'None', 11),
(575, 10, 'Gothorita', 'Frisk', 'Competitive', 'Shadow Tag', 'None', 11),
(577, 10, 'Solosis', 'Overcoat', 'Magic Guard', 'Regenerator', 'None', 11),
(579, 10, 'Reuniclus', 'Overcoat', 'Magic Guard', 'Regenerator', 'None', 11),
(581, 10, 'Swanna', 'Keen Eye', 'Big Pecks', 'Hydration', 'None', 12),
(583, 10, 'Vanilluxe', 'Ice Body', 'Snow Warning', 'Weak Armor', 'None', 12),
(585, 10, 'Deerling', 'Chlorophyll', 'Sap Sipper', 'Serene Grace', 'None', 12);

INSERT INTO BUILDS (build_name, owner_id, pokemon_id_1, pokemon_id_2, pokemon_id_3, pokemon_id_4, pokemon_id_5, pokemon_id_6, timestamp) VALUES

('123456789012345678906789012', 1, 1, 2, 3, 4, 5, 6, NOW()),
('build2', 1, 7, 8, 9, 10, 182, 183, NOW()),
('build3', 1, 184, 185, 1, 3, 5, 7, NOW()),
('build4', 1, 2, 4, 6, 8, 10, 182, NOW()),
('build5', 1, 183, 184, 185, 1, 2, 3, NOW()),
('build6', 1, 4, 5, 6, 7, 8, 9, NOW()),
('build7', 1, 10, 182, 183, 184, 185, 1, NOW()),
('build8', 1, 2, 3, 4, 5, 6, 7, NOW()),
('build9', 1, 8, 9, 10, 182, 183, 184, NOW()),
('build10', 1, 185, 1, 2, 3, 4, 5, NOW()),

/* OWNER USER2 */
('build11', 2, 11, 12, 13, 14, 15, 16, NOW()),
('build12', 2, 17, 18, 19, NULL, NULL, NULL, NOW()),
('build13', 2, 20, 186, 187, 188, NULL, NULL, NOW()),
('build14', 2, 189, 11, 12, 13, 14, 15, NOW()),
('build15', 2, 16, 17, NULL, 18, 19, 20, NOW()),
('build16', 2, 186, NULL, 187, 188, 189, 11, NOW()),
('build17', 2, 12, 13, 14, NULL, 15, 16, NOW()),
('build18', 2, 17, 18, 19, 20, 186, NULL, NOW()),
('build19', 2, 187, 188, 189, NULL, NULL, 11, NOW()),
('build20', 2, 12, 13, 14, 15, 16, 17, NOW()),

/* OWNER USER3 */
('build21', 3, 21, 22, 23, 24, 25, 26, NOW()),
('build22', 3, 27, 28, 29, 30, 190, NULL, NOW()),
('build23', 3, 191, 192, 193, 21, 22, NULL, NOW()),
('build24', 3, 23, 24, 25, 26, 27, 28, NOW()),
('build25', 3, 29, 30, 190, 191, 192, NULL, NOW()),
('build26', 3, 193, 21, 22, 23, 24, 25, NOW()),
('build27', 3, 26, 27, 28, NULL, 29, 30, NOW()),
('build28', 3, 190, 191, 192, 193, 21, 22, NOW()),
('build29', 3, 23, 24, 25, NULL, 26, 27, NOW()),
('build30', 3, 28, 29, 30, 190, 191, NULL, NOW()),

/* OWNER USER4 */
('build31', 4, 31, 32, 33, 34, 35, 36, NOW()),
('build32', 4, 37, 38, 39, 40, 194, NULL, NOW()),
('build33', 4, 195, 196, 197, 31, 32, NULL, NOW()),
('build34', 4, 33, 34, 35, 36, 37, 38, NOW()),
('build35', 4, 39, 40, 194, 195, 196, NULL, NOW()),
('build36', 4, 197, 31, 32, 33, 34, 35, NOW()),
('build37', 4, 36, 37, 38, NULL, 39, 40, NOW()),
('build38', 4, 194, 195, 196, 197, 31, 32, NOW()),
('build39', 4, 33, 34, 35, NULL, 36, 37, NOW()),
('build40', 4, 38, 39, 40, 194, 195, NULL, NOW()),

/* OWNER USER5 */
('build41', 5, 41, 42, 43, 44, 45, 46, NOW()),
('build42', 5, 47, 48, 49, 50, 198, NULL, NOW()),
('build43', 5, 199, 200, 201, 41, 42, NULL, NOW()),
('build44', 5, 43, 44, 45, 46, 47, 48, NOW()),
('build45', 5, 49, 50, 198, 199, 200, NULL, NOW()),
('build46', 5, 201, 41, 42, 43, 44, 45, NOW()),
('build47', 5, 46, 47, 48, NULL, 49, 50, NOW()),
('build48', 5, 198, 199, 200, 201, 41, 42, NOW()),
('build49', 5, 43, 44, 45, NULL, 46, 47, NOW()),
('build50', 5, 48, 49, 50, 198, 199, NULL, NOW()),

/* OWNER USER6 */
('build51', 6, 51, 52, 53, 54, 55, 56, NOW()),
('build52', 6, 57, 58, 59, 60, 202, NULL, NOW()),
('build53', 6, 203, 204, 205, 51, 52, NULL, NOW()),
('build54', 6, 53, 54, 55, 56, 57, 58, NOW()),
('build55', 6, 59, 60, 202, 203, 204, NULL, NOW()),
('build56', 6, 205, 51, 52, 53, 54, 55, NOW()),
('build57', 6, 56, 57, 58, NULL, 59, 60, NOW()),
('build58', 6, 202, 203, 204, 205, 51, 52, NOW()),
('build59', 6, 53, 54, 55, NULL, 56, 57, NOW()),
('build60', 6, 58, 59, 60, 202, 203, NULL, NOW()),

/* OWNER USER7 */
('build61', 7, 61, 62, 63, 64, 65, 66, NOW()),
('build62', 7, 67, 68, 69, 70, 206, NULL, NOW()),
('build63', 7, 207, 208, 209, 61, 62, NULL, NOW()),
('build64', 7, 63, 64, 65, 66, 67, 68, NOW()),
('build65', 7, 69, 70, 206, 207, 208, NULL, NOW()),
('build66', 7, 209, 61, 62, 63, 64, 65, NOW()),
('build67', 7, 66, 67, 68, NULL, 69, 70, NOW()),
('build68', 7, 206, 207, 208, 209, 61, 62, NOW()),
('build69', 7, 63, 64, 65, NULL, 66, 67, NOW()),
('build70', 7, 68, 69, 70, 206, 207, NULL, NOW()),

/* OWNER USER8 */
('build71', 8, 71, 72, 73, 74, 75, 76, NOW()),
('build72', 8, 77, 78, 79, 80, 210, NULL, NOW()),
('build73', 8, 211, 212, 213, 71, 72, NULL, NOW()),
('build74', 8, 73, 74, 75, 76, 77, 78, NOW()),
('build75', 8, 79, 80, 210, 211, 212, NULL, NOW()),
('build76', 8, 213, 71, 72, 73, 74, 75, NOW()),
('build77', 8, 76, 77, 78, NULL, 79, 80, NOW()),
('build78', 8, 210, 211, 212, 213, 71, 72, NOW()),
('build79', 8, 73, 74, 75, NULL, 76, 77, NOW()),
('build80', 8, 78, 79, 80, 210, 211, NULL, NOW()),

/* OWNER USER9 */
('build81', 9, 81, 82, 83, 84, 85, 86, NOW()),
('build82', 9, 87, 88, 89, 90, 214, NULL, NOW()),
('build83', 9, 215, 216, 217, 81, 82, NULL, NOW()),
('build84', 9, 83, 84, 85, 86, 87, 88, NOW()),
('build85', 9, 89, 90, 214, 215, 216, NULL, NOW()),
('build86', 9, 217, 81, 82, 83, 84, 85, NOW()),
('build87', 9, 86, 87, 88, NULL, 89, 90, NOW()),
('build88', 9, 214, 215, 216, 217, 81, 82, NOW()),
('build89', 9, 83, 84, 85, NULL, 86, 87, NOW()),
('build90', 9, 88, 89, 90, 214, 215, NULL, NOW()),

/* OWNER USER10 */
('build91', 10, 91, 92, 93, 94, 95, 96, NOW()),
('build92', 10, 97, 98, 99, 100, 218, NULL, NOW()),
('build93', 10, 219, 220, 221, 91, 92, NULL, NOW()),
('build94', 10, 93, 94, 95, 96, 97, 98, NOW()),
('build95', 10, 99, 100, 218, 219, 220, NULL, NOW()),
('build96', 10, 221, 91, 92, 93, 94, 95, NOW()),
('build97', 10, 96, 97, 98, NULL, 99, 100, NOW()),
('build98', 10, 218, 219, 220, 221, 91, 92, NOW()),
('build99', 10, 93, 94, 95, NULL, 96, 97, NOW()),
('build100', 10, 98, 99, 100, 218, 219, NULL, NOW()),

/* OWNER USER11 */
('build101', 11, 101, 102, 103, 104, 105, 106, NOW()),
('build102', 11, 107, 108, 109, 110, 222, NULL, NOW()),
('build103', 11, 223, 224, 225, 101, 102, NULL, NOW()),
('build104', 11, 103, 104, 105, 106, 107, 108, NOW()),
('build105', 11, 109, 110, 222, 223, 224, NULL, NOW()),
('build106', 11, 225, 101, 102, 103, 104, 105, NOW()),
('build107', 11, 106, 107, 108, NULL, 109, 110, NOW()),
('build108', 11, 222, 223, 224, 225, 101, 102, NOW()),
('build109', 11, 103, 104, 105, NULL, 106, 107, NOW()),
('build110', 11, 108, 109, 110, 222, 223, NULL, NOW()),

/* OWNER USER12 */
('build111', 12, 111, 112, 113, 114, 115, 116, NOW()),
('build112', 12, 117, 118, 119, 120, 226, NULL, NOW()),
('build113', 12, 227, 228, 229, 111, 112, NULL, NOW()),
('build114', 12, 113, 114, 115, 116, 117, 118, NOW()),
('build115', 12, 119, 120, 226, 227, 228, NULL, NOW()),
('build116', 12, 229, 111, 112, 113, 114, 115, NOW()),
('build117', 12, 116, 117, 118, NULL, 119, 120, NOW()),
('build118', 12, 226, 227, 228, 229, 111, 112, NOW()),
('build119', 12, 113, 114, 115, NULL, 116, 117, NOW()),
('build120', 12, 118, 119, 120, 226, 227, NULL, NOW());