package com.example;

import static org.junit.jupiter.api.Assertions.assertTrue;

import java.time.Duration;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import io.github.bonigarcia.wdm.WebDriverManager;

public class AppTest {
    private WebDriver driver;

    @BeforeEach
    public void setUp() {
        // Set up WebDriver and launch Chrome browser
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();

        // Maximize window and set implicit wait
        driver.manage().window().maximize();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(5));
    }

    @Test
    public void searchForKrakow() {
        // Open Google
        driver.get("http://www.czarnijaslo.pl");

        // Handle "Accept Cookies" pop-up (if present)
        try {
            WebElement acceptCookiesButton = driver.findElement(
                    By.xpath("//button[contains(text(),'Accept all')] | //button[contains(text(),'Zgadzam się')]"));
            acceptCookiesButton.click();
        } catch (Exception e) {
            System.out.println("No cookies popup found, continuing...");
        }

        // Find search box and enter "Krakow"
        WebElement searchBox = driver.findElement(By.name("q"));
        searchBox.sendKeys("Krakow");
        searchBox.sendKeys(Keys.RETURN);

        // Verify that results contain the word "Krakow"
        WebElement results = driver.findElement(By.cssSelector("div[id='abc']"));
        assertTrue(results.getText().toLowerCase().contains("krakow"), "Search results do not contain 'Krakow'");
    }

    @AfterEach
    public void tearDown() {
        // Close the browser
        if (driver != null) {
            driver.quit();
        }
    }

}
