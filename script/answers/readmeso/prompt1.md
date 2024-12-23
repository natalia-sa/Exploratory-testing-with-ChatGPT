# Prompt 1

“From the point of view of a tester, generate exploratory test cases to the readme generator app. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number].
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test results
”

## Images

readme1.png, readme2.png, readme3.png, readme4.png, readme5.png, readme6.png, readme7.png, readme8.png

## Answer

Based on the provided screenshots of the readme generator app's GUI, here are exploratory test cases for the application:

### Test Case 1 BUG (coffee button disappear)

1. **Description**: Verify that the "Get Started" button navigates to the README editor.
   - **Prerequisites**: User is on the homepage (https://readme.so).
   - **Steps**:
     1. Open the homepage in a web browser.
     2. Click the "Get Started" button.
   - **Expected results**: The user should be directed to the README editor page.

### Test Case 2

2. **Description**: Verify that the user can switch the language from the default language to another language.
   - **Prerequisites**: User is on the homepage or the editor page.
   - **Steps**:
     1. Click on the language dropdown on the top right corner.
     2. Select a different language from the dropdown menu.
   - **Expected results**: The language of the application should change to the selected language.

### Test Case 3

3. **Description**: Verify that the user can add a "Title and Description" section to the README.
   - **Prerequisites**: User is on the README editor page.
   - **Steps**:
     1. Click the "Title and Description" section on the left sidebar.
   - **Expected results**: The "Title and Description" section should appear in the editor area.

### Test Case 4

4. **Description**: Verify that the user can preview the README content.
   - **Prerequisites**: User has added content to the README (e.g., "Title and Description").
   - **Steps**:
     1. Switch the preview tab from "Raw" to "Preview."
   - **Expected results**: The right panel should show a formatted preview of the README content.

### Test Case 5

5. **Description**: Verify that the "Night Mode" feature toggles the theme of the editor.
   - **Prerequisites**: User is on the README editor page.
   - **Steps**:
     1. Click the moon icon to switch to night mode.
   - **Expected results**: The theme of the editor should change to a dark theme.

### Test Case 6

6. **Description**: Verify that the "Reset" button clears all sections in the README editor.
   - **Prerequisites**: User has added one or more sections to the editor.
   - **Steps**:
     1. Click the "Reset" button at the top left.
   - **Expected results**: All sections should be cleared from the editor.

### Test Case 7

7. **Description**: Verify the functionality of the "Download" button for exporting README.
   - **Prerequisites**: User has created a README with content.
   - **Steps**:
     1. Click the "Download" button.
   - **Expected results**: A file download should be initiated, saving the README content as a markdown file.

### Test Case 8

8. **Description**: Verify that the user can add a custom section.
   - **Prerequisites**: User is on the README editor page.
   - **Steps**:
     1. Click on "Custom Section" in the left sidebar.
     2. Enter a title for the custom section.
     3. Click "Add Section."
   - **Expected results**: A new custom section with the given title should be added to the editor.

### Test Case 9 BUG (dark mode icon disappear)

9. **Description**: Verify that the user can delete a section.
   - **Prerequisites**: User has added a section (e.g., "Title and Description").
   - **Steps**:
     1. Click the trash can icon next to the section's name.
   - **Expected results**: The selected section should be removed from the editor.

### Test Case 10

10. **Description**: Verify that the user can use the "Sponsor" button to navigate to the sponsorship page.
    - **Prerequisites**: User is on the README editor page.
    - **Steps**:
      1. Click the "Sponsor" button.
    - **Expected results**: The user should be directed to the sponsorship page or modal.

### Test Case 11

11. **Description**: Verify that the "Support" modal appears when clicking the coffee button.
    - **Prerequisites**: User is on the README editor page.
    - **Steps**:
      1. Click the yellow coffee cup button at the bottom right.
    - **Expected results**: A modal should appear, allowing the user to support by buying a coffee.

These test cases will ensure comprehensive coverage of the GUI functionality for the readme generator app.