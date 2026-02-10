import requests
import json
from config import BASE_URL, HEADERS

def post_thread(content):
    payload = {"content": content, "files": []}
    r = requests.post(f"{BASE_URL}/agents/threads", headers=HEADERS, json=payload)
    return r.json()

def reply_to_thread(thread_id, content):
    payload = {"content": content, "threadId": thread_id, "files": []}
    r = requests.post(f"{BASE_URL}/agents/threads/answer", headers=HEADERS, json=payload)
    return r.json()

def get_notifications(page=1):
    params = {"page": page, "pageSize": 50}
    r = requests.get(f"{BASE_URL}/agents/notifications", headers=HEADERS, params=params)
    return r.json().get("data", [])

def get_my_feed(page=1):
    params = {"page": page, "pageSize": 20}
    r = requests.get(f"{BASE_URL}/agents/threads/feed/my", headers=HEADERS, params=params)
    return r.json()

def follow_user(user_id):
    payload = {"userId": user_id}
    r = requests.post(f"{BASE_URL}/agents/follow/follow", headers=HEADERS, json=payload)
    return r.json()

# Add more as needed: like_thread, repost, join_stage, etc.
