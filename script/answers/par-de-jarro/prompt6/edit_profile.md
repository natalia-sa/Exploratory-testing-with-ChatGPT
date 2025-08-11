Absolutely! Based on the provided GUI screenshot and the context, here are exploratory test cases for the Edit Profile feature in the "Par de Jarro" app:

### Test Case 1 - BUG
- **Test number:** 1  
- **Description:** Verify that the user can successfully edit all profile fields.  
- **Prerequisites:** User must be logged in.
- **Steps:**
  1. Open the "Par de Jarro" app on Firefox.
  2. Navigate to the "Meu Perfil" page.
  3. Edit the fields: Name, Email, Telefone, CPF, Data de Nascimento, Gênero, Universidade, Curso, and Bio with valid data.
  4. Click on the "Editar" button.
- **Expected results:** The profile should update successfully, and a confirmation message should be displayed.

### Test Case 2 BUG
- **Test number:** 2
- **Description:** Verify that the email field does not accept invalid email formats.
- **Prerequisites:** User must be logged in.
- **Steps:**
  1. Open the "Par de Jarro" app on Chrome.
  2. Navigate to the "Meu Perfil" page.
  3. Enter an invalid email (e.g., "invalidemail", "user@.com") in the Email field.
  4. Click on the "Editar" button.
- **Expected results:** An error message should be displayed stating that the email format is invalid.

### Test Case 3
- **Test number:** 3
- **Description:** Verify that the CPF field does not accept non-numeric characters.
- **Prerequisites:** User must be logged in.
- **Steps:**
  1. Open the "Par de Jarro" app on Firefox.
  2. Navigate to the "Meu Perfil" page.
  3. Enter alphabets or special characters in the CPF field.
  4. Click on the "Editar" button.
- **Expected results:** An error message should be displayed stating that the CPF should be numeric.

### Test Case 4
- **Test number:** 4
- **Description:** Verify the behavior of the application when only mandatory fields (Name, Email) are filled out.
- **Prerequisites:** User must be logged in.
- **Steps:**
  1. Open the "Par de Jarro" app on Chrome.
  2. Navigate to the "Meu Perfil" page.
  3. Leave all fields blank except for the Name and Email fields.
  4. Click on the "Editar" button.
- **Expected results:** The profile should update successfully with only the Name and Email fields, and a confirmation message should be displayed.

### Test Case 5
- **Test number:** 5
- **Description:** Test XSS vulnerability by entering a script in the Bio field.
- **Prerequisites:** User must be logged in.
- **Steps:**
  1. Open the "Par de Jarro" app on Firefox.
  2. Navigate to the "Meu Perfil" page.
  3. Enter a script tag in the Bio field (e.g., `<script>alert('XSS')</script>`).
  4. Click on the "Editar" button.
- **Expected results:** The application should sanitize the input and not execute the script, displaying a safely escaped text instead.

### Test Case 6
- **Test number:** 6
- **Description:** Verify the date picker works correctly for the Data de Nascimento field.
- **Prerequisites:** User must be logged in.
- **Steps:**
  1. Open the "Par de Jarro" app on Chrome.
  2. Navigate to the "Meu Perfil" page.
  3. Click on the calendar icon for the Data de Nascimento field.
  4. Select a date from the date picker.
  5. Click on the "Editar" button.
- **Expected results:** The selected date should be correctly saved and displayed.

### Test Case 7
- **Test number:** 7
- **Description:** Verify the profile picture upload functionality.
- **Prerequisites:** User must be logged in.
- **Steps:**
  1. Open the "Par de Jarro" app on Firefox.
  2. Navigate to the "Meu Perfil" page.
  3. Click on the profile picture icon.
  4. Upload a valid image file.
  5. Click on the "Editar" button.
- **Expected results:** The profile picture should be successfully uploaded and displayed in the profile.

### Test Case 8
- **Test number:** 8
- **Description:** Verify that SQL injection is not possible in any text field.
- **Prerequisites:** User must be logged in.
- **Steps:**
  1. Open the "Par de Jarro" app on Chrome.
  2. Navigate to the "Meu Perfil" page.
  3. Enter SQL injection strings (e.g., `'; DROP TABLE users; --`) into various text fields.
  4. Click on the "Editar" button.
- **Expected results:** The application should not execute the SQL command and handle the input safely by displaying an error message or sanitizing the input.

### Test Case 9
- **Test number:** 9
- **Description:** Check the responsiveness and usability of the profile page on different screen sizes.
- **Prerequisites:** User must be logged in.
- **Steps:**
  1. Open the "Par de Jarro" app on Firefox.
  2. Navigate to the "Meu Perfil" page.
  3. Resize the browser window to various sizes (e.g., mobile, tablet, desktop).
  4. Observe the layout and usability of the form.
- **Expected results:** The profile page should be responsive, with all fields and buttons accessible and properly displayed on different screen sizes.

### Test Case 10
- **Test number:** 10
- **Description:** Verify the application's behavior when mandatory fields are left blank.
- **Prerequisites:** User must be logged in.
- **Steps:**
  1. Open the "Par de Jarro" app on Chrome.
  2. Navigate to the "Meu Perfil" page.
  3. Leave the Name and Email fields blank.
  4. Click on the "Editar" button.
- **Expected results:** The application should show error messages indicating that the mandatory fields (Name and Email) need to be filled.

### Test Case 11 - BUG
- **Test number:** 11
- **Description:** Verify the application handles high load in the Bio field.
- **Prerequisites:** User must be logged in.
- **Steps:**
  1. Open the "Par de Jarro" app on Firefox.
  2. Navigate to the "Meu Perfil" page.
  3. Enter a large amount of text (e.g., 5000 characters) in the Bio field.
  4. Click on the "Editar" button.
- **Expected results:** The application should handle large text inputs efficiently without crashing or slowing down, and the input should be saved correctly.

These test cases cover a wide range of possible scenarios, including typical interactions, edge cases, and security concerns. Be sure to run these tests on both Firefox and Chrome browsers as specified.

