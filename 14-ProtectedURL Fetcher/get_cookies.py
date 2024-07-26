import requests

url = "PROTECTED_URL"

# Add headers and cookies
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Perform the GET request to the protected URL with headers and cookies
response = requests.get(url, headers=headers, cookies=cookies_dict)

# Check the response content
if response.status_code == 200:
    # If the response is successful (status code 200), write the content to a file
    with open("downloaded_file", "wb") as file:
        file.write(response.content)
else:
    # If the response is not successful, print an error message with the status code
    print("Failed to download the file:", response.status_code)
