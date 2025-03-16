*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Variables ***
${URL}    https://czarnijaslo.pl/
${CSS_ROZGRYWKI}    .menu-item-10461

*** Keywords ***
Przygotowanie Srodowiska
    Open Browser    https://czarnijaslo.pl/    chrome
    Wait Until Element Is Visible    css=#menu-menu-3 ${CSS_ROZGRYWKI} 
    # od nas do przegladarki
    
    Mouse Over    css=#menu-menu-3 ${CSS_ROZGRYWKI}
    Wait Until Element Is Visible    css=#menu-menu-3 .menu-item-10357
    Click Element    css=#menu-menu-3 .menu-item-10357
    Wait Until Location Is    https://czarnijaslo.pl/competition/4-liga-podkarpacka/
    Scroll Element Into View    css=a[href="https://czarnijaslo.pl/club/czarni-jaslo/"]
    
    Click Element    css=a[href="https://czarnijaslo.pl/club/czarni-jaslo/"]
    Wait Until Location Is    https://czarnijaslo.pl/club/czarni-jaslo/

*** Test Cases ***
Clicking on Rozgrywki
    [Setup]    Przygotowanie Srodowiska    
    ${club_infos}    Get WebElements   css=.club-header__option-value
    
    ${count}    Get Length    ${club_infos}
    Log    Znaleziono ${count} elementów

    ${founded_element}    Get From List    ${club_infos}    2
    ${founded}    Get Text    ${founded_element}
    Should Be Equal As Strings    ${founded}    1910
    
    Close Browser

