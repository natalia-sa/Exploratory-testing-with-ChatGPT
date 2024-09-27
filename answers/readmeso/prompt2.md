# Prompt 2

“From the point of view of a tester, give me exploratory test cases to the readme generator app, covering all the functionalities, suggesting unusual flows, trying to find possible bugs, failures, security issues, etc. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test results”

## Images

readme1.png, readme2.png, readme3.png, readme4.png, readme5.png, readme6.png, readme7.png, readme8.png

## Answer

Certainly! Below are some exploratory test cases for the README generator app based on the provided screenshots:

### Test Cases:

#### [Test 1]

- **Description: Change Language and Check Translation**
- **Prerequisites:**
  - Launch the README generator app.
- **Steps:**
  1. On the initial screen, click the language selector dropdown in the top right corner.
  2. Select a different language (e.g., French).
  3. Observe the translation of the interface.
- **Expected Results:**
  - The interface should translate into the selected language accurately.
  - No elements should be left untranslated.
  - The usability should be intact in the new language.

#### [Test 2]

- **Description: Add and Modify Section Content**
- **Prerequisites:**
  - Launch the README generator app.
  - Ensure you are on the editor page.
- **Steps:**
  1. Click on the "Title and Description" section in the left panel.
  2. Edit the content in the editor by typing a project title and description.
  3. Click on the "Acknowledgements" section and add details.
  4. Observe the rendered preview on the right.
- **Expected Results:**
  - The content should be appropriately updated in the preview section.
  - No unexpected behavior or error messages should occur.

#### [Test 3]

- **Description: Toggle Between ‘Preview’ and ‘Raw’**
- **Prerequisites:**
  - Launch the README generator app.
  - Ensure there is content in the editor.
- **Steps:**
  1. Click on the "Preview" button on the right top side of the editor.
  2. Click on the "Raw" button next to it.
  3. Observe the changes in the display.
- **Expected Results:**
  - Toggling should switch between rendered and raw Markdown views smoothly.
  - No display or formatting issues should arise.

#### [Test 4]

- **Description: Use Night Mode and Day Mode**
- **Prerequisites:**
  - Launch the README generator app.
- **Steps:**
  1. Click the sun/moon icon to switch between night mode and day mode.
  2. Observe the changes in the interface theme.
- **Expected Results:**
  - The interface should switch themes without any issues.
  - All text and buttons should remain readable and properly formatted.

#### [Test 5]

- **Description: Add and Test Custom Section**
- **Prerequisites:**
  - Launch the README generator app.
- **Steps:**
  1. Click the "+ Custom Section" button in the left panel.
  2. Input a name for the custom section and click "Add Section".
  3. Add content to the custom section.
  4. Check the preview and raw views.
- **Expected Results:**
  - The custom section should get added and display correctly.
  - Content should be editable and visible in the preview and raw views.

#### [Test 6]

- **Description: Reset Editor**
- **Prerequisites:**
  - Launch the README generator app.
  - Ensure there is content in the editor.
- **Steps:**
  1. Click the "Reset" button in the editor.
  2. Confirm the reset if prompted.
  3. Observe the changes in the editor.
- **Expected Results:**
  - All sections and content in the editor should be cleared.
  - No residual data should remain.

#### [Test 7]

- **Description: Check Download Functionality**
- **Prerequisites:**
  - Launch the README generator app.
  - Ensure there is content in the editor.
- **Steps:**
  1. Click the "Download" button on the top right of the editor.
  2. Observe the file download.
  3. Open the downloaded file and review its contents.
- **Expected Results:**
  - The README should download without issues.
  - The content should match what was present in the editor.

#### [Test 8] BUG (display scrolls horizontally)

- **Description: Test Input Validation for Sections**
- **Prerequisites:**
  - Launch the README generator app.
  - Ensure you are in the editor with the "Title and Description" section selected.
- **Steps:**
  1. Input invalid data such as special characters or excessive text length in the "Title and Description" section.
  2. Save and observe the display in the preview.
- **Expected Results:**
  - The app should handle invalid inputs gracefully without crashes.
  - Appropriate error messages should be shown if necessary limits are exceeded or if invalid characters are input.

#### [Test 9]

- **Description: Test Unusual Navigation Flow**
- **Prerequisites:**
  - Launch the README generator app.
  - Ensure you are on the main editor page.
- **Steps:**
  1. Rapidly click through different sections on the left panel.
  2. Switch between "Preview" and "Raw" views frequently.
  3. Toggle night and day mode during the navigation.
- **Expected Results:**
  - The app should handle rapid navigation smoothly.
  - No errors, crashes, or performance lags should occur.

#### [Test 10]

- **Description: Donate Functionality Test**
- **Prerequisites:**
  - Launch the README generator app.
  - Ensure that the "Buy Me a Coffee" modal is accessible.
- **Steps:**
  1. Click on the "Buy Me a Coffee" button.
  2. Enter valid data into all input fields.
  3. Attempt a dummy transaction.
- **Expected Results:**
  - The modal should function correctly with no UX/UI issues.
  - Incomplete/dummy transactions should be gracefully handled or blocked.

---

By following these test cases, a thorough exploratory testing session can be performed on the README generator app to identify potential bugs, UX issues, and security concerns.
