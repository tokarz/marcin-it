*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Test Cases ***
Test_daty
    #otwieramy strone
    Open Browser    https://czarnijaslo.pl/    chrome
    Maximize Browser Window
    #czekamy na zaladowanie i klikamy w 4liga
    Wait Until Location Is    https://czarnijaslo.pl/ 
    Wait Until Element Is Visible    xpath=//div[@class="tdb-menu-items-pulldown"]//div[@class="tdb-menu-item-text"][contains(text(),"Rozgrywki")]
    Click Element    css=.tdb-block-menu .menu-item-10461
    Click Element    xpath=//div[@class="tdb-menu-items-pulldown"]//div[@class="tdb-menu-item-text"][contains(text(),"Rozgrywki")]
    #kikamy w czarnych
    Wait Until Element Is Visible    xpath=//div[@class="competition__group-wrapper"]//div[@class="d-flex flex-column"]//a[contains(@href, "https://czarnijaslo.pl/club/czarni-jaslo/")]
    Click Element    xpath=//div[@class="competition__group-wrapper"]//div[@class="d-flex flex-column"]//a[contains(@href, "https://czarnijaslo.pl/club/czarni-jaslo/")]
    #sprawdzenie daty
    ${info}    Get WebElements    xpath=//div[@class="club-header__option-value"]
    ${count}    Get Length    ${info}
    ${rok_zalozenia}    Get From List    ${info}    1
    ${rok}    Get Text    ${rok_zalozenia}
    Should Be Equal As Strings    ${rok}    1910
    Log To Console    Data zalozenia: ${rok}
    Close Browser


