## Prompt 6.14

“
From the point of view of a tester who will perform an exploratory testing session, give me test cases to the Readme generated confirmation modal in the readme generator app. Please consider that to carry out these tests you only have access to the Linux operating system, and the Firefox and Chrome browsers. This app does not have a connection to any type of database and there are no user registration and login options. Consider potential edge cases, unusual flows and try to find possible bugs. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test result
”

## Images

readme1.png, readme2.png

## Answer

### Test Case 01
- **Description**: Verify the confirmation modal is displayed after the README is generated.
- **Prerequisites**: Access the app on Linux with either Firefox or Chrome.
- **Steps**:
  1. Navigate to the README generator app.
  2. Customize a README by adding various sections.
  3. Click the "Download" button to generate the README.
- **Expected results**: The confirmation modal should appear immediately after the README is generated with the message "Readme Generated!"

### Test Case 02
- **Description**: Verify the confirmation modal is displayed correctly across different languages.
- **Prerequisites**: Access the app on Linux with either Firefox or Chrome. Ensure language settings can be changed.
- **Steps**:
  1. Navigate to the README generator app.
  2. Change the language of the app to different available options like French, Spanish, etc.
  3. Customize a README and click the "Download" button.
  4. Check if the confirmation modal appears and the message is properly translated.
- **Expected results**: The confirmation modal should appear with the message "Readme Generated!" correctly translated to the selected language.

### Test Case 03
- **Description**: Verify the download button triggers the confirmation modal without any sections added.
- **Prerequisites**: Access the app on Linux with either Firefox or Chrome.
- **Steps**:
  1. Navigate to the README generator app.
  2. Click the “Download” button without adding any sections to the README.
- **Expected results**: The confirmation modal should appear even if no sections were added, confirming the README is generated.

### Test Case 04
- **Description**: Verify that clicking the "Sponsor" button on the confirmation modal redirects to the appropriate sponsorship page.
- **Prerequisites**: Access the app on Linux with either Firefox or Chrome.
- **Steps**:
  1. Generate a README and make the confirmation modal appear.
  2. Click on the "Sponsor" button in the confirmation modal.
- **Expected results**: The page should redirect to the appropriate sponsorship page.

### Test Case 05
- **Description**: Verify the confirmation modal appearance when the window is resized.
- **Prerequisites**: Access the app on Linux with either Firefox or Chrome.
- **Steps**:
  1. Navigate to the README generator app.
  2. Resize the browser window to various dimensions (e.g., making it very narrow or very wide).
  3. Customize a README and click the "Download" button.
- **Expected results**: The confirmation modal should still appear correctly centered and fully visible regardless of window size.

### Test Case 06 
- **Description**: Verify the behavior of the confirmation modal under poor network conditions.
- **Prerequisites**: Access the app on Linux with either Firefox or Chrome. Use browser developer tools to simulate different network conditions.
- **Steps**:
  1. Navigate to the README generator app.
  2. Simulate a network condition with high latency or poor connectivity in the developer tools.
  3. Customize a README and click the "Download" button.
- **Expected results**: The confirmation modal should eventually appear once the network condition permits the download event, without freezing or causing errors.

### Test Case 07
- **Description**: Verify the modal’s accessibility features.
- **Prerequisites**: Access the app on Linux with either Firefox or Chrome.
- **Steps**:
  1. Navigate to the README generator app.
  2. Customize a README and click the "Download" button.
  3. Use screen readers to verify if the confirmation modal and its contents are properly read out.
- **Expected results**: The screen reader should correctly identify and read out the content of the confirmation modal, ensuring it's accessible.

### Test Case 08
- **Description**: Verify the modal display if multiple README generations are attempted in quick succession.
- **Prerequisites**: Access the app on Linux with either Firefox or Chrome.
- **Steps**:
  1. Navigate to the README generator app.
  2. Customize a README and click the "Download" button.
  3. Quickly, before dismissing the modal, try to generate another README.
- **Expected results**: The app should handle multiple README generation attempts gracefully, either by queuing them or displaying a suitable message. Only one modal should be displayed at any time.

0 senseless
0 bugs
