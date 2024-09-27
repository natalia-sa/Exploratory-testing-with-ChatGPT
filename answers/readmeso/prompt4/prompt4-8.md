# Secondary prompt 8

"
From the point of view of a tester, give me exploratory test cases to the Delete Section feature in the readme generator app, suggesting unusual flows, trying to find possible bugs, failures, security issues, etc. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test results
"

## Images

readme1.png, readme2.png

### Answer

Here are some exploratory test cases for the Deleting Sections feature in the README generator app:

### Test Case 1 
- **Description:** Attempt to delete a section that has not been modified.
- **Prerequisites:** Access to the README generator app with a default `Title and Description` section.
- **Steps:**
  1. Open the README generator app.
  2. Ensure the `Title and Description` section has not been modified.
  3. Click on the trash can icon next to the `Title and Description` section.
- **Expected results:** The `Title and Description` section is deleted without any warning or confirmation message.

### Test Case 2
- **Description:** Try to delete the last remaining section in the README.
- **Prerequisites:** Access to the README generator app with only one section present (e.g., `Title and Description`).
- **Steps:**
  1. Open the README generator app.
  2. Ensure that only the `Title and Description` section is present.
  3. Click on the trash can icon next to the `Title and Description` section.
- **Expected results:** The application should either not allow the last section to be deleted or prompt a warning message indicating that at least one section must be present.

### Test Case 3
- **Description:** Delete a section after switching the app language.
- **Prerequisites:** Access to the README generator app.
- **Steps:**
  1. Open the README generator app.
  2. Change the application language to a different language (e.g., Spanish).
  3. Ensure the `Title and Description` section is present.
  4. Click on the trash can icon next to the `Title and Description` section.
- **Expected results:** The section is deleted correctly, and all prompts or messages are displayed in the selected language.

### Test Case 4
- **Description:** Attempt to delete a custom-created section.
- **Prerequisites:** Access to the README generator app and a custom section created.
- **Steps:**
  1. Open the README generator app.
  2. Create a custom section by clicking on `+ Custom Section`.
  3. Ensure the custom section appears in the section list.
  4. Click on the trash can icon next to the custom section.
- **Expected results:** The custom section is deleted without any issues, and no residual data is left behind in the editor or preview.

### Test Case 5
- **Description:** Try to delete multiple sections sequentially.
- **Prerequisites:** Access to the README generator app with at least three sections (e.g., `Title and Description`, `Acknowledgements`, `API Reference`).
- **Steps:**
  1. Open the README generator app.
  2. Ensure at least three sections are present.
  3. Click on the trash can icon next to each section sequentially, starting with `Title and Description`.
- **Expected results:** Each section is deleted appropriately without impacting the remaining sections. The deletion order should not affect the app's behavior.

### Test Case 6
- **Description:** Attempt to delete a section while the editor is in dark mode.
- **Prerequisites:** Access to the README generator app with dark mode enabled.
- **Steps:**
  1. Open the README generator app.
  2. Switch the editor to dark mode.
  3. Ensure the `Title and Description` section is present.
  4. Click on the trash can icon next to the `Title and Description` section.
- **Expected results:** The section is deleted correctly while the app remains in dark mode, and there are no visual discrepancies.

### Test Case 7 - BUG Scrolls horizontally
- **Description:** Attempt to delete a section that contains a large amount of content.
- **Prerequisites:** Access to the README generator app with a section filled with a large amount of text.
- **Steps:**
  1. Open the README generator app.
  2. Fill the `Title and Description` section with a large amount of text (e.g., several paragraphs).
  3. Click on the trash can icon next to the `Title and Description` section.
- **Expected results:** The section is deleted correctly, and the application handles the deletion of large content without performance issues.

### Test Case 8 
- **Description:** Attempt to delete a section when the app is in an offline state.
- **Prerequisites:** Access to the README generator app and network disconnection.
- **Steps:**
  1. Open the README generator app.
  2. Disconnect the device from the internet.
  3. Ensure the `Title and Description` section is present.
  4. Click on the trash can icon next to the `Title and Description` section.
- **Expected results:** An appropriate error message is displayed indicating the app is offline, and the section is not deleted.

### Test Case 9
- **Description:** Attempt to delete a section without any confirmation prompt.
- **Prerequisites:** Access to the README generator app with a section added (default behavior).
- **Steps:**
  1. Open the README generator app.
  2. Ensure the `Title and Description` section is present.
  3. Click on the trash can icon next to the `Title and Description` section.
  4. Observe if any confirmation prompt appears before deletion.
- **Expected results:** The section should be deleted immediately without any confirmation prompt. If there is a prompt, the bug is identified.

### Test Case 10 -  SENSELESS
- **Description:** Attempt to delete a section while multiple sections are expanded.
- **Prerequisites:** Access to the README generator app with multiple sections expanded.
- **Steps:**
  1. Open the README generator app.
  2. Expand multiple sections (e.g., `Title and Description`, `Acknowledgements`, `API Reference`).
  3. Click on the trash can icon next to any expanded section.
- **Expected results:** The selected section is deleted without affecting the state (expanded/collapsed) of the other sections.

1 bug
1 senseless