# Python-Project-05 (Student Management System)

<h3>Student Management System (SMS) </h3><br>
A robust, CLI-based Student Management System built with Python. This project manages student records using JSON for persistent data storage, implementing full CRUD (Create, Read, Update, Delete) functionality with data validation.

<h3>Features</h3>
1- Add Student: Register new students with unique IDs (prevents duplicates).<br>
2- View Records: Search for a specific student by ID or view the entire database.<br>
3- Update Data: Edit existing student information (Name, Email, etc.) dynamically.<br>
4- Delete Records: Remove student data with a safety confirmation prompt.<br>
5- Data Persistence: Automatically saves all changes to a std.json file.<br>
6- Error Handling: Prevents crashes from invalid inputs or corrupted data files.<br>

<h3>System Architecture</h3><br>
This project was designed following professional software engineering principles:<br>
1. Use Case Diagram<br>
The system allows an Administrator to interact with the core database through five main operations.
2. Entity Relationship Diagram (ERD)<br>
The data is structured around the Student entity with the following attributes:
<code>std_ID (Primary Key / Unique)
std_name, std_fname, std_age, std_Email, std_phone, std_section</code>
3. Data Flow (DFD)<br>
Data flows from the user input through validation logic in Python before being committed to the std.json storage file.

<h3>Tech Stack</h3><br>
<b>Language</b>: Python 3.x<br>
<b>Storage</b>: JSON (JavaScript Object Notation)<br>
<b>Modules</b>: os, json<br>

<h4>Installation & Usage</h4><br>
Clone the repository:
Bash
git clone https://github.com/yourusername/student-management-system.git
<br>
Navigate to the directory:
Bash
cd student-management-system
<br>
<h4>Run the application:</h4>
Bash
python main.py<br>
<h3>Code Structure</h3>
Plaintext
<code>── main.py          # Main application logic and loop
├── std.json         # Data storage file (generated automatically)
└── README.md        # Project documentation</code>├
