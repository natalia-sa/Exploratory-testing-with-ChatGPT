## Prompt 6.13

“
From the point of view of a tester who will perform an exploratory testing session, give me test cases to the "Buy me a coffee" functionality (support feature) in the readme generator app. Please consider that to carry out these tests you only have access to the Linux operating system, and the Firefox and Chrome browsers. This app does not have a connection to any type of database and there are no user registration and login options. Consider potential edge cases, unusual flows and try to find possible bugs. I will provide screenshots of the app GUI. The test cases should follow the structure below:

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
- **Description**: Verify that the "Buy me a coffee" window opens correctly when the coffee cup icon is clicked.
- **Prerequisites**: The user should be on the main editor screen of the app.
- **Steps**:
  1. Launch the readme generator app in Firefox or Chrome on a Linux system.
  2. Navigate to the main editor screen.
  3. Click on the coffee cup icon in the bottom right corner of the screen.
- **Expected results**: The "Buy me a coffee" window should appear with options to purchase coffee, enter a name/social handle, leave a comment, and a button to support.

### Test Case 2
- **Description**: Verify that the user can enter text in the name/social handle and comment fields in the "Buy me a coffee" window.
- **Prerequisites**: The "Buy me a coffee" window should be open.
- **Steps**:
  1. Click on the name/social handle field in the "Buy me a coffee" window.
  2. Enter a valid name or social handle.
  3. Click on the comment field.
  4. Enter a comment.
- **Expected results**: Text should be entered and displayed correctly in both fields without any issues.

### Test Case 3
- **Description**: Verify the functionality of the coffee quantity selection buttons.
- **Prerequisites**: The "Buy me a coffee" window should be open.
- **Steps**:
  1. Observe the default coffee quantity (which is 1).
  2. Click on the coffee quantity buttons (1, 3, 5, 10) one by one.
- **Expected results**: The coffee quantity should change according to the button clicked. The corresponding support amount should update as well.

### Test Case 4
- **Description**: Verify the proper functioning of the "Support" button.
- **Prerequisites**: The "Buy me a coffee" window should be open, and text should be entered into the name/social handle and comment fields.
- **Steps**:
  1. Select a coffee quantity.
  2. Enter a name/social handle and a comment.
  3. Click the "Support" button.
- **Expected results**: A confirmation should be displayed, and the purchase should be recorded in the recent supporters list.

### Test Case 5
- **Description**: Verify the behavior when no name/social handle or comment is entered.
- **Prerequisites**: The "Buy me a coffee" window should be open.
- **Steps**:
  1. Select a coffee quantity.
  2. Leave the name/social handle and comment fields empty.
  3. Click the "Support" button.
- **Expected results**: The application should handle missing information gracefully, either by displaying an error message or by proceeding with the support action without any issues.

### Test Case 6
- **Description**: Verify the behavior for unsupported or special characters in the name/social handle and comment fields.
- **Prerequisites**: The "Buy me a coffee" window should be open.
- **Steps**:
  1. Enter unsupported or special characters (such as emojis, symbols) in the name/social handle and comment fields.
  2. Click the "Support" button.
- **Expected results**: The application should either allow the input without errors or display appropriate validation messages.

### Test Case 7
- **Description**: Verify that the recent supporters are correctly displayed in the "Buy me a coffee" window.
- **Prerequisites**: There should be some existing supporters.
- **Steps**:
  1. Open the "Buy me a coffee" window.
  2. Observe the recent supporters list.
- **Expected results**: The recent supporters list should display names and comments from the most recent supporters, if any.

### Test Case 8
- **Description**: Verify the responsiveness of the "Buy me a coffee" window on different screen sizes.
- **Prerequisites**: The "Buy me a coffee" window should be open.
- **Steps**:
  1. Change the size of the browser window to various resolutions.
  2. Observe the elements within the "Buy me a coffee" window.
- **Expected results**: The window and its elements should resize appropriately without any layout issues or content overlapping.

### Test Case 9
- **Description**: Verify the functionality of the "Buy me a coffee" window when accessed through different languages in the app.
- **Prerequisites**: The app should support multiple languages.
- **Steps**:
  1. Change the app language using the language selection dropdown.
  2. Open the "Buy me a coffee" window.
- **Expected results**: The "Buy me a coffee" window should display correctly formatted text in the selected language without any issues.

### Test Case 10
- **Description**: Verify the handling of network issues during the support process.
- **Prerequisites**: The "Buy me a coffee" window should be open.
- **Steps**:
  1. Open the developer tools in Firefox or Chrome (F12).
  2. Go to the network tab and simulate a network outage.
  3. Try to complete the support process by clicking the "Support" button.
- **Expected results**: The application should display an appropriate error message indicating network issues.

0 senseless
0 bugs
