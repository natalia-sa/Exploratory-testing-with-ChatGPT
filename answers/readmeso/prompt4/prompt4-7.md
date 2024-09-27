# Secondary prompt 7

"
From the point of view of a tester, give me exploratory test cases to the Editing Sections feature in the readme generator app, suggesting unusual flows, trying to find possible bugs, failures, security issues, etc. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test results
"

## Images

readme1.png, readme2.png

### Answer

Here are some exploratory test cases for the Editing Sections feature in the README generator app:

### Test Case 1 BUG (Dark mode button dissapear)
#### Description:
Test adding multiple sections one after another without saving in between and then deleting them all.
#### Prerequisites:
The app should be launched, and the user should be on the README editor page.
#### Steps:
1. Click on the "Acknowledgements" section to add it to the README.
2. Click on the "API Reference" section to add it to the README.
3. Click on the "Appendix" section to add it to the README.
4. Without saving, delete the "Acknowledgements" section.
5. Delete the "API Reference" section.
6. Delete the "Appendix" section.
#### Expected Results:
All sections should be added and then removed successfully without any error messages, and the editor should remain in a stable state.

### Test Case 2
#### Description:
Test for special characters and HTML tags within section titles and content.
#### Prerequisites:
The app should be launched, and the user should be on the README editor page.
#### Steps:
1. Click on the "Custom Section" button.
2. Enter special characters and HTML tags (e.g., `<script>`, `&`, `<>`).
3. Add some content with the special characters within the custom section.
#### Expected Results:
The app should properly display the special characters and HTML tags as plain text without executing them or causing layout issues.

### Test Case 3
#### Description:
Test the stability of the editor by rapidly adding and removing sections.
#### Prerequisites:
The app should be launched, and the user should be on the README editor page.
#### Steps:
1. Rapidly click to add and remove different sections (e.g., "Authors", "Badges", "Deployment") for about 2 minutes.
#### Expected Results:
The app should function correctly without crashing or showing significant lag. The editor should remain responsive throughout the test.

### Test Case 4 - BUG (start editing in english than change to portuguese)
#### Description:
Test the language switch functionality while editing a section.
#### Prerequisites:
The app should be launched, and the user should be on the README editor page.
#### Steps:
1. Start editing the "Title and Description" section.
2. Midway through editing, switch the language from English to another language (e.g., French).
3. Continue editing in the new language.
#### Expected Results:
The app should correctly switch languages without losing any entered data. The editor should reflect the change in language seamlessly.

### Test Case 5 - SENSELESS
#### Description:
Test editing a section with very large text inputs.
#### Prerequisites:
The app should be launched, and the user should be on the README editor page.
#### Steps:
1. Click on the "Title and Description" section to edit it.
2. Enter a very long project description (e.g., several paragraphs or multiple pages of text).
3. Save the section.
#### Expected Results:
The app should handle the large input without slowing down significantly, crashing, or cutting off the text. The full input should be saved and displayed correctly in the preview.

### Test Case 6 - SENSELESS
#### Description:
Test for potential cross-site scripting (XSS) vulnerabilities.
#### Prerequisites:
The app should be launched, and the user should be on the README editor page.
#### Steps:
1. Click on the "Title and Description" section to edit it.
2. Enter a script tag with JavaScript code (e.g., `<script>alert('XSS')</script>`).
3. Save the section.
#### Expected Results:
The JavaScript code should be sanitized and not executed. The text `<script>alert('XSS')</script>` should appear as plain text in the preview.

### Test Case 7
#### Description:
Test the "Reset" functionality after making numerous changes.
#### Prerequisites:
The app should be launched, and the user should be on the README editor page.
#### Steps:
1. Add several sections and make significant edits to each section.
2. Click the "Reset" button to reset all changes.
3. Confirm reset if prompted.
#### Expected Results:
All sections and edits should be removed, and the README should return to its initial state. No residue of changes should remain.

### Test Case 8 - BUG (general problems)
#### Description:
Test the functionality under different screen resolutions and aspect ratios.
#### Prerequisites:
The app should be launched.
#### Steps:
1. Resize the browser to various resolutions and aspect ratios (e.g., mobile, tablet, and desktop sizes).
2. Ensure each of the sections is editable and behaves as expected at each resolution.
#### Expected Results:
The app should be responsive to different screen resolutions, and all controls should remain usable. There should not be any layout issues or elements that become inaccessible.

These test cases aim to ensure the reliability of the Editing Sections feature under various conditions.

3 bugs
2 senseless
