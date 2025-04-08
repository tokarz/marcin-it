*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    libs/MojeMetody.py

Resource   Logowanie.robot




*** Test Cases ***

test1
    Logowanie Meczyki
    #Custom Hover    locator=a[href="/bukmacherzy"]
    #Hover And Click    selector1=a[href="/bukmacherzy"]    selector2=a[href="/bukmacherzy/nowy-bukmacher/165"] 
    #Sleep    5s
    Custom Click    locator=a[href="/newsy"]
    Location Should Be    url=https://www.meczyki.pl/newsy
