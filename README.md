<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

1.- Create integration with the Public API(https://jsonplaceholder.typicode.com/) and
Save the information in a DB Postgres:
This integration must have everything related to an integration, such as validation of
sent data, validation of obtained data and all the necessary layers for this API.
You must integrate all available methods:

* GET 	/posts
* GET 	/posts/1
* GET 	/posts/1/comments
* GET 	/comments?postId=1
* POST 	/posts
* PUT 	/posts/1
* PATCH 	/posts/1
* DELETE 	/posts/1

2.- With the fake data that was saved in the DB, an API must be made that can save more data (any other data that is not from the integration) and consult the information. The API must be developed in GraphQL. Recommended library: Graphene

### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [Strawberry Graphql](https://strawberry.rocks)
* [SQLAlchemy](https://www.sqlalchemy.org)
* [Alembic](https://alembic.sqlalchemy.org/en/latest/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* Clone repository
  ```sh
  git clone https://github.com/miltonvera96/crehanatest.git
  ```


### Installation


1. Build container
    ```sh
      sudo docker-compose up
    ```

2. Go to [https://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

You can test the results with these pre-built queries and mutations.

* Get all posts
    ```graphql
    query {
      posts {
        id
        title
        userId
        body
      }
    }
    ```

* Get post's comments
    ```graphql
    query {
      commentsByPost(postId:1) {
        id
        name
        email
        body
      }
    }
    ```

* Add new post
    ```graphql
    mutation {
      addPost(
        body: "Fox in Socks", title: "Dr. Seuss", userId:1) {
        success
        message
        code
        post{
		    id
            title
    	    userId
    	    body
        }
    }
}

For more queries go to: `queries_to_test.txt`

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- Automated Tests -->
## Tests
There is also a container in which the test are executed, but if you want to test it by yourself
follow the next steps.


* Create virtual environment on the root directory
  ```sh
  python3 -m venv ./venv
  ```
* Activate enviroment
  ```sh
  source venv/bin/activate
  ```
  
* Install requirements
  ```sh
  pip install -r requirements.txt 
  ```

* Init tests
  ```sh
  python -m pytest ./tests/
  ```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Milton Vera - [LinkedIn](https://www.linkedin.com/in/milton-vera/) - miltonvera96@gmail.com

Project Link: [https://github.com/miltonvera96/crehanatest](https://github.com/miltonvera96/crehanatest)

<p align="right">(<a href="#top">back to top</a>)</p>
