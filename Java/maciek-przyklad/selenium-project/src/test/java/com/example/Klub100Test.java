package com.example;

import static org.junit.jupiter.api.Assertions.assertEquals;
import java.time.Duration;
import java.util.List;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import com.example.POM.MainPage;

import io.github.bonigarcia.wdm.WebDriverManager;


public class Klub100Test  extends AppTest{
    private WebDriver driver;
    private MainPage mainPage;
    

    @Test
    public void testKlub100(){
        mainPage.setUp();
        mainPage.open();
        mainPage.click_klub100();
        mainPage.sprawdzLink("https://czarnijaslo.pl/");
        mainPage.tearDown();
    }

    @Test
    public void testClickAndBack(){
        mainPage.setUp();
        mainPage.open();
        mainPage.click_klub100();
        mainPage.clickArtykolKlub100(0);
        mainPage.back();
        mainPage.clickArtykolKlub100(1);
        mainPage.back();
        mainPage.clickArtykolKlub100(2);
        mainPage.back();
        mainPage.clickArtykolKlub100(3);
        mainPage.back();
        mainPage.clickArtykolKlub100(4);
        mainPage.back();
        mainPage.clickArtykolKlub100(5);
        mainPage.back();
        mainPage.clickArtykolKlub100(6);
        mainPage.back();
        mainPage.clickArtykolKlub100(7);
        mainPage.back();
        mainPage.clickArtykolKlub100(8);
        mainPage.back();
        mainPage.clickArtykolKlub100(9);
        mainPage.back();
        mainPage.tearDown();
    }
}


