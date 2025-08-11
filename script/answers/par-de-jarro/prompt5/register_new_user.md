Certainly! Below are exploratory test cases for the "Register new user" feature in the "Par de Jarro" app. These test cases focus on possible bugs, unusual flows, and security issues.

### Test Case 1
- **Test Number**: TC001
- **Description**: Register a new user with valid details.
- **Prerequisites**: The user is on the registration page.
- **Steps**:
  1. Enter a valid Full Name in the "Nome Completo" field.
  2. Select a valid Gender in the "Gênero" field.
  3. Enter a valid Email in the "Email" field.
  4. Enter a valid password in the "Senha" field.
  5. Enter a brief bio in the "Bio" field.
  6. Enter a valid phone number in the "Telefone" field.
  7. Enter a valid CPF number in the "CPF" field.
  8. Enter the correct course in the "Curso" field.
  9. Enter the university name in the "Universidade" field.
  10. Click the "Criar Conta" button.
- **Expected Results**: User is successfully registered, and a success message is displayed. The user is redirected to the login page.

### Test Case 2
- **Test Number**: TC002
- **Description**: Register with an already registered Email.
- **Prerequisites**: The user is on the registration page, and the Email is already registered.
- **Steps**:
  1. Enter valid details in all fields, but use an Email that is already registered.
  2. Click the "Criar Conta" button.
- **Expected Results**: An error message displays stating that the Email is already in use.

### Test Case 3 - BUG
- **Test Number**: TC003
- **Description**: Register with invalid Email format.
- **Prerequisites**: The user is on the registration page.
- **Steps**:
  1. Enter valid details in all fields except enter an invalid Email format.
  2. Click the "Criar Conta" button.
- **Expected Results**: An error message indicates that the Email format is invalid and prevents registration.

### Test Case 4 - NONSENSICAL
- **Test Number**: TC004
- **Description**: Register with a weak password.
- **Prerequisites**: The user is on the registration page.
- **Steps**:
  1. Enter valid details in all fields except enter a weak password such as "12345".
  2. Click the "Criar Conta" button.
- **Expected Results**: An error message indicates that the password is too weak and prevents registration. 

### Test Case 5
- **Test Number**: TC005
- **Description**: Attempt to register without filling any fields.
- **Prerequisites**: The user is on the registration page.
- **Steps**:
  1. Leave all fields empty.
  2. Click the "Criar Conta" button.
- **Expected Results**: Proper validation messages appear for each mandatory field, and registration is prevented.

### Test Case 6
- **Test Number**: TC006
- **Description**: Attempt to register with invalid CPF number.
- **Prerequisites**: The user is on the registration page.
- **Steps**:
  1. Enter valid details in all fields except enter an invalid CPF number.
  2. Click the "Criar Conta" button.
- **Expected Results**: An error message indicates that the CPF format is invalid and prevents registration.

### Test Case 7
- **Test Number**: TC007
- **Description**: Test SQL Injection in the registration fields.
- **Prerequisites**: The user is on the registration page.
- **Steps**:
  1. Enter valid details in all fields except use SQL injection strings like "'; DROP TABLE users; --" in all fields.
  2. Click the "Criar Conta" button.
- **Expected Results**: The system should sanitize inputs to prevent SQL injection and display an appropriate error message.

### Test Case 8 - BUG
- **Test Number**: TC008
- **Description**: Register user with the maximum allowed characters in all fields.
- **Prerequisites**: The user is on the registration page.
- **Steps**:
  1. Fill out all fields with the maximum allowed characters.
  2. Click the "Criar Conta" button.
- **Expected Results**: The user is successfully registered, or an error appears if the character limit exceeds the backend constraints.

### Test Case 9
- **Test Number**: TC009
- **Description**: Register user when the database is down.
- **Prerequisites**: The user is on the registration page, and database is not accessible.
- **Steps**:
  1. Enter valid details in all fields.
  2. Click the "Criar Conta" button.
- **Expected Results**: An error message displays indicating a database connection issue and preventing registration.

### Test Case 10
- **Test Number**: TC010
- **Description**: Verify if password encryption is applied during registration.
- **Prerequisites**: The user is on the registration page.
- **Steps**:
  1. Perform registration with valid details.
  2. Verify in the database if the password is encrypted.
- **Expected Results**: The password should not be stored in plain text in the database; it should be encrypted.

These test cases are designed to cover a variety of scenarios that could reveal potential bugs, edge cases, or security vulnerabilities in the "Register new user" feature of the "Par de Jarro" app.

