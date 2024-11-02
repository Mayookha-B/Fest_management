# Fest_management
This script sets up a simple college fest management system using Python with a Tkinter GUI and SQLite as the database. However, there are a few important improvements and considerations to note:

Observations and Recommendations:
Database Connection Issue:

In the setup_database function, the database file name is 'college_fest.sql', but in the other functions (add_student, register_for_event), it is 'college_fest.db'. Ensure consistency in the file name to avoid creating separate databases.
