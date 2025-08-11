Here are some exploratory test cases for the "View Profile" feature in the Par de Jarro app:

### Test Case 1 - BUG
- **Test Number:** TC001
- **Description:** View profile details for a registered user.
- **Prerequisites:** User has successfully logged into the app with valid credentials.
- **Steps:**  
  1. Open the app.
  2. Log in using valid credentials.
  3. Click on the profile icon at the top-right corner.
  4. Observe the profile details.
- **Expected Results:** The complete and correct profile information of the user is displayed, including name, email, phone number, CPF, birth date, gender, university, course, and bio. No sensitive information should be exposed to unauthorized users.

### Test Case 2
- **Test Number:** TC002
- **Description:** View profile details without logging in.
- **Prerequisites:** App is open without logging in.
- **Steps:**  
  1. Open the app.
  2. Try to click on the profile icon at the top-right corner.
- **Expected Results:** The app should prompt the user to log in and not display any profile information.

### Test Case 3
- **Test Number:** TC003
- **Description:** Verify the data format consistency in the profile.
- **Prerequisites:** User has successfully logged into the app with valid credentials.
- **Steps:**
  1. Open the app.
  2. Log in using valid credentials.
  3. Click on the profile icon at the top-right corner.
  4. Observe the profile details.
- **Expected Results:** Ensure data fields comply with expected formats: email format should be validated, phone number should have the correct pattern and format, birth date should be in DD/MM/YYYY format.

### Test Case 4
- **Test Number:** TC004
- **Description:** Verify error message for failed profile data retrieval.
- **Prerequisites:** User has successfully logged into the app with valid credentials, and there is a simulated failure in the database connection.
- **Steps:**
  1. Open the app.
  2. Log in using valid credentials.
  3. Click on the profile icon at the top-right corner.
- **Expected Results:** The app should display an appropriate error message indicating the profile data retrieval failure without crashing.

### Test Case 5
- **Test Number:** TC005
- **Description:** Access profile page and check for any HTML/JavaScript injection vulnerabilities.
- **Prerequisites:** User has successfully logged into the app with valid credentials.
- **Steps:**
  1. Log in as a user with profile information potentially containing special characters or scripts.
  2. Click on the profile icon at the top-right corner.
  3. Observe the displayed profile details.
- **Expected Results:** The app should properly escape or sanitize special characters, and no injected HTML/JavaScript should execute.

### Test Case 6
- **Test Number:** TC006
- **Description:** Check profile picture upload functionality.
- **Prerequisites:** User has successfully logged into the app with valid credentials.
- **Steps:**
  1. Open the app.
  2. Log in using valid credentials.
  3. Click on the profile icon at the top-right corner.
  4. Try to upload a profile picture.
- **Expected Results:** The user should be able to upload a valid image file, and it should be correctly displayed as the profile picture. Invalid file types should be rejected with an appropriate error message.

### Test Case 7
- **Test Number:** TC007
- **Description:** Verify that editing profile information works correctly.
- **Prerequisites:** User has successfully logged into the app with valid credentials.
- **Steps:**
  1. Open the app.
  2. Log in using valid credentials.
  3. Click on the profile icon at the top-right corner.
  4. Click the "Edit" button.
  5. Modify some profile details (e.g., email, phone number).
  6. Save the changes.
  7. Refresh the profile page.
- **Expected Results:** The modified profile details should be properly updated and displayed. 

### Test Case 8
- **Test Number:** TC008
- **Description:** Check profile accessibility when the user account is disabled or deleted.
- **Prerequisites:** User account is disabled or deleted in the database.
- **Steps:**
  1. Open the app.
  2. Attempt to log in using the disabled/deleted account credentials.
  3. Attempt to access the profile page.
- **Expected Results:** The user should receive an appropriate error message, and access to the profile page should be denied.

These test cases help ensure the reliability, security, and proper functioning of the "View Profile" feature in the Par de Jarro app.