Here are some exploratory test cases for the "Par de Jarro" app based on the given features:

### Test Case 1 - SENSELESS, no field birth date
- **Description:** New user registration with valid details
- **Prerequisites:** Ensure the app is accessible, and the registration page is available
- **Steps:**
  1. Navigate to the registration page.
  2. Fill in all the required fields with valid information (name, email, phone number, CPF, date of birth, gender, university, course, and bio).
  3. Click on the "Register" button.
- **Expected results:** The user should successfully register and receive a confirmation message.

### Test Case 2 - BUG, errors are not shown in frontend
- **Description:** New user registration with invalid email
- **Prerequisites:** Ensure the app is accessible, and the registration page is available
- **Steps:**
  1. Navigate to the registration page.
  2. Fill in all the fields with valid information except the email field, which should contain an invalid email format (e.g., "invalidemail").
  3. Click on the "Register" button.
- **Expected results:** The app should display an error message indicating an invalid email format.

### Test Case 3
- **Description:** Login with valid credentials
- **Prerequisites:** Ensure the user account is already created, and the app's login page is available.
- **Steps:**
  1. Navigate to the login page.
  2. Enter a valid email and password.
  3. Click the "Login" button.
- **Expected results:** The user should successfully login and be redirected to their profile page.

### Test Case 4
- **Description:** Login with invalid credentials
- **Prerequisites:** Ensure the app's login page is available.
- **Steps:**
  1. Navigate to the login page.
  2. Enter an invalid email or password.
  3. Click the "Login" button.
- **Expected results:** The app should display an error message indicating incorrect email or password.

### Test Case 5
- **Description:** Logout functionality
- **Prerequisites:** Ensure the user is logged in
- **Steps:**
  1. Navigate to the logout option in the app (usually found in the profile or settings menu).
  2. Click on the "Logout" button.
- **Expected results:** The user should be successfully logged out and redirected to the login page.

### Test Case 6 - BUG, wrong birthdate
- **Description:** Profile viewing
- **Prerequisites:** Ensure the user is logged in
- **Steps:**
  1. Navigate to the user's profile page.
- **Expected results:** The user's profile information should be displayed correctly as shown in the provided screenshot.

### Test Case 7 - SENSELESS
- **Description:** Profile editing and saving
- **Prerequisites:** Ensure the user is logged in
- **Steps:**
  1. Navigate to the user's profile page.
  2. Click on the "Edit" button.
  3. Modify one or more fields (e.g., changing the phone number).
  4. Click on the "Save" button.
- **Expected results:** The changes should be successfully saved, and the profile page should reflect the updated information.

### Test Case 8 - SENSELESS
- **Description:** Boundary testing on input fields (e.g., Name, Email)
- **Prerequisites:** Ensure the app's registration or profile editing page is available.
- **Steps:**
  1. Navigate to the registration or profile editing page.
  2. Enter the maximum allowed characters in the "Name" field.
  3. Enter the minimum allowed characters in the "Name" field.
  4. Repeat for the "Email" field and other input fields.
- **Expected results:** The app should properly handle and validate boundary conditions, allowing valid inputs and rejecting inputs exceeding allowed limits.

### Test Case 9
- **Description:** Cross-field validation (e.g., ensuring the "Email" field does not accept phone numbers)
- **Prerequisites:** Ensure the app's registration or profile editing page is available.
- **Steps:**
  1. Navigate to the registration or profile editing page.
  2. Enter a phone number in the "Email" field.
  3. Try saving the form.
- **Expected results:** The app should display an error message indicating invalid input for the "Email" field.

### Test Case 10
- **Description:** Unusual flow - Logging out while editing profile
- **Prerequisites:** Ensure the user is logged in and on the profile editing page.
- **Steps:**
  1. Start editing the profile.
  2. Without saving changes, click the logout button.
- **Expected results:** The app should warn the user about unsaved changes or successfully logout but discard unsaved changes.

These test cases should help identify potential bugs and ensure the functionality of the "Par de Jarro" app across various scenarios.

3 senseless
2 bugs