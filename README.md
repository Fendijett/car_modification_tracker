# Car Modification Tracker

## Purpose

The Car Modification Tracker is a web application designed for car enthusiasts to manage and keep track of their personal vehicle details and modifications. Users can input their vehicle information, list current modifications, plan future modifications, and mark modifications as purchased or installed.

## Features

- User authentication: Register and log in to manage personal vehicle details and modifications.
- Add, edit, and delete vehicle information.
- Track modifications for each vehicle with status updates (Planned, Purchased, Installed).
- CSRF protection for secure form submissions.

## Technologies Used

- **Language**: Python
- **Framework**: Flask
- **Database**: SQLite (SQLAlchemy for ORM)
- **User Authentication**: Flask-Login
- **Form Handling and Validation**: Flask-WTF
- **Password Hashing**: Flask-Bcrypt

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/car_modification_tracker.git
   cd car_modification_tracker

2. **Create a virtual enviroment:**
   python -m venv venv

2. **Activate the virtual enviroment:**
   On Windows:
venv\Scripts\activate
   On macOS/Linux:
source venv/bin/activate

2. **Install the required dependencies:**
    pip install -r requirements.txt

2. **Set up the database:**
    flask shell
    from app import db
    db.create_all()
    exit()

2. **Run the application:**
    flask run


## Project Structure

car_modification_tracker/
│
├── app.py                  # Main application file
├── models.py               # Database models
├── forms.py                # Forms for handling user input
├── users.py                # User-related routes and authentication
├── templates/
│   ├── base.html           # Base template
│   ├── index.html          # Home page
│   ├── register.html       # Registration page
│   ├── login.html          # Login page
│   ├── add_vehicle.html    # Add vehicle page
│   ├── vehicle.html        # Vehicle details page
│   └── edit_vehicle.html   # Edit vehicle page
├── static/
│   └── styles.css          # CSS file for styling
└── requirements.txt        # List of dependencies

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or suggestions.