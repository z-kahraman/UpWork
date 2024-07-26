# Protected URL Data Fetcher

This project includes scripts to fetch data from a protected URL that can only be accessed through a browser session. The solution uses Selenium for browser automation and `requests` for data retrieval. This README provides an overview of the project, how to set up and run the scripts, and their purposes.

## Project Overview

The goal of this project is to automate the process of fetching data from a URL that requires authentication or session management, which cannot be accessed directly via HTTP requests. The solution involves two main Python scripts:

1. **`get_cookies.py`**: Uses Selenium to automate a browser session to log in and retrieve cookies.
2. **`fetch_protected_url.py`**: Uses the retrieved cookies to access the protected URL and download the data.

## Prerequisites

- Python 3.x
- Selenium
- Requests
- WebDriver Manager (for managing browser drivers)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/username/repository.git
   cd repository
   ```

2. **Install Dependencies**

   Ensure you have the required Python packages installed. You can install them using pip:

   ```bash
   pip install selenium requests webdriver_manager
   ```

## Usage

### 1. Retrieve Cookies

The `get_cookies.py` script is used to obtain cookies from the browser session. This is useful for accessing protected URLs that require authentication.

Usage:

1. Edit `get_cookies.py` to replace "PROTECTED_URL" with the actual URL you want to access.
2. If login is required, uncomment and update the lines for login credentials.
3. Run the script:

   ```bash
   python get_cookies.py
   ```

   This will print the cookies to the console.

### 2. Fetch Data from Protected URL

The `fetch_protected_url.py` script uses the cookies obtained from `get_cookies.py` to fetch data from the protected URL.

Usage:

1. Edit `fetch_protected_url.py` to replace "PROTECTED_URL" with the actual URL you want to access.
2. Ensure the `cookies_dict` is correctly populated with the cookies obtained from `get_cookies.py`.
3. Run the script:

   ```bash
   python fetch_protected_url.py
   ```

   This will download the file from the protected URL and save it as `downloaded_file`.

## Script Details

### get_cookies.py

This script performs the following steps:

1. Starts a browser session using Selenium.
2. Navigates to the protected URL.
3. Performs necessary actions such as logging in (if required).
4. Waits for the page to load.
5. Retrieves cookies from the browser session.
6. Saves cookies in a dictionary format.

### fetch_protected_url.py

This script performs the following steps:

1. Loads the cookies obtained from `get_cookies.py`.
2. Uses the `requests` library to send a GET request to the protected URL with the necessary headers and cookies.
3. Checks the response status code.
4. Saves the response content to a file if the request is successful.

## Contributing

Feel free to fork the repository and submit pull requests. If you have any issues or suggestions, please open an issue on the GitHub repository page.

## License

This project is licensed under the MIT License - see the LICENSE file for details.