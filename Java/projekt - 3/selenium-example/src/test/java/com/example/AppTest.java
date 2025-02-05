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



/**
 * Unit test for simple App.
 */
public class AppTest 

{
     @Test
    public void testNaglowekStrony() {
        // Upewnij się, że masz ustawiony chromedriver w systemie
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver");

        WebDriver driver = new ChromeDriver();
        
        try {
            // Wejdź na stronę www.czarnijaslo.pl
            driver.get("https://www.czarnijaslo.pl");

            // Pobierz tytuł strony
            String title = driver.getTitle();
            
            // Sprawdzamy, czy tytuł zawiera "czarni jaslo"
            assertTrue(title.toLowerCase().contains("czarni jasło"), 
                    "Tytuł strony nie zawiera 'czarni jasło'. Aktualny tytuł: " + title);
        } finally {
            // Zamknij przeglądarkę po teście
            driver.quit();
        }
    }

    
}
