import pytest 
import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

creat_post = {
    "title": "Новый пост",
    "body": "Создан новый пост",
    "userId": 1
}

change_post = {
    "title": "Обновленный пост",
    "body": "Обновили пост",
    "userId": 1
}

def test_creat_post():
    response = requests.post(url, json=creat_post) # создаем post-запрос
    assert response.status_code == 201
    assert response.json()["title"] == creat_post["title"]
    assert response.json()["body"] == creat_post["body"]
    assert response.json()["userId"] == creat_post["userId"]


def test_update_post():
    response = requests.post(url, json=creat_post) # создаем post-запрос
    post_id = response.json()["id"] # получаем id созданного поста
    response = requests.put(f"{url}/{post_id}", json=change_post)
    assert response.status_code == 200
    assert response.json()["title"] == change_post["title"]
    assert response.json()["body"] == change_post["body"]
    assert response.json()["userId"] == change_post["userId"]

def test_delete_post():
    response = requests.post(url, json=creat_post) # создаем post-запрос
    post_id = response.json()["id"] # получаем id созданного поста
    
    # Удаляем пост
    response = requests.delete(f"{url}/{post_id}")
    assert response.status_code == 200
    assert response.text == ""