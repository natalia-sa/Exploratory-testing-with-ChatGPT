## Prompt 5.13

“
From the point of view of a tester who will perform an exploratory testing session, give me test cases to the "Buy me a coffee" functionality (support feature) in the readme generator app. This app does not have a connection to any type of database and there are no user registration and login options. Consider potential edge cases, unusual flows and try to find possible bugs. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test results
”

## Images

readme1.png, readme2.png, readme6.png

## Answer

### Test Case 1
- **Description:** Verify that the "Buy me a coffee" button is clickable and opens the payment modal.
- **Prerequisites:** Access to the README generator app's main page.
- **Steps:**
  1. Navigate to the README generator main page.
  2. Locate the "Buy me a coffee" button in the bottom right corner.
  3. Click on the "Buy me a coffee" button.
- **Expected Results:** 
  - The "Buy me a coffee" modal should open when the button is clicked.

---

### Test Case 2
- **Description:** Test the functionality to support with the default coffee count.
- **Prerequisites:** The payment modal is open.
- **Steps:**
  1. Open the payment modal by clicking the "Buy me a coffee" button.
  2. Ensure the default option of 1 coffee is selected.
  3. Click on the "Support $5" button.
- **Expected Results:** 
  - Users should be redirected to the payment process for supporting with 1 coffee ($5).

---

### Test Case 3
- **Description:** Test the functionality to support with a custom coffee count.
- **Prerequisites:** The payment modal is open.
- **Steps:**
  1. Open the payment modal by clicking the "Buy me a coffee" button.
  2. Select a different coffee count (for example, 5 coffees).
  3. Click on the "Support $25" button.
- **Expected Results:** 
  - Users should be redirected to the payment process for supporting with 5 coffees ($25).

---

### Test Case 4
- **Description:** Validate the "name or @yoursocial" field.
- **Prerequisites:** The payment modal is open.
- **Steps:**
  1. Open the payment modal by clicking the "Buy me a coffee" button.
  2. Leave the "name or @yoursocial" field empty.
  3. Click the "Support" button.
  4. Enter a name in the field and click "Support" again.
- **Expected Results:** 
  - The transaction should proceed even if the "name or @yoursocial" field is left empty.
  - If a name is provided, it should be displayed in the recent supporters section upon successful transaction.

---

### Test Case 5
- **Description:** Validate the "Say something nice..." field.
- **Prerequisites:** The payment modal is open.
- **Steps:**
  1. Open the payment modal by clicking the "Buy me a coffee" button.
  2. Leave the "Say something nice..." field empty.
  3. Click the "Support" button.
  4. Enter a message in the field and click "Support" again.
- **Expected Results:** 
  - The transaction should proceed even if the "Say something nice..." field is left empty.
  - If a message is provided, it should be displayed in the recent supporters section upon successful transaction.

---

### Test Case 6
- **Description:** Ensure the "Recent Supporters" section updates correctly.
- **Prerequisites:** At least one completed transaction.
- **Steps:**
  1. Complete a transaction with a name and a message.
  2. Observe the "Recent Supporters" section in the payment modal.
- **Expected Results:** 
  - The transaction details should appear in the "Recent Supporters" section with the provided name and message.

---

### Test Case 7
- **Description:** Check the functionality of the payment modal close button.
- **Prerequisites:** The payment modal is open.
- **Steps:**
  1. Open the payment modal by clicking the "Buy me a coffee" button.
  2. Click the close (X) button on the modal.
- **Expected Results:** 
  - The payment modal should close, returning to the main interface.

---

### Test Case 8
- **Description:** Test the "Buy me a coffee" button behavior in different languages.
- **Prerequisites:** The app's language set to different options.
- **Steps:**
  1. Change the app's language using the language selector on the homepage.
  2. Click the "Buy me a coffee" button in each language setting.
- **Expected Results:** 
  - The "Buy me a coffee" button and modal should function correctly regardless of the selected language.

---

### Test Case 9
- **Description:** Verify the integration with the payment processor.
- **Prerequisites:** The payment modal is open.
- **Steps:**
  1. Open the payment modal by clicking the "Buy me a coffee" button.
  2. Click on "Support" and proceed to the payment process.
  3. Complete the payment process.
- **Expected Results:** 
  - Users should be redirected to a secure payment processor interface.
  - Upon successful payment, users should be redirected back to the app with a confirmation message or update in the "Recent Supporters" section.

---

### Test Case 10
- **Description:** Check for responsiveness of the "Buy me a coffee" button on different devices (desktop, tablet, mobile).
- **Prerequisites:** Access to the README generator app on different devices.
- **Steps:**
  1. Navigate to the README generator main page on different devices (desktop, tablet, mobile).
  2. Click on the "Buy me a coffee" button.
- **Expected Results:** 
  - The button and modal should be responsive and usable on different device interfaces without layout issues.

---

Running these tests should cover most of the potential issues and ensure that the "Buy me a coffee" functionality works smoothly for end users.

0 bugs
0 senseless
