USE football;

-- Insert teams from the 2023/24 season
INSERT INTO teams (name, country) VALUES
    ('Arsenal', 'England'),
    ('Real Madrid', 'Spain'),
    ('Inter Milan', 'Italy'),
    ('Bayern Munich', 'Germany');

-- Insert players for each team (15 players per team)
-- Arsenal players
INSERT INTO players (name, position, nationality, birthdate) VALUES
    ('Aaron Ramsdale', 'Goalkeeper', 'England', '1998-05-14'),
    ('Ben White', 'Defender', 'England', '1997-10-08'),
    ('Gabriel Magalhães', 'Defender', 'Brazil', '1997-12-19'),
    ('William Saliba', 'Defender', 'France', '2001-03-24'),
    ('Kieran Tierney', 'Defender', 'Scotland', '1997-06-05'),
    ('Thomas Partey', 'Midfielder', 'Ghana', '1993-06-13'),
    ('Granit Xhaka', 'Midfielder', 'Switzerland', '1992-09-27'),
    ('Martin Ødegaard', 'Midfielder', 'Norway', '1998-12-17'),
    ('Bukayo Saka', 'Forward', 'England', '2001-09-05'),
    ('Gabriel Jesus', 'Forward', 'Brazil', '1997-04-03'),
    ('Eddie Nketiah', 'Forward', 'England', '1999-05-30'),
    ('Emile Smith Rowe', 'Midfielder', 'England', '2000-07-28'),
    ('Rob Holding', 'Defender', 'England', '1995-09-20'),
    ('Takehiro Tomiyasu', 'Defender', 'Japan', '1998-11-05'),
    ('Reiss Nelson', 'Forward', 'England', '1999-12-10');

-- Real Madrid players
INSERT INTO players (name, position, nationality, birthdate) VALUES
    ('Thibaut Courtois', 'Goalkeeper', 'Belgium', '1992-05-11'),
    ('Dani Carvajal', 'Defender', 'Spain', '1992-01-11'),
    ('Éder Militão', 'Defender', 'Brazil', '1998-01-18'),
    ('David Alaba', 'Defender', 'Austria', '1992-06-24'),
    ('Ferland Mendy', 'Defender', 'France', '1995-06-08'),
    ('Casemiro', 'Midfielder', 'Brazil', '1992-02-23'),
    ('Luka Modrić', 'Midfielder', 'Croatia', '1985-09-09'),
    ('Toni Kroos', 'Midfielder', 'Germany', '1990-01-04'),
    ('Federico Valverde', 'Midfielder', 'Uruguay', '1998-07-22'),
    ('Karim Benzema', 'Forward', 'France', '1987-12-19'),
    ('Vinícius Júnior', 'Forward', 'Brazil', '2000-07-12'),
    ('Rodrygo', 'Forward', 'Brazil', '2001-01-09'),
    ('Marco Asensio', 'Forward', 'Spain', '1996-01-21'),
    ('Nacho Fernández', 'Defender', 'Spain', '1990-01-18'),
    ('Lucas Vázquez', 'Forward', 'Spain', '1991-07-01');

-- Inter Milan players
INSERT INTO players (name, position, nationality, birthdate) VALUES
    ('Samir Handanović', 'Goalkeeper', 'Slovenia', '1984-07-14'),
    ('Milan Škriniar', 'Defender', 'Slovakia', '1995-02-11'),
    ('Stefan de Vrij', 'Defender', 'Netherlands', '1992-02-05'),
    ('Alessandro Bastoni', 'Defender', 'Italy', '1999-04-13'),
    ('Denzel Dumfries', 'Defender', 'Netherlands', '1996-04-18'),
    ('Marcelo Brozović', 'Midfielder', 'Croatia', '1992-11-16'),
    ('Nicolo Barella', 'Midfielder', 'Italy', '1997-02-07'),
    ('Hakan Çalhanoğlu', 'Midfielder', 'Turkey', '1994-02-08'),
    ('Arturo Vidal', 'Midfielder', 'Chile', '1987-05-22'),
    ('Edin Džeko', 'Forward', 'Bosnia and Herzegovina', '1986-03-17'),
    ('Lautaro Martínez', 'Forward', 'Argentina', '1997-08-22'),
    ('Joaquín Correa', 'Forward', 'Argentina', '1994-08-13'),
    ('Ivan Perišić', 'Forward', 'Croatia', '1989-02-02'),
    ('Matteo Darmian', 'Defender', 'Italy', '1989-12-02'),
    ('Andrea Ranocchia', 'Defender', 'Italy', '1988-02-16');

-- Bayern Munich players
INSERT INTO players (name, position, nationality, birthdate) VALUES
    ('Manuel Neuer', 'Goalkeeper', 'Germany', '1986-03-27'),
    ('Benjamin Pavard', 'Defender', 'France', '1996-03-28'),
    ('Dayot Upamecano', 'Defender', 'France', '1998-10-27'),
    ('Lucas Hernández', 'Defender', 'France', '1996-02-14'),
    ('Alphonso Davies', 'Defender', 'Canada', '2000-11-02'),
    ('Joshua Kimmich', 'Midfielder', 'Germany', '1995-02-08'),
    ('Leon Goretzka', 'Midfielder', 'Germany', '1995-02-06'),
    ('Thomas Müller', 'Forward', 'Germany', '1989-09-13'),
    ('Leroy Sané', 'Forward', 'Germany', '1996-01-11'),
    ('Serge Gnabry', 'Forward', 'Germany', '1995-07-14'),
    ('Kingsley Coman', 'Forward', 'France', '1996-06-13'),
    ('Robert Lewandowski', 'Forward', 'Poland', '1988-08-21'),
    ('Jamal Musiala', 'Midfielder', 'Germany', '2003-02-26'),
    ('Niklas Süle', 'Defender', 'Germany', '1995-09-03'),
    ('Eric Maxim Choupo-Moting', 'Forward', 'Cameroon', '1989-03-23');

-- Assign players to teams in player_history
-- For simplicity, assuming all players joined their teams on the same date
-- Arsenal players
INSERT INTO player_history (player_id, team_id, start_date) VALUES
    (1, 1, '2023-08-01'),
    (2, 1, '2023-08-01'),
    (3, 1, '2023-08-01'),
    (4, 1, '2023-08-01'),
    (5, 1, '2023-08-01'),
    (6, 1, '2023-08-01'),
    (7, 1, '2023-08-01'),
    (8, 1, '2023-08-01'),
    (9, 1, '2023-08-01'),
    (10, 1, '2023-08-01'),
    (11, 1, '2023-08-01'),
    (12, 1, '2023-08-01'),
    (13, 1, '2023-08-01'),
    (14, 1, '2023-08-01'),
    (15, 1, '2023-08-01');

-- Real Madrid players
INSERT INTO player_history (player_id, team_id, start_date) VALUES
    (16, 2, '2023-08-01'),
    (17, 2, '2023-08-01'),
    (18, 2, '2023-08-01'),
    (19, 2, '2023-08-01'),
    (20, 2, '2023-08-01'),
    (21, 2, '2023-08-01'),
    (22
::contentReference[oaicite:1]{index=1}
 
