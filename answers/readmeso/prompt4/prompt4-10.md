# Secondary prompt 10

"
From the point of view of a tester, give me exploratory test cases to the Preview and Raw Tabs features in the readme generator app, suggesting unusual flows, trying to find possible bugs, failures, security issues, etc. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test results
"

## Images

readme1.png, readme2.png

### Answer

Here are some exploratory test cases for the Preview and Raw tabs in the README generator app:

### Test Case 1 - SENSELESS
- **Description:** Verify that the Preview tab accurately displays changes made in the editor in real-time.
- **Prerequisites:** The user should be logged into the README generator app.
- **Steps:**
  1. Navigate to the Editor page.
  2. Ensure the Preview tab is active.
  3. Make changes to the "Title and Description" section in the editor.
  4. Observe the Preview tab for real-time updates.
- **Expected results:** The changes made in the editor should immediately reflect in the Preview tab accurately.

### Test Case 2 - SENSELESS
- **Description:** Test the behavior of the Raw tab when mixed content (text, images, and links) is added.
- **Prerequisites:** The user should be logged into the README generator app.
- **Steps:**
  1. Navigate to the Editor page.
  2. Ensure the Raw tab is active.
  3. Add mixed content (text, images, and links) in the editor.
  4. Switch to the Raw tab and inspect the display of the content.
- **Expected results:** The Raw tab should correctly display the markdown of the mixed content without any formatting issues.

### Test Case 3 - SENSELESS
- **Description:** Check for data consistency between the Editor, Preview, and Raw tabs when adding and removing sections rapidly.
- **Prerequisites:** The user should be logged into the README generator app.
- **Steps:**
  1. Navigate to the Editor page.
  2. Sequentially add multiple sections in quick succession.
  3. Switch between the Editor, Preview, and Raw tabs after each addition.
  4. Quickly remove the sections one by one, switching between tabs after each removal.
- **Expected results:** Each tab should update consistently without delay, and no data loss or inconsistencies should be observed.

### Test Case 4 - SENSELESS
- **Description:** Test the application's response to switching between multiple languages and verify translations in the Preview and Raw tabs.
- **Prerequisites:** The user should be logged into the README generator app.
- **Steps:**
  1. Navigate to the Editor page.
  2. Using the language switcher, change the language multiple times.
  3. Observe the Preview and Raw tabs after making each switch.
- **Expected results:** The Preview and Raw tabs should display the correct translations for the selected language, and no elements should appear untranslated or broken.

### Test Case 5 - SENSELESS
- **Description:** Verify that long texts, special characters, and emojis are handled correctly in the Preview and Raw tabs.
- **Prerequisites:** The user should be logged into the README generator app.
- **Steps:**
  1. Navigate to the Editor page.
  2. Add a large amount of text, special characters, and emojis to the editor.
  3. Switch to the Preview and Raw tabs and inspect the content display.
- **Expected results:** The Preview tab should render the content correctly without truncation or misalignment, and the Raw tab should properly show the corresponding markdown code.

### Test Case 6 - SENSELESS
- **Description:** Assess the behavior of the Preview and Raw tabs under different screen sizes and resolutions.
- **Prerequisites:** The user should be logged into the README generator app.
- **Steps:**
  1. Navigate to the Editor page.
  2. Adjust the browser window to different screen sizes (small, medium, and large).
  3. Observe the rendering of content in the Preview and Raw tabs at each size.
- **Expected results:** The content in both tabs should be responsive and displayed correctly regardless of screen size or resolution, and no overlapping or misalignment should be present.

### Test Case 7 - SENSELESS
- **Description:** Check for any security vulnerabilities by attempting to inject malicious scripts into the editor and viewing them in the Preview and Raw tabs.
- **Prerequisites:** The user should be logged into the README generator app.
- **Steps:**
  1. Navigate to the Editor page.
  2. Attempt to inject a simple script (e.g., `<script>alert('XSS')</script>`) into the editor.
  3. Switch to the Preview and Raw tabs and inspect the handling of the script.
- **Expected results:** The application should sanitize the input and prevent script execution. The Preview and Raw tabs should display the script as text without executing it.

### Test Case 8 - SENSELESS
- **Description:** Evaluate the stability of the application under prolonged use, focusing on the Preview and Raw tabs.
- **Prerequisites:** The user should be logged into the README generator app.
- **Steps:**
  1. Navigate to the Editor page.
  2. Continuously edit and save changes to various sections over a prolonged period (e.g., one hour).
  3. Regularly switch between the Preview and Raw tabs during this period.
- **Expected results:** The application should maintain stability and performance without crashes, lag, or errors. All changes should be reflected accurately in both tabs.

These exploratory test cases aim to cover a wide range of scenarios, focusing on the Preview and Raw tabs, to uncover potential bugs, failures, and security issues.


0 bugs
8 senseless