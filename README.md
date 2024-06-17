Nikto GUI with Ollama AI Integration
This project provides a graphical user interface (GUI) for running Nikto web server scans. The GUI is built using PyQt5 and includes integrated AI-powered chat functionality using the Ollama AI model. Additionally, it features user authentication and database management for storing scan results.

Features
User Authentication: Secure login system for users.
Database Management: Uses SQLite for storing user information and scan results.
Nikto Integration: Allows users to run Nikto scans on specified targets with custom options.
Progress and Output Display: Real-time progress updates and display of scan results.
Error Handling: Captures and displays errors during the scan process.
Ollama AI Chat: Integrated chat functionality using the Ollama AI model.
Requirements
Python 3.x
PyQt5
sqlite3
ollama
nikto_commands (Custom module for running Nikto commands)
Installation
Clone the repository:

sh
Copy code
git clone https://github.com/yourusername/nikto-gui.git
cd nikto-gui
Install the required Python packages:

sh
Copy code
pip install pyqt5 sqlite3 ollama
Ensure Nikto is installed on your system:
Download and install Nikto from here.

Set up the database:
The database will be automatically set up when you first run the application. It includes tables for users and scans.

Usage
Run the application:

sh
Copy code
python nikto_gui.py
Login:
Use the login dialog to authenticate. If you don't have an account, you will need to sign up first.

Run a Nikto Scan:

Enter the target URL and desired options.
Start the scan and monitor progress in real-time.
View the results once the scan is complete.
Chat with Ollama AI:

Use the integrated chat interface to interact with the Ollama AI model for assistance or information.
Project Structure
nikto_gui.py: Main application file.
ollama.py: Integration for Ollama AI model.
nikto_commands.py: Module for running Nikto commands.
users.db: SQLite database for storing user information and scan results.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License.
