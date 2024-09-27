## Prompt 6.5

“
From the point of view of a tester who will perform an exploratory testing session, give me test cases to the Section search functionality in the readme generator app. Please consider that to carry out these tests you only have access to the Linux operating system, and the Firefox and Chrome browsers. This app does not have a connection to any type of database and there are no user registration and login options. Consider potential edge cases, unusual flows and try to find possible bugs. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test result
”

## Images

readme1.png, readme2.png

## Answer

### Test Case 001
- **Description:** Verify that the section search functionality returns relevant results in both Firefox and Chrome.
- **Prerequisites:** The app is accessible via Firefox and Chrome on Linux.
- **Steps:**
  1. Open the Readme Generator app in Firefox.
  2. In the "Search for a section" input field, type a query (e.g., "API").
  3. Verify that relevant sections (like "API Reference") are shown in the search results.
  4. Repeat steps 1-3 in Chrome.
- **Expected Results:** The search results should display sections relevant to the query in both Firefox and Chrome.

---

### Test Case 002
- **Description:** Verify that the search results are updated in real-time as the user types.
- **Prerequisites:** The app is accessible via Firefox and Chrome on Linux.
- **Steps:**
  1. Open the Readme Generator app in Firefox.
  2. In the "Search for a section" input field, type a query slowly, one character at a time (e.g., start with "A", then "P", then "I").
  3. Observe the search results after each keystroke.
  4. Repeat steps 1-3 in Chrome.
- **Expected Results:** The search results should update in real-time after each keystroke, showing the most relevant sections.

---

### Test Case 003
- **Description:** Verify that searching for a non-existent section returns no results.
- **Prerequisites:** The app is accessible via Firefox and Chrome on Linux.
- **Steps:**
  1. Open the Readme Generator app in Firefox.
  2. In the "Search for a section" input field, type a query that is unlikely to match any section (e.g., "XYZ").
  3. Verify that no sections are shown as search results.
  4. Repeat steps 1-3 in Chrome.
- **Expected Results:** No sections should be shown in the search results for a non-existent query.

---

### Test Case 004
- **Description:** Verify the case sensitivity of the search functionality.
- **Prerequisites:** The app is accessible via Firefox and Chrome on Linux.
- **Steps:**
  1. Open the Readme Generator app in Firefox.
  2. In the "Search for a section" input field, type a section name in lowercase (e.g., "api reference").
  3. Verify the search results.
  4. Clear the input field and type the same section name in uppercase (e.g., "API REFERENCE").
  5. Verify the search results.
  6. Repeat steps 1-5 in Chrome.
- **Expected Results:** The search functionality should be case-insensitive, returning the same results for both uppercase and lowercase queries.

---

### Test Case 005
- **Description:** Verify search functionality with partial queries.
- **Prerequisites:** The app is accessible via Firefox and Chrome on Linux.
- **Steps:**
  1. Open the Readme Generator app in Firefox.
  2. In the "Search for a section" input field, type a partial query (e.g., "Aut" for "Authors").
  3. Verify that sections that partially match the query ("Authors", "Automatic", etc.) are shown in the results.
  4. Repeat steps 1-3 in Chrome.
- **Expected Results:** Sections partially matching the query should be displayed in the search results.

---

### Test Case 006
- **Description:** Verify the search functionality with an empty input field.
- **Prerequisites:** The app is accessible via Firefox and Chrome on Linux.
- **Steps:**
  1. Open the Readme Generator app in Firefox.
  2. In the "Search for a section" input field, ensure that it is empty.
  3. Verify that all available sections are listed.
  4. Repeat steps 1-3 in Chrome.
- **Expected Results:** All sections should be listed if the search input field is empty.

---

### Test Case 007
- **Description:** Verify that special characters in the search input do not break the functionality.
- **Prerequisites:** The app is accessible via Firefox and Chrome on Linux.
- **Steps:**
  1. Open the Readme Generator app in Firefox.
  2. In the "Search for a section" input field, type some special characters (e.g., "@#!$%").
  3. Verify that the app does not crash and handles the input gracefully.
  4. Repeat steps 1-3 in Chrome.
- **Expected Results:** The app should not crash, and special characters should not break the search functionality.

---

### Test Case 008
- **Description:** Verify that the search input field can handle a very long string of characters.
- **Prerequisites:** The app is accessible via Firefox and Chrome on Linux.
- **Steps:**
  1. Open the Readme Generator app in Firefox.
  2. In the "Search for a section" input field, type a very long string of characters (e.g., 500+ characters).
  3. Verify that the app does not crash and handles the input gracefully.
  4. Repeat steps 1-3 in Chrome.
- **Expected Results:** The app should not crash, and the search functionality should handle long inputs gracefully.

---

### Test Case 009
- **Description:** Verify that the search box is focused correctly when clicked.
- **Prerequisites:** The app is accessible via Firefox and Chrome on Linux.
- **Steps:**
  1. Open the Readme Generator app in Firefox.
  2. Click on the "Search for a section" input field.
  3. Ensure the cursor is visible and the field is ready for input.
  4. Repeat steps 1-3 in Chrome.
- **Expected Results:** Clicking on the search box should place the cursor inside the input field and be ready to accept input.

---

### Test Case 010
- **Description:** Verify the behavior of the search functionality when switching languages.
- **Prerequisites:** The app is accessible via Firefox and Chrome on Linux, and supports multiple languages.
- **Steps:**
  1. Open the Readme Generator app in Firefox and select a different language (e.g., Spanish).
  2. In the "Search for a section" input field, type a query relevant to the selected language (e.g., "API" for "Español").
  3. Verify that relevant sections are shown in the search results.
  4. Repeat steps 1-3 in Chrome.
- **Expected Results:** The search functionality should return relevant sections even when the app is in a language other than English.

0 bugs
0 senseless
