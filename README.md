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

## How to run
```
pip install -r requirements.txt
python api_automation.py
pytest -v
```
