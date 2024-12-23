## Prompt 6.4

“
From the point of view of a tester who will perform an exploratory testing session, give me test cases to the Section selection (clickable sections in the sidebar) in the readme generator app. Please consider that to carry out these tests you only have access to the Linux operating system, and the Firefox and Chrome browsers. This app does not have a connection to any type of database and there are no user registration and login options. Consider potential edge cases, unusual flows and try to find possible bugs. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test result
”

## Images

readme1.png, readme2.png

## Answer

### Test Cases for Section Selection in the Readme Generator App

---

#### Test Case 1
- **Description:** Ensure each section in the sidebar is clickable, and the corresponding section is added to the README content in the editor.
- **Prerequisites:** The application should be open and accessible on either Firefox or Chrome browser on a Linux operating system.
- **Steps:**
  1. Open the Readme Generator app in Firefox.
  2. Click on the "Get Started" button on the main page.
  3. In the "Sections" sidebar, click on each section from top to bottom (e.g., "Acknowledgements," "API Reference," "Appendix," etc.).
  4. Verify that each clicked section appears in the editor pane and the corresponding content template is loaded.
- **Expected Results:** Each section should be correctly added to the editor pane, showing the appropriate template for that section.

---

#### Test Case 2 BUG (dark mode button disappear)
- **Description:** Verify the removal of a section from the sidebar and ensure it is removed from the README content in the editor.
- **Prerequisites:** The application should be open and accessible on either Firefox or Chrome browser on a Linux operating system.
- **Steps:**
  1. Open the Readme Generator app in Chrome.
  2. Click on the "Get Started" button on the main page.
  3. In the "Sections" sidebar, click on "Acknowledgements" to add it to the editor pane.
  4. After adding, click the trash bin icon next to the added "Acknowledgements" section in the editor pane.
  5. Observe the editor pane and verify that the "Acknowledgements" section is removed.
- **Expected Results:** The "Acknowledgements" section should be removed from the editor pane, and no residual content should remain.

---

#### Test Case 3
- **Description:** Test updating the order of sections in the sidebar and ensure the order is reflected correctly in the README content in the editor.
- **Prerequisites:** The application should be open and accessible on either Firefox or Chrome browser on a Linux operating system.
- **Steps:**
  1. Open the Readme Generator app in Firefox.
  2. Click on the "Get Started" button on the main page.
  3. Add multiple sections (e.g., "Acknowledgements," "API Reference," "Appendix") to the editor.
  4. Drag and drop to reorder the sections in the sidebar.
  5. Verify the order of the sections is updated correctly in the editor pane.
- **Expected Results:** The order of sections in the editor should match the updated order from the sidebar drag-and-drop action.

---

#### Test Case 4
- **Description:** Verify that clicking the “Reset” button clears all added sections in the editor.
- **Prerequisites:** The application should be open and accessible on either Firefox or Chrome browser on a Linux operating system.
- **Steps:**
  1. Open the Readme Generator app in Chrome.
  2. Click on the "Get Started" button on the main page.
  3. Add multiple sections (e.g., "Appendix," "Authors," "Badges") to the editor.
  4. Click the “Reset” button at the top of the sidebar.
  5. Confirm whether all sections are cleared from the editor pane.
- **Expected Results:** All added sections should be cleared from the editor pane, and the default state should be restored.

---

#### Test Case 5
- **Description:** Check that sections are not added multiple times if clicked repeatedly in the sidebar.
- **Prerequisites:** The application should be open and accessible on either Firefox or Chrome browser on a Linux operating system.
- **Steps:**
  1. Open the Readme Generator app in Firefox.
  2. Click on "Get Started" and enter the editor.
  3. Click the "Acknowledgements" section multiple times in quick succession.
  4. Observe the editor pane to see if multiple instances of the section are added.
- **Expected Results:** Each section should only be added once to the editor, regardless of how many times it is clicked in quick succession.

---

#### Test Case 6
- **Description:** Validate that the search functionality for sections works and filters results correctly.
- **Prerequisites:** The application should be open and accessible on either Firefox or Chrome browser on a Linux operating system.
- **Steps:**
  1. Open the Readme Generator app in Chrome.
  2. Click on the "Get Started" button to enter the editor.
  3. Use the search bar in the “Sections” sidebar and type part of a section name (e.g., "Authors").
  4. Verify the search results are filtered correctly based on the entered text.
- **Expected Results:** Only sections that match the search term should be displayed in the sidebar, allowing easy access to the desired section.

---

#### Test Case 7
- **Description:** Test section selection and content editing in multiple languages.
- **Prerequisites:** The application should be open and accessible on either Firefox or Chrome browser on a Linux operating system. Select a non-English language.
- **Steps:**
  1. Open the Readme Generator app.
  2. Change the language via the language switcher in the top right corner to another language (e.g., Français).
  3. Click the "Get Started" button.
  4. Add a section from the sidebar (e.g., "Acknowledgements").
  5. Enter some text in the added section in the selected language.
  6. Observe whether the added section and entered content are displayed correctly.
- **Expected Results:** The interface and section content should be displayed correctly in the chosen language, and text input should reflect the selected language.

These test cases aim to ensure comprehensive coverage of various functionalities, including the usability of the section selection feature in different scenarios and edge cases, to identify any potential bugs or issues.


1 bug 
0 senseless
