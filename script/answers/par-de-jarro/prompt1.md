Based on the given screenshot of the app "Par de Jarro," here are exploratory test cases that cover the features of new user registration, login, logout, profile viewing, and profile editing:

### 1. New User Registration
#### 1.1 Test Case: Register a New User with Valid Data
- Description: Verify that a new user can register with valid data.
- Prerequisites: None.
- Steps:
  1. Navigate to the registration page.
  2. Enter valid data in the required fields (Name, Email, Password, etc.).
  3. Click the "Register" button.
- Expected results: The user is successfully registered and redirected to the main page/dashboard.

#### 1.2 Test Case: Attempt Registration with Already Used Email - BUG, nothing is shown in frontend
- Description: Verify that the system prevents registration with an email that is already in use.
- Prerequisites: An existing user with the same email.
- Steps:
  1. Navigate to the registration page.
  2. Enter data in the required fields using an already registered email.
  3. Click the "Register" button.
- Expected results: An error message is displayed indicating that the email is already in use.

### 2. Login
#### 2.1 Test Case: Login with Valid Credentials
- Description: Verify that a user can log in with valid credentials.
- Prerequisites: An existing user account.
- Steps:
  1. Navigate to the login page.
  2. Enter a valid email and password.
  3. Click the "Login" button.
- Expected results: User is successfully logged in and redirected to the main page/dashboard.

#### 2.2 Test Case: Login with Invalid Credentials
- Description: Verify that the system prevents login with invalid credentials.
- Prerequisites: None.
- Steps:
  1. Navigate to the login page.
  2. Enter an invalid email and/or password.
  3. Click the "Login" button.
- Expected results: An error message is displayed indicating incorrect email or password.

### 3. Logout
#### 3.1 Test Case: Logout Successfully
- Description: Verify that a logged-in user can log out successfully.
- Prerequisites: User must be logged in.
- Steps:
  1. Click on the "Logout" button/link.
- Expected results: User is logged out and redirected to the login page.

### 4. Profile Viewing - BUG, wrong birthdate info
#### 4.1 Test Case: View User Profile
- Description: Verify that a logged-in user can view their profile.
- Prerequisites: User must be logged in.
- Steps:
  1. Click on the profile link/icon.
- Expected results: User’s profile page is displayed with all the user's details as shown in the screenshot.

### 5. Profile Editing - SENSELESS
#### 5.1 Test Case: Edit User Profile with Valid Data
- Description: Verify that a logged-in user can successfully edit their profile with valid data.
- Prerequisites: User must be logged in.
- Steps:
  1. Navigate to the "Profile" page.
  2. Click on the "Edit" button.
  3. Update the profile details (e.g., Name, Email, Phone, etc.).
  4. Click on the "Save" button.
- Expected results: The profile is successfully updated, and the changes are reflected on the profile page.

#### 5.2 Test Case: Edit Profile with Invalid Data - SENSELESS
- Description: Verify that the system prevents updating the profile with invalid data.
- Prerequisites: User must be logged in.
- Steps:
  1. Navigate to the "Profile" page.
  2. Click on the "Edit" button.
  3. Enter invalid data in the fields (e.g., incorrect email format).
  4. Click on the "Save" button.
- Expected results: An error message is displayed indicating the invalid fields, and the profile is not updated.

#### 5.3 Test Case: Attempt to Save Profile without Making Any Changes - SENSELESS
- Description: Verify the system's behavior when attempting to save the profile without making any changes.
- Prerequisites: User must be logged in.
- Steps:
  1. Navigate to the "Profile" page.
  2. Click on the "Edit" button.
  3. Click on the "Save" button without making any changes.
- Expected results: The system should either save without any changes (no alteration message) or provide a message saying no changes were made.

These test cases cover basic functionality and ensure the app "Par de Jarro" operates as expected for these critical user actions.


3 senseless
2 bugs