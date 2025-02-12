package moj.pakiet;

import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.testng.annotations.Test;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.theInstance;

public class PrzykladTest {

    @Test
    public void test(){

       RestAssured.baseURI = "https://jsonplaceholder.typicode.com/";

        given()

        .when()
            .get("users")

        .then()
            .statusCode(200)
            .body("[0].id" , equalTo(1));

    }
    
}
