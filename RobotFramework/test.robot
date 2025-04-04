*** Settings ***
Library    SeleniumLibrary
*** Variables ***
${URL}    https://czarnijaslo.pl/ 
${Aktualnosci}    css=#menu-menu-3 .menu-item-327         

*** Test Cases ***
My_test
    Open Browser    ${URL}   chrome
    Wait Until Element Is Visible    ${Aktualnosci}
    Click Element    ${Aktualnosci}
    Wait Until Location Is    https://czarnijaslo.pl/category/wydarzenia/
    ${current_url}=    Get Location
    Should Be Equal As Strings    ${current_url}    https://czarnijaslo.pl/category/wydarzenia/
    Close Browser

My_test2
    Open Browser    ${URL}    firefox
    Wait Until Location Is    ${URL}
    Click Element    css=#menu-menu-3 .menu-item-20775
    Wait Until Location Is    https://www.facebook.com/APCzarniJaslo
    ${current_url}=    Get Location    
    Should Be Equal As Strings    ${current_url}    https://www.facebook.com/APCzarniJaslo
    Close Browser

My_test3
    
    Open Browser    ${URL}   chrome
    Maximize Browser Window
   
    Wait Until Element Is Visible    css=.tdb-search-icon.tdb-search-icon-svg
    Click Element    css=.tdb-search-icon.tdb-search-icon-svg
   
    Wait Until Element Is Visible    css=.tdb-head-search-form-input
    Click Element    css=.tdb-head-search-form-input
    Input Text    css=.tdb-head-search-form-input    trener
    Click Element    css=.tdb-head-search-form-btn
    
    Wait Until Element Is Visible    css=.td-module-title:first-child
    Click Element    css=.td-module-title:first-child
   
    Wait Until Location Is    https://czarnijaslo.pl/staz-trenerow-w-girona-fc/
    ${current_url}=    Get Location    
    Should Be Equal As Strings    ${current_url}    https://czarnijaslo.pl/staz-trenerow-w-girona-fc/
    
    Close Browser

My_test4
    Open Browser    ${URL}    chrome
    Maximize Browser Window
    
    Wait Until Element Is Visible    css=#menu-menu-3 .menu-item-626
    Sleep    3
    Click Element    css=#menu-menu-3 .menu-item-626
    
    Wait Until Location Is    https://czarnijaslo.pl/category/klub-100/
    Sleep    3
    Wait Until Element Is Visible    css=div.td_module_11 .item-details .td-read-more
    Click Element    css=div.td_module_11 .item-details .td-read-more
    
    Go Back

    Sleep    5
    
    Close Browser
    
My_click_all_readmore
    Open Browser    ${URL}    chrome
    Maximize Browser Window
    
    Sleep    2
    Click Element    css=#menu-menu-3 .menu-item-626
    
    Wait Until Location Is    https://czarnijaslo.pl/category/klub-100/
    Sleep    2
    Wait Until Element Is Visible    css=div.td_module_11 .item-details .td-read-more
    
    ${read_more_buttons}    Get WebElements    css=.td-read-more

    ${count}    Get Length    ${read_more_buttons}

    FOR    ${index}    IN RANGE    ${count}
        ${current_location}    Get Location    
        Run Keyword If   ${index} > 5    Continue For Loop   

        ${aktualny_button}    Set Variable    ${read_more_buttons}[${index}]

        Wait Until Element Is Visible    ${aktualny_button}
        Click Element    ${aktualny_button}
        
        Wait Until Location Is Not    https://czarnijaslo.pl/category/klub-100/
        Go Back
        Wait Until Location Is    https://czarnijaslo.pl/category/klub-100/
    END
    
    Sleep    5
    
    Close Browser




