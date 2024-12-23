## Prompt 5.9

“
From the point of view of a tester who will perform an exploratory testing session, give me test cases to the Section delete functionality in the readme generator app. This app does not have a connection to any type of database and there are no user registration and login options. Consider potential edge cases, unusual flows and try to find possible bugs. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test results
”

## Images

readme1.png, readme2.png

## Answer

Here are some exploratory testing cases for the "Section delete" functionality in the README generator app:

---

### Test Case 1 
- **Description:** Check the deletion of a single section.
- **Prerequisites:** Ensure you have one section added, for instance, "Title and Description."
- **Steps:**
  1. Open the README generator app.
  2. Add a section like "Title and Description" if not already present.
  3. Click on the delete icon (trash bin) next to the "Title and Description" section.
- **Expected Results:** The "Title and Description" section should be removed from the editor, and the section list should update to reflect the removal.

---

### Test Case 2
- **Description:** Verify that the section is deleted immediately after adding it.
- **Prerequisites:** None.
- **Steps:**
  1. Open the README generator app.
  2. Immediately add a section like "API Reference."
  3. Click on the delete icon (trash bin) next to the "API Reference" section.
- **Expected Results:** The "API Reference" section should be deleted from the section list and editor.

---

### Test Case 3
- **Description:** Test deletion of multiple different sections sequentially.
- **Prerequisites:** Ensure multiple sections are added, such as "Acknowledgements", "Appendix", and "Authors."
- **Steps:**
  1. Open the README generator app.
  2. Add multiple sections (e.g., "Acknowledgements", "Appendix", and "Authors").
  3. Sequentially click the delete icon next to each section from top to bottom.
- **Expected Results:** Each selected section should be removed from the section list and editor one by one, without affecting the remaining sections.

---

### Test Case 4
- **Description:** Validate deletion of all available sections.
- **Prerequisites:** Ensure multiple sections such as "Title and Description," "Acknowledgements," "Authors," and "API Reference" are added.
- **Steps:**
  1. Open the README generator app.
  2. Add several sections (e.g., "Title and Description," "Acknowledgements," "Authors," "API Reference").
  3. Click on the delete icon next to each section until all sections are deleted.
- **Expected Results:** All sections should be removed from the section list and editor, resulting in an empty/clean state of the app.

---

### Test Case 5 - SENSELESS
- **Description:** Test deletion functionality with an unsaved README.
- **Prerequisites:** Add one or more sections without saving/exporting the README.
- **Steps:**
  1. Open the README generator app.
  2. Add a section like "Deployment."
  3. Without saving/exporting, click the delete icon next to the "Deployment" section.
- **Expected Results:** The "Deployment" section should be removed, and the unsaved state should be maintained.

---

### Test Case 6 - SENSELESS
- **Description:** Try to delete a non-existent section (Edge case).
- **Prerequisites:** One section added and immediately deleted.
- **Steps:**
  1. Open the README generator app.
  2. Add a section like "Badges."
  3. Delete the "Badges" section.
  4. Attempt to click the delete button again on the deleted section.
- **Expected Results:** An appropriate error message should be displayed or nothing should happen since the section no longer exists.

---

### Test Case 7
- **Description:** Confirm UI updates after section deletion.
- **Prerequisites:** Ensure at least one section is added.
- **Steps:**
  1. Open the README generator app.
  2. Add a section like "Contributing."
  3. Click on the delete icon next to the "Contributing" section.
- **Expected Results:** The "Contributing" section should be removed from both the editor interface and the preview pane, and the remaining UI should adjust accordingly (e.g., no empty spaces or broken layout).

---

### Test Case 8 - SENSELESS
- **Description:** Validate undo functionality (if available) after deleting a section.
- **Prerequisites:** Ensure at least one section is added.
- **Steps:**
  1. Open the README generator app.
  2. Add a section like "Demo."
  3. Delete the "Demo" section.
  4. Look for an "Undo" option and click it.
- **Expected Results:** The "Demo" section should be restored to its previous position with all its content intact.

---

These test cases cover normal, edge, and exceptional scenarios surrounding the section deletion functionality to uncover potential bugs and ensure robustness of the app.

0 bug
3 senseless
