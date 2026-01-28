🎬 FilmFusion – Dynamic Scheduling and Booking Platform

FilmFusion is a Python-based multiplex scheduling and ticket booking application built using Tkinter. The platform provides an intuitive interface for theatre administrators to manage movies and revenue, while allowing users to browse movies, book seats, and track booking history.
The system supports dynamic seat pricing based on movie ratings, offering a realistic simulation of real-world theatre operations.

✨ Features
👨‍💼 Admin Module
    Add and manage movies
    Schedule movie shows
    View revenue collection and booking data

🎟️ User Module
    Browse available movies
    Book seats across different seat categories
    View booking history
    Account-based login system

💺 Seat Management
    Multiple seat categories
    Dynamic pricing based on movie ratings

🛠️ Tech Stack
    Python 3
    Tkinter (GUI)
    Pillow (PIL) for image handling
    CSV for persistent data storage

📋 Prerequisites
Ensure the following are installed before running the application:
    Python 3.x
    Tkinter (usually included with Python)
    Pillow module

⚙️ Installation

Clone the repository
git clone https://github.com/HariniLV-3103/filmfusion.git
cd filmfusion

Install required dependencies
pip install pillow

⚠️ Tkinter generally comes pre-installed with Python. If not, install it via your system package manager.

▶️ Usage
Run the application using:
    python main.py

📁 File Structure
main.py — Core application logic
movies.csv — Stores movie details
past_bookings.csv — Stores booking history
users.csv — Stores user account credentials

📌 All CSV files must be in the same directory as main.py.

🔐 Login Credentials
Admin
    Username: admin
    Password: admin

User
    Credentials are created during account registration
    Stored securely in users.csv

📝 Notes
Seat categories and pricing logic can be modified in the SeatBooking class.
Ensure all CSV files exist and are properly formatted before running the application.

🚀 Future Enhancements
    Database integration (MySQL / MongoDB)
    Online payment simulation
    Enhanced UI styling
    Analytics dashboard for admins
