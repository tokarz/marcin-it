*** Settings ***
Library    SeleniumLibrary
Library    Collections
Resource    logowanieMeczyki.robot

*** Variables ***
${selektor_strzelcyLaLiga}    //h4[@class="title" and contains(text(), "Strzelcy")]
${selektor_1miejsce}    //div[@class="table stats-table"]//table[@class="base"]//td[@class="longer"]:first-child

*** Test Cases ***
Test1
    logowanieMeczyki
    Sleep    2
    Scroll Element Into View    xpath=${selektor_strzelcyLaLiga}
    #Execute Javascript    window.scrollTo(0, document.body.scrollHeight);
    Click Element    xpath=${selektor_strzelcyLaLiga}
    Wait Until Element Is Visible    xpath=${selektor_1miejsce}
    Element Should Contain    xpath=${selektor_1miejsce}    Robert Lewandowski
