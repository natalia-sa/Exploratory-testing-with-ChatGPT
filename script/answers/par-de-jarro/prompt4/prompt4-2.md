
[1] BUG, wrong birthdate
- Description: Login with valid credentials and access profile page.
- Prerequisites: Valid user account exists with known Email and Password.
- Steps:
  1. Open the "Par de Jarro" app.
  2. Navigate to the login screen.
  3. Enter valid email and password.
  4. Click on the login button.
  5. After login, navigate to the profile page.
- Expected results: User successfully logs in and is redirected to the profile page where user details are displayed as shown in the profile screenshot.

[2]
- Description: Login with invalid credentials.
- Prerequisites: Valid email not associated with any account.
- Steps:
  1. Open the "Par de Jarro" app.
  2. Navigate to the login screen.
  3. Enter an invalid email and password.
  4. Click on the login button.
- Expected results: The app should display an error message indicating invalid credentials and should not log the user in.

[3]
- Description: Password field should be masked when typing.
- Prerequisites: None.
- Steps:
  1. Open the "Par de Jarro" app.
  2. Navigate to the login screen.
  3. Enter the email.
  4. Enter the password.
- Expected results: The password entered should be masked or hidden to obstruct visibility while typing.

[4]
- Description: Login with an empty email field.
- Prerequisites: None.
- Steps:
  1. Open the "Par de Jarro" app.
  2. Navigate to the login screen.
  3. Leave the email field empty.
  4. Enter a valid password.
  5. Click on the login button.
- Expected results: The app should display a validation error indicating that the email field cannot be empty.

[5]
- Description: Login with an empty password field.
- Prerequisites: None.
- Steps:
  1. Open the "Par de Jarro" app.
  2. Navigate to the login screen.
  3. Enter a valid email.
  4. Leave the password field empty.
  5. Click on the login button.
- Expected results: The app should display a validation error indicating that the password field cannot be empty.

[6]
- Description: Login with an incorrect email format.
- Prerequisites: None.
- Steps:
  1. Open the "Par de Jarro" app.
  2. Navigate to the login screen.
  3. Enter an invalid email format (e.g., "notanemail").
  4. Enter a valid password.
  5. Click on the login button.
- Expected results: The app should display a validation error indicating that the email format is incorrect.

[7] - SENSELESS
- Description: Login after resetting a forgotten password.
- Prerequisites: A valid email associated with an account and access to the associated email inbox.
- Steps:
  1. Open the "Par de Jarro" app.
  2. Navigate to the login screen.
  3. Click on "Forgot Password".
  4. Enter the email associated with the account.
  5. Follow the instructions sent to the email to reset the password.
  6. Navigate to the login screen again.
  7. Enter the email and the new password.
  8. Click on the login button.
- Expected results: The user should be able to log in successfully with the new password.

[8] SENSELESS
- Description: Attempt to login while the network is offline.
- Prerequisites: Network connection is turned off.
- Steps:
  1. Open the "Par de Jarro" app with the network turned off.
  2. Navigate to the login screen.
  3. Enter valid email and password.
  4. Click on the login button.
- Expected results: The app should display an error message indicating there is no network connection and should not proceed with the login attempt.

[9] - SENSELESS
- Description: Check if "remember me" functionality saves login credentials.
- Prerequisites: None.
- Steps:
  1. Open the "Par de Jarro" app.
  2. Navigate to the login screen.
  3. Enter valid email and password.
  4. Check the "remember me" checkbox.
  5. Click on the login button and ensure successful login.
  6. Log out of the app.
  7. Close and reopen the app.
  8. Navigate to the login screen.
- Expected results: The email field should be pre-filled with the previously entered email if "remember me" is functioning correctly.

[10]
- Description: Login with same credentials on two different devices simultaneously.
- Prerequisites: Two devices should have the "Par de Jarro" app installed.
- Steps:
  1. Open the "Par de Jarro" app on Device 1.
  2. Navigate to the login screen on Device 1.
  3. Enter valid email and password and click on the login button on Device 1.
  4. Open the "Par de Jarro" app on Device 2.
  5. Navigate to the login screen on Device 2.
  6. Enter the same email and password used on Device 1 and click on the login button on Device 2.
- Expected results: Both devices should be able to log in with the same credentials without logging out the other.

These exploratory test cases cover a range of scenarios that could uncover bugs or unexpected behavior in the login functionality of the "Par de Jarro" app.

3 senseless
1 bug