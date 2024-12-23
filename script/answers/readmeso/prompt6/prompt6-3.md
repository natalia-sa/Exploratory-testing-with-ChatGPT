## Prompt 6.3

“
From the point of view of a tester who will perform an exploratory testing session, give me test cases to the Sponsor button functionality in the readme generator app. Please consider that to carry out these tests you only have access to the Linux operating system, and the Firefox and Chrome browsers. This app does not have a connection to any type of database and there are no user registration and login options. Consider potential edge cases, unusual flows and try to find possible bugs. I will provide screenshots of the app GUI. The test cases should follow the structure below:

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
- **Description**: Verify that clicking the "Sponsor" button directs the user to the sponsorship page.
- **Prerequisites**: The Readme Generator app is open in Chrome or Firefox on a Linux system.
- **Steps**:
  1. Open the Readme Generator app in Chrome.
  2. Click on the "Sponsor" button located on the main page.
  3. Verify the page or tab it directs you to.
  4. Repeat steps 1-3 in Firefox.
- **Expected Results**: Upon clicking the "Sponsor" button, the user should be directed to the sponsorship page in both browsers.

---

### Test Case 2
- **Description**: Verify that the "Sponsor" button is clickable and changes state upon interacting.
- **Prerequisites**: The Readme Generator app is open in Chrome or Firefox on a Linux system.
- **Steps**:
  1. Open the Readme Generator app in Chrome.
  2. Hover over the "Sponsor" button and observe any visual changes.
  3. Click on the "Sponsor" button and observe any immediate feedback (e.g., color change, button press animation).
  4. Repeat steps 1-3 in Firefox.
- **Expected Results**: The "Sponsor" button should be clickable and exhibit visual feedback (such as a color change or button press animation) during interaction in both browsers.

---

### Test Case 3
- **Description**: Verify responsiveness of the "Sponsor" button in various screen sizes.
- **Prerequisites**: The Readme Generator app is open in Chrome or Firefox on a Linux system.
- **Steps**:
  1. Open the Readme Generator app in Chrome.
  2. Resize the browser window to different dimensions (mobile, tablet, desktop).
  3. Observe the position and usability of the "Sponsor" button.
  4. Click on the "Sponsor" button at each screen size.
  5. Repeat steps 1-4 in Firefox.
- **Expected Results**: The "Sponsor" button should be visible, properly aligned, and fully functional across all screen sizes in both browsers.

---

### Test Case 4
- **Description**: Verify that the "Sponsor" button is accessible via keyboard navigation.
- **Prerequisites**: The Readme Generator app is open in Chrome or Firefox on a Linux system.
- **Steps**:
  1. Open the Readme Generator app in Chrome.
  2. Use the `Tab` key to navigate to the "Sponsor" button.
  3. Use the `Enter` key to activate the "Sponsor" button.
  4. Repeat steps 1-3 in Firefox.
- **Expected Results**: The "Sponsor" button should be accessible via keyboard navigation and activate correctly with the `Enter` key in both browsers.

---

### Test Case 5
- **Description**: Verify the "Sponsor" button functionality when the network is offline.
- **Prerequisites**: The Readme Generator app is open in Chrome or Firefox on a Linux system.
- **Steps**:
  1. Open the Readme Generator app in Chrome.
  2. Disable the network connection (turn off Wi-Fi or unplug Ethernet cable).
  3. Click on the "Sponsor" button.
  4. Observe the application behavior or any error messages.
  5. Re-enable the network connection.
  6. Repeat steps 1-5 in Firefox.
- **Expected Results**: The "Sponsor" button should attempt to load the sponsorship page but display an appropriate error message (e.g., "No internet connection") when the network is offline in both browsers.

---

### Test Case 6 - SENSELESS
- **Description**: Verify the behavior of the "Sponsor" button with the browser's back and forward navigation.
- **Prerequisites**: The Readme Generator app is open in Chrome or Firefox on a Linux system.
- **Steps**:
  1. Open the Readme Generator app in Chrome.
  2. Click on the "Sponsor" button to navigate to the sponsorship page.
  3. Use the browser's back button to return to the Readme Generator app.
  4. Use the browser's forward button to navigate back to the sponsorship page.
  5. Repeat steps 1-4 in Firefox.
- **Expected Results**: Navigation using the browser's back and forward buttons should work seamlessly, taking the user back and forth between the Readme Generator app and the sponsorship page.

---

### Test Case 7 
- **Description**: Verify the behavior of the "Sponsor" button when the text is modified via browser developer tools.
- **Prerequisites**: The Readme Generator app is open in Chrome or Firefox on a Linux system.
- **Steps**:
  1. Open the Readme Generator app in Chrome.
  2. Open browser developer tools (usually by pressing `F12`).
  3. Modify the text of the "Sponsor" button to something else (e.g., "Support Us").
  4. Click the modified "Sponsor" button.
  5. Repeat steps 1-4 in Firefox.
- **Expected Results**: Modifying the button text should not affect the button's functionality, and it should still direct the user to the sponsorship page upon clicking.

Each test case aims to uncover any potential issues or edge cases that might affect the usability and functionality of the "Sponsor" button.

1 senseless
0 bugs

