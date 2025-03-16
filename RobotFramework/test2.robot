*** Settings ***
Library    SeleniumLibrary
Library    Browser

*** Variables ***
     

*** Test Cases ***

Test_logowania_meczyki
    SeleniumLibrary.Open Browser    https://www.meczyki.pl/    chrome
    SeleniumLibrary.Maximize Browser Window
    #Zaakceptuj cookies
    SeleniumLibrary.Wait Until Element Is Visible    id=sp_message_iframe_1174352    timeout=10s
    SeleniumLibrary.Select Frame    id=sp_message_iframe_1174352
    SeleniumLibrary.Click Button    xpath=//button[contains(text(),'Zaakceptuj i zamknij')]  # Dostosuj ten selektor według potrzeby
    SeleniumLibrary.Unselect Frame
    #Klikamy przycisk logowania
    SeleniumLibrary.Wait Until Element Is Visible   xpath=//div[@class="col buttons"]//a[@href="/logowanie.html"]
    SeleniumLibrary.Click Element    xpath=//div[@class="col buttons"]//a[@href="/logowanie.html"]
    #Dane logowania
    SeleniumLibrary.Wait Until Element Is Visible    css=.input-formatter:first-child
    SeleniumLibrary.Click Element    css=.input-formatter:first-child
    SeleniumLibrary.Input Text    xpath=//input[@placeholder="Login lub adres e-mail"]    czarny-python
    SeleniumLibrary.Input Text    xpath=//input[@placeholder="Hasło"]    Tester#!Tester#!
    #Click zaloguj
    SeleniumLibrary.Click Element    css=.login-button
    #Wyloguj
    SeleniumLibrary.Wait Until Element Is Visible    css=.user-arrow
    SeleniumLibrary.Click Element    css=.user-arrow
    SeleniumLibrary.Click Element    css=.user-menu .router-link-exact-active
    #zamknij przegladarke
    SeleniumLibrary.Close Browser

