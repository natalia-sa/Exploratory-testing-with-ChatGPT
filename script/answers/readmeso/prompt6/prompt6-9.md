## Prompt 6.9

“
From the point of view of a tester who will perform an exploratory testing session, give me test cases to the Section delete functionality in the readme generator app. Please consider that to carry out these tests you only have access to the Linux operating system, and the Firefox and Chrome browsers. This app does not have a connection to any type of database and there are no user registration and login options. Consider potential edge cases, unusual flows and try to find possible bugs. I will provide screenshots of the app GUI. The test cases should follow the structure below:

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
- **Description:** Verify section-delete functionality works as expected.
- **Prerequisites:** A section added to the README generator.
- **Steps:**
  1. Open the app in Firefox on Linux.
  2. Add a section “Acknowledgements” by clicking on it from the left panel.
  3. Click on the trash bin icon next to the Acknowledgements section in the Sections list.
- **Expected Results:** The Acknowledgements section should be removed from both the Sections list and the Preview editor.

---

### Test Case 2
- **Description:** Verify deleting a section updates the Preview pane correctly.
- **Prerequisites:** At least two sections added to the README generator.
- **Steps:**
  1. Open the app in Chrome on Linux.
  2. Add sections “Acknowledgements” and “API Reference” by clicking on them.
  3. Delete the Acknowledgements section by clicking the trash bin icon.
- **Expected Results:** The Preview pane should no longer display the Acknowledgements section, only the API Reference.

---

### Test Case 3
- **Description:** Verify the delete button for a section is present and clickable.
- **Prerequisites:** A section added to the README generator.
- **Steps:**
  1. Open the app in Firefox on Linux.
  2. Add a section “Contributing” by clicking on it.
  3. Check the existence of the trash bin icon next to the Contributing section.
  4. Attempt to click on the trash bin icon.
- **Expected Results:** The trash bin icon should be visible, and the section should be removed upon clicking.

---

### Test Case 4
- **Description:** Verify that deleting a section doesn’t affect other sections.
- **Prerequisites:** At least three sections added to the README generator.
- **Steps:**
  1. Open the app in Chrome on Linux.
  2. Add sections “Introduction”, “Contributing”, and “Acknowledgements”.
  3. Delete the Contributing section by clicking the trash bin icon.
- **Expected Results:** The Introduction and Acknowledgements sections remain intact, and only Contributing is removed.

---

### Test Case 5
- **Description:** Verify sections can be deleted multiple times in a session.
- **Prerequisites:** At least one section added to the README.
- **Steps:**
  1. Open the app in Firefox on Linux.
  2. Add and delete the section “API Reference” multiple times.
- **Expected Results:** Each time a section is added and deleted, it should be removed without errors or crashes.

---

### Test Case 6 - senseless
- **Description:** Verify deleting a section when no section is added initially.
- **Prerequisites:** No section should be added initially.
- **Steps:**
  1. Open the app in Chrome on Linux.
  2. Attempt to click the trash bin icon next to “Project Title” or any default section.
- **Expected Results:** The application should handle this gracefully, either by showing an appropriate message or having no effect.

---

### Test Case 7 - senseless
- **Description:** Verify undo functionality after deleting a section.
- **Prerequisites:** A section added to the README, with at least one edit.
- **Steps:**
  1. Open the app in Firefox on Linux.
  2. Add the “Environment Variables” section and enter some text.
  3. Delete the section by clicking the trash bin icon.
  4. Attempt to undo the delete (if there’s any undo button/shortcut).
- **Expected Results:** If an undo feature is available, it should restore the deleted section with its content.

---

### Test Case 8
- **Description:** Verify deleting a section in different languages.
- **Prerequisites:** At least one section added, app language set to different languages.
- **Steps:**
  1. Open the app in Firefox on Linux.
  2. Change the language to French.
  3. Add the “Déploiement” section (likely “Deployment” in French).
  4. Delete the section by clicking the trash bin icon.
- **Expected Results:** The section should be deleted correctly regardless of the language setting of the app.

---

### Test Case 9
- **Description:** Verify deleting a custom section.
- **Prerequisites:** A custom section added to the README.
- **Steps:**
  1. Open the app in Chrome on Linux.
  2. Add a custom section by clicking on “+ Custom Section”.
  3. Delete the custom section by clicking the trash bin icon.
- **Expected Results:** The custom section should be removed completely from the Sections list and Preview pane.

---

### Test Case 10
- **Description:** Verify that deleting a section does not leave behind any remnants.
- **Prerequisites:** A section added to the README.
- **Steps:**
  1. Open the app in Firefox on Linux.
  2. Add the “Color Reference” section.
  3. Enter data into the section.
  4. Delete the section by clicking the trash bin icon.
- **Expected Results:** No part of the Color Reference section content should remain in the Editor or Preview panes.



0 bugs
2 senseless