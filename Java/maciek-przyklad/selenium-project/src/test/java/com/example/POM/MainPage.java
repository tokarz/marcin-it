package com.example.POM;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.time.Duration;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import io.github.bonigarcia.wdm.WebDriverManager;

public class MainPage {
    WebDriver driver;

    public MainPage(WebDriver driver) {
        this.driver = driver;

    }

    public void click_aktualnosci(String selektor) {
        WebElement aktualnosci = driver.findElements(By.cssSelector(selektor)).get(1); // Zwróć drugi element
        aktualnosci.click();

    }
    public void click_klub100() {
        WebElement element = driver.findElement(By.cssSelector(".menu-item-626"));
        element.click();
    }
    public void clickArtykolKlub100(int ktoryArt) {
        WebElement element = driver.findElements(By.cssSelector(".td-read-more")).get(ktoryArt);
        element.click();
    }
    public void back(){
        driver.navigate().back();
    }

    public void open() {
        this.driver.get("https://czarnijaslo.pl/");
    }

    @BeforeEach
    public void setUp() {
        // Setup ChromeDriver
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();

        // Maximize window and set implicit wait
        driver.manage().window().maximize();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(5));
    }
    
    @AfterEach
    public void tearDown() {
        // Close the browser
        if (driver != null) {
            driver.quit();
        }
    }
    public void sprawdzLink(String link){
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        wait.until(ExpectedConditions.urlToBe(link));
        String currentUrl = driver.getCurrentUrl();
        String expectedUrl = link;
        assertEquals(expectedUrl, currentUrl, "Weryfikacja URL nie powiodła się!");
    }

    }

