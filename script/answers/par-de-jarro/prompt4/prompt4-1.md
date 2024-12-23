Certainly! Here are some exploratory test cases for the "Register new user" feature in the "Par de Jarro" application:

---

### [Test 001] - BUG, iit is possible to register without inputting name
- **Description:** Attempt to register with an empty "Nome Completo" field.
- **Prerequisites:** The registration page is open.
- **Steps:**
  1. Leave the "Nome Completo" field empty.
  2. Fill in all other fields with valid information.
  3. Click on the "Criar Conta" button.
- **Expected results:** The system should display a validation message indicating that the "Nome Completo" field is required.

---

### [Test 002]
- **Description:** Register with special characters in the "Nome Completo" field.
- **Prerequisites:** The registration page is open.
- **Steps:**
  1. Enter a name with special characters (e.g., "@#!$%") in the "Nome Completo" field.
  2. Fill in all other fields with valid information.
  3. Click on the "Criar Conta" button.
- **Expected results:** The system should either:
  - Reject the input and provide a validation message, or
  - Ensure the special characters are handled correctly upon successful registration.

---

### [Test 003] - BUG, errors are not shown in frontend
- **Description:** Register using an invalid CPF number.
- **Prerequisites:** The registration page is open.
- **Steps:**
  1. Enter a valid name in the "Nome Completo" field.
  2. Enter an invalid CPF number in the "CPF" field.
  3. Fill in all other fields with valid information.
  4. Click on the "Criar Conta" button.
- **Expected results:** The system should display an error message indicating that the CPF number is invalid.

---

### [Test 004]
- **Description:** Register using an already registered Email.
- **Prerequisites:** The registration page is open. At least one user with the same email is already registered.
- **Steps:**
  1. Enter a valid name in the "Nome Completo" field.
  2. Enter a valid email that has already been used for another account in the "Email" field.
  3. Fill in all other fields with valid information.
  4. Click on the "Criar Conta" button.
- **Expected results:** The system should display an error message indicating that the email is already in use.

---

### [Test 005] - SENSELESS
- **Description:** Register with a weak password.
- **Prerequisites:** The registration page is open.
- **Steps:**
  1. Enter a weak password (e.g., "12345") in the "Senha" field.
  2. Fill in all other fields with valid information.
  3. Click on the "Criar Conta" button.
- **Expected results:** The system should display an error message indicating that the password is too weak and suggest criteria for a strong password.

---

### [Test 006] - SENSELESS
- **Description:** Register with mismatching "Senha" and "Confirmar Senha" fields.
- **Prerequisites:** The registration page is open.
- **Steps:**
  1. Enter a password in the "Senha" field.
  2. Enter a different password in the "Confirmar Senha" field.
  3. Fill in all other fields with valid information.
  4. Click on the "Criar Conta" button.
- **Expected results:** The system should display an error message indicating that the passwords do not match.

---

### [Test 007]
- **Description:** Register with alphabetic characters in the "Telefone" field.
- **Prerequisites:** The registration page is open.
- **Steps:**
  1. Enter alphabetic characters (e.g., "abc") in the "Telefone" field.
  2. Fill in all other fields with valid information.
  3. Click on the "Criar Conta" button.
- **Expected results:** The system should display a validation message indicating that the "Telefone" field must contain only numerical characters.

---

### [Test 008] BUG, error 500 instead of the correct error
- **Description:** Submit the form with the "Bio" field containing very long text.
- **Prerequisites:** The registration page is open.
- **Steps:**
  1. Enter a valid name in the "Nome Completo" field.
  2. Enter very long text in the "Bio" field.
  3. Fill in all other fields with valid information.
  4. Click on the "Criar Conta" button.
- **Expected results:** The system should either:
  - Truncate the bio if a character limit exists, or
  - Accept the input without performance issues.

---

### [Test 009]
- **Description:** Attempt to register with an invalid email format.
- **Prerequisites:** The registration page is open.
- **Steps:**
  1. Enter an invalid email format (e.g., "user@com") in the "Email" field.
  2. Fill in all other fields with valid information.
  3. Click on the "Criar Conta" button.
- **Expected results:** The system should display an error message indicating the email format is invalid.

---

### [Test 010]
- **Description:** Register with all fields filled correctly.
- **Prerequisites:** The registration page is open.
- **Steps:**
  1. Enter valid information in all fields.
  2. Click on the "Criar Conta" button.
- **Expected results:** The system should successfully create the account and redirect the user to the login page or homepage.

---

These exploratory test cases aim to uncover potential bugs and ensure the robustness of the user registration feature by testing unusual and edge cases.

3 bugs
2 senseless