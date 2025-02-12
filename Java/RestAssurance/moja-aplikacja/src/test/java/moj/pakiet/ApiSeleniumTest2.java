package moj.pakiet;

import org.junit.jupiter.api.Test;
import io.github.bonigarcia.wdm.WebDriverManager;
import io.restassured.RestAssured;
import io.restassured.response.Response;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.Test;

public class ApiSeleniumTest2 {


    @Test
    public void selenumTest(){
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com";

        Response response = RestAssured
        

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

            WebElement userName = driver.findElement(By.tagName("h1"));
            String displayedUserName = userName.getText();
            System.out.println("User name : " + displayedUserName);






        }



        


      


    }
    
}
