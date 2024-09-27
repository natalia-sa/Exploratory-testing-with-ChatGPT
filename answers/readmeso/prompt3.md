# Prompt 3

“From the point of view of a tester, give me exploratory test cases to the readme generator app,
covering all the functionalities, suggesting unusual flows, trying to find possible bugs, failures, security issues,
etc. I will provide screenshots of the app GUI. The images contain tags that identify some features and characteristics
of the app. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test results”

## Images

readme1.png, readme2.png, readme3.png, readme4.png, readme5.png, readme6.png, readme7.png, readme8.png

## Answer

### Test Case 1

- **Description:** Verify the language selection functionality on the landing page.
- **Prerequisites:** Access to the landing page with language selection dropdown visible.
- **Steps:**
  1. Navigate to the landing page.
  2. Click on the "Select language" dropdown.
  3. Select each language one by one from the dropdown.
  4. Observe if the content on the page changes to the selected language.
- **Expected results:** The page content should change to the selected language after making a selection from the dropdown.

### Test Case 2 BUG (coffee button disappear)

- **Description:** Test the "Get Started" button to ensure it redirects to the editor.
- **Prerequisites:** Access to the landing page.
- **Steps:**
  1. Navigate to the landing page.
  2. Click on the "Get Started" button.
- **Expected results:** Clicking the "Get Started" button should redirect the user to the editor page.

### Test Case 3

- **Description:** Verify adding and resetting a section in the editor.
- **Prerequisites:** Access to the editor page.
- **Steps:**
  1. Navigate to the editor.
  2. Click on "Title and Description" to add the section.
  3. Enter some text in the editor.
  4. Click on the "Reset" button for that section.
- **Expected results:** The section should be reset to its default state, losing any changes made.

### Test Case 4 BUG (dark mode button disappear)

- **Description:** Test the delete section functionality.
- **Prerequisites:** Access to the editor page with at least one section added.
- **Steps:**
  1. Navigate to the editor.
  2. Ensure the "Title and Description" section is present.
  3. Click on the delete (trash bin) icon of the section.
- **Expected results:** The "Title and Description" section should be deleted from the editor.

### Test Case 5

- **Description:** Verify the "Download README file" functionality.
- **Prerequisites:** Access to the editor page with the content in the editor.
- **Steps:**
  1. Navigate to the editor.
  2. Add and complete a section with some content.
  3. Click on the "Download" button.
- **Expected results:** A README file with the user's content should be successfully downloaded.

### Test Case 6

- **Description:** Test the dark mode toggle functionality.
- **Prerequisites:** Access to the editor page.
- **Steps:**
  1. Navigate to the editor.
  2. Click on the "Switch to dark mode" icon.
- **Expected results:** The appearance of the page should switch to dark mode. Clicking the icon again should toggle back to light mode.

### Test Case 7

- **Description:** Test the "Preview markdown content" and "See raw content" functionality.
- **Prerequisites:** Access to the editor page with some content.
- **Steps:**
  1. Navigate to the editor.
  2. Add some content under "Title and Description".
  3. Click on "Raw" and "Preview" buttons switching between them.
- **Expected results:** The pane on the right should switch between raw markdown and the rendered preview of the content.

### Test Case 8

- **Description:** Verify the "Create custom section" functionality.
- **Prerequisites:** Access to the editor page.
- **Steps:**
  1. Navigate to the editor.
  2. Click on "+ Custom Section".
  3. Enter a title for the new section in the dialog box.
  4. Click "Add Section".
- **Expected results:** A new custom section should be added to the list of sections and available for content editing.

### Test Case 9

- **Description:** Verify if all elements reset when clicking on the "Reset" button at the top of the page.
- **Prerequisites:** Access to the editor with multiple sections added and filled with content.
- **Steps:**
  1. Navigate to the editor.
  2. Add several sections and fill them with content.
  3. Click on the "Reset" button at the top of the page.
- **Expected results:** All sections should be removed and the page should reset to its initial state.

### Test Case 10

- **Description:** Test the "Make donation" functionality.
- **Prerequisites:** Access to the editor.
- **Steps:**
  1. Navigate to the editor.
  2. Click on the "yellow coffee button" to make a donation.
  3. Follow the steps to input the donation information and message.
  4. Attempt to complete the payment.
- **Expected results:** The donation process should proceed without errors, providing feedback for a successful donation.

### Test Case 11 (Unusual Flow) BUG (preview scrolls horizontally)

- **Description:** Verify the reaction of the app to extremely large input in sections.
- **Prerequisites:** Access to the editor page.
- **Steps:**
  1. Navigate to the editor.
  2. Add a section.
  3. Paste an extremely large amount of text into the section.
- **Expected results:** The app should handle the large input gracefully without crashing or becoming unresponsive.

### Test Case 12 (Unusual Flow)

- **Description:** Verify functionality with continuous rapid switching between languages.
- **Prerequisites:** Access to the landing page with language selection dropdown.
- **Steps:**
  1. Navigate to the landing page.
  2. Continuously and rapidly change the language selection.
- **Expected results:** The application should handle rapid changes without breaking the layout, content, or functionality.
