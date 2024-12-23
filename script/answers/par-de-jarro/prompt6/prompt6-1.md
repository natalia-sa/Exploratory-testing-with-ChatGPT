Sure! Below are some test cases for the "Register new user" feature of the “Par de Jarro” app.

### Test Case 001
- **Description:** Register a new user with valid data in all fields.
- **Prerequisites:** App is running locally on a Linux machine.
- **Steps:**
  1. Open Firefox or Chrome browser and navigate to `http://localhost:3000/signUp`.
  2. Fill in the fields with the following details:
     - Full Name: João da Silva
     - Gender: Masculino
     - Email: joao.silva@example.com
     - Password: Password123
     - Bio: Student of Computer Science
     - Phone: +5511999999999
     - CPF: 123.456.789-10
     - Course: Computer Science
     - University: [select from list]
  3. Click on the "Criar Conta" button.
- **Expected results:** A successful registration message appears, and the user is redirected to the dashboard.

### Test Case 002 BUG, it is possible to register
- **Description:** Attempt to register a new user with missing mandatory fields.
- **Prerequisites:** App is running locally on a Linux machine.
- **Steps:**
  1. Open Firefox or Chrome browser and navigate to `http://localhost:3000/signUp`.
  2. Leave the "Full Name" field empty.
  3. Fill in the other fields with valid details.
  4. Click on the "Criar Conta" button.
- **Expected results:** The application should display a validation message indicating the requirement to fill in the Full Name field.

### Test Case 003 - BUG, error is not shown in frontend
- **Description:** Register with an invalid email format.
- **Prerequisites:** App is running locally on a Linux machine.
- **Steps:**
  1. Open Firefox or Chrome browser and navigate to `http://localhost:3000/signUp`.
  2. Fill in the fields with the following data:
     - Full Name: Ana Souza
     - Gender: Feminino
     - Email: ana.souzaexample.com (missing @)
     - Password: Password123
     - Bio: Medical student
     - Phone: +5511988888888
     - CPF: 987.654.321-00
     - Course: Medicine
     - University: [select from list]
  3. Click on the "Criar Conta" button.
- **Expected results:** The application should display a validation message indicating the email format is incorrect.

### Test Case 004 SENSELESS
- **Description:** Register a new user with a weak password.
- **Prerequisites:** App is running locally on a Linux machine.
- **Steps:**
  1. Open Firefox or Chrome browser and navigate to `http://localhost:3000/signUp`.
  2. Fill in the fields with the following data:
     - Full Name: Lucas Oliveira
     - Gender: Masculino
     - Email: lucas.oliveira@example.com
     - Password: 12345 (weak password)
     - Bio: Law student
     - Phone: +5511977777777
     - CPF: 123.456.789-00
     - Course: Law
     - University: [select from list]
  3. Click on the "Criar Conta" button.
- **Expected results:** The application should display a message indicating the password is too weak or doesn't meet the password requirements.

### Test Case 005
- **Description:** Attempt to register a user with an already registered email.
- **Prerequisites:** An existing user registered with the email "already.registered@mail.com".
- **Steps:**
  1. Open Firefox or Chrome browser and navigate to `http://localhost:3000/signUp`.
  2. Fill in the fields with the following data:
     - Full Name: Pedro Gomes
     - Gender: Masculino
     - Email: already.registered@mail.com
     - Password: SecurePass78
     - Bio: Chemistry student
     - Phone: +5511966666666
     - CPF: 999.888.777-66
     - Course: Chemistry
     - University: [select from list]
  3. Click on the "Criar Conta" button.
- **Expected results:** The application should display a message that the email is already registered.

### Test Case 006
- **Description:** Register a new user by inputting a non-numeric value in the CPF field.
- **Prerequisites:** App is running locally on a Linux machine.
- **Steps:**
  1. Open Firefox or Chrome browser and navigate to `http://localhost:3000/signUp`.
  2. Fill in the fields with the following data:
     - Full Name: Maria Fernanda
     - Gender: Feminino
     - Email: maria.fernanda@example.com
     - Password: Password543
     - Bio: Engineering student
     - Phone: +5511955555555
     - CPF: ABCD1234 (non-numeric)
     - Course: Engineering
     - University: [select from list]
  3. Click on the "Criar Conta" button.
- **Expected results:** The application should display a validation message indicating the CPF must be numeric.

### Test Case 007  - BUG error 500
- **Description:** Ensure field lengths are validated correctly by entering data that exceeds the maximum allowed length.
- **Prerequisites:** App is running locally on a Linux machine.
- **Steps:**
  1. Open Firefox or Chrome browser and navigate to `http://localhost:3000/signUp`.
  2. Fill in the fields with data exceeding usual max lengths, e.g., a bio with 1000 characters.
  3. Click on the "Criar Conta" button.
- **Expected results:** The application should display a validation message indicating that the character limit has been exceeded on the relevant field(s).

By performing these test cases, the exploratory testing will cover common scenarios, edge cases, and potential user errors, ensuring the registration feature is robust and user-friendly.