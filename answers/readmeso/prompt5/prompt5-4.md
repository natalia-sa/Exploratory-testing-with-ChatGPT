## Prompt 5.4

“
From the point of view of a tester who will perform an exploratory testing session, give me test cases to the Section selection (clickable sections in the sidebar) in the readme generator app. This app does not have a connection to any type of database and there are no user registration and login options. Consider potential edge cases, unusual flows and try to find possible bugs. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test results
”

## Images

readme1.png, readme2.png

## Answer

### Test Case 001
- **Description:** Ensure clicking on different sections in the sidebar loads the correct content in the editor.
- **Prerequisites:** Application is running and sidebar is visible with all sections listed.
- **Steps:**
  1. Click on "Acknowledgements" in the sidebar.
  2. Observe the content loaded in the editor.
  3. Click on "API Reference" in the sidebar.
  4. Observe the content loaded in the editor.
  5. Repeat clicking on each section and observe the content loaded in the editor.
- **Expected results:** Each section clicked in the sidebar should load the corresponding content in the editor without any delay or errors.

### Test Case 002 
- **Description:** Verify that clicking on the same section multiple times does not produce any errors.
- **Prerequisites:** Application is running and sidebar is visible with all sections listed.
- **Steps:**
  1. Click on "Title and Description" in the sidebar.
  2. Observe the content loaded in the editor.
  3. Click on "Title and Description" again multiple times.
- **Expected results:** Clicking the same section multiple times should not produce any UI errors, crashes, or duplicate content in the editor.

### Test Case 003
- **Description:** Check for any UI issues when rapidly switching between sections.
- **Prerequisites:** Application is running and sidebar is visible with all sections listed.
- **Steps:**
  1. Rapidly click on "Appendix".
  2. Immediately switch to "Authors".
  3. Immediately switch to "Badges".
  4. Continue rapidly switching between different sections randomly.
- **Expected results:** The UI should update correctly and the editor should display the content relevant to the last clicked section without lag or visual errors.

### Test Case 004
- **Description:** Ensure the "Reset" button resets the current content in the editor.
- **Prerequisites:** Application is running with some content already loaded in the editor.
- **Steps:**
  1. Make some changes to the content in the editor.
  2. Click the "Reset" button.
- **Expected results:** The content in the editor should reset to its default state for the selected section.

### Test Case 005 - SENSELESS
- **Description:** Validate the functionality of the "Custom Section" button.
- **Prerequisites:** Application is running and the sidebar is visible with all sections listed.
- **Steps:**
  1. Click on the "Custom Section" button in the sidebar.
  2. Observe if a new editable section is created in the editor.
  3. Enter content into the new custom section.
- **Expected results:** Clicking "Custom Section" should create a new section in the editor, and entering content should work without any issues.

### Test Case 006
- **Description:** Ensure that the language change in the dropdown does not affect the section navigation and content loading.
- **Prerequisites:** Application is running and the language dropdown is visible.
- **Steps:**
  1. Change the language from the dropdown list.
  2. Click on different sections in the sidebar.
  3. Observe if the content is loaded correctly as per the chosen language.
- **Expected results:** Changing the language should update the UI accordingly but should not affect the section navigation and content loading functionality.

### Test Case 007
- **Description:** Check the behavior when no sections are selected.
- **Prerequisites:** Application is running.
- **Steps:**
  1. Do not click on any section.
  2. Observe the initial state of the editor.
- **Expected results:** The editor should either be empty or have a placeholder message instructing the user to select a section.

### Test Case 008
- **Description:** Validate scrolling behavior in the sidebar while selecting sections.
- **Prerequisites:** Application is running, and there are enough sections to enable sidebar scrolling.
- **Steps:**
  1. Scroll down the sidebar.
  2. Click on a section at the bottom.
  3. Scroll back to the top and click on another section.
- **Expected results:** The sidebar scroll position should not affect the functionality of section selection, and the content in the editor should update according to the section clicked.

### Test Case 009 - BUG Dark mode button disapear
- **Description:** Check for accidental section deletions and the resulting behavior.
- **Prerequisites:** Application is running, and a section is loaded in the editor.
- **Steps:**
  1. Select a section.
  2. Attempt to delete it by clicking on the trash can icon.
- **Expected results:** The section should be deleted from the editor pane, and a confirmation modal should appear if applicable. There should be no accidental deletions without user confirmation.

### Test Case 010
- **Description:** Validate the behavior of the editor when switching between "Preview" and "Raw" modes.
- **Prerequisites:** Application is running, and a section is loaded in the editor.
- **Steps:**
  1. Switch to "Preview" mode.
  2. Observe the content layout.
  3. Switch to "Raw" mode.
  4. Observe the content formatting.
  5. Switch between the two modes multiple times.
- **Expected results:** Switching between "Preview" and "Raw" modes should update the editor's content view accordingly without any loss of data or formatting issues.

1 senseless
1 bugs
