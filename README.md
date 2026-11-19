# API Automation using Requests

Tests for the public API https://jsonplaceholder.typicode.com

## Task 1 - api_automation.py
- Fetches all posts
- Checks the status code is 200
- Checks every post has userId, id, title and body
- Saves the first 5 posts to posts.json

## Task 2 - test_api.py (Pytest)
- Response time is less than 2 seconds
- Schema validation using pydantic
- Parameterized test for /posts, /comments and /users

## Task 3 - Task3_Postman_Collection.json (Postman)
- GET /posts - status is 200, response is a non-empty array, every post has userId, id, title and body, response time under 2 seconds
- POST /posts - status is 201, response contains the same title and body that were sent, saves the new id
- DELETE /posts/{id} - deletes the created post, status is 200 or 204
- Base URL, title and body are stored as collection variables

## How to run
```
pip install -r requirements.txt
python api_automation.py
pytest -v
```

### Postman collection
- In Postman, click Import and select Task3_Postman_Collection.json
- Open the collection and click Run to execute all requests with their tests

Or run it from the command line with Newman:
```
npm install -g newman
newman run Task3_Postman_Collection.json
```
