### Test Case 1
- **Description:** Verify that the toggle between light and dark mode works correctly.
- **Prerequisites:** The ReadMe generator app is accessible.
- **Steps:**
  1. Open the ReadMe generator app.
  2. Locate the night mode toggle button at the top-right corner.
  3. Click on the toggle button to switch to dark mode.
  4. Observe the changes.
  5. Click again on the toggle button to switch to light mode.
  6. Observe the changes.
- **Expected results:** On clicking the toggle button:
  * In step 3, the app should change the theme to dark mode, with background and text colors adjusting accordingly.
  * In step 5, the app should revert to light mode with appropriate changes in colors.

### Test Case 2
- **Description:** Verify if the mode selected is persistent after reloading the page.
- **Prerequisites:** The ReadMe generator app is accessible.
- **Steps:**
  1. Open the ReadMe generator app.
  2. Toggle to dark mode.
  3. Refresh the page.
  4. Observe the current mode.
- **Expected results:** The app should retain the dark mode after reload.

### Test Case 3
- **Description:** Verify behavior after switching modes multiple times.
- **Prerequisites:** The ReadMe generator app is accessible.
- **Steps:**
  1. Open the ReadMe generator app.
  2. Toggle to dark mode.
  3. Toggle back to light mode.
  4. Repeat steps 2 and 3 multiple times (at least 10 times).
  5. Observe any visual or functional issues.
- **Expected results:** The application should switch themes correctly without any lag, glitches, or crashes.

### Test Case 4
- **Description:** Verify the functionality of elements within the dark and light modes.
- **Prerequisites:** The ReadMe generator app is accessible.
- **Steps:**
  1. Open the ReadMe generator app.
  2. Toggle to dark mode.
  3. Click on various sections (e.g., "Title and Description," "Acknowledgements").
  4. Toggle back to light mode.
  5. Click on various sections again.
- **Expected results:** Elements should be accessible and functional in both modes without any rendering issues.

### Test Case 5
- **Description:** Verify if mode switching impacts the editor content.
- **Prerequisites:** The ReadMe generator app is accessible.
- **Steps:**
  1. Open the ReadMe generator app.
  2. Enter some content in the editor area.
  3. Toggle to dark mode.
  4. Ensure the content in the editor is intact and visible.
  5. Toggle back to light mode.
  6. Ensure the content in the editor is still intact and visible.
- **Expected results:** The content in the editor should remain unchanged and visible after switching modes.

### Test Case 6
- **Description:** Verify mode switching on different screen resolutions.
- **Prerequisites:** The ReadMe generator app is accessible.
- **Steps:**
  1. Open the ReadMe generator app on different devices or using responsive mode in the browser (e.g., mobile, tablet, desktop).
  2. Toggle to dark mode.
  3. Observe the changes.
  4. Toggle back to light mode.
  5. Observe the changes.
- **Expected results:** The app should switch themes correctly without any layout issues on different screen resolutions.

### Test Case 7  
- **Description:** Verify mode switching behavior when changing the language.
- **Prerequisites:** The ReadMe generator app is accessible.
- **Steps:**
  1. Open the ReadMe generator app.
  2. Change the language from the dropdown menu.
  3. Toggle to dark mode.
  4. Toggle back to light mode.
  5. Change the language again.
  6. Repeat toggling between modes.
- **Expected results:** The app should support mode switching seamlessly even after changing the language without any functional or visual errors.
