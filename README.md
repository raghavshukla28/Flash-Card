# UPSC Quiz Application
This UPSC Quiz Application is a flashcard-based quiz game developed using Python and the tkinter library. The app is designed to enhance learning for UPSC aspirants by presenting questions and allowing users to check their answers interactively. The application tracks user scores and updates the quiz data dynamically by removing known questions.

Features
Flashcard-Based Learning

Displays a question on a flashcard for a limited time.
Automatically flips to reveal the answer after a set interval.
Interactive Score Tracking

Users can mark answers as known or unknown.
Correct answers increase the score, while incorrect answers reduce it.
Dynamic Question Removal

Known questions are removed from the pool, ensuring continuous learning of unknown topics.
Progress is saved locally for future sessions.
Responsive Design

Handles long questions and answers using automatic text wrapping.
Supports both front and back card visuals.
Requirements
Python 3.x
Required Python Modules:
tkinter (standard library)
pandas (data manipulation)
random (for question selection)
textwrap (for text formatting)
How to Use
Setup Files

Place the following files in the specified directories:
Question file: data/french_words.csv (Ensure it has "Question" and "Answer" columns).
Images: Place card_front.png, card_back.png, wrong.png, and right.png in an images folder.
Install Dependencies
Install the pandas library if not already available:

bash
Copy code
pip install pandas
Run the Application
Start the app by running:

bash
Copy code
python quiz_app.py
Gameplay

The app displays a question.
After 4 seconds, the answer is revealed.
Users can click the ✓ button for a known answer or the ✗ button for an unknown one.
The score updates based on the user's choice.
Progress Save

Known questions are removed from the pool and saved to data/unknown_questions.csv.
Restarting the app resumes with only the remaining questions.
File Details
quiz_app.py: Main script for running the application.
data/french_words.csv: Initial question dataset (requires "Question" and "Answer" columns).
data/unknown_questions.csv: Updated question dataset after filtering known answers.
Images:
card_front.png: Front side of the flashcard.
card_back.png: Back side of the flashcard.
wrong.png: Image for the "Unknown" button.
right.png: Image for the "Known" button.
Customization
Question Pool
Replace data/french_words.csv with your own dataset. Ensure the file contains "Question" and "Answer" columns.

Card Display Time
Adjust the flip interval by modifying flip_timer duration in seconds:

python
Copy code
flip_timer = window.after(4000, func=flip_card)
Score Logic
Modify scoring increments or decrements in the known_answer() and unknown_answer() functions.

Notes
Ensure all required images and data files are in their respective directories before running the application.
If no unknown questions remain, the app automatically resets to the original dataset.
Contact
Feel free to suggest improvements or report any issues. Happy learning! 😊
