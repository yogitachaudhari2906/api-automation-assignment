import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
required_keys = {"userId", "id", "title", "body"}

res = requests.get(url, timeout=10)
assert res.status_code == 200, f"Expected 200 but got {res.status_code}"
print("Status code:", res.status_code)

posts = res.json()
print("Total posts:", len(posts))

# find posts which are missing any required key
bad_posts = [p.get("id") for p in posts if not required_keys.issubset(p)]
assert not bad_posts, f"Posts missing keys: {bad_posts}"
print("All posts have required keys")

with open("posts.json", "w") as f:
    json.dump(posts[:5], f, indent=4)

print("Saved first 5 posts to posts.json")
