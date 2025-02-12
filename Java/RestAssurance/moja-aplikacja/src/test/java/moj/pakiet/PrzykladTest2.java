package moj.pakiet;

import org.junit.jupiter.api.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class PrzykladTest2 {

    @Test
    public void test9() {

        WebDriver driver = new ChromeDriver();

        driver.get("https://jsonplaceholder.typicode.com/users/1");



    }

}
