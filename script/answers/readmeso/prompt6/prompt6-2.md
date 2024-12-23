## Prompt 6.2

“
From the point of view of a tester who will perform an exploratory testing session, give me test cases to the Get Started button functionality in the readme generator app. Please consider that to carry out these tests you only have access to the Linux operating system, and the Firefox and Chrome browsers. This app does not have a connection to any type of database and there are no user registration and login options. Consider potential edge cases, unusual flows and try to find possible bugs. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test result
”

## Images

readme1.png, readme2.png

## Answer

### Test Case 1 - BUG COFFE button disappear
- **Description**: Verify if the "Get Started" button leads to the editor page.
- **Prerequisites**: Access to readme.so in a Linux environment using Firefox or Chrome.
- **Steps**:
  1. Open the browser (Firefox or Chrome) and navigate to `https://readme.so`.
  2. Click the "Get Started" button.
- **Expected Results**: The application should navigate to the editor page with URL `https://readme.so/editor`.

---

### Test Case 2
- **Description**: Verify if the "Get Started" button works correctly in different screen resolutions.
- **Prerequisites**: Access to readme.so in a Linux environment using Firefox or Chrome.
- **Steps**:
  1. Open the browser (Firefox or Chrome) and navigate to `https://readme.so`.
  2. Resize the browser window to different screen resolutions (e.g., 1024x768, 1280x720, 1920x1080).
  3. Click the "Get Started" button in each resolution.
- **Expected Results**: The application should navigate to the editor page correctly in all screen resolutions.

---

### Test Case 3
- **Description**: Verify the response of the "Get Started" button when the application is opened in multiple tabs and one tab has an ongoing operation.
- **Prerequisites**: Access to readme.so in a Linux environment using Firefox or Chrome.
- **Steps**:
  1. Open the browser (Firefox or Chrome) and navigate to `https://readme.so`.
  2. Open a new tab and navigate to `https://readme.so`.
  3. In the first tab, perform an ongoing operation (e.g., customize README sections).
  4. While the operation is ongoing, click the "Get Started" button in the second tab.
- **Expected Results**: The application should navigate to the editor page in the second tab without affecting the ongoing operation in the first tab.

---

### Test Case 4
- **Description**: Verify behavior when the "Get Started" button is clicked multiple times quickly.
- **Prerequisites**: Access to readme.so in a Linux environment using Firefox or Chrome.
- **Steps**:
  1. Open the browser (Firefox or Chrome) and navigate to `https://readme.so`.
  2. Click the "Get Started" button multiple times quickly.
- **Expected Results**: The application should only navigate to the editor page once, ignoring multiple clicks.

---

### Test Case 5 
- **Description**: Verify if the "Get Started" button is functional with JavaScript disabled.
- **Prerequisites**: Access to readme.so in a Linux environment using Firefox or Chrome. JavaScript disabled in the browser settings.
- **Steps**:
  1. Open the browser (Firefox or Chrome) and navigate to `https://readme.so`.
  2. Disable JavaScript in the browser settings.
  3. Refresh the page.
  4. Click the "Get Started" button.
- **Expected Results**: The "Get Started" button should be non-functional, and the user should remain on the same page.

---

### Test Case 6
- **Description**: Verify if the "Get Started" button works correctly with different language settings.
- **Prerequisites**: Access to readme.so in a Linux environment using Firefox or Chrome.
- **Steps**:
  1. Open the browser (Firefox or Chrome) and navigate to `https://readme.so`.
  2. Change the language settings using the language selection dropdown.
  3. Click the "Get Started" button.
- **Expected Results**: The application should navigate to the editor page correctly regardless of the selected language.

---

### Test Case 7 
- **Description**: Verify the tooltip or hover text of the "Get Started" button.
- **Prerequisites**: Access to readme.so in a Linux environment using Firefox or Chrome.
- **Steps**:
  1. Open the browser (Firefox or Chrome) and navigate to `https://readme.so`.
  2. Hover the mouse over the "Get Started" button and observe any tooltip or hover text that appears.
- **Expected Results**: A tooltip with a relevant message should appear on hovering over the "Get Started" button.

---

### Test Case 8 SENSELESS
- **Description**: Verify the appearance and functionality of the "Get Started" button in different themes (if applicable).
- **Prerequisites**: Access to readme.so in a Linux environment using Firefox or Chrome.
- **Steps**:
  1. Open the browser (Firefox or Chrome) and navigate to `https://readme.so`.
  2. Change the theme (if available) from light to dark mode or vice versa.
  3. Observe the appearance of the "Get Started" button in the different themes.
  4. Click the "Get Started" button in each theme.
- **Expected Results**: The "Get Started" button should appear correctly and function as expected in each theme.

---

### Test Case 9
- **Description**: Verify the behavior of the "Get Started" button with browser zoom levels.
- **Prerequisites**: Access to readme.so in a Linux environment using Firefox or Chrome.
- **Steps**:
  1. Open the browser (Firefox or Chrome) and navigate to `https://readme.so`.
  2. Change the browser zoom level (e.g., 50%, 100%, 150%).
  3. Click the "Get Started" button at each zoom level.
- **Expected Results**: The application should navigate to the editor page correctly at each zoom level.

---

### Test Case 10
- **Description**: Verify the keyboard accessibility of the "Get Started" button.
- **Prerequisites**: Access to readme.so in a Linux environment using Firefox or Chrome.
- **Steps**:
  1. Open the browser (Firefox or Chrome) and navigate to `https://readme.so`.
  2. Use the "Tab" key to navigate to the "Get Started" button.
  3. Press the "Enter" key or "Spacebar" to activate the button.
- **Expected Results**: The application should navigate to the editor page when the button is activated using the keyboard.

1 senseless
1 bugs
