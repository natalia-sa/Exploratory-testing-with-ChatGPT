Given the provided information and screenshot, here are some detailed test cases for the "Edit Profile" feature in the app "Par de Jarro":

### Test Case 1: Edit Name Field
1. **Description:** Verify that the user can edit their name.
2. **Prerequisites:** The user is logged into the app and on the "Meu Perfil" page.
3. **Steps:**
   1. Click on the "Nome" field.
   2. Change the existing text (e.g., add a middle name).
   3. Click the "Editar" button at the bottom.
   4. Refresh the page.
4. **Expected results:** The new name is displayed in the "Nome" field after refreshing.

### Test Case 2: Check Invalid Email Format - BUG, this format, without @ do not show message
1. **Description:** Verify that the system shows an error when an invalid email format is entered.
2. **Prerequisites:** The user is logged into the app and on the "Meu Perfil" page.
3. **Steps:**
   1. Click on the "Email" field.
   2. Delete the existing text and enter an invalid email format (e.g., "invalidemail.com").
   3. Click the "Editar" button.
4. **Expected results:** An error message is shown indicating an invalid email format.

### Test Case 3: Edit Phone Number
1. **Description:** Verify that the user can update their phone number.
2. **Prerequisites:** The user is logged into the app and on the "Meu Perfil" page.
3. **Steps:**
   1. Click on the "Telefone" field.
   2. Change the phone number.
   3. Click the "Editar" button at the bottom.
   4. Refresh the page.
4. **Expected results:** The new phone number is displayed in the "Telefone" field after refreshing.

### Test Case 4: Validate CPF Field Format
1. **Description:** Verify that the CPF field does not accept invalid CPF formats.
2. **Prerequisites:** The user is logged into the app and on the "Meu Perfil" page.
3. **Steps:**
   1. Click on the "CPF" field.
   2. Enter an invalid CPF number (e.g., "123456").
   3. Click the "Editar" button.
4. **Expected results:** An error message is displayed indicating an invalid CPF format.

### Test Case 5: Date of Birth Validation
1. **Description:** Verify that the system does not accept invalid date formats in the Date of Birth field.
2. **Prerequisites:** The user is logged into the app and on the "Meu Perfil" page.
3. **Steps:**
   1. Click on the "Data de nascimento" field.
   2. Enter an invalid date (e.g., "31/02/2000").
   3. Click the "Editar" button.
4. **Expected results:** An error message is displayed indicating an invalid date.

### Test Case 6: Update Bio Field
1. **Description:** Verify that the user can add or update their bio.
2. **Prerequisites:** The user is logged into the app and on the "Meu Perfil" page.
3. **Steps:**
   1. Click on the "Bio" field.
   2. Enter a new bio.
   3. Click the "Editar" button.
   4. Refresh the page.
4. **Expected results:** The new bio is displayed in the "Bio" field after refreshing.

### Test Case 7: Select University from List
1. **Description:** Verify that the user can select a university from a predefined list.
2. **Prerequisites:** The user is logged into the app and on the "Meu Perfil" page.
3. **Steps:**
   1. Click on the "Universidade" dropdown list.
   2. Select a different university from the list.
   3. Click the "Editar" button.
   4. Refresh the page.
4. **Expected results:** The selected university is displayed in the "Universidade" field after refreshing.

### Test Case 8: Save Without Changes
1. **Description:** Verify that clicking "Editar" without making any changes still processes correctly.
2. **Prerequisites:** The user is logged into the app and on the "Meu Perfil" page.
3. **Steps:**
   1. Click the "Editar" button without making any changes to the fields.
4. **Expected results:** No changes are made to the profile, and there are no error messages.

### Test Case 9: Input Edge Cases for Name Field
1. **Description:** Verify that the name field handles edge cases such as very long names.
2. **Prerequisites:** The user is logged into the app and on the "Meu Perfil" page.
3. **Steps:**
   1. Click on the "Nome" field.
   2. Enter a very long name (e.g., more than 100 characters).
   3. Click the "Editar" button.
4. **Expected results:** The system either truncates the name to the acceptable length or shows an error message indicating the input is too long.

### Test Case 10: Test Functionality on Different Browsers
1. **Description:** Verify that the Edit Profile functionality works correctly on both Firefox and Chrome.
2. **Prerequisites:** The user is logged into the app and on the "Meu Perfil" page. The app should be accessed from both Firefox and Chrome browsers on Linux.
3. **Steps:**
   1. Follow the steps of any of the above test cases in Firefox.
   2. Repeat the same steps in Chrome.
4. **Expected results:** The Edit Profile functionality works as expected on both browsers without any discrepancies.

These test cases aim to cover a variety of potential user actions, edge cases, and scenarios to ensure the Edit Profile feature works correctly across different conditions and browsers.