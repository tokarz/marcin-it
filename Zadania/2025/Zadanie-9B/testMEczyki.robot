*** Settings ***
Library    SeleniumLibrary
Library    Collections
Resource    logowanieMeczyki.robot

*** Variables ***
${selektor_strzelcyLaLiga}    //a[@href="/liga/laliga/7/ranking/strzelcy"]
${selektor_1miejsce}    td.longer > a.wrappy[href*="/zawodnik/r-lewandowski/41310"]
${selektor_do_scrolla}    //a[@href="/porady/liga-mistrzow-gdzie-ogladac/18"]


*** Test Cases ***
Test1
    logowanieMeczyki
    Sleep    2
    Scroll Element Into View    xpath=${selektor_do_scrolla}
    Click Element    xpath=${selektor_strzelcyLaLiga}
    Sleep    2
    Click Element    css=${selektor_1miejsce}
    Location Should Be    https://www.meczyki.pl/zawodnik/r-lewandowski/41310


Test2
    logowanieMeczyki    
    Sleep    2    
    Scroll Element Into View    xpath=${selektor_strzelcyLaLiga}
    Click Element    xpath=${selektor_strzelcyLaLiga}
    Sleep    2
    ${lista}    Get WebElements    
    
