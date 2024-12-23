## Prompt 5.12

“
From the point of view of a tester who will perform an exploratory testing session, give me test cases to the Download button functionality in the readme generator app. This app does not have a connection to any type of database and there are no user registration and login options. Consider potential edge cases, unusual flows and try to find possible bugs. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test result
”

## Images

readme1.png, readme2.png

## Answer

### Test Case 1
- **Description:** Verify the download functionality when a README file is generated with all default sections.
- **Prerequisites:** The user has accessed the README generator app.
- **Steps:**
  1. Click on “Get Started”.
  2. Leave all sections as default without modification.
  3. Click on the "Download" button.
- **Expected Results:** A README.md file should be downloaded containing all default sections.

---

### Test Case 2
- **Description:** Verify the download functionality after modifying some sections.
- **Prerequisites:** The user has accessed the README generator app.
- **Steps:**
  1. Click on “Get Started”.
  2. Modify the “Title and Description” section.
  3. Click on the "Download" button.
- **Expected Results:** A README.md file should be downloaded containing the modified “Title and Description” section.

---

### Test Case 3
- **Description:** Verify the download button functionality when no section is edited or added.
- **Prerequisites:** The user has accessed the README generator app.
- **Steps:**
  1. Click on “Get Started”.
  2. Click directly on the "Download" button without modifying any section.
- **Expected Results:** A README.md file should be downloaded containing the default sections without any modification.

---

### Test Case 4
- **Description:** Verify the download button functionality after removing a section.
- **Prerequisites:** The user has accessed the README generator app.
- **Steps:**
  1. Click on “Get Started”.
  2. Delete the “Acknowledgements” section by clicking the trash icon next to it.
  3. Click on the "Download" button.
- **Expected Results:** A README.md file should be downloaded without the “Acknowledgements” section.

---

### Test Case 5
- **Description:** Verify the download functionality in a different language interface.
- **Prerequisites:** The user has accessed the README generator app.
- **Steps:**
  1. Change the language from the dropdown menu to "Español".
  2. Click on “Get Started”.
  3. Click on the "Download" button.
- **Expected Results:** A README.md file should be downloaded, and its contents should remain the same regardless of the interface language.

---

### Test Case 6
- **Description:** Verify the download button functionality with an empty README file.
- **Prerequisites:** The user has accessed the README generator app.
- **Steps:**
  1. Click on “Get Started”.
  2. Remove all sections.
  3. Click on the "Download" button.
- **Expected Results:** A README.md file should be downloaded but should be empty or contain a minimal structure depending on the app's handling of empty files.

---

### Test Case 7
- **Description:** Verify the download button functionality after adding a custom section.
- **Prerequisites:** The user has accessed the README generator app.
- **Steps:**
  1. Click on “Get Started”.
  2. Add a custom section by clicking “Custom Section” and entering some text.
  3. Click on the "Download" button.
- **Expected Results:** A README.md file should be downloaded containing the newly added custom section.

---

### Test Case 8
- **Description:** Verify the download button remains active after multiple edits.
- **Prerequisites:** The user has accessed the README generator app.
- **Steps:**
  1. Click on “Get Started”.
  2. Edit “Project Title” multiple times.
  3. Add and remove various sections.
  4. Click on the "Download" button.
- **Expected Results:** A README.md file should be downloaded containing the final edits and sections.

---

### Test Case 9
- **Description:** Verify the download button functionality with a mix of default and edited sections.
- **Prerequisites:** The user has accessed the README generator app.
- **Steps:**
  1. Click on “Get Started”.
  2. Modify the “Title and Description” section.
  3. Keep “Acknowledgements” section as default.
  4. Add a new “Authors” section and input customized content.
  5. Click on the "Download" button.
- **Expected Results:** A README.md file should be downloaded containing both default and modified sections accurately.

---

### Test Case 10 (BUG - scrolls horizontally)
- **Description:** Verify the handling of large inputs in the sections and the download functionality.
- **Prerequisites:** The user has accessed the README generator app.
- **Steps:**
  1. Click on “Get Started”.
  2. Add extensive content in the “Title and Description” and “API Reference” sections.
  3. Click on the "Download" button.
- **Expected Results:** A README.md file should be downloaded correctly bearing all the extensive inputs without truncation or app crash.

---

These test cases explore various scenarios for the download functionality, covering both typical user flows and edge cases.


1 bugs
0 senseless
