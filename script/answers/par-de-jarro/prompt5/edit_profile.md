Sure, here are exploratory test cases for the Edit Profile feature in the Par de jarro app:

### Test Case 1:
- **Test Number:** 1
- **Description:** Edit profile with valid data.
- **Prerequisites:** User must be logged in to the app.
- **Steps:**
  1. Navigate to the Edit Profile page.
  2. Update each field with valid and correct information.
  3. Click on the "Editar" button.
- **Expected Results:** The profile should be updated successfully, and the changes should be reflected immediately on the profile page.

### Test Case 2: BUG
- **Test Number:** 2
- **Description:** Edit profile with an invalid email format.
- **Prerequisites:** User must be logged in to the app.
- **Steps:**
  1. Navigate to the Edit Profile page.
  2. Change the email to an invalid format (e.g., "invalidemail.com").
  3. Click on the "Editar" button.
- **Expected Results:** An error message should appear indicating that the email format is incorrect, and the profile should not be updated.

### Test Case 3:
- **Test Number:** 3
- **Description:** Edit profile with a blank mandatory field.
- **Prerequisites:** User must be logged in to the app.
- **Steps:**
  1. Navigate to the Edit Profile page.
  2. Clear any mandatory field, e.g., the name field.
  3. Click on the "Editar" button.
- **Expected Results:** An error message should appear indicating that the field cannot be left blank, and the profile should not be updated.

### Test Case 4:
- **Test Number:** 4
- **Description:** SQL Injection attempt in the name field.
- **Prerequisites:** User must be logged in to the app.
- **Steps:**
  1. Navigate to the Edit Profile page.
  2. Enter the following text in the name field: "Robert'); DROP TABLE Users;--".
  3. Click on the "Editar" button.
- **Expected Results:** The application should sanitize the input and not execute any harmful SQL commands. An error message should appear or the input should be saved as plain text.

### Test Case 5:
- **Test Number:** 5
- **Description:** Upload a profile picture with unsupported file format.
- **Prerequisites:** User must be logged in to the app.
- **Steps:**
  1. Navigate to the Edit Profile page.
  2. Attempt to upload a profile picture in an unsupported format (e.g., .exe file).
  3. Click on the "Editar" button.
- **Expected Results:** An error message should appear indicating that the file format is not supported, and the profile picture should not be updated.

### Test Case 6:
- **Test Number:** 6
- **Description:** Enter special characters in the name and bio fields.
- **Prerequisites:** User must be logged in to the app.
- **Steps:**
  1. Navigate to the Edit Profile page.
  2. Enter special characters (e.g., "!@#$%^&*") in the name and bio fields.
  3. Click on the "Editar" button.
- **Expected Results:** The special characters should be accepted if they are valid characters for these fields, and the profile should be updated successfully.

### Test Case 7:
- **Test Number:** 7
- **Description:** Edit profile with a very long bio.
- **Prerequisites:** User must be logged in to the app.
- **Steps:**
  1. Navigate to the Edit Profile page.
  2. Enter a very long text (e.g., 1000+ characters) in the bio field.
  3. Click on the "Editar" button.
- **Expected Results:** The application should either truncate the text to a permissible length or display an error message indicating that the text is too long.

### Test Case 8: BUG
- **Test Number:** 8
- **Description:** Enter an invalid date of birth.
- **Prerequisites:** User must be logged in to the app.
- **Steps:**
  1. Navigate to the Edit Profile page.
  2. Enter an invalid date (e.g., 30/02/2022) in the date of birth field.
  3. Click on the "Editar" button.
- **Expected Results:** An error message should appear indicating that the date is invalid, and the profile should not be updated.

### Test Case 9:
- **Test Number:** 9
- **Description:** Test XSS vulnerability in bio field.
- **Prerequisites:** User must be logged in to the app.
- **Steps:**
  1. Navigate to the Edit Profile page.
  2. Enter a script tag (e.g., "<script>alert('XSS')</script>") in the bio field.
  3. Click on the "Editar" button.
- **Expected Results:** The application should sanitize the input and not execute the script. The profile should be updated without any cross-site scripting (XSS) vulnerability.

### Test Case 10:
- **Test Number:** 10
- **Description:** Update profile information and verify database update.
- **Prerequisites:** User must be logged in to the app. Database access rights are required to verify the update.
- **Steps:**
  1. Navigate to the Edit Profile page.
  2. Update any field with new data.
  3. Click on the "Editar" button.
  4. Access the database and verify that the changes are reflected correctly in the user’s record.
- **Expected Results:** The profile should be updated correctly, and the database should reflect the new information accurately.

These exploratory test cases aim to cover a wide array of typical and edge case scenarios to ensure the Edit Profile feature functions correctly and securely.
