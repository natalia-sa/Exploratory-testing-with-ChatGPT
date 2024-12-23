# Secondary prompt 9

"
From the point of view of a tester, give me exploratory test cases to the Reset Button feature to clear all sections  in the readme generator app, suggesting unusual flows, trying to find possible bugs, failures, security issues, etc. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test results
"

## Images

readme1.png, readme2.png

### Answer

Here are some exploratory test cases for the Reset Button feature in the README generator app:

### Test Case 1
- **Description:** Verify that pressing the Reset button clears all sections.
- **Prerequisites:** Multiple sections must be added and populated with text.
- **Steps:**
  1. Open the README generator app.
  2. Add several sections (e.g., Title and Description, Acknowledgements, API Reference).
  3. Populate the sections with dummy text.
  4. Click on the "Reset" button.
- **Expected results:** All text and sections should be cleared, leaving a blank state.

### Test Case 2
- **Description:** Verify that the Reset button works when no sections are added.
- **Prerequisites:** Ensure no sections are added.
- **Steps:**
  1. Open the README generator app.
  2. Ensure that no sections have been added.
  3. Click on the "Reset" button.
- **Expected results:** No change in the state of the app since there are no sections to clear.

### Test Case 3
- **Description:** Verify reset functionality after switching languages.
- **Prerequisites:** Add multiple sections and populate them with dummy text.
- **Steps:**
  1. Open the README generator app.
  2. Add and populate multiple sections.
  3. Change the language from the language selection dropdown.
  4. Click on the "Reset" button.
- **Expected results:** All sections should be cleared regardless of the language selected.

### Test Case 4
- **Description:** Verify that pressing Reset button multiple times in quick succession does not cause application crash or unwanted behavior.
- **Prerequisites:** Add multiple sections and populate with text.
- **Steps:**
  1. Open the README generator app.
  2. Add and populate multiple sections.
  3. Click the "Reset" button rapidly multiple times.
- **Expected results:** The application should handle the multiple clicks gracefully, clearing data once and remaining stable.

### Test Case 5
- **Description:** Verify that data is correctly cleared when the Reset button is pressed with a custom section added.
- **Prerequisites:** Add a custom section and populate it with text.
- **Steps:**
  1. Open the README generator app.
  2. Add a custom section and populate it with text.
  3. Click on the "Reset" button.
- **Expected results:** The custom section and its content should be cleared along with other sections.

### Test Case 6
- **Description:** Verify that the Reset action is persisted across sessions.
- **Prerequisites:** Add sections, populate them with text, and reset.
- **Steps:**
  1. Open the README generator app and add/populate sections.
  2. Click on the "Reset" button.
  3. Close and reopen the app.
- **Expected results:** The sections should remain cleared when the app is reopened since the data was reset previously.

### Test Case 7
- **Description:** Verify that the Reset button works correctly while sections are being modified (e.g., while typing).
- **Prerequisites:** Add a section and start typing.
- **Steps:**
  1. Open the README generator app.
  2. Add a section and start typing in the editor.
  3. While still typing, click on the "Reset" button.
- **Expected results:** All sections should be cleared immediately, halting any current input action without causing errors.

### Test Case 8
- **Description:** Verify edge case of large text data being reset.
- **Prerequisites:** Add a section and populate with a large amount of text (e.g., several pages of text).
- **Steps:**
  1. Open the README generator app.
  2. Add a section and paste a large amount of text.
  3. Click on the "Reset" button.
- **Expected results:** The large text data in the section should be cleared completely without performance issues or crashes.

### Test Case 9
- **Description:** Verify reset functionality after switching themes.
- **Prerequisites:** Add multiple sections and populate them with dummy text.
- **Steps:**
  1. Open the README generator app.
  2. Add and populate multiple sections.
  3. Switch to dark mode using the theme toggle.
  4. Click on the "Reset" button.
- **Expected results:** All sections should be cleared regardless of the theme, and the theme should remain in the dark mode.

### Test Case 10 -  SENSELESS
- **Description:** Verify that the Reset button clears unsaved changes.
- **Prerequisites:** Add sections and make unsaved changes.
- **Steps:**
  1. Open the README generator app.
  2. Add and populate sections with text but do not save the changes.
  3. Click on the "Reset" button.
- **Expected results:** All unsaved changes should be cleared immediately, reverting the app to a blank state.

These test cases cover a broad range of usual and unusual scenarios for the Reset button functionality in the README generator app.


0 bugs
1 senseless