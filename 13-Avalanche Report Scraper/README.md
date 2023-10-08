# Avalanche Report Scraper

This Python script is used to scrape various safety information from the Avalanche Report website.

## Getting Started

These instructions will guide you on setting up an environment to run and develop the project on your local machine.

### Prerequisites

To run this project, you'll need the following:

- Python 3.x
- MySQL database
- Internet connection

### Installation

Follow these steps to get a local copy of the project:

1. Clone this repository:
```sh
   git clone https://github.com/yourusername/avalanche-report-scraper.git
```

2. Navigate to the project directory:
```sh
cd avalanche-report-scraper
```

3. Create a virtual environment and install the required Python dependencies:

sh

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt

3. Create your MySQL database and update the connection details in the config.py file.

sql

CREATE DATABASE Avalanche;

4. Database structure:

The table structure in the MySQL database for this project is as follows:

    DangerRatings table:
        id (int, auto-incremented, primary key)
        valid_time (datetime)
        main_value (int)
        loc_ref (varchar)
        valid_elevation (int)

5. Run the script:

sh

    python scrape.py

Usage

When you run the project script, data will be scraped from the Avalanche Report website and stored in the MySQL database.
Contributing

    If you want to contribute to this project, open an issue before submitting a pull request.
    If you find any bugs or issues, please report them by opening an issue.

License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/z-kahraman/upwork/blob/main/13-Avalanche%20Report%20Scraper/LICENSE.md) file for details.
