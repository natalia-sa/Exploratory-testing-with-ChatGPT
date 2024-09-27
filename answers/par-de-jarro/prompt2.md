# Test Case 1: New User Registration with Valid Inputs - SENSELESS, no field birthdate
- **Description:** This test case verifies new user registration using valid inputs.
- **Prerequisites:** None
- **Steps:**
  1. Open the registration page of the app.
  2. Enter valid data into each field (name, email, phone number, CPF, birth date, gender, university, course, bio).
  3. Submit the registration form.
- **Expected results:** The user is successfully registered, and a confirmation message is displayed.

# Test Case 2: New User Registration with Invalid Email - BUG, no error shown in frontend
- **Description:** This test case ensures the app handles invalid email formats during registration.
- **Prerequisites:** None
- **Steps:**
  1. Open the registration page of the app.
  2. Enter valid data into each field except "Email" (use invalid formats such as "test@").
  3. Submit the registration form.
- **Expected results:** An error message is displayed, indicating that the email format is invalid.

# Test Case 3: Login with Valid Credentials
- **Description:** This test case verifies user login with valid credentials.
- **Prerequisites:** An existing user account with known valid credentials.
- **Steps:**
  1. Open the login page of the app.
  2. Enter the correct email and password.
  3. Submit the login form.
- **Expected results:** The user is successfully logged in and redirected to the home page or dashboard.

# Test Case 4: Login with Incorrect Password
- **Description:** This test case ensures the app handles incorrect password attempts.
- **Prerequisites:** An existing user account with a known email.
- **Steps:**
  1. Open the login page of the app.
  2. Enter the correct email and an incorrect password.
  3. Submit the login form.
- **Expected results:** An error message is displayed, indicating incorrect login credentials.

# Test Case 5: Logout Functionality
- **Description:** This test case verifies that a user can log out successfully.
- **Prerequisites:** The user must be logged in.
- **Steps:**
  1. Click on the logout button or link.
- **Expected results:** The user is logged out and redirected to the login page.

# Test Case 6: Viewing Profile Information - BUG, wrong birthdate info
- **Description:** This test case ensures a logged-in user can view their profile information correctly.
- **Prerequisites:** The user must be logged in with a filled profile.
- **Steps:**
  1. Navigate to the ‘My Profile’ section from the dashboard.
- **Expected results:** The user's profile information is displayed accurately, referring to the provided GUI screenshot.

# Test Case 7: Profile Editing with Valid Input - BUG, changes are not shown immidiatly
- **Description:** This test case verifies that editing the profile with valid inputs works correctly.
- **Prerequisites:** The user must be logged in and able to access the profile page.
- **Steps:**
  1. Navigate to the ‘My Profile’ section.
  2. Click the "Editar" button.
  3. Modify the profile fields with valid data.
  4. Save the changes.
- **Expected results:** The profile updates are saved successfully, and a confirmation message is shown.

# Test Case 8: Profile Editing with Invalid Phone Number
- **Description:** This test case checks if the app handles profile updates with invalid phone numbers.
- **Prerequisites:** The user must be logged in and able to access the profile page.
- **Steps:**
  1. Navigate to the ‘My Profile’ section.
  2. Click the "Editar" button.
  3. Change the phone number to an invalid format (e.g., use letters or insufficient digits).
  4. Save the changes.
- **Expected results:** An error message is displayed, indicating an invalid phone number format.

# Test Case 9: Unusual Flow - Navigating Away During Registration
- **Description:** This test case examines the app's behavior when a user navigates away during the registration process.
- **Prerequisites:** None
- **Steps:**
  1. Open the registration page of the app.
  2. Start entering registration information.
  3. Navigate away to a different page.
  4. Return to the registration page.
- **Expected results:** The registration page should either retain the previously entered data or clear it depending on the app's expected user experience design.

# Test Case 10: Unusual Flow - Multiple Login Attempts
- **Description:** This test case checks the app's response to multiple consecutive failed login attempts.
- **Prerequisites:** A user account with known credentials.
- **Steps:**
  1. Open the login page of the app.
  2. Enter the correct email and an incorrect password and submit the form.
  3. Repeat step 2 multiple times (at least 5 times).
- **Expected results:** The app should handle multiple failed attempts appropriately; potential security measures such as CAPTCHA or account lockout should be in place after several failed login attempts.

3 bugs
1 senseless