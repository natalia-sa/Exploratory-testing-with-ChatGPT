## Prompt 5.1

“
From the point of view of a tester who will perform an exploratory testing session, give me test cases to the Language selection functionality in the readme generator app. This app does not have a connection to any type of database and there are no user registration and login options. Consider potential edge cases, unusual flows and try to find possible bugs. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test results
”

## Images

readme1.png, readme2.png

## Answer

Certainly! Here are some detailed test cases based on the screenshots you provided:

### Test Case 1 
- **Description:** Validate the default language is set to English.
- **Prerequisites:** The user must be on the main screen of the README generator app.
- **Steps:**
  1. Launch the README generator app.
  2. Observe the language of the text on the main screen.
- **Expected Results:** The default language of the text on the main screen should be English.

### Test Case 2
- **Description:** Verify the language selection to French.
- **Prerequisites:** The user must be on the main screen of the README generator app.
- **Steps:**
  1. Click on the language icon at the top right corner.
  2. Select "Français" from the dropdown menu.
  3. Observe the changes in the UI language.
- **Expected Results:** The UI language should change to French.

### Test Case 3 - BUG
- **Description:** Verify the language selection to an RTL (right-to-left) language, such as Arabic.
- **Prerequisites:** The user must be on the main screen of the README generator app.
- **Steps:**
  1. Click on the language icon at the top right corner.
  2. Select "Arabic" from the dropdown menu.
  3. Observe the changes in the UI language.
- **Expected Results:** The UI language should change to Arabic and the alignment of text should adapt to right-to-left.

### Test Case 4 
- **Description:** Validate that all provided languages are selectable and properly reflected in the UI.
- **Prerequisites:** The user must be on the main screen of the README generator app.
- **Steps:**
  1. Click on the language icon at the top right corner.
  2. Sequentially select each language from the dropdown list.
  3. For each selection, observe the changes in the UI language.
- **Expected Results:** Each selected language should be reflected in the UI correctly.

### Test Case 5
- **Description:** Check for language persistence after page refresh.
- **Prerequisites:** A different language (other than English) must be selected.
- **Steps:**
  1. Select any language from the dropdown menu (e.g., Español).
  2. Refresh the page using the browser's refresh button.
  3. Observe the language of the content after the refresh.
- **Expected Results:** The page should reload with the same selected language (Español).

### Test Case 6 (coffee button disappear)
- **Description:** Confirm reverting back to English from another language.
- **Prerequisites:** The user must have previously changed the language to any other than English.
- **Steps:**
  1. Click on the language icon at the top right corner.
  2. Select "English" from the dropdown menu.
  3. Observe the UI language after the change.
- **Expected Results:** The UI language should revert back to English.

### Test Case 7 
- **Description:** Validate the application's functionality remains the same after changing languages.
- **Prerequisites:** None.
- **Steps:**
  1. Change the language to any other than English.
  2. Interact with the application by adding and deleting sections, customizing the title, and downloading the README.
  3. Observe the usability and functionality of the app post-language change.
- **Expected Results:** The application's functionality should remain consistent and unaffected by the language change.

### Test Case 8
- **Description:** Test unusual and rapid language switching.
- **Prerequisites:** None.
- **Steps:**
  1. Click on the language icon at the top right corner.
  2. Rapidly switch between different languages multiple times.
  3. Observe the application’s behavior during and after the rapid switching.
- **Expected Results:** The application should handle rapid language changes smoothly without crashing or displaying broken UI.

### Test Case 9
- **Description:** Verify that 'Incorrect Translation?' link works and leads to the proper feedback mechanism.
- **Prerequisites:** None.
- **Steps:**
  1. Select any language from the dropdown menu.
  2. Click on the "Incorrect Translation?" link at the bottom of the dropdown menu.
  3. Observe the response after clicking the link.
- **Expected Results:** A feedback mechanism or form should appear for reporting incorrect translations.

### Test Case 10 BUG
- **Description:** Check for broken or missing translations in sections and components.
- **Prerequisites:** The user must be on the main screen of the README generator app.
- **Steps:**
  1. Select any language from the dropdown menu.
  2. Navigate through different sections and components of the application (e.g., Title and Description, Acknowledgements, API Reference).
  3. Observe text elements to check for broken or missing translations.
- **Expected Results:** All text elements should be correctly translated without any missing or broken translations.

These test cases should help ensure the robustness of the language selection functionality in the README generator app.

3 bugs
0 senseless