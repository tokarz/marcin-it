package com.example.POM;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class MainPage {
    WebDriver driver;

    public MainPage(WebDriver driver) {
        this.driver = driver;

    }

    public void click(String selektor) {
        WebElement aktualnosci = driver.findElements(By.cssSelector(selektor)).get(1); // Zwróć drugi element
        aktualnosci.click();

    }
    public void open(){
        this.driver.get("https://czarnijaslo.pl/");
    }
}
