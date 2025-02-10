package moj.pakiet;

import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.testng.annotations.Test;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.theInstance;

public class RestAssuredTest {

    @Test
    public void test3(){
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com/";

        given()
        .when()
            .get("posts/1/comments")
        .then()
            .statusCode(200)
            //.body("postId" , equalTo(1))
            //.body("name" , equalTo("id labore ex et quam laborum"));
            .body("[0].name", equalTo("id labore ex et quam laborum")); 
    }       

    @Test
    public void test4(){
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com/";

        given()
        .when()
            .get("posts")
        .then() 
            .statusCode(200)
            .body("[0].id" , equalTo(1));
    }

    @Test
    public void test5(){
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com/";

        given()
        .when()
            .get("comments?postId=2")
        .then()
            .statusCode(200)
            .body("[0].email" , equalTo("Presley.Mueller@myrl.com"));
            
    }

    @Test
    public void test6(){
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com/";

        given()
        .when()
            .get("comments?postId=10")
        .then()
            .statusCode(200)
            .body("[4].id" , equalTo(50))
            .body("[4].email" , equalTo("Kiana_Predovic@yasmin.io"));
    }


    @Test
    public void test7(){
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com/";

        String requestBody = "{ \"title\": \"heeeeeej\", \"body\": \"cialooo\", \"userId\": 222}";


        given()
            .contentType(ContentType.JSON)
            .contentType(requestBody)
        .when()
            .post("posts")
        .then()
            .statusCode(201)
            .extract().response();
    }


    @Test
    public void testGetUser() {
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com";

        given()
            .when()
                .get("/users/1")
            .then()
                .statusCode(200)
                .body("id", equalTo(1))
                .body("name", equalTo("Leanne Graham"));
    }

    @Test
    public void testCreatePost() {
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com";

        String requestBody = "{ \"title\": \"foo\", \"body\": \"bar\", \"userId\": 1 }";

        Response response =
            given()
                .header("Content-Type", "application/json")
                .body(requestBody)
            .when()
                .post("/posts")
            .then()
                .statusCode(201)
                .extract().response();

        System.out.println("Response: " + response.asString());
    }
}
