Here are the exploratory test cases based on the screenshots provided for the Par de jarro app's login feature:

### Test Case 1

- **Test Number**: TC001
- **Description**: Test login with valid credentials
- **Prerequisites**: User account must already be registered in the application.
- **Steps**:
  1. Open the login page.
  2. Enter a valid email and password.
  3. Click on the "Entrar" button.
- **Expected Results**: User should be redirected to the dashboard or home page, indicating a successful login.

### Test Case 2

- **Test Number**: TC002
- **Description**: Test login with invalid password
- **Prerequisites**: User account must already be registered.
- **Steps**:
  1. Open the login page.
  2. Enter a valid email and an incorrect password.
  3. Click on the "Entrar" button.
- **Expected Results**: User should receive an error message indicating that the password is incorrect.

### Test Case 3

- **Test Number**: TC003
- **Description**: Test login with email not registered
- **Prerequisites**: Ensure the email used is not registered in the database.
- **Steps**:
  1. Open the login page.
  2. Enter an unregistered email and any password.
  3. Click on the "Entrar" button.
- **Expected Results**: User should receive an error message indicating that the email is not found in the system.

### Test Case 4

- **Test Number**: TC004
- **Description**: Test SQL injection in the login fields
- **Prerequisites**: Ensure the web application has a database connected.
- **Steps**:
  1. Open the login page.
  2. Enter `'; DROP TABLE users;--` in both email and password fields.
  3. Click on the "Entrar" button.
- **Expected Results**: The system should not execute the SQL command. The user should see an error message about invalid credentials.

### Test Case 5

- **Test Number**: TC005
- **Description**: Test login with empty fields
- **Prerequisites**: None
- **Steps**:
  1. Open the login page.
  2. Leave the email and password fields empty.
  3. Click on the "Entrar" button.
- **Expected Results**: User should see an error message indicating that both fields are required.

### Test Case 6

- **Test Number**: TC006
- **Description**: Test login with XSS script injection
- **Prerequisites**: None
- **Steps**:
  1. Open the login page.
  2. Enter `<script>alert('XSS');</script>` in both email and password fields.
  3. Click on the "Entrar" button.
- **Expected Results**: The system should not execute the script; it should treat it as plain text. User should see an error message about invalid credentials.

### Test Case 7

- **Test Number**: TC007
- **Description**: Test login with special characters
- **Prerequisites**: Ensure user account has special characters in the email and password.
- **Steps**:
  1. Open the login page.
  2. Enter an email and password with special characters (e.g., `user!@#email.com`, `P@$$w0rd!`).
  3. Click on the "Entrar" button.
- **Expected Results**: User should be able to log in successfully if credentials are correct.

### Test Case 8

- **Test Number**: TC008
- **Description**: Test login while the database is down
- **Prerequisites**: Simulate the database being down.
- **Steps**:
  1. Open the login page.
  2. Enter any email and password.
  3. Click on the "Entrar" button.
- **Expected Results**: User should see an error message indicating that the service is temporarily unavailable.

### Test Case 9

- **Test Number**: TC009
- **Description**: Test login with HTML tags
- **Prerequisites**: None
- **Steps**:
  1. Open the login page.
  2. Enter `<b>bold</b>` in both email and password fields.
  3. Click on the "Entrar" button.
- **Expected Results**: The system should treat the HTML tags as plain text and prompt an error message about invalid credentials.

### Test Case 10

- **Test Number**: TC010
- **Description**: Test session expiration after login
- **Prerequisites**: User account must be registered; the application should have session control.
- **Steps**:
  1. Log in with valid credentials.
  2. Wait for the session to expire (simulate if possible).
  3. Try to navigate to a different page.
- **Expected Results**: User should be redirected to the login page, indicating the session has expired.

