*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://czarnijaslo.pl/

*** Test Cases ***
REQ1_TS1_TC3: Testing clicking on "Aktualnosci"
    Open Browser    https://czarnijaslo.pl/    chrome
    Sleep    10s
    # od nas do przegladarki
    
    ${current_url}=    Get Location
    Should Be Equal As Strings    ${current_url}    https://czarnijaslo.pl/category/wydarzenia/
    Close Browser

REQ1_TS1_TC4: Testing clicking on "Sponsoring"
    Open Browser    https://czarnijaslo.pl/    chrome
    Sleep    10s
    # od nas do przegladarki
    Click Element    css=#menu-menu-3 .menu-item-327
    
    Sleep    5s
    ${current_url}=    Get Location
    Should Be Equal As Strings    ${current_url}    https://czarnijaslo.pl/sponsoring/
    Close Browser
    

REQ3_1 Test przycisku Koszulki meczowe 2024/25: Testing clicking on "Sponsoring"
    Open Browser    https://czarnijaslo.pl/    chrome
    Wait Until Element Is Visible    css=#menu-menu-3 .menu-item-327
    Mouse Over    css=.menu-item-kibice
    Click Element    css=.koszulki-meczowe


click_all_readmore
    Open Browser    ${URL}    chrome
    Maximize Browser Window
    Sleep    5
    Click Element    css=#menu-menu-3 .menu-item-626
    
    Wait Until Location Is    https://czarnijaslo.pl/category/klub-100/
    Sleep    3
    
    ${read_more_buttons}    Get WebElements    css=.td-read-more

    ${count}    Get Length    ${read_more_buttons}

    FOR  ${index}  IN RANGE  ${count}
        ${aktualny_button}    Set Variable    ${read_more_buttons}[${index}]

        Wait Until Element Is Visible    ${aktualny_button}
        Click Element    ${aktualny_button}
        Wait Until Location Is Not    https://czarnijaslo.pl/category/klub-100/
        Go Back
        Wait Until Location Is    https://czarnijaslo.pl/category/klub-100/
    END
    
    Sleep    5
    
    Close Browser