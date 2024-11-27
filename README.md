# Fitpeo-automation-testing

This project automates interactions with the Fitpeo website's revenue calculator using Python and Selenium. The script navigates to the revenue calculator page, interacts with UI components (sliders, text fields, and checkboxes), and validates output values.

Features:
  Automates navigation to the Fitpeo revenue calculator page.
  Simulates user interactions with sliders and text inputs.
  Selects CPT codes using checkboxes.
  Validates the "Total Recurring Reimbursement" value against an expected output.
  Logs progress and errors for debugging.
  
  
  Script Workflow
      1.	Opens the Fitpeo homepage and navigates to the revenue calculator.
      2.	Adjusts sliders and updates input fields with custom values.
      3.	Selects predefined CPT codes.
      4.	Validates the header text for "Total Recurring Reimbursement."
      5.	Prints the validation result to the console.

Objective:
The purpose of this assignment is to demonstrate the ability to automate web interactions using Selenium. The script automates the navigation and interaction with the Fitpeo website's revenue calculator, verifies the output, and validates the functionality.
1.Script Description:
        •	Initializes a Chrome browser session using selenium.webdriver.
        •	Opens the Fitpeo homepage and maximizes the browser window for better visibility.
2. Navigation:
        •	Navigates to the "Revenue Calculator" page by locating and clicking the corresponding element.
3.Interaction with UI Components:
        •	Scrolls to specific sections of the page.
        •	Adjusts a slider on the revenue calculator.
        •	Updates a text field and performs validation by entering predefined values.
        •	Selects checkboxes for CPT codes by simulating user clicks.
4.Validation:
        •	Verifies that the revenue calculator page is loaded correctly by checking the URL.
        •	Validates the "Total Recurring Reimbursement" header text against an expected value ($110160).
5. Exception Handling:
        •	Catches and logs any errors during execution to ensure the script fails gracefully and provides feedback.
6.Finalization:
        •	Ensures the browser is closed using the finally block, regardless of whether the script runs successfully or encounters an error.


Challenges and Solutions
1.Dynamic Elements:
    •	Some elements might load dynamically; the script uses WebDriverWait to handle such cases.
2.Scroll and Click:
    •	Elements not visible within the viewport are scrolled into view using JavaScript to ensure interactions are smooth.

3.Error Handling:
    •	A try-except block is implemented to catch and print errors, along with detailed stack traces for debugging


Conclusion
This automation script is a demonstration of using Selenium to perform browser-based testing and interaction. It ensures the Fitpeo revenue calculator's critical functionalities are validated, meeting the requirements of the assignment.
