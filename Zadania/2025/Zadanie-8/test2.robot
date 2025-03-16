*** Settings ***
Library    SeleniumLibrary
Library    Collections
*** Variables ***


*** Keywords ***

Setup
    Open Browser    https://www.meczyki.pl/    chrome
    Maximize Browser Window
Logowanie Meczyki
    #Zaakceptuj cookies
    Wait Until Element Is Visible    id=sp_message_iframe_1174352    timeout=10s
    Select Frame    id=sp_message_iframe_1174352
    Click Button    xpath=//button[contains(text(),'Zaakceptuj i zamknij')]  # Dostosuj ten selektor według potrzeby
    Unselect Frame
    #Klikamy przycisk logowania
    Wait Until Element Is Visible   xpath=//div[@class="col buttons"]//a[@href="/logowanie.html"]
    Click Element    xpath=//div[@class="col buttons"]//a[@href="/logowanie.html"]
    #Dane logowania
    Wait Until Element Is Visible    css=.input-formatter:first-child
    Click Element    css=.input-formatter:first-child
    Input Text    xpath=//input[@placeholder="Login lub adres e-mail"]    czarny-python
    Input Text    xpath=//input[@placeholder="Hasło"]    Tester#!Tester#!
    #Click zaloguj
    Click Element    css=.login-button

Rozwiniecie opcji usera
    Wait Until Element Is Visible    css=.user-arrow
    Click Element    css=.user-arrow

Klikniecie Profilu uzytkownika
    Click Element    xpath=//div[@class="user-menu"]//a[contains(text(),"Twój profil")]

Klikniecie ekstraklasa
    Scroll Element Into View    xpath=//div[@class="col"]//ul[@class="nav nav-sidebar"]//li[@class="nav-sidebar-menu-item"]//a[@href="/liga/ekstraklasa/119"]
    Click Element    xpath =//div[@class="col"]//ul[@class="nav nav-sidebar"]//li[@class="nav-sidebar-menu-item"]//a[@href="/liga/ekstraklasa/119"]
    
    

    


*** Test Cases ***
Test_przycisku wyloguj  
    Setup  
    Logowanie Meczyki
    Rozwiniecie opcji usera
    SeleniumLibrary.Click Element    css=.user-menu .router-link-exact-active
    Log To Console    ///Wylogowano///
    #zamknij przegladarke
    SeleniumLibrary.Close Browser

Test_sprawdzenie_nazwy_uzytkownika
    Setup
    Logowanie Meczyki
    Rozwiniecie opcji usera
    Klikniecie Profilu uzytkownika
    Wait Until Element Is Visible    css=.username
    ${username}    Get WebElement    css=.username
    ${nazwa}    Get Text    ${username}
    Should Be Equal As Strings    ${nazwa}    czarny-python
    Log To Console    nazwaUzytkownika : ${nazwa}
    Run Keyword If    '${nazwa}' != 'czarny-python'    Log To Console    Błąd: Nazwa użytkownika jest niepoprawna: ${nazwa}
    Close Browser

Test_sprawdzenie_czy_raków_lider
    Setup
    Logowanie Meczyki
    Klikniecie ekstraklasa  
    ${selektory}    Get WebElements    xpath=//div[@class="table boxy-wrappy"]//div[@class="texts condensed"]//span[@class="top" and contains(text(), "Raków Częstochowa")]      
    ${count}    Get Length    ${selektory}
    ${dobry_selektor}    Get From List    ${count}    1
    ${rakow}    Get Text    ${dobry_selektor}
    Should Be Equal As Strings    ${rakow}    Raków Częstochowa
    Log To Console    ///Klub to : ${rakow}///
    Run Keyword If    '${rakow}' != 'Raków Częstochowa'    Log To Console    Błąd: Klub jest zły!!!
    Close Browser

    
