
--6) napisz selekty w plikach SQL albo w pythonie (jak wolisz):


--1) wszytkie mecze Wisly Kraków, z ostatniego miesiaca
    
SELECT mecz_id, data_meczu, wynik_gospodarz, wynik_gosc
FROM public.mecze
JOIN kluby AS gospodarze ON mecze.klub_gospodarz_id = gospodarze.klub_id
JOIN kluby AS goscie ON mecze.klub_gosc_id = goscie.klub_id
WHERE (gospodarze.nazwa = 'Wisła Kraków' OR goscie.nazwa = 'Wisła Kraków') 
  AND data_meczu >= CURRENT_DATE - INTERVAL '30 days';   
--- nie wiedzialem jak polaczyc dwa razy kluby bo musialem podac klub_gospodarz_id i klub_gosc_id za jednym rzem wiec dopytalem czata po wielu probach
--- i dodalem te aliasy , pozniej nie wiedzialem jak z data zrobic i tez spytalem czata bo nie mialem jeszcze takiego przykladu

--2)wszystkie mecze Lecha na wyjezdzie 

SELECT mecz_id , data_meczu , wynik_gospodarz, wynik_gosc  FROM mecze
JOIN kluby ON mecze.klub_gosc_id = kluby.klub_id
WHERE nazwa = 'Lech Poznań'
---tu nie bylo problemu :D

--3)wszystkie zwyciestwa Rakowa Czestochowa

SELECT mecz_id , data_meczu , wynik_gospodarz, wynik_gosc FROM mecze
JOIN kluby AS gospodarz ON mecze.klub_gospodarz_id = gospodarz.klub_id
JOIN kluby AS gosc ON mecze.klub_gosc_id = gosc.klub_id
WHERE (gospodarz.nazwa = 'Raków Częstochowa' AND wynik_gospodarz > wynik_gosc)
OR (gosc.nazwa = 'Raków Częstochowa' AND wynik_gosc > wynik_gospodarz);
--- tu tez mialem problem z tym wynikiem jak to zapisac zeby mi pokazalo wpierw kiedy wygrali u siebie i wtedy kiedy na wyjezdzie

--4)wszystkie porazki albo zwyciestwa Jagielonii u siebie 

SELECT mecz_id , data_meczu , wynik_gospodarz, wynik_gosc FROM mecze
JOIN kluby ON mecze.klub_gospodarz_id = kluby.klub_id
WHERE nazwa = 'Jagiellonia Białystok' AND wynik_gospodarz > wynik_gosc
OR nazwa ='Jagiellonia Białystok' AND wynik_gospodarz < wynik_gosc;
--tu mi poszlo w miare ok bo podobnie juz do wczesniejszego z tym ze tylko u siebie wiec nie trzeba uzywac aliasow

--5)ostatnie 5 meczow Legii z Wisłą (dane  możesz dopisać do tabeli żeby ładnie było widać, ale  sam SELECT też wystarczy)

SELECT mecz_id , data_meczu , wynik_gospodarz, wynik_gosc FROM mecze
JOIN kluby AS gosp ON mecze.klub_gospodarz_id = gosp.klub_id
JOIN kluby AS gosc ON mecze.klub_gosc_id = gosc.klub_id
WHERE gosp.nazwa = 'Legia Warszawa' AND gosc.nazwa = 'Wisła Kraków'
OR gosp.nazwa = 'Wisła Kraków' AND gosc.nazwa = 'Legia Warszawa'
ORDER BY data_meczu DESC
LIMIT 5
--- tu mi poszlo ok i mysle ze jest git

--6) historię wszystkich klubów założonych przed wojną :)
a
