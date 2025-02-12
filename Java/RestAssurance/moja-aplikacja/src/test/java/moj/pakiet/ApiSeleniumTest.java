package moj.pakiet;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.Test;

import io.github.bonigarcia.wdm.WebDriverManager;
import io.restassured.RestAssured;
import io.restassured.response.Response;



public class ApiSeleniumTest {
    
    @Test
    public void test() {
        // Step 1: API Request to Get First User ID
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com";
        Response response = RestAssured
                .given()
                .when()
                .get("/users")
                .then()
                .statusCode(200)
                .extract()
                .response();

        // Extracting the first user's ID
        int firstUserId = response.jsonPath().getInt("[0].id");
        String firstUserName = response.jsonPath().getString("[0].name");

        System.out.println("Extracted User ID: " + firstUserId);
        System.out.println("Extracted User Name: " + firstUserName);

        // Step 2: Open Browser and Navigate to User Page
        WebDriverManager.chromedriver().setup();
        WebDriver driver = new ChromeDriver();

        try {
            String userUrl = "https://jsonplaceholder.typicode.com/users/" + firstUserId;
            driver.get(userUrl);

            // Step 3: Validate Page Title
            String pageTitle = driver.getTitle();
            System.out.println("Page Title: " + pageTitle);

            // Step 4: Extract and Print User Name from the Page
            WebElement userNameElement = driver.findElement(By.tagName("h1"));
            String displayedUserName = userNameElement.getText();
            System.out.println("User Name on Page: " + displayedUserName);

            // Validate if the extracted name matches the API response
            if (firstUserName.equals(displayedUserName)) {
                System.out.println("✅ User name matches the API response!");
            } else {
                System.out.println("❌ User name does not match the API response!");
            }

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // Step 5: Close the browser
            driver.quit();
        }
    }
}
