### Test Case 1 - BUG
- **Description:** Verify if the language selection functionality updates the interface text to the selected language.
- **Prerequisites:** The application is open in a web browser.
- **Steps:**
  1. Identify the language selection dropdown (icon with "A" and a language selection arrow).
  2. Click on the dropdown to display the list of available languages.
  3. Select a language (e.g., Français).
  4. Observe if the interface text changes to the selected language.
- **Expected Results:** The interface text is updated to Français immediately after selection.

### Test Case 2 - NONSENSICAL
- **Description:** Verify if the application properly handles non-supported languages.
- **Prerequisites:** The application is open in a web browser.
- **Steps:**
  1. Identify the language selection dropdown.
  2. Check the list of available languages.
  3. Attempt to select a language that is not in the dropdown list by providing a keyboard input or any available method.
- **Expected Results:** The application should not change the language, and an error message should be displayed if an unsupported language is selected.

### Test Case 3
- **Description:** Verify if the default language is set correctly and changes correctly when a new language is selected.
- **Prerequisites:** The application is open in a web browser for the first time.
- **Steps:**
  1. Open the application and note the default language (usually English).
  2. Change the language using the language selection dropdown to another language (e.g., Español).
  3. Change the language back to the default (English).
- **Expected Results:** The default language should be English when first opened, and switching between languages should correctly update the interface text each time the language is selected.

### Test Case 4
- **Description:** Verify the persistence of selected language across different sessions.
- **Prerequisites:** The application is open in a web browser.
- **Steps:**
  1. Open the application and select a different language using the language selection dropdown (e.g., Deutsch).
  2. Close the web browser.
  3. Reopen the web browser and navigate to the application.
- **Expected Results:** The selected language (Deutsch) should be retained and applied when the application is reopened.

### Test Case 5 - BUG
- **Description:** Verify if the language selection functionality works on different sections of the application.
- **Prerequisites:** The application is open in a web browser.
- **Steps:**
  1. Open the application and select a different language using the language selection dropdown (e.g., 中文简体).
  2. Navigate through different sections (e.g., Title and Description, Acknowledgements, API Reference).
  3. Observe if all sections display text in the selected language.
- **Expected Results:** All sections should reflect the text in the selected language (中文简体).

### Test Case 6
- **Description:** Verify the application's behavior when rapidly changing languages.
- **Prerequisites:** The application is open in a web browser.
- **Steps:**
  1. Open the application.
  2. Quickly change the language multiple times using the language selection dropdown (e.g., switch between Italiano, Türkçe, and Português within quick succession).
  3. Observe the interface text for any delays or inconsistency.
- **Expected Results:** The application should handle rapid language changes smoothly without any delays, crashes, or text inconsistencies.

### Test Case 7
- **Description:** Verify the appearance and functionality of the language dropdown on different screen sizes and resolutions.
- **Prerequisites:** The application is open in a web browser.
- **Steps:**
  1. Resize the browser window to different resolutions (e.g., desktop, tablet, mobile view).
  2. Open the language selection dropdown in each resolution.
  3. Attempt to select different languages in each resolution.
- **Expected Results:** The language selection dropdown should be fully functional and properly displayed across all screen sizes and resolutions.

### Test Case 8
- **Description:** Verify if the "Incorrect Translation?" link works as expected.
- **Prerequisites:** The application is open in a web browser and a language other than English is selected.
- **Steps:**
  1. Select a different language from the dropdown (e.g., Español).
  2. Click on the "Incorrect Translation?" link at the bottom of the language selection dropdown.
  3. Observe the action taken by the application.
- **Expected Results:** Clicking the "Incorrect Translation?" link should lead to a feedback form or a method to report incorrect translations.
