import requests

user_message = "Can you tell me the conversion factor of INR to USD?"

request_message = {"message": user_message}

url= "http://localhost:5678/webhook/b4234a44-0377-464e-9360-c57f60211a2f"

response = requests.post(url, json= request_message)

print(response.json(),[0],["Output"])