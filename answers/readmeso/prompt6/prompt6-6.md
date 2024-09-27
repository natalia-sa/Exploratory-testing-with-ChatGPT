## Prompt 6.6

“
From the point of view of a tester who will perform an exploratory testing session, give me test cases to the Add custom section functionality in the readme generator app. Please consider that to carry out these tests you only have access to the Linux operating system, and the Firefox and Chrome browsers. This app does not have a connection to any type of database and there are no user registration and login options. Consider potential edge cases, unusual flows and try to find possible bugs. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test result
”

## Images

readme1.png, readme2.png, readme5.png

## Answer

### Test Case 01
- **Description:** Verify that a custom section can be successfully added with a valid title.
- **Prerequisites:** Browser (Firefox or Chrome) on a Linux machine.
- **Steps:**
  1. Open the app in Firefox or Chrome.
  2. Click the `Get Started` button.
  3. Click the `+ Custom Section` button on the left panel.
  4. Enter a valid section title (e.g., "Custom Section 1") in the input field.
  5. Click the `Add Section` button.
- **Expected Results:** The new custom section with the given title should appear in the sections list and be visible in the editor.

---

### Test Case 02 BUG (adds the previous section again)
- **Description:** Verify that attempting to add a custom section with an empty title is properly handled.
- **Prerequisites:** Browser (Firefox or Chrome) on a Linux machine.
- **Steps:**
  1. Open the app in Firefox or Chrome.
  2. Click the `Get Started` button.
  3. Click the `+ Custom Section` button on the left panel.
  4. Leave the section title input field empty.
  5. Click the `Add Section` button.
- **Expected Results:** The app should display an error message or otherwise prevent the section from being added without a title.

---

### Test Case 03
- **Description:** Verify that special characters can be used in the custom section title.
- **Prerequisites:** Browser (Firefox or Chrome) on a Linux machine.
- **Steps:**
  1. Open the app in Firefox or Chrome.
  2. Click the `Get Started` button.
  3. Click the `+ Custom Section` button on the left panel.
  4. Enter a section title with special characters (e.g., "!@#$%^&*()_+").
  5. Click the `Add Section` button.
- **Expected Results:** The custom section with special characters in its title should be added successfully and be visible in the editor.

---

### Test Case 04 
- **Description:** Verify that the custom section title field does not exceed the maximum character limit.
- **Prerequisites:** Browser (Firefox or Chrome) on a Linux machine.
- **Steps:**
  1. Open the app in Firefox or Chrome.
  2. Click the `Get Started` button.
  3. Click the `+ Custom Section` button on the left panel.
  4. Enter a section title with more than 100 characters.
  5. Click the `Add Section` button.
- **Expected Results:** The app should truncate the title to the maximum allowable length or display an error message indicating the title is too long.

---

### Test Case 05
- **Description:** Verify the behavior of the app when adding multiple custom sections.
- **Prerequisites:** Browser (Firefox or Chrome) on a Linux machine.
- **Steps:**
  1. Open the app in Firefox or Chrome.
  2. Click the `Get Started` button.
  3. Click the `+ Custom Section` button on the left panel multiple times (e.g., 5 times).
  4. Enter a unique title for each custom section.
  5. Click the `Add Section` button for each title.
- **Expected Results:** All added custom sections should appear in the sections list and be visible in the editor with their respective titles.

---

### Test Case 06
- **Description:** Verify that the application saves the custom section when the page is refreshed.
- **Prerequisites:** Browser (Firefox or Chrome) on a Linux machine.
- **Steps:**
  1. Open the app in Firefox or Chrome.
  2. Click the `Get Started` button.
  3. Click the `+ Custom Section` button on the left panel.
  4. Enter a valid section title (e.g., "Saved Section").
  5. Click the `Add Section` button.
  6. Refresh the page.
- **Expected Results:** The custom section should still be present in the sections list and visible in the editor after the page refresh.

---

### Test Case 07
- **Description:** Verify the visual representation of a custom section in the Preview and Raw tabs.
- **Prerequisites:** Browser (Firefox or Chrome) on a Linux machine.
- **Steps:**
  1. Open the app in Firefox or Chrome.
  2. Click the `Get Started` button.
  3. Click the `+ Custom Section` button on the left panel.
  4. Enter a valid section title (e.g., "Visual Test Section").
  5. Click the `Add Section` button.
  6. Click the `Preview` and `Raw` tabs.
- **Expected Results:** The custom section should be properly rendered in the `Preview` tab and correctly formatted in the `Raw` tab.

---

### Test Case 08 - bug
- **Description:** Verify the application’s behavior when adding a very long custom section title.
- **Prerequisites:** Browser (Firefox or Chrome) on a Linux machine.
- **Steps:**
  1. Open the app in Firefox or Chrome.
  2. Click the `Get Started` button.
  3. Click the `+ Custom Section` button on the left panel.
  4. Enter a very long custom section title with more than 200 characters.
  5. Click the `Add Section` button.
- **Expected Results:** The app should handle the long title gracefully, either by truncating it or displaying an error that indicates the title is too long.

2 bugs
0 senseless