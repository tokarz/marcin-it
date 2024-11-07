import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;
import java.util.List;







class X {
    String id = "Moja Klasa";
    int ilosc = 100;



}


















public class SeleniumTest {
   main(args) {
        // Set up the Chrome driver
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver"); // Podaj ścieżkę do chromedriver
        WebDriver driver = new ChromeDriver();

        try {
            // 1. Otwórz stronę docelową
            driver.get("https://czarnijaslo.pl/");  // Podaj rzeczywisty URL

            // 2. Czekaj, aż element z selektorem CSS '.menu-item-327' będzie obecny
            WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
            List<WebElement> wszystkieOpcje = wait.until(
                    ExpectedConditions.presenceOfAllElementsLocatedBy(By.cssSelector(".menu-item-327"))
            );

            // 3. Znajdź drugi element i kliknij
            WebElement aktualnosci = wszystkieOpcje.get(1);
            aktualnosci.click();

            // 4. Poczekaj, aż nawigacja na nową stronę się zakończy
            wait.until(ExpectedConditions.urlContains("category/wydarzenia")); // Fragment URL, który ma się pojawić

            // 5. Sprawdź bieżący URL
            String currentUrl = driver.getCurrentUrl();
            String expectedUrl = "https://czarnijaslo.pl/category/wydarzenia/";  // Podaj oczekiwany URL
            if (currentUrl.equals(expectedUrl)) {
                System.out.println("URL verification passed!");
            } else {
                System.out.println("URL verification failed! Expected: " + expectedUrl + ", but got: " + currentUrl);
            }

        } finally {
            // 6. Zamknij przeglądarkę po zakończeniu
            driver.quit();
        }
    }
}