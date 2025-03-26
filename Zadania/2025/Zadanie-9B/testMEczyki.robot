*** Settings ***
Library    SeleniumLibrary
Library    Collections
Resource    logowanieMeczyki.robot

*** Variables ***
${selektor_strzelcyLaLiga}    //a[@href="/liga/laliga/7/ranking/strzelcy"]
${selektor_1miejsce}    //div[@class="table stats-table"]//table[@class="base"]//td[@class="longer"]:first-child
${selektor_do_scrolla}    //a[@href="/porady/liga-mistrzow-gdzie-ogladac/18"]


*** Test Cases ***
Test1
    logowanieMeczyki
    Sleep    2
    Scroll Element Into View    xpath=${selektor_do_scrolla}
    Click Element    xpath=${selektor_strzelcyLaLiga}
    Sleep    2
    ${lista_elementow}    Get WebElements    xpath=//td[@class="longer"]
    ${liczba_elementow}    Get Length    ${lista_elementow}
    ${pierwszy}    Get From List    ${liczba_elementow}    1
    ${znaleziony}    Get Text    ${pierwszy}
    Should Be Equal As Strings    ${znaleziony}    Robert Lewandowski  


    Wait Until Element Is Visible    xpath=${selektor_1miejsce}
    Element Should Contain    xpath=${selektor_1miejsce}    Robert Lewandowski


Test2
    logowanieMeczyki    
    Sleep    2    
    Scroll Element Into View    xpath=${selektor_strzelcyLaLiga}
    Click Element    xpath=${selektor_strzelcyLaLiga}
    Sleep    2
    ${lista}    Get WebElements    
    
