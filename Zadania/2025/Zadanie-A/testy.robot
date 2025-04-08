*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    libs/MojeMetody.py

Resource   Logowanie.robot




*** Test Cases ***

test1
    Logowanie Meczyki
    #Custom Hover    locator=a[href="/bukmacherzy"]
    Sleep    2s
    Hover And Click    css:a[href="/bukmacherzy"]    a[href="/bukmacherzy/nowy-bukmacher/165"] 
    #Custom Click    css:a[href="/newsy"]
    Location Should Be    url=https://www.meczyki.pl/bukmacherzy/nowy-bukmacher/165
