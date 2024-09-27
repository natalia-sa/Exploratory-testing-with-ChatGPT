# Secondary prompt 12

"
From the point of view of a tester, give me exploratory test cases to the Day/Night Mode Toggle feature in the readme generator app, suggesting unusual flows, trying to find possible bugs, failures, security issues, etc. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test results
"

## Images

readme1.png, readme2.png, readme4.png

### Answer

1. **Test Number:** E01
   - **Description:** Toggling the Day/Night Mode multiple times rapidly.
   - **Prerequisites:** App is loaded and the Toggle button is visible.
   - **Steps:**
     1. Load the app and ensure the Toggle button for Day/Night mode is visible.
     2. Click on the Toggle button rapidly (at least 10 times within 5 seconds).
   - **Expected Results:** The app should switch between Day and Night modes correctly without any lag, graphical glitches, or crashes.

2. **Test Number:** E02 - SENSELESS
   - **Description:** Toggling Day/Night Mode during different stages of editing the README.
   - **Prerequisites:** App is loaded, and a section is being edited.
   - **Steps:**
     1. Load the app and start editing a section.
     2. Change some text in the editor.
     3. Toggle between Day/Night modes while in the text editing state.
     4. Save the changes and verify the display.
   - **Expected Results:** The text content should remain unchanged, and the visual transition should be smooth. The current state of the editor should be preserved.

3. **Test Number:** E03
   - **Description:** Toggling Day/Night Mode with different languages selected.
   - **Prerequisites:** App is loaded, and the language dropdown is functional.
   - **Steps:**
     1. Load the app and select a different language, e.g., French.
     2. Toggle the Day/Night mode.
     3. Change the language to another, e.g., Spanish.
     4. Toggle the Day/Night mode again.
   - **Expected Results:** The app should correctly switch languages and modes seamlessly. The text should be perfectly readable in both Day and Night modes for all languages.

4. **Test Number:** E04
   - **Description:** Toggling Day/Night Mode while creating a large README file.
   - **Prerequisites:** App is loaded, and README sections are being added.
   - **Steps:**
     1. Load the app and start adding multiple sections to the README.
     2. Once several sections have been added, toggle between Day and Night modes.
   - **Expected Results:** The large document should display correctly in both Day and Night modes without any formatting issues or text overlap.

5. **Test Number:** E05
   - **Description:** Toggling Day/Night Mode during network fluctuations.
   - **Prerequisites:** App is loaded, and network monitoring tools are available.
   - **Steps:**
     1. Load the app and start creating or editing a README.
     2. While toggling between Day/Night modes, simulate network fluctuations (e.g., intermittent connectivity).
   - **Expected Results:** The app should handle network fluctuations gracefully, maintaining the selected mode without crashing or significant lag.

6. **Test Number:** E06
   - **Description:** Inspect the security of Day/Night Mode toggle (checking for any unexpected behavior or console errors).
   - **Prerequisites:** App is loaded, console, and debugging tools available.
   - **Steps:**
     1. Load the app and open the browser’s console.
     2. Toggle the Day/Night mode several times.
     3. Monitor the console for any errors or warnings.
   - **Expected Results:** There should be no console errors or warnings that indicate vulnerabilities or issues in the toggle functionality.

7. **Test Number:** E07
   - **Description:** Toggling Day/Night Mode after clearing browser cache.
   - **Prerequisites:** App is loaded, and browser cache can be cleared.
   - **Steps:**
     1. Load the app and toggle the Day/Night mode to ensure functionality.
     2. Clear the browser cache.
     3. Reload the app and try toggling the Day/Night mode again.
   - **Expected Results:** The toggle should work correctly even after the cache is cleared, with no loss of settings or rendering issues.

8. **Test Number:** E08
   - **Description:** Inspect Day/Night Mode behavior with assistive technologies.
   - **Prerequisites:** App is loaded, and assistive technologies (e.g., screen readers) are set up.
   - **Steps:**
     1. Load the app and activate assistive technologies.
     2. Toggle the Day/Night mode and observe the behavior.
   - **Expected Results:** The app should seamlessly switch between modes and remain fully accessible with assistive technologies, narrating the correct state and remaining operable.

9. **Test Number:** E09
   - **Description:** Toggling the Day/Night Mode on different devices (e.g., desktop, tablet, mobile).
   - **Prerequisites:** App is accessible on various device types.
   - **Steps:**
     1. Load the app on a desktop and toggle the Day/Night mode.
     2. Load the app on a tablet and toggle the Day/Night mode.
     3. Load the app on a mobile device and toggle the Day/Night mode.
   - **Expected Results:** The toggle should work seamlessly across all devices, maintaining a consistent and responsive layout suitable for each device type.

10. **Test Number:** E010
    - **Description:** Toggling Day/Night Mode after forcibly interrupting the session (e.g., closing browser/tab suddenly while toggling).
    - **Prerequisites:** App is loaded, and the browser session can be interrupted.
    - **Steps:**
      1. Load the app and toggle the Day/Night mode.
      2. During the toggling, suddenly close the browser or tab.
      3. Reopen the browser/tab and reload the app.
    - **Expected Results:** The app should resume without issues, and the last selected mode should be correctly retained and applied.


    0 bugs
    1 senseless