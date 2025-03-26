*** Settings ***
Library    SeleniumLibrary
Library    Collections
*** Variables ***
${id_frame}    sp_message_iframe_1174352    
${click_zaakceptuj_frame}    //button[contains(text(),'Zaakceptuj i zamknij')]   
${selektor_logowanie}    xpath=//div[@class="col buttons"]//a[@href="/logowanie.html"]
${input}    .input-formatter:first-child  
${login}    //input[@placeholder="Login lub adres e-mail"]  
${haslo}    //input[@placeholder="Hasło"]     
${selektor_zaloguj}    .login-button

*** Keywords ***
Logowanie Meczyki
    Open Browser    https://www.meczyki.pl/    chrome
    Maximize Browser Window
    #Zaakceptuj cookies
    Wait Until Element Is Visible    id=${id_frame}    timeout=10s
    Select Frame    id=${id_frame}
    Click Button    xpath=${click_zaakceptuj_frame}
    Unselect Frame
    #Klikamy przycisk logowania
    Wait Until Element Is Visible   xpath=//div[@class="col buttons"]//a[@href="/logowanie.html"]
    Click Element    xpath=//div[@class="col buttons"]//a[@href="/logowanie.html"]
    #Dane logowania
    Wait Until Element Is Visible    css=${input}
    Click Element    css=${input}
    Input Text    xpath=${login}    czarny-python
    Input Text    xpath=${haslo}    Tester#!Tester#!
    #Click zaloguj
    Click Element    css=${selektor_zaloguj}