# API Automation using Requests

Script to test the public API https://jsonplaceholder.typicode.com/posts

## What it does
- Fetches all posts
- Checks the status code is 200
- Checks every post has userId, id, title and body
- Saves the first 5 posts to posts.json

## How to run
```
pip install -r requirements.txt
python api_automation.py
```
