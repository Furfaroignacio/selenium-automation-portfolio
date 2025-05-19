import requests

def test_get_users_status_code():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    assert response.status_code == 200

def test_get_users_length():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 10

def test_get_user_invalid_status_code():
    url = "https://jsonplaceholder.typicode.com/users/999"
    response = requests.get(url)
    assert response.status_code == 404

def test_post_user_status_code():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.post(url, json={"title": "foo", "body": "bar", "userId": 1})
    assert response.status_code == 201


def test_delete_post_status_code():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.delete(url)
    assert response.status_code == 200