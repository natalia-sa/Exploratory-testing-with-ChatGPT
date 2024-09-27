## Prompt 5.6

“
From the point of view of a tester who will perform an exploratory testing session, give me test cases to the Add custom section functionality in the readme generator app. This app does not have a connection to any type of database and there are no user registration and login options. Consider potential edge cases, unusual flows and try to find possible bugs. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test results
”

## Images

readme1.png, readme2.png, readme5.png

## Answer

### Test Case 1
- **Description:** Add a new custom section with a valid title and verify it appears in the editor and preview.
- **Prerequisites:** The app should be running and accessible.
- **Steps:**
  1. Open the app and click on "Get Started."
  2. Click on the "+ Custom Section" button.
  3. Enter a valid title (e.g., "Custom Section 1") in the input box.
  4. Click "Add Section."
- **Expected Results:** The new custom section should appear both in the editor and the preview.

### Test Case 2 - BUG (it adds the previous section)
- **Description:** Add a new custom section with an empty title and verify appropriate error handling.
- **Prerequisites:** The app should be running and accessible.
- **Steps:**
  1. Open the app and click on "Get Started."
  2. Click on the "+ Custom Section" button.
  3. Leave the title input box empty.
  4. Click "Add Section."
- **Expected Results:** The app should not allow an empty title and should display an error message.

### Test Case 3 - BUG
- **Description:** Add a new custom section with a very long title and verify how it is handled.
- **Prerequisites:** The app should be running and accessible.
- **Steps:**
  1. Open the app and click on "Get Started."
  2. Click on the "+ Custom Section" button.
  3. Enter a very long title (e.g., 256 characters) in the input box.
  4. Click "Add Section."
- **Expected Results:** The app should either accept the long title and display it correctly or limit the title length with an appropriate error message.

### Test Case 4
- **Description:** Add multiple custom sections sequentially and verify they are listed correctly.
- **Prerequisites:** The app should be running and accessible.
- **Steps:**
  1. Open the app and click on "Get Started."
  2. Click on the "+ Custom Section" button.
  3. Enter a valid title for the first section (e.g., "Custom Section 1") and click "Add Section."
  4. Repeat steps 2-3 for additional sections (e.g., "Custom Section 2", "Custom Section 3").
- **Expected Results:** All added custom sections should appear in the editor and the preview in the order they were added.

### Test Case 5
- **Description:** Add a custom section with special characters in the title and verify handling.
- **Prerequisites:** The app should be running and accessible.
- **Steps:**
  1. Open the app and click on "Get Started."
  2. Click on the "+ Custom Section" button.
  3. Enter a title with special characters (e.g., "@#$%^&*()") in the input box.
  4. Click "Add Section."
- **Expected Results:** The new custom section should appear both in the editor and the preview with special characters displayed correctly.

### Test Case 6
- **Description:** Verify app behavior when adding a custom section during offline mode.
- **Prerequisites:** The app should be running and accessible. Use a network disconnection tool to simulate offline mode.
- **Steps:**
  1. Disconnect the internet (simulate offline mode).
  2. Open the app and attempt to click on "Get Started."
  3. Try to add a custom section by clicking "+ Custom Section" and entering a valid title.
- **Expected Results:** The app should handle the offline mode gracefully, either by showing an error message or by storing the added section locally.

### Test Case 7
- **Description:** Cancel the addition of a custom section and verify it does not appear in the editor and preview.
- **Prerequisites:** The app should be running and accessible.
- **Steps:**
  1. Open the app and click on "Get Started."
  2. Click on the "+ Custom Section" button.
  3. Enter a valid title (e.g., "Custom Section 1") in the input box.
  4. Click "Cancel" instead of "Add Section."
- **Expected Results:** The custom section should not appear in the editor or the preview.

### Test Case 8
- **Description:** Add a custom section with leading and trailing whitespace in the title and verify the handling.
- **Prerequisites:** The app should be running and accessible.
- **Steps:**
  1. Open the app and click on "Get Started."
  2. Click on the "+ Custom Section" button.
  3. Enter a title with leading and trailing whitespace (e.g., "  Custom Section  ") in the input box.
  4. Click "Add Section."
- **Expected Results:** The new custom section should appear in the editor and the preview with leading and trailing whitespace trimmed.


2 bugs
0 senseless
