# System Architecture

The Student Management System follows a simple modular architecture.

## Main Components

1. User Interface
   - Menu-driven console interface
   - Takes input from the user
   - Displays results and messages

2. Student Management
   - Add student
   - View student
   - Search student
   - Update student
   - Delete student

3. Academic Management
   - Add marks
   - Calculate grade

4. Attendance Management
   - Add attendance percentage
   - Validate attendance input

5. Storage Module
   - `storage.py`
   - Saves student records to `students.json`
   - Loads saved records when the program starts

## Workflow

User → Main Menu → Select Operation → Process Student Data → Save/Load JSON Data → Display Result