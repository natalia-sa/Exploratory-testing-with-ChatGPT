## Prompt 5.10

“
From the point of view of a tester who will perform an exploratory testing session, give me test cases to the Toggle between Preview and Raw view in the readme generator app. This app does not have a connection to any type of database and there are no user registration and login options. Consider potential edge cases, unusual flows and try to find possible bugs. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test results
”

## Images

readme1.png, readme2.png, readme3.png

## Answer

### Test Case 1
- **Description:** Toggle between Preview and Raw view with default content.
- **Prerequisites:** App is opened at the /editor URL, default content present.
- **Steps:**
  1. Open the app to the Editor screen with default content.
  2. Click on the "Raw" tab on the right panel.
  3. Observe the display changes.
  4. Click on the "Preview" tab.
  5. Observe the display changes.
- **Expected Results:**
  - The "Raw" tab should display the content in raw format.
  - The "Preview" tab should return to the formatted view.

---

### Test Case 2 - SENSELESS
- **Description:** Toggle between Preview and Raw view immediately after making changes.
- **Prerequisites:** App is opened at the /editor URL, section is editable, and content can be modified.
- **Steps:**
  1. Open the app to the Editor screen.
  2. Modify the content in the editor (e.g., change the project title).
  3. Without saving, click on the "Raw" tab.
  4. Observe the display changes.
  5. Click on the "Preview" tab.
  6. Observe the display changes.
- **Expected Results:**
  - The "Raw" tab should immediately display the modified content in raw format.
  - The "Preview" tab should reflect the changes made in a formatted view.

---

### Test Case 3
- **Description:** Toggle between Preview and Raw view with an empty content section.
- **Prerequisites:** App is opened at the /editor URL, section is editable, and content can be removed.
- **Steps:**
  1. Open the app to the Editor screen.
  2. Delete all content in the editor.
  3. Click on the "Raw" tab.
  4. Observe the display changes.
  5. Click on the "Preview" tab.
  6. Observe the display changes.
- **Expected Results:**
  - The "Raw" tab should display an empty or minimal structure.
  - The "Preview" tab should reflect an empty or minimal view.

---

### Test Case 4
- **Description:** Toggle between Preview and Raw view after adding multiple sections.
- **Prerequisites:** App is opened at the /editor URL, multiple sections can be added, and content is editable.
- **Steps:**
  1. Open the app to the Editor screen.
  2. Add multiple sections (e.g., Acknowledgements, API Reference).
  3. Fill in content in the added sections.
  4. Click on the "Raw" tab.
  5. Observe the display changes.
  6. Click on the "Preview" tab.
  7. Observe the display changes.
- **Expected Results:**
  - The "Raw" tab should display all added sections and their content in raw format.
  - The "Preview" tab should display all added sections and their content in a formatted view.

---

### Test Case 5
- **Description:** Interacting with other UI elements while toggling views.
- **Prerequisites:** App is opened at the /editor URL, section is editable, and there are other interactive UI elements (e.g., language switcher, reset button).
- **Steps:**
  1. Open the app to the Editor screen.
  2. Modify the content in the editor.
  3. Click on the "Raw" tab.
  4. Change the language from the language switcher.
  5. Click on the "Preview" tab.
  6. Reset the section and observe the display changes.
- **Expected Results:**
  - The "Raw" tab should properly display content changes despite language switch.
  - The "Preview" tab should correctly display the formatted view.
  - Resetting should clear the content and both Preview and Raw views should reflect this.

---

### Test Case 6
- **Description:** Using dark mode while toggling between Preview and Raw view.
- **Prerequisites:** App is opened at the /editor URL, allows the toggle of dark mode.
- **Steps:**
  1. Open the app to the Editor screen.
  2. Enable dark mode from the toggle on the top right.
  3. Modify the content in the editor.
  4. Click on the "Raw" tab.
  5. Observe the display changes.
  6. Click on the "Preview" tab.
  7. Observe the display changes.
- **Expected Results:**
  - Dark mode should apply consistently across both Preview and Raw views.
  - Content and UI elements should remain legible and properly formatted in dark mode.

---

Feel free to refine these test cases based on the application's specific behavior and requirements observed during the testing session.

0 bugs
1 senseless

