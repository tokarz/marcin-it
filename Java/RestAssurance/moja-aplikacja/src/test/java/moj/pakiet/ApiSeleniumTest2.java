package moj.pakiet;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.Test;

import io.github.bonigarcia.wdm.WebDriverManager;
import io.restassured.RestAssured;
import io.restassured.response.Response;


public class ApiSeleniumTest2 {


    @Test
    public void selenumTest(){
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com";

        Response response = RestAssured        //Nie wiem czemu podkresla mi tu RestAssured i cos nie dziala 
        given()
        .when()
            .get("posts/1/comments")
        .then()
            .statusCode(200)
            .extract()
            .response();

        int postId = response.jsonPath().getInt("[0].postId");
        String email = response.jsonPath().getString("[0].email");

        System.out.println("Extracted post Id : " + postId);
        System.out.println("Extracted email : " + email);

        WebDriverManager.chromedriver().setup();
        WebDriver driver = new ChromeDriver();

        try {
            String userUrl = "https://jsonplaceholder.typicode.com/posts/1/comments" + postId;
            driver.get(userUrl);

            String pageTitle = driver.getTitle();
            System.out.println("Page title : " + pageTitle);

            WebElement emailWebElement = driver.findElement(By.tagName("h1"));  //Selektor do wymiany bo nie wiem jak go zlokalizowac na tej stronie####
            String displayedEmail = emailWebElement.getText();
            System.out.println("User name : " + displayedEmail);

            if (email.equals(displayedEmail)) {
                System.out.println("✅ Email name matches the API response!");
            } else {
                System.out.println("❌ Email name does not match the API response!");
            }

            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                driver.quit();
            }



        }


    }
    

