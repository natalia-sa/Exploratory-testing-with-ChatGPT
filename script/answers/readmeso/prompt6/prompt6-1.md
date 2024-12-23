## Prompt 6.1

“
From the point of view of a tester who will perform an exploratory testing session, give me test cases to the Language selection functionality in the readme generator app. Please consider that to carry out these tests you only have access to the Linux operating system, and the Firefox and Chrome browsers. This app does not have a connection to any type of database and there are no user registration and login options. Consider potential edge cases, unusual flows and try to find possible bugs. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test result
”

## Images

readme1.png, readme2.png

## Answer

### Test Case 1
- **Description**: Verify the language is correctly changed when a different language is selected from the dropdown menu.
- **Prerequisites**: The application is launched on Firefox or Chrome browser on a Linux operating system.
- **Steps**:
    1. Open the readme generator app.
    2. Click on the language selection icon to open the dropdown menu.
    3. Select "Français" from the dropdown menu.
    4. Observe the language change on the interface.
- **Expected Results**: The interface language should change to French.

---

### Test Case 2
- **Description**: Verify the application remembers the selected language after refreshing the page.
- **Prerequisites**: The application is launched on Firefox or Chrome browser on a Linux operating system.
- **Steps**:
    1. Open the readme generator app.
    2. Select "Español" from the language dropdown menu.
    3. Refresh the browser tab.
    4. Observe the interface language after refreshing.
- **Expected Results**: The interface language should remain in Spanish after refreshing.

---

### Test Case 3 
- **Description**: Verify that switching between multiple languages in sequence updates the UI correctly.
- **Prerequisites**: The application is launched on Firefox or Chrome browser on a Linux operating system.
- **Steps**:
    1. Open the readme generator app.
    2. Select "Deutsch" from the language dropdown menu.
    3. Verify the UI language is changed to German.
    4. Open the language dropdown menu again and select "Русский".
    5. Verify the UI language is changed to Russian.
    6. Open the language dropdown menu again and select "Türkçe".
    7. Verify the UI language is changed to Turkish.
- **Expected Results**: The UI should correctly update to German, then Russian, and finally Turkish.

---

### Test Case 4
- **Description**: Verify behavior when selecting the same language multiple times in succession.
- **Prerequisites**: The application is launched on Firefox or Chrome browser on a Linux operating system.
- **Steps**:
    1. Open the readme generator app.
    2. Select "Italiano" from the language dropdown menu.
    3. Verify the UI language is changed to Italian.
    4. Select "Italiano" again from the dropdown menu.
    5. Observe the UI behavior.
- **Expected Results**: The UI should remain in Italian without any error or flicker.

---

### Test Case 5
- **Description**: Verify the application’s response to selecting the "Incorrect Translation?" link.
- **Prerequisites**: The application is launched on Firefox or Chrome browser on a Linux operating system.
- **Steps**:
    1. Open the readme generator app.
    2. Open the language dropdown menu and select any language.
    3. Click on the "Incorrect Translation?" link at the bottom of the dropdown menu.
    4. Observe what happens next.
- **Expected Results**: The application should navigate to a feedback/report page for translation issues or open an appropriate feedback dialog.

---

### Test Case 6
- **Description**: Verify the default language is English when no language is selected.
- **Prerequisites**: The application is launched on Firefox or Chrome browser on a Linux operating system for the first time or after clearing browser data.
- **Steps**:
    1. Open the readme generator app in a new browser profile or after clearing browser data.
    2. Observe the default language on the interface.
- **Expected Results**: The interface should display text in English by default.

---

### Test Case 7
- **Description**: Verify the compatibility of language selection functionality on both Firefox and Chrome browsers.
- **Prerequisites**: The application is launched on both Firefox and Chrome browsers on a Linux operating system.
- **Steps**:
    1. Open the readme generator app in Firefox.
    2. Select "Português" from the language dropdown menu.
    3. Verify the UI language is changed to Portuguese.
    4. Open the readme generator app in Chrome.
    5. Select "Bahasa Indonesia" from the language dropdown menu.
    6. Verify the UI language is changed to Indonesian.
- **Expected Results**: The language selection functionality should work correctly on both Firefox and Chrome browsers.

---

### Test Case 8 BUG (some languages do not have translation)
- **Description**: Verify the language selection does not affect the contents of the editor sections.
- **Prerequisites**: The application is launched on Firefox or Chrome browser on a Linux operating system.
- **Steps**:
    1. Open the readme generator app.
    2. Enter some content in the "Title and Description" section.
    3. Select "日本語" from the language dropdown menu.
    4. Verify if the content in the "Title and Description" section remains unchanged.
- **Expected Results**: The content entered in the editor sections should remain unchanged after changing the interface language.

---

### Test Case 9 BUG
- **Description**: Verify the language selection for right-to-left languages like Arabic.
- **Prerequisites**: The application is launched on Firefox or Chrome browser on a Linux operating system.
- **Steps**:
    1. Open the readme generator app.
    2. Select "عربى" from the language dropdown menu.
    3. Verify if the interface changes to right-to-left layout correctly.
- **Expected Results**: The interface should change to Arabic with a right-to-left layout.

---

### Test Case 10
- **Description**: Verify if the language dropdown menu is scrollable and accessible.
- **Prerequisites**: The application is launched on Firefox or Chrome browser on a Linux operating system. Ensure dropdown menu items exceed viewport height.
- **Steps**:
    1. Open the readme generator app.
    2. Click on the language selection icon to open the dropdown menu.
    3. Attempt to scroll through the list of languages.
- **Expected Results**: The dropdown menu should be scrollable, and all languages should be accessible for selection.

2 bugs
0 senseless
