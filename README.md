Project Report: User Management and Preference Selection System

1. Executive Summary

This program is a Python-based automation script designed to register user names and log their preferences continuously. The primary function of this script is to maintain a persistent log of visitors in a text file (user.txt) while interacting with them through a basic choice menu. It runs indefinitely until a user provides an input outside of the specified choices.

2. Code Architecture & Breakdown

• Infinite Loop (while True): Ensures the script continuously runs and serves consecutive users without crashing or needing a manual restart.
• Persistent Data Storage (with open(...)): Appends each entered user name to an external file named user.txt. It utilizes the 'a' (append) mode to preserve previous records and introduces a newline character (\n) for clean formatting.
• Conditional Logic (if-elif-else): Evaluates the user's choice to dynamically determine the output:
	• Selecting coffee displays a price of 12$.
	• Selecting smoke displays a price of 5$.
	• Any other input triggers the exit sequence.
• Program Termination (exit()): Safely breaks the loop and shuts down the script when an invalid or exit-intent option is entered.

3. Technical Review & Performance


Feature	Assessment	Status
Data Persistence	Automatically creates user.txt if it does not exist.	✅ Optimal
Resource Management	The with statement guarantees proper file closing after writing.	✅ Safe
Input Validation	Strict matching case (coffee vs Coffee will trigger exit).	⚠️ Vulnerable


4. Recommendations for Enhancement

To elevate this project to a production-ready standard, the following improvements are highly recommended:
• Case Insensitivity: Apply the .lower() method to the inputs (y.lower()) so variations like "Coffee" or "Smoke" do not accidentally terminate the application.
• Typo Corrections: Fix the terminal output string from 'welcom' to 'Welcome'.
• Graceful Exit: Replace exit() with the standard loop control break statement to prevent abrupt runtime crashes in certain IDE environments.
