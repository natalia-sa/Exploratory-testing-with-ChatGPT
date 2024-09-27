## Prompt 5.11

“
From the point of view of a tester who will perform an exploratory testing session, give me test cases to the Toggle between light and dark modes in the readme generator app. This app does not have a connection to any type of database and there are no user registration and login options. Consider potential edge cases, unusual flows and try to find possible bugs. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test results
”

## Images

readme1.png, readme2.png, readme4.png

## Answer

### Test Case 1
- **Description:** Verify that the app correctly toggles between light and dark modes.
- **Prerequisites:** The app should be opened and displaying in light mode initially.
- **Steps:**
  1. Open the README generator app.
  2. Locate the toggle button for switching between light and dark modes.
  3. Click the toggle button to switch to dark mode.
  4. Observe the changes in the app’s color scheme.
  5. Click the toggle button again to switch back to light mode.
- **Expected Results:**
  1. After clicking the toggle button, the app should switch to dark mode with appropriate color changes in the background, text, and editor sections.
  2. After clicking the toggle button again, the app should switch back to light mode with appropriate color adjustments.

---

### Test Case 2
- **Description:** Verify that the toggle button reflects the current state (light or dark mode).
- **Prerequisites:** The app should be opened.
- **Steps:**
  1. Open the README generator app.
  2. Observe the icon or design of the toggle button (e.g., a sun icon for light mode, moon icon for dark mode).
  3. Click the toggle button to switch to dark mode.
  4. Observe the icon or design of the toggle button.
  5. Click the toggle button again to switch back to light mode.
  6. Observe the icon or design of the toggle button.
- **Expected Results:**
  1. The toggle button should initially show the sun icon, indicating light mode.
  2. After switching to dark mode, the toggle button should change to the moon icon.
  3. After switching back to light mode, the toggle button should revert to the sun icon.

---

### Test Case 3
- **Description:** Verify the persistence of the theme toggle between sessions.
- **Prerequisites:** The app should be opened.
- **Steps:**
  1. Open the README generator app.
  2. Switch the app to dark mode.
  3. Close the browser or tab.
  4. Reopen the README generator app.
  5. Observe the color scheme of the app.
- **Expected Results:**
  1. The app should reopen in the dark mode.
  2. The color scheme and theme should persist between sessions.

---

### Test Case 4
- **Description:** Verify the visibility and functionality of different UI elements in dark mode.
- **Prerequisites:** The app should be opened.
- **Steps:**
  1. Open the README generator app in light mode.
  2. Locate all key UI elements, including buttons, text fields, dropdown menus, etc.
  3. Switch to dark mode.
  4. Observe the visibility and functionality of all UI elements again.
- **Expected Results:**
  1. All UI elements should be clearly visible and functional in dark mode without any overlapping or disappearing.

---

### Test Case 5
- **Description:** Check for any screen flickering or lag while toggling between modes.
- **Prerequisites:** The app should be opened.
- **Steps:**
  1. Open the README generator app.
  2. Click the toggle button multiple times in quick succession to switch between light and dark modes.
- **Expected Results:**
  1. The app should toggle modes smoothly without any screen flickering or noticeable lag.

---

### Test Case 6
- **Description:** Verify text readability in dark mode.
- **Prerequisites:** The app should be opened in light mode.
- **Steps:**
  1. Open the README generator app.
  2. Switch to dark mode.
  3. Observe the readability of the text in different sections.
  4. Enter some sample text in the editor section and preview it in both modes.
- **Expected Results:**
  1. All text should be easily readable in dark mode.
  2. Text in the editor section should contrast well with the background in both modes.

---

### Test Case 7 - BUG (responsiveness issues)
- **Description:** Validate the theme behavior in different screen resolutions and sizes.
- **Prerequisites:** The app should be opened.
- **Steps:**
  1. Open the README generator app in a desktop browser.
  2. Switch to dark mode.
  3. Resize the browser window to various resolutions (e.g., mobile, tablet, desktop).
  4. Observe the app's appearance and functionality at each resolution in dark mode.
- **Expected Results:**
  1. The dark mode should be consistently applied across all screen sizes.
  2. No elements should be misaligned or distorted when resizing the window.

---

### Test Case 8
- **Description:** Verify the state of the theme toggle after a browser refresh.
- **Prerequisites:** The app should be opened in light mode.
- **Steps:**
  1. Open the README generator app.
  2. Switch to dark mode.
  3. Refresh the browser page.
- **Expected Results:**
  1. The app should maintain the dark mode state after the page refresh.

---

### Test Case 9
- **Description:** Verify that the theme toggle works correctly immediately after page load.
- **Prerequisites:** The app should be opened in light mode.
- **Steps:**
  1. Open the README generator app.
  2. As soon as the page loads, click the toggle button to switch to dark mode.
- **Expected Results:**
  1. The app should immediately switch to dark mode without any delay or errors.


  1 bugs
  0 senseless
