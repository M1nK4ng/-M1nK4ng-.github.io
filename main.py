from fastapi import FastAPI
import requests
import json

app = FastAPI()

@app.get("/get-data")
def get_data():
    # Gọi API
    url = "https://fakerapi.it/api/v1/users?_quantity=10"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": f"Lỗi khi gọi API: {response.status_code}"}

    users = response.json().get('data', [])

    # Chỉ lấy name, username, password
    result = []
    for user in users:
        result.append({
            "name": user.get("firstname", "") + " " + user.get("lastname", ""),
            "username": user.get("username", ""),
            "password": user.get("password", "")
        })

    # Lưu vào file JSON
    with open('data.json', 'w') as f:
        json.dump(result, f, indent=4)

    return {"message": "Dữ liệu đã được lưu vào data.json", "data": result}
