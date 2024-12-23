# Secondary prompt 13

"
From the point of view of a tester, give me exploratory test cases to the Completion Modal feature in the readme generator app, suggesting unusual flows, trying to find possible bugs, failures, security issues, etc. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test results
"

## Images

readme1.png, readme7.png

### Answer

### Test Case 001
- **Description**: Verify the Completion Modal appears correctly upon generating a README.
- **Prerequisites**: The user should create a README with at least one section (e.g., Title and Description).
- **Steps**:
  1. Open the README generator app.
  2. Add the "Title and Description" section and fill in some text.
  3. Click on the "Download" button in the top right corner.
  4. Observe the appearance of the Completion Modal.
- **Expected results**: The Completion Modal should appear, showing a message that the README has been generated, with options to reach out on Twitter and to sponsor.

### Test Case 002 - SENSELESS
- **Description**: Verify the Completion Modal handles unsupported characters.
- **Prerequisites**: The user should create a README with unsupported characters in the sections.
- **Steps**:
  1. Open the README generator app.
  2. Add the "Title and Description" section and fill in the text with unsupported characters (e.g., emojis, special symbols).
  3. Click on the "Download" button.
  4. Observe the appearance and content of the Completion Modal.
- **Expected results**: The Completion Modal should appear without any display issues. The content with unsupported characters should appear correctly.

### Test Case 003
- **Description**: Verify the behavior of the Completion Modal when the user clicks the "Download" button rapidly.
- **Prerequisites**: The user should be on the editor page with a README ready to be generated.
- **Steps**:
  1. Open the README generator app.
  2. Add a few sections to the README document.
  3. Rapidly click the "Download" button multiple times.
  4. Observe the behavior of the Completion Modal.
- **Expected results**: The Completion Modal should appear only once despite multiple clicks, and the system should prevent multiple modal overlays.

### Test Case 004
- **Description**: Verify the behavior of the Completion Modal with a very large README.
- **Prerequisites**: The user should create a README that includes numerous sections (e.g., adding all available sections).
- **Steps**:
  1. Open the README generator app.
  2. Add all the available sections in the left panel and fill in each section.
  3. Click the "Download" button.
  4. Observe the appearance and content of the Completion Modal.
- **Expected results**: The Completion Modal should appear without performance issues. The modal should not delay, crash, or exhibit incorrect behavior due to the large README size.

### Test Case 005
- **Description**: Verify the Completion Modal's appearance and information in different languages.
- **Prerequisites**: The user should be on the main page of the README generator app.
- **Steps**:
  1. Open the README generator app and change the language using the dropdown menu.
  2. Change the language to a non-default language (e.g., Français).
  3. Add some sections to the README.
  4. Click the "Download" button.
  5. Observe the appearance and content of the Completion Modal.
- **Expected results**: The Completion Modal should appear in the chosen language, displaying the correct message and options. There should be no translation errors.

### Test Case 006
- **Description**: Verify the security aspect of the Completion Modal upon generating a README.
- **Prerequisites**: The user should be on the editor page and have a README prepared.
- **Steps**:
  1. Open the README generator app.
  2. Add several sections and fill them with random text.
  3. Check for any signs of XSS by entering scripts or special HTML tags in the sections.
  4. Click the "Download" button.
  5. Observe the Completion Modal and any elements within it for security breaches.
- **Expected results**: The Completion Modal should sanitize the input, preventing any scripts or HTML code from executing. The modal should appear normally without any injected content.

### Test Case 007
- **Description**: Verify the Completion Modal's responsiveness on different devices and screen sizes.
- **Prerequisites**: The user should use different devices (e.g., desktop, tablet, mobile phone).
- **Steps**:
  1. Open the README generator app on several devices with varying screen sizes.
  2. Add sections to the README and fill them.
  3. Click the "Download" button on each device.
  4. Observe the appearance and behavior of the Completion Modal.
- **Expected results**: The Completion Modal should be fully responsive, correctly displaying on all screen sizes and devices without layout issues.


1 senseless
0 bugs