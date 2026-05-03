import requests
import json

BASE_URL = "http://127.0.0.1:8000"

# Test 1 - Register
print("Test 1: Register user")
data = {
    "username": "saasuser",
    "email": "saas@test.com",
    "password": "test123456"
}
response = requests.post(f"{BASE_URL}/api/register", json=data)
print(f"Status: {response.status_code}")
print(f"Response: {response.text}")

# Test 2 - Login
print("\nTest 2: Login user")
data = {
    "email": "saas@test.com",
    "password": "test123456"
}
response = requests.post(f"{BASE_URL}/api/login", json=data)
print(f"Status: {response.status_code}")
if response.status_code == 200:
    token = response.json().get("access_token")
    print(f"Token received: {token[:20]}...")

# Test 3 - Get Stats
print("\nTest 3: Get stats")
response = requests.get(f"{BASE_URL}/api/stats")
print(f"Status: {response.status_code}")
print(f"Response: {response.text}")

# Test 4 - Get docs
print("\nTest 4: Swagger docs")
response = requests.get(f"{BASE_URL}/docs")
print(f"Status: {response.status_code}")
print(f"Swagger: OK")

print("\n✅ All tests completed!")
