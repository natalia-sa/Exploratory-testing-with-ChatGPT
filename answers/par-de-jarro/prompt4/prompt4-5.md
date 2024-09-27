Certainly! Below are some exploratory test cases for the "edit profile" feature in the app "Par de Jarro," based on the provided screenshot.

### Test Case 1: 
- **Description**: Edit profile with maximal field lengths.
- **Prerequisites**: User is logged into their profile.
- **Steps**:
  1. Click on the "Nome" field and input a name with 255 characters.
  2. Click on the "Email" field and input an email with 255 characters.
  3. Click on the "Telefone" field and input a phone number with the maximal digits allowed.
  4. Click on the "CPF" field and input a CPF with 14 characters (formatted).
  5. Click on the "Data de nascimento" field and select a date.
  6. Click on the "Gênero" field and input maximal allowed characters.
  7. Click on the "Universidade" field and input maximal allowed characters.
  8. Click on the "Curso" field and input maximal allowed characters.
  9. Click on the "Bio" field and input a long string with 1000 characters.
  10. Click on "Editar" to save the changes.
- **Expected Results**: Profile is updated successfully with no truncation or data loss.

### Test Case 2: BUG, with this specific email format no error message is shown
- **Description**: Edit profile with invalid email format.
- **Prerequisites**: User is logged into their profile.
- **Steps**:
  1. Click on the “Email” field and input an invalid email (e.g., "invalidemail.com").
  2. Click on “Editar” to save the changes.
- **Expected Results**: An error message is displayed indicating that the email format is not valid and the profile is not updated.

### Test Case 3: 
- **Description**: Edit profile with special characters in text fields.
- **Prerequisites**: User is logged into their profile.
- **Steps**:
  1. Click on the "Nome" field and input a name with special characters (e.g., "N@mé#123").
  2. Click on the "Email" field and input a valid email.
  3. Click on the "Telefone" field and input a valid phone number.
  4. Click on the "CPF" field and input a valid CPF.
  5. Click on the "Data de nascimento" field and select a date.
  6. Click on the "Gênero" field and input special characters.
  7. Click on the "Universidade" field and input special characters (e.g., "Univ#1@2021").
  8. Click on the "Curso" field and input special characters (e.g., "Coursé!2021").
  9. Click on the "Bio" field and input special characters.
  10. Click on “Editar” to save the changes.
- **Expected Results**: Profile is updated successfully with special characters correctly handled.

### Test Case 4:
- **Description**: Edit profile with xss attack attempt in Bio field.
- **Prerequisites**: User is logged into their profile.
- **Steps**:
  1. Click on the "Bio" field and input a typical XSS script (e.g., `<script>alert("XSS")</script>`).
  2. Click on "Editar" to save the changes.
- **Expected Results**: The input is sanitized, and the script is not executed. The profile displays the sanitized text, preventing any XSS attack.

### Test Case 5: BUG
- **Description**: Edit Date of Birth with future date.
- **Prerequisites**: User is logged into their profile.
- **Steps**:
  1. Click on the "Data de nascimento" field.
  2. Select a future date from the calendar picker.
  3. Click on "Editar" to save the changes.
- **Expected Results**: An error message is displayed indicating that the date of birth cannot be in the future and the profile is not updated.

### Test Case 6:
- **Description**: Edit profile and clear mandatory fields.
- **Prerequisites**: User is logged into their profile.
- **Steps**:
  1. Delete the contents of the "Nome" field.
  2. Delete the contents of the "Email" field.
  3. Click on "Editar" to save the changes.
- **Expected Results**: Error messages are displayed indicating that "Nome" and "Email" fields cannot be empty. Profile is not updated.

### Test Case 7:
- **Description**: Concurrency test when two users edit the profile simultaneously.
- **Prerequisites**: Two users logged into the same profile on different devices.
- **Steps**:
  1. User A edits and tries to save the changes in the profile.
  2. Simultaneously, User B also edits and tries to save different changes in the profile.
- **Expected Results**: System should handle concurrent updates gracefully and display a message if the profile has been updated by another user. Possible conflict resolution mechanism should be considered.

By following these exploratory test cases, the robustness, security, and usability of the "edit profile" feature in "Par de Jarro" can be thoroughly evaluated.

2 bugs
0 senseless