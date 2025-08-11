Here are some exploratory test cases for the "Register new user" feature in the Par de Jarro app:

### Test Case 001
**Description:** Register a new user with valid information
- **Prerequisites:** None
- **Steps:**
  1. Open the registration page.
  2. Enter valid information in all fields.
  3. Click on the "Criar Conta" button.
- **Expected results:** User should be successfully registered, and the database should store user information. The user is redirected to the login or dashboard page.

### Test Case 002
**Description:** Attempt to register a user with an already registered email
- **Prerequisites:** An existing user account with a specific email.
- **Steps:**
  1. Open the registration page.
  2. Enter information, using the email that is already registered.
  3. Click on the "Criar Conta" button.
- **Expected results:** The system should display an error message stating that the email is already in use.

### Test Case 003 - BUG
**Description:** Register a user with missing mandatory fields
- **Prerequisites:** None
- **Steps:**
  1. Open the registration page.
  2. Leave one or more mandatory fields (e.g., email, password) empty.
  3. Click on the "Criar Conta" button.
- **Expected results:** The system should display an error message indicating that all mandatory fields must be filled.

### Test Case 004 - BUG
**Description:** Enter invalid email format
- **Prerequisites:** None
- **Steps:**
  1. Open the registration page.
  2. Enter invalid email format in the email field (e.g., "invalidemail@").
  3. Fill in the rest of the fields with valid information.
  4. Click on the "Criar Conta" button.
- **Expected results:** The system should display an error message requesting a valid email format.

### Test Case 005 - NONSENSICAL
**Description:** Enter password that is too short
- **Prerequisites:** None
- **Steps:**
  1. Open the registration page.
  2. Enter a password that is less than the minimum required length (e.g., less than 8 characters) in the password field.
  3. Fill in the rest of the fields with valid information.
  4. Click on the "Criar Conta" button.
- **Expected results:** The system should display an error message indicating that the password must be at least the minimum required length.

### Test Case 006
**Description:** Input special characters in fields where not allowed (e.g., CPF number)
- **Prerequisites:** None
- **Steps:**
  1. Open the registration page.
  2. Enter special characters in the CPF field (e.g., "!@#$%").
  3. Fill in the rest of the fields with valid information.
  4. Click on the "Criar Conta" button.
- **Expected results:** The system should display an error message indicating that special characters are not allowed in the CPF field.

### Test Case 007
**Description:** Verify database entry after successful registration
- **Prerequisites:** None
- **Steps:**
  1. Open the registration page.
  2. Enter valid information in all fields.
  3. Click on the "Criar Conta" button.
  4. Access the database to find the registered user data.
- **Expected results:** The new user data should be present in the database with correct details matching what was entered in the form.

### Test Case 008
**Description:** Check the registration form layout and alignment on different screen sizes (browser responsiveness)
- **Prerequisites:** None
- **Steps:**
  1. Open the registration page on Firefox.
  2. Resize the browser window to various sizes.
  3. Check the layout and alignment of the registration form on different sizes.
  4. Repeat steps 1-3 on Chrome.
- **Expected results:** The registration form should be properly aligned and usable across different screen sizes.

### Test Case 009
**Description:** Ensure security by testing SQL injection in any input field
- **Prerequisites:** None
- **Steps:**
  1. Open the registration page.
  2. Enter a malicious SQL statement (e.g., "' OR 1=1 --") in an input field.
  3. Fill in the rest of the fields with valid information.
  4. Click on the "Criar Conta" button.
- **Expected results:** The system should sanitize input and display an error message without allowing SQL injection.

### Test Case 010
**Description:** Test the timeout session during registration process
- **Prerequisites:** None
- **Steps:**
  1. Open the registration page.
  2. Enter partial information but do not submit the form.
  3. Wait for the session to timeout (if applicable).
  4. Attempt to submit the form after the session timeout.
- **Expected results:** The system should prompt the user to re-login or refresh the session and secure the entered data until it is refreshed.

