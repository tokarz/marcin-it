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

public class AppTest {
    public final String CSS_WYDARZENIA = ".menu-item-327";
    public final String CSS_KLUB100 = ".menu-item-626";
    private WebDriver driver;
    private MainPage mainPage;

    @BeforeEach
    public void setUp() {
        // Set up WebDriver and launch Chrome browser
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();

        // Maximize window and set implicit wait
        driver.manage().window().maximize();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(5));
        this.mainPage = new MainPage(driver);
    }

    @Test
    public void testKlub100(){
        mainPage.open();
        mainPage.click_aktualnosci(CSS_KLUB100);
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        wait.until(ExpectedConditions.urlToBe("https://czarnijaslo.pl/category/klub-100/"));
            String currentUrl = driver.getCurrentUrl();
            String expectedUrl = "https://czarnijaslo.pl/category/klub-100/";
            assertEquals(expectedUrl, currentUrl, "Weryfikacja URL nie powiodła się!");


    }

    @Test
    public void testAktualnosci() {
        // Użycie WebDriverManager do automatycznego ustawiania chromedrivera (jeśli chcesz)
        // WebDriverManager.chromedriver().setup();

        // Ustawienie ścieżki do chromedrivera, jeśli nie używasz WebDriverManager
       // System.setProperty("webdriver.chrome.driver", "path/to/chromedriver");

        //WebDriver driver = new ChromeDriver();

        try {
            // 1. Otwórz stronę docelową
            mainPage.open();

            // 2. Czekaj aż elementy o klasie CSS '.menu-item-327' będą obecne
            WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
            wait.until(isElementVisible());

            // 3. Zidentyfikuj drugi element i kliknij go
            mainPage.click(CSS_WYDARZENIA);

            // 4. Czekaj aż zmieni się URL po kliknięciu
            wait.until(ExpectedConditions.urlToBe("https://czarnijaslo.pl/category/wydarzenia/"));

            // 5. Weryfikacja URL
            String currentUrl = driver.getCurrentUrl();
            String expectedUrl = "https://czarnijaslo.pl/category/wydarzenia/";
            assertEquals(expectedUrl, currentUrl, "Weryfikacja URL nie powiodła się!");

        } finally {
            // 6. Zamknij przeglądarkę po zakończeniu testu
            driver.quit();
        }
    }

    @Test
    public void testAkademia(){
        
            driver.get("https://czarnijaslo.pl/");

            
            WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
            List<WebElement> wszystkieElementyAkademia = wait.until(
                ExpectedConditions.presenceOfAllElementsLocatedBy(By.cssSelector(".menu-item-18804"))
            );

           
            if (wszystkieElementyAkademia.size() > 1) {
                WebElement drugiElement = wszystkieElementyAkademia.get(1);
                drugiElement.click();

               
                wait.until(ExpectedConditions.urlToBe("https://www.facebook.com/APCzarniJaslo"));

               
                String currentUrl = driver.getCurrentUrl();
                String expectedUrl = "https://www.facebook.com/APCzarniJaslo";

                if (currentUrl.equals(expectedUrl)) {
                    System.out.println("URL verification passed!");
                } else {
                    System.out.println("URL verification failed! Expected: " + expectedUrl + ", but got: " + currentUrl);
                }
            } else {
                System.out.println("Nie znaleziono wystarczającej liczby elementów!");
            }

        }


    @Test
    public void testJuniorzyMlodsi(){
           
            driver.get("https://czarnijaslo.pl/");

        
            WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
            WebElement druzyny = wait.until(
                ExpectedConditions.visibilityOfElementLocated(By.cssSelector(".menu-item-10460"))
            );
            druzyny.click();

        
            WebElement juniorzyMlodsi = wait.until(
                ExpectedConditions.visibilityOfElementLocated(By.cssSelector(".menu-item-10362"))
            );
            juniorzyMlodsi.click();

      
            String expectedUrl = "https://czarnijaslo.pl/juniorzy-mlodsi/";
            wait.until(ExpectedConditions.urlToBe(expectedUrl));

        
            String currentUrl = driver.getCurrentUrl();
            if (currentUrl.equals(expectedUrl)) {
                System.out.println("URL verification passed!");
            } else {
                System.out.println("URL verification failed! Expected: " + expectedUrl + ", but got: " + currentUrl);
            }

    }

    private ExpectedCondition<List<WebElement>> isElementVisible(){
        return ExpectedConditions.presenceOfAllElementsLocatedBy(By.cssSelector(CSS_WYDARZENIA));
    }



    @AfterEach
    public void tearDown() {
        // Close the browser
        if (driver != null) {
            driver.quit();
        }
    }

}
