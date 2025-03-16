*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
My_test
    Open Browser    https://czarnijaslo.pl/    chrome
    Wait Until Element Is Visible    css=#menu-menu-3 .menu-item-327
    Click Element    css=#menu-menu-3 .menu-item-327
    Wait Until Location Is    https://czarnijaslo.pl/category/wydarzenia/
    ${current_url}=    Get Location
    Should Be Equal As Strings    ${current_url}    https://czarnijaslo.pl/category/wydarzenia/
    Close Browser

My_test2
    Open Browser    https://czarnijaslo.pl/     firefox
    Wait Until Location Is    https://czarnijaslo.pl/ 
    Click Element    css=#menu-menu-3 .menu-item-20775
    Wait Until Location Is    https://www.facebook.com/APCzarniJaslo
    ${current_url}=    Get Location    
    Should Be Equal As Strings    ${current_url}    https://www.facebook.com/APCzarniJaslo
    Close Browser

My_test3
    Open Browser    https://czarnijaslo.pl/    chrome
    Maximize Browser Window
    Wait Until Element Is Visible    css=.tdb-search-icon.tdb-search-icon-svg
    Click Button    css=.tdb-search-icon.tdb-search-icon-svg
    Wait Until Element Is Visible    css=.tdb-head-search-form-input
    Click Button    css=.tdb-head-search-form-input
    Input Text    css=.tdb-head-search-form-input    trener
    Click Button    css=.tdb-head-search-form-btn"
    Wait Until Element Is Visible    css=.td-module-title(0)
    Click Button    css=.td-module-title
    Wait Until Location Is    https://czarnijaslo.pl/staz-trenerow-w-girona-fc/
    ${current_url}=    Get Location    
    Should Be Equal As Strings    ${current_url}    https://czarnijaslo.pl/staz-trenerow-w-girona-
    Close Browser

My_test4
    Open Browser    https://czarnijaslo.pl/     chrome
    Maximize Browser Window
    Wait Until Location Is    https://czarnijaslo.pl/ 
    Click Element    css=#menu-menu-3 .menu-item-626
    Wait Until Location Is    https://czarnijaslo.pl/category/klub-100/
    Click Element    css=.td-read-more:first-child
    Go Back
    Close Browser



