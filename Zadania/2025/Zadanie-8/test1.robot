*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    PythonLibs/Logger.py
Library    PythonLibs/Clicker.py

*** Variables ***
${Rozgrywki}    .tdb-block-menu .menu-item-10461  
${xpath_rozgrywki}    //div[@class="tdb-menu-items-pulldown"]//div[@class="tdb-menu-item-text"][contains(text(),"IV liga")]  
${URL}    https://czarnijaslo.pl/
${link_to_czarnijaslo}    //div[@class="competition__group-wrapper"]//div[@class="d-flex flex-column"]//a[contains(@href, "https://czarnijaslo.pl/club/czarni-jaslo/")]    
*** Test Cases ***
Test_daty
    #otwieramy strone
    Open Browser    ${URL}    firefox
    Maximize Browser Window
    Log My Data    helloworld
    #czekamy na zaladowanie i klikamy w 4liga
    Wait Until Location Is    ${URL} 
    #Wait Until Element Is Visible    xpath=${Rozgrywki}
    Sleep    3
    Mouse Over   css=${Rozgrywki}
    #Click Element    xpath=${xpath_rozgrywki}
    Click Xpath    ${xpath_rozgrywki}    
    #kikamy w czarnych
    Wait Until Element Is Visible    xpath=${link_to_czarnijaslo}
    Click Element    xpath=${link_to_czarnijaslo}
    #sprawdzenie daty
    ${info}    Get WebElements    xpath=//div[@class="club-header__option-value"]
    ${count}    Get Length    ${info}
    ${rok_zalozenia}    Get From List    ${info}    1
    ${rok}    Get Text    ${rok_zalozenia}
    Should Be Equal As Strings    ${rok}    1910
    Log To Console    Data zalozenia: ${rok}
    Close Browser


