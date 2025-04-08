*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    libs/MojeMetody.py

Resource   Logowanie.robot




*** Test Cases ***

test1
    Logowanie Meczyki
    Custom Hover    css=a[href="/bukmacherzy"] 
    Sleep    5s
