## Black Diamond Utilities Project


 **Inspiration**
The Black Diamond Utilities Project was inspired by a vision to create user-friendly, powerful, and accessible security tools for professionals and enthusiasts alike. The goal is to simplify the complexities of advanced cybersecurity tools, making them more approachable for users of all skill levels. This initiative aims to bridge the gap between functionality and usability, ensuring that even the most advanced tools can be effectively utilized without a steep learning curve.

The inspiration for this project came from the need to provide robust security solutions that are not only effective but also easy to use. By integrating modern GUI elements and AI-driven assistance, we aim to enhance the user experience and streamline the workflow of security analysts, penetration testers, and IT professionals.

**Upcoming Projects**
As part of the Black Diamond Utilities Project, we are excited to announce several upcoming tools that will feature graphical user interfaces built for various Kali Linux tools:

Nmap GUI:
A graphical user interface for the Nmap tool, making network scanning and discovery more intuitive. Users will be able to easily configure scan options, view detailed scan results, and generate reports.

Metasploit GUI:
An interface for the Metasploit framework, simplifying the process of exploiting vulnerabilities and managing payloads. This tool will include features for easy target selection, module management, and session handling.


Aircrack-ng GUI:
An easy-to-use interface for the Aircrack-ng suite, designed for wireless network security testing. This tool will guide users through capturing and analyzing wireless traffic, cracking WEP/WPA keys, and monitoring network activity.

Hydra GUI:
A graphical interface for Hydra, the popular password cracking tool. Users will benefit from a more accessible way to configure and execute brute-force attacks, with real-time progress updates and result logging.

Wireshark GUI Enhancements:
Improved GUI elements for Wireshark, enhancing its usability for packet analysis and network troubleshooting. This will include customizable dashboards
and simplified navigation for analyzing captured packets.


**Conclusion**

The Black Diamond Utilities Project aims to revolutionize the way users interact with advanced cybersecurity tools by providing intuitive graphical user interfaces and integrating AI-driven support. These upcoming projects will empower users to perform complex security tasks with ease, ensuring that powerful tools are accessible to everyone, regardless of their technical expertise. Stay tuned for these exciting developments, and join us in making the cybersecurity landscape more user-friendly and effective.



## Nikto GUI with Ollama AI Integration
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
