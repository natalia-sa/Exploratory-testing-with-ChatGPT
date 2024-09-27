## Prompt 6.12

“
From the point of view of a tester who will perform an exploratory testing session, give me test cases to the Download button functionality in the readme generator app. Please consider that to carry out these tests you only have access to the Linux operating system, and the Firefox and Chrome browsers. This app does not have a connection to any type of database and there are no user registration and login options. Consider potential edge cases, unusual flows and try to find possible bugs. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test result
”

## Images

readme1.png, readme2.png

## Answer

### Test Case 01
- **Description**: Verify that the README file is successfully downloaded in Firefox when clicking the "Download" button.
- **Prerequisites**: Application is open in Firefox on Linux with a valid README content present in the editor.
- **Steps**:
  1. Navigate to the README editor page in Firefox.
  2. Enter valid content in the README editor sections.
  3. Click on the "Download" button.
- **Expected Results**: A README markdown file (.md) is downloaded to the default download folder with the entered content.

---

### Test Case 02
- **Description**: Verify that the README file is successfully downloaded in Chrome when clicking the "Download" button.
- **Prerequisites**: Application is open in Chrome on Linux with a valid README content present in the editor.
- **Steps**:
  1. Navigate to the README editor page in Chrome.
  2. Enter valid content in the README editor sections.
  3. Click on the "Download" button.
- **Expected Results**: A README markdown file (.md) is downloaded to the default download folder with the entered content.

---

### Test Case 03
- **Description**: Verify the behavior when the "Download" button is clicked with an empty README editor.
- **Prerequisites**: Application is open in Firefox or Chrome on Linux with no content in the README editor.
- **Steps**:
  1. Navigate to the README editor page.
  2. Ensure the editor is empty (no sections or content entered).
  3. Click on the "Download" button.
- **Expected Results**: An empty README markdown file (.md) is downloaded to the default download folder.

---

### Test Case 04
- **Description**: Verify that the download works correctly when sections are added, edited, and removed multiple times.
- **Prerequisites**: Application is open in Firefox or Chrome on Linux.
- **Steps**:
  1. Navigate to the README editor page.
  2. Add multiple sections (e.g., Title and Description, API Reference).
  3. Edit the content of each section.
  4. Remove a section and add a new one.
  5. Click on the "Download" button.
- **Expected Results**: A README markdown file (.md) is downloaded with the final content as edited.

---

### Test Case 05
- **Description**: Verify the download functionality with special characters and different languages in the README content.
- **Prerequisites**: Application is open in Firefox or Chrome on Linux.
- **Steps**:
  1. Navigate to the README editor page.
  2. Add sections with various special characters (e.g., !@#$%^&*()).
  3. Enter content in various languages (e.g., French, Chinese).
  4. Click on the "Download" button.
- **Expected Results**: A README markdown file (.md) is downloaded with the same special characters and multiple-language content preserved.

---

### Test Case 06
- **Description**: Verify the app's responsiveness by resizing the browser window while editing and downloading the README.
- **Prerequisites**: Application is open in Firefox or Chrome on Linux.
- **Steps**:
  1. Navigate to the README editor page.
  2. Enter valid content in the README editor sections.
  3. Resize the browser window to a smaller size and back to full screen.
  4. Click on the "Download" button.
- **Expected Results**: A README markdown file (.md) is downloaded correctly, and the layout does not break during resizing.

---

### Test Case 07
- **Description**: Verify the download functionality when operating in different themes (e.g., light and dark modes).
- **Prerequisites**: Application is open in Firefox or Chrome on Linux.
- **Steps**:
  1. Navigate to the README editor page.
  2. Toggle between dark and light modes.
  3. Enter valid content in the README editor sections.
  4. Click on the "Download" button.
- **Expected Results**: A README markdown file (.md) is downloaded successfully with consistent content regardless of the theme.

---

### Test Case 08 
- **Description**: Verify that non-responsive "Download" button is handled properly.
- **Prerequisites**: Application is open in Firefox or Chrome on Linux.
- **Steps**:
  1. Navigate to the README editor page.
  2. Simulate slow or no network connection (use a tool/extensions to throttle network speed).
  3. Enter valid content in the README editor sections.
  4. Click on the "Download" button.
- **Expected Results**: Either the download starts after a delay, or a user-friendly error message is displayed indicating the connectivity issue.

---

### Test Case 09
- **Description**: Verify the download button functionality after switching the languages.
- **Prerequisites**: Application open in Firefox or Chrome on Linux.
- **Steps**:
  1. Navigate to the README editor page.
  2. Change the application language using the language dropdown menu.
  3. Enter valid content in the README editor sections.
  4. Click on the "Download" button.
- **Expected Results**: A README markdown file (.md) is downloaded with the same sections/content regardless of the UI language.

---

### Test Case 10
- **Description**: Verify the download functionality in both preview and raw views.
- **Prerequisites**: Application open in Firefox or Chrome on Linux.
- **Steps**:
  1. Navigate to the README editor page.
  2. Enter valid content in the README editor sections.
  3. Toggle between 'Preview' and 'Raw' views.
  4. Click on the "Download" button in each view.
- **Expected Results**: A README markdown file (.md) is downloaded with the same content irrespective of the view mode.

---

These test cases should help uncover potential issues with the download functionality in various usage scenarios.

0 bugs
0 senseless