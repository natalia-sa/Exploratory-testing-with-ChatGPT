## Prompt 6.7

“
From the point of view of a tester who will perform an exploratory testing session, give me test cases to the Reset button functionality in the readme generator app. Please consider that to carry out these tests you only have access to the Linux operating system, and the Firefox and Chrome browsers. This app does not have a connection to any type of database and there are no user registration and login options. Consider potential edge cases, unusual flows and try to find possible bugs. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test result
”

## Images

readme1.png, readme2.png

## Answer

### Test Case 001
- **Description:** Verify that clicking the Reset button clears all sections and content.
- **Prerequisites:** The user is on the Readme editor page with at least one section added and some content entered.
- **Steps:**
  1. Add a few sections and enter some content in each one.
  2. Click on the `Reset` button.
- **Expected Results:** All sections and content should be cleared, returning the editor to its initial empty state.

---

### Test Case 002
- **Description:** Verify that the Reset button resets the content of the default sections.
- **Prerequisites:** The user is on the Readme editor page with default sections pre-populated with content.
- **Steps:**
  1. Edit the content of the default sections such as "Project Title" and "Description."
  2. Click on the `Reset` button.
- **Expected Results:** The content of the default sections should be cleared.

---

### Test Case 003
- **Description:** Verify the Reset button functionality in different browsers (Mozilla Firefox and Google Chrome).
- **Prerequisites:** The user has access to both Firefox and Chrome browsers on a Linux operating system.
- **Steps:**
  1. Open the Readme editor page in Firefox.
  2. Add sections and content.
  3. Click the `Reset` button.
  4. Repeat steps 1-3 in Chrome.
- **Expected Results:** The Reset button should work correctly in both browsers, clearing all sections and content.

---

### Test Case 004
- **Description:** Verify that the Reset button removes all custom sections added by the user.
- **Prerequisites:** The user is on the Readme generator app page with custom sections added.
- **Steps:**
  1. Add some custom sections.
  2. Enter content in those custom sections.
  3. Click the `Reset` button.
- **Expected Results:** Custom sections and their contents should be removed, and the editor should revert to its default state.

---

### Test Case 005 - senseless
- **Description:** Verify Reset functionality with unsaved changes in the editor.
- **Prerequisites:** The user has unsaved changes in the Readme editor.
- **Steps:**
  1. Make edits to existing sections and add new content without saving/exporting it.
  2. Click the `Reset` button.
- **Expected Results:** All unsaved changes should be discarded, and the editor should be cleared.

---

### Test Case 006 - senseless
- **Description:** Verify Reset button functionality after switching between sections without saving.
- **Prerequisites:** The user is on the Readme editor page.
- **Steps:**
  1. Edit content in one section.
  2. Switch to another section and edit content without saving the changes in the previous section.
  3. Click on the `Reset` button.
- **Expected Results:** All changes across all sections, both saved and unsaved, should be cleared.

---

### Test Case 007
- **Description:** Verify the Reset button functionality when no sections are added.
- **Prerequisites:** The user is on the Readme editor page without adding any section.
- **Steps:**
  1. Ensure no sections are added.
  2. Click the `Reset` button.
- **Expected Results:** No error should occur; the editor should remain in its initial empty state.

---

### Test Case 008
- **Description:** Verify if the Reset button is clickable and responsive.
- **Prerequisites:** The user is on the Readme editor page.
- **Steps:**
  1. Attempt to click the `Reset` button multiple times.
- **Expected Results:** The Reset button should be clickable and responsive; it should reset the editor each time without requiring multiple clicks.

---

### Test Case 009
- **Description:** Verify that the Reset button does not interfere with the language settings of the app.
- **Prerequisites:** The user is on the Readme editor page in a non-default language setting.
- **Steps:**
  1. Change the language of the app from the language dropdown.
  2. Add sections and content.
  3. Click on the `Reset` button.
- **Expected Results:** All sections and contents should be cleared, but the language setting should remain as chosen by the user.

---

### Test Case 010
- **Description:** Verify the Reset button functionality when sections contain special characters and formatting.
- **Prerequisites:** The user is on the Readme editor page.
- **Steps:**
  1. Add sections containing special characters, symbols, and complex formatting.
  2. Click on the `Reset` button.
- **Expected Results:** All sections and contents, including special characters and formatting, should be cleared.


0 bugs
2 senseless