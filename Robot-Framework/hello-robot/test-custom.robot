*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
REQ1_TS1_TC3: Testing clicking on "Aktualnosci"
    Open Browser    https://czarnijaslo.pl/    chrome

    ${menu-items}    Get WebElement    css=.menu-item
    
    # FOR    ${item}    IN    ${menu-items}
    #     Log To Console    Element
    # END

    # FOR    ${i}    IN RANGE    3    5
    #     Log    Iteration ${i}
    # END
    
    # Run Keyword If    ${menu-items}.length >=5    Log    Za duzo opcji widocznych
    
    

    Run Keyword If    2 > 1   Log To Console    2 wieksze od 1
    # ${current_url}=    Get Location
    # Should Be Equal As Strings    ${current_url}    https://czarnijaslo.pl/category/wydarzenia/
    Close Browser