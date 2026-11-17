import pytest
import requests
from pydantic import BaseModel

url = "https://jsonplaceholder.typicode.com"


class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str


class Comment(BaseModel):
    postId: int
    id: int
    name: str
    email: str
    body: str


class User(BaseModel):
    id: int
    name: str
    username: str
    email: str


def test_response_time():
    res = requests.get(url + "/posts")
    assert res.status_code == 200
    assert res.elapsed.total_seconds() < 2


def test_post_schema():
    res = requests.get(url + "/posts")
    for p in res.json():
        Post(**p)


@pytest.mark.parametrize("endpoint, model", [
    ("/posts", Post),
    ("/comments", Comment),
    ("/users", User)
])
def test_endpoints(endpoint, model):
    res = requests.get(url + endpoint)
    assert res.status_code == 200
    assert res.elapsed.total_seconds() < 2

    data = res.json()
    assert len(data) > 0
    for item in data:
        model(**item)
