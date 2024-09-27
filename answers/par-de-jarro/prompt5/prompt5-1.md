Sure! Below are some exploratory test cases for the "Register New User" feature in the “Par de Jarro” app:

---

### Test Case 1
- **Description:** Test registration with all valid fields
- **Prerequisites:** None
- **Steps:**
  1. Open the registration page of the app.
  2. Enter a valid full name.
  3. Select a valid gender.
  4. Enter a valid email address.
  5. Enter a strong password.
  6. Enter a short bio.
  7. Enter a valid phone number.
  8. Enter a valid CPF (Brazilian individual taxpayer registry identification).
  9. Enter a valid course name.
  10. Select a university from the list.
  11. Click the "Criar Conta" (Create Account) button.
- **Expected results:** User is successfully registered and directed to a confirmation or welcome page.

---

### Test Case 2 BUG, it is possible to register
- **Description:** Test registration with missing mandatory fields
- **Prerequisites:** None
- **Steps:**
  1. Open the registration page of the app.
  2. Leave the full name field empty.
  3. Enter valid information in all other fields.
  4. Click the "Criar Conta" button.
- **Expected results:** Registration is not allowed. An error message indicating the full name field is required should be displayed.

---

### Test Case 3 BUG, errors are not shown in frontend
- **Description:** Test registration with invalid email format
- **Prerequisites:** None
- **Steps:**
  1. Open the registration page of the app.
  2. Enter a valid full name.
  3. Select a valid gender.
  4. Enter an invalid email address (e.g., "invalidemail").
  5. Enter a strong password.
  6. Enter a short bio.
  7. Enter a valid phone number.
  8. Enter a valid CPF.
  9. Enter a valid course name.
  10. Select a university from the list.
  11. Click the "Criar Conta" button.
- **Expected results:** Registration is not allowed. An error message indicating the invalid email format should be displayed.

---

### Test Case 4
- **Description:** Test registration with an existing email
- **Prerequisites:** Another account registered with the same email
- **Steps:**
  1. Open the registration page of the app.
  2. Enter a valid full name.
  3. Select a valid gender.
  4. Enter an email address already in use.
  5. Enter a strong password.
  6. Enter a short bio.
  7. Enter a valid phone number.
  8. Enter a valid CPF.
  9. Enter a valid course name.
  10. Select a university from the list.
  11. Click the "Criar Conta" button.
- **Expected results:** Registration is not allowed. An error message indicating the email address is already in use should be displayed.

---

### Test Case 5 SENSELESS
- **Description:** Test registration with password under minimum length
- **Prerequisites:** None
- **Steps:**
  1. Open the registration page of the app.
  2. Enter a valid full name.
  3. Select a valid gender.
  4. Enter a valid email address.
  5. Enter a password with fewer than the minimum required characters.
  6. Enter a short bio.
  7. Enter a valid phone number.
  8. Enter a valid CPF.
  9. Enter a valid course name.
  10. Select a university from the list.
  11. Click the "Criar Conta" button.
- **Expected results:** Registration is not allowed. An error message indicating the password does not meet the minimum length requirement should be displayed.

---

### Test Case 6
- **Description:** Test registration with special characters in Full Name
- **Prerequisites:** None
- **Steps:**
  1. Open the registration page of the app.
  2. Enter a full name with special characters (e.g., "J@n3 Do3").
  3. Fill in valid information for all other fields.
  4. Click the "Criar Conta" button.
- **Expected results:** Registration result depends on app rules. If special characters are not allowed, an error message should be displayed indicating invalid characters in the full name. If allowed, user is successfully registered.

---

### Test Case 7 BUG, error 500 instead of correct error
- **Description:** Test registration with long text in Bio
- **Prerequisites:** None
- **Steps:**
  1. Open the registration page of the app.
  2. Enter a valid full name.
  3. Select a valid gender.
  4. Enter a valid email address.
  5. Enter a strong password.
  6. Enter a very long bio text (e.g., 2000 characters).
  7. Enter a valid phone number.
  8. Enter a valid CPF.
  9. Enter a valid course name.
  10. Select a university from the list.
  11. Click the "Criar Conta" button.
- **Expected results:** Registration result depends on app rules. If there is a bio character limit, an error message should indicate exceeding character limit. If allowed, user is successfully registered.

---

These test cases cover potential edge cases, unusual flows, and possible bugs for the "Register New User" feature in the “Par de Jarro” app.

3 bugs
1 senseless