import requests

# The API endpoint
url = "http://localhost:8000/upload"

# Open the file in binary mode and send it with the POST request
file_path = 'D:\Workspace\GMIIOT-Backend\gmiiot_email_setup.csv'
with open(file_path, 'rb') as f:
    files = {'gmiiot_email_setup': f}
    response = requests.post(url, files=files)

# A GET request to the API
response = requests.post(url)

# Print the response
print(response.text)


