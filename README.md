# VTGTextUtils.in

VTGTextUtils.in is a text analysis and manipulation web application built with Python (Django framework), HTML, and Bootstrap CSS. It provides a simple, user-friendly interface to perform various text processing tasks such as cleaning, formatting, and analyzing text.

## Features
- Remove Punctuations – Clean text by removing unnecessary punctuation marks.
- Make Capitalized – Convert text into capitalized format.
- New Line Remover – Strip out extra line breaks for cleaner text.
- Extra Space Remover – Eliminate redundant spaces between words.
- Count All Characters – Get the total character count of your text.

## Tech Stack
Frontend: HTML, Bootstrap CSS  
Backend: Python, Django Framework  
Deployment: Runs locally on 127.0.0.1:8000 (can be deployed to any server)

## Project Overview
The homepage provides a navigation bar with links to Home, WhatsApp, Instagram, LinkedIn, and GitHub. It includes a large text input area with placeholder text "Enter your text here to analyze it....", toggle switches for enabling/disabling text processing options, a Start Analyzing button to process the text, and a footer © 2025. Created and Designed by Er. Yash Varshney.

## Installation & Setup
Clone the repository:
```bash
git clone https://github.com/Yash-Varshney911/Text_Utilization_System.git
cd Text_Utilization_System
```
Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```
Install dependencies:
Run the Django development server:
```bash
python manage.py runserver
```
Open in browser:
```
http://127.0.0.1:8000/
```

## Project Structure
```
Text_Utilization_System/
│── textutils/        # Django app containing views, models, templates
│── static/           # CSS, JS, Bootstrap files
│── templates/        # HTML templates
│── manage.py         # Django project manager
```

## Contributing
Contributions are welcome! Fork the repository, create a new branch (feature-xyz), commit your changes, and submit a pull request.

## Author
Er. Yash Varshney  
Created and Designed in 2025
