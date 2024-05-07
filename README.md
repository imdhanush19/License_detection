

# Automatic License Plate Recognition System

This Python script utilizes OpenCV and Tesseract OCR to perform Automatic License Plate Recognition (ALPR) from images. It extracts license plate information from images and stores it in a MySQL database for further processing.

## Features

- Detects license plates from images using Haar cascades.
- Extracts alphanumeric characters from the detected license plate using Tesseract OCR.
- Stores the extracted license plate information in a MySQL database.
- Provides a simple and efficient method for ALPR.

## Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/your_username/alpr-system.git
```

2. Install the required dependencies:

```
pip install opencv-python pytesseract mysql-connector-python
```

3. Download and install Tesseract OCR from the official website: [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

4. Specify the correct paths for Tesseract OCR and the Haar cascade file in the script.

## Usage

1. Run the script by executing the following command:

```
python alpr.py
```

2. Provide the path to the image containing the license plate when prompted.

3. The script will detect the license plate, extract the alphanumeric characters, and store the information in the MySQL database.

## Database Setup

1. Create a MySQL database and table using the following schema:

```
CREATE DATABASE alpr_db;

USE alpr_db;

CREATE TABLE vehicle (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_no VARCHAR(20) NOT NULL,
    owner_name VARCHAR(100) NOT NULL,
    vehicle_type VARCHAR(50) NOT NULL
);
```

2. Update the database connection details in the script (host, username, password, database name) to match your MySQL setup.



---

