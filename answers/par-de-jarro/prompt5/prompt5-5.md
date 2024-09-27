### [Test 001]
- **Description:** Verify that the user can successfully edit and save their profile information.
- **Prerequisites:** User must be logged in and have access to the Edit Profile screen.
- **Steps:**
  1. Navigate to the Edit Profile screen.
  2. Update fields such as "Nome," "Telefone," "Email," "Gênero," "Universidade," "Curso," and "Bio".
  3. Click on "Editar".
- **Expected results:** The profile information should be updated and saved successfully. A success message should be displayed.

### [Test 002] 
- **Description:** Verify that the user cannot leave mandatory fields empty.
- **Prerequisites:** User must be logged in and have access to the Edit Profile screen.
- **Steps:**
  1. Navigate to the Edit Profile screen.
  2. Clear the "Nome" field.
  3. Click on "Editar".
- **Expected results:** The system should prompt the user that the "Nome" field cannot be empty and prevent saving.

### [Test 003] BUG no error message is shown with this specific format
- **Description:** Validate email format in the "Email" field.
- **Prerequisites:** User must be logged in and have access to the Edit Profile screen.
- **Steps:**
  1. Navigate to the Edit Profile screen.
  2. Enter an invalid email format, such as "invalidemail.com" in the "Email" field.
  3. Click on "Editar".
- **Expected results:** The system should display an error message indicating the email format is invalid and prevent saving.

### [Test 004]
- **Description:** Validate the phone number format in the "Telefone" field.
- **Prerequisites:** User must be logged in and have access to the Edit Profile screen.
- **Steps:**
  1. Navigate to the Edit Profile screen.
  2. Enter an invalid phone number format, such as "12345" in the "Telefone" field.
  3. Click on "Editar".
- **Expected results:** The system should display an error message indicating the phone number format is invalid and prevent saving.

### [Test 005]
- **Description:** Verify that the CPF number is properly formatted and valid.
- **Prerequisites:** User must be logged in and have access to the Edit Profile screen.
- **Steps:**
  1. Navigate to the Edit Profile screen.
  2. Enter an invalid CPF number, such as "123.456.789-01" in the "CPF" field.
  3. Click on "Editar".
- **Expected results:** The system should display an error message indicating the CPF is invalid and prevent saving.

### [Test 006]
- **Description:** Check for special characters in the "Nome" field.
- **Prerequisites:** User must be logged in and have access to the Edit Profile screen.
- **Steps:**
  1. Navigate to the Edit Profile screen.
  2. Enter special characters like "!@#$%" in the "Nome" field.
  3. Click on "Editar".
- **Expected results:** The system should either sanitize the input or display an error message indicating special characters are not allowed.

### [Test 007]
- **Description:** Validate the date format in the "Data de nascimento" field.
- **Prerequisites:** User must be logged in and have access to the Edit Profile screen.
- **Steps:**
  1. Navigate to the Edit Profile screen.
  2. Enter an invalid date format, such as "2000/03/04" in the "Data de nascimento" field.
  3. Click on "Editar".
- **Expected results:** The system should display an error message indicating the date format is invalid and prevent saving.

### [Test 008]
- **Description:** Verify that the "Universidade" field displays a list of valid universities.
- **Prerequisites:** User must be logged in and have access to the Edit Profile screen.
- **Steps:**
  1. Navigate to the Edit Profile screen.
  2. Click on the "Universidade" field to display the dropdown list.
  3. Browse through the list to ensure all universities are listed.
- **Expected results:** The dropdown should display a list of valid universities from the system.

### [Test 009]
- **Description:** Check that the user can upload and change their profile picture.
- **Prerequisites:** User must be logged in and have access to the Edit Profile screen.
- **Steps:**
  1. Navigate to the Edit Profile screen.
  2. Click on the camera icon to upload a new profile picture.
  3. Select an image file from the local machine.
  4. Click on "Editar" to save changes.
- **Expected results:** The new profile picture should be updated successfully, and a success message should be displayed.

### [Test 010]
- **Description:** Test the system's response when a user tries to input an excessively long text in the "Bio" field.
- **Prerequisites:** User must be logged in and have access to the Edit Profile screen.
- **Steps:**
  1. Navigate to the Edit Profile screen.
  2. Enter a long text (e.g., 500 characters) in the "Bio" field.
  3. Click on "Editar".
- **Expected results:** The system should either save the bio up to a maximum character limit or display an error message if the text is too long.

1 bug
0 senseless