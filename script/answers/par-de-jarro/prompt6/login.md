Here are some exploratory test cases for the Login feature of the Par de jarro app. 

### Test Case 001
- **Description:** Verify login with valid credentials.
- **Prerequisites:** A registered user with valid credentials.
- **Steps:**
  1. Open the app in Firefox.
  2. Navigate to the login page.
  3. Enter the email and password of the registered user.
  4. Click on the "Entrar" button.
- **Expected results:** The user should be successfully logged in and redirected to their profile page.

### Test Case 002
- **Description:** Verify login with invalid email.
- **Prerequisites:** None.
- **Steps:**
  1. Open the app in Chrome.
  2. Navigate to the login page.
  3. Enter an invalid email and a valid password.
  4. Click on the "Entrar" button.
- **Expected results:** An error message should be displayed indicating that the email is not registered.

### Test Case 003
- **Description:** Verify login with empty email field.
- **Prerequisites:** None.
- **Steps:**
  1. Open the app in Firefox.
  2. Navigate to the login page.
  3. Leave the email field empty and enter a valid password.
  4. Click on the "Entrar" button.
- **Expected results:** An error message should be displayed indicating that the email field is required.

### Test Case 004
- **Description:** Verify login with incorrect password.
- **Prerequisites:** A registered user with valid credentials.
- **Steps:**
  1. Open the app in Chrome.
  2. Navigate to the login page.
  3. Enter a valid email and an incorrect password.
  4. Click on the "Entrar" button.
- **Expected results:** An error message should be displayed indicating that the password is incorrect.

### Test Case 005
- **Description:** Verify the login functionality with SQL injection.
- **Prerequisites:** None.
- **Steps:**
  1. Open the app in Firefox.
  2. Navigate to the login page.
  3. Enter "`OR 1=1; --`" in the email field and any password.
  4. Click on the "Entrar" button.
- **Expected results:** SQL injection should be prevented, and an error message should be displayed.

### Test Case 006
- **Description:** Verify logout functionality.
- **Prerequisites:** A user must be logged in.
- **Steps:**
  1. Open the app in Chrome.
  2. Log in using valid credentials.
  3. Click on the logout button.
- **Expected results:** The user should be logged out, and redirected to the login page.

### Test Case 007
- **Description:** Verify login with Cross-Site Scripting (XSS) attack.
- **Prerequisites:** None.
- **Steps:**
  1. Open the app in Firefox.
  2. Navigate to the login page.
  3. Enter `<script>alert('XSS')</script>` in the email field and any password.
  4. Click on the "Entrar" button.
- **Expected results:** XSS should be prevented and an error message should be displayed.

### Test Case 008
- **Description:** Verify the form validation messages.
- **Prerequisites:** None.
- **Steps:**
  1. Open the app in Chrome.
  2. Navigate to the login page.
  3. Try to click on the "Entrar" button without entering the email and password.
- **Expected results:** Validation messages should be displayed indicating that both fields are required.

### Test Case 009
- **Description:** Verify the "Forgot Password" link functionality.
- **Prerequisites:** None.
- **Steps:**
  1. Open the app in Firefox.
  2. Navigate to the login page.
  3. Click on the "Forgot Password" link.
- **Expected results:** The user should be redirected to a page where they can reset their password.

### Test Case 010
- **Description:** Verify successful login persists across browser sessions.
- **Prerequisites:** A registered user with valid credentials.
- **Steps:**
  1. Open the app in Chrome.
  2. Login using valid credentials.
  3. Close the browser without logging out.
  4. Reopen the browser and navigate to the home page.
- **Expected results:** The user session should be maintained, and the user should be automatically logged in.

