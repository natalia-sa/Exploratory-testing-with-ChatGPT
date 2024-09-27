## Prompt 6.8

“
From the point of view of a tester who will perform an exploratory testing session, give me test cases to the Section edit functionality in the readme generator app. Please consider that to carry out these tests you only have access to the Linux operating system, and the Firefox and Chrome browsers. This app does not have a connection to any type of database and there are no user registration and login options. Consider potential edge cases, unusual flows and try to find possible bugs. I will provide screenshots of the app GUI. The test cases should follow the structure below:

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
- **Description:** Add a new section and edit its title and content.
- **Prerequisites:** Access to a Linux operating system with Firefox or Chrome browser.
- **Steps:**
  1. Open the readme generator app in a browser.
  2. Click on "Get Started" to access the editor.
  3. Click "Acknowledgements" from the list of sections on the left side.
  4. Click on the new "Acknowledgements" section that appears in the editor.
  5. Change the title to "Thanks" and add some content.
  6. Observe the preview section on the right to see if the changes reflect.
- **Expected Results:** The new section should be added, and any title and content changes should be accurately reflected in the preview.

---

### Test Case 2
- **Description:** Remove an existing section from the readme.
- **Prerequisites:** Access to a Linux operating system with Firefox or Chrome browser.
- **Steps:**
  1. Open the readme generator app in a browser.
  2. Click on "Get Started" to access the editor.
  3. Click on the trash icon beside the "Title and Description" section.
  4. Confirm the removal if prompted.
  5. Observe the editor and preview panes to ensure the section is removed.
- **Expected Results:** The "Title and Description" section should be removed from both the editor and preview panes.

---

### Test Case 3 SENSELESS
- **Description:** Edit an existing section's title to an empty string.
- **Prerequisites:** Access to a Linux operating system with Firefox or Chrome browser.
- **Steps:**
  1. Open the readme generator app in a browser.
  2. Click on "Get Started" to access the editor.
  3. Click on the "Title and Description" section.
  4. Change the title to an empty string and save.
  5. Observe the editor and preview panes to ensure the changes reflect.
- **Expected Results:** The application should not allow the title to be an empty string or should display a validation error message.

---

### Test Case 4 - bug (scrolls horizontally)
- **Description:** Test the app's behavior when adding a section with very long text content.
- **Prerequisites:** Access to a Linux operating system with Firefox or Chrome browser.
- **Steps:**
  1. Open the readme generator app in a browser.
  2. Click on "Get Started" to access the editor.
  3. Click "Documentation" from the list of sections.
  4. Add very long text content to the "Documentation" section.
  5. Observe the editor and preview panes to check for performance issues or text overflow.
- **Expected Results:** The app should handle long text content smoothly without any performance issues or text overflow problems.

---

### Test Case 5
- **Description:** Add multiple custom sections and edit their content.
- **Prerequisites:** Access to a Linux operating system with Firefox or Chrome browser.
- **Steps:**
  1. Open the readme generator app in a browser.
  2. Click on "Get Started" to access the editor.
  3. Click "+ Custom Section" from the list of sections on the left side multiple times.
  4. For each custom section added, change the section title and content.
  5. Observe the preview pane to ensure each section displays correctly.
- **Expected Results:** Each custom section should be able to be added and edited, with accurate reflection in the preview pane.

---

### Test Case 6 - senseless
- **Description:** Test localization by changing the language and verifying section names translation.
- **Prerequisites:** Access to a Linux operating system with Firefox or Chrome browser.
- **Steps:**
  1. Open the readme generator app in a browser.
  2. Switch language from the dropdown menu located at the top-right corner.
  3. Verify that section names and any static text within the editor change to the selected language.
- **Expected Results:** The application should accurately translate section names and static text to the chosen language.

---

### Test Case 7
- **Description:** Test the "Reset" functionality.
- **Prerequisites:** Access to a Linux operating system with Firefox or Chrome browser.
- **Steps:**
  1. Open the readme generator app in a browser.
  2. Make changes to several sections, including adding custom content and new sections.
  3. Click on the "Reset" button at the top.
  4. Confirm the reset if prompted.
  5. Observe the editor and preview panes to ensure it has been reset to default.
- **Expected Results:** All the changes should be reverted, restoring the editor to its default state.

---

### Test Case 8 SENSELESS
- **Description:** Verify behavior when network connection is lost.
- **Prerequisites:** Access to a Linux operating system with Firefox or Chrome browser.
- **Steps:**
  1. Open the readme generator app in a browser and start editing a section.
  2. Disable the network connection on the machine.
  3. Continue attempting to edit and save sections.
  4. Observe the behavior of the application, including any error messages.
- **Expected Results:** The application should handle the loss of network connection gracefully, providing appropriate error messages and potentially saving data locally (if supported).

---

### Test Case 9
- **Description:** Test the functionality of switching between different view modes (Preview and Raw).
- **Prerequisites:** Access to a Linux operating system with Firefox or Chrome browser.
- **Steps:**
  1. Open the readme generator app in a browser.
  2. Click on "Get Started" to access the editor.
  3. Edit an existing section's content.
  4. Switch between "Preview" and "Raw" view modes.
  5. Observe the changes in both views to ensure consistency.
- **Expected Results:** Both "Preview" and "Raw" views should accurately reflect the content changes, and the switching between them should be smooth without any data loss or format issues.

---

### Test Case 10 - bugs (responsiveness issues)
- **Description:** Check responsiveness and layout on different window sizes.
- **Prerequisites:** Access to a Linux operating system with Firefox or Chrome browser.
- **Steps:**
  1. Open the readme generator app in a browser.
  2. Resize the browser window to various sizes, including minimum and maximum possible dimensions.
  3. Ensure the sections, editor, and preview panes adjust accordingly and remain usable.
- **Expected Results:** The application should adjust its layout responsively, maintaining usability and readability across different window sizes.


2 bugs
3 senseless