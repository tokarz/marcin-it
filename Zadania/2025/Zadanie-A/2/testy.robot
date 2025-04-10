*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    Keywords.py

*** Variables ***
${url_czarni}    https://czarnijaslo.pl/
*** Keywords ***

*** Test Cases ***
test1   
    Open Browser    ${url_czarni}   chrome
    Maximize Browser Window
    Wyszukiwarka    czarni
    Kliknij Artykul1
    Sprawdz Url    https://czarnijaslo.pl/match/czarni-jas%c5%82o-stal-ii-mielec-2025-04-12/
    Close Browser

test2
    Open Browser    ${url_czarni}   chrome
    Maximize Browser Window
    Wyszukiwarka    sokol
    Kliknij Artykul2
    Sprawdz Url    https://czarnijaslo.pl/konferencja-po-sokole-sieniawa/
    Close Browser

test3
     Open Browser    ${url_czarni}   chrome
    Maximize Browser Window
    Wyszukiwarka    facebook
    Kliknij Artykul3
    Sprawdz Url    https://czarnijaslo.pl/charlie-works-wspiera-czarnych/
    Close Browser


    
