# Secondary prompt 14

"
From the point of view of a tester, give me exploratory test cases to the Support Modal feature in the readme generator app, suggesting unusual flows, trying to find possible bugs, failures, security issues, etc. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test results
"

## Images

readme2.png, readme6.png

### Answer

### Test Case 1
- **Description:** Test the Support Modal with no input and check for error handling
- **Prerequisites:** Support Modal feature must be enabled on the app
- **Steps:**
  1. Click on the support button to open the Support Modal.
  2. Leave the "Name or @yoursocial" field empty.
  3. Leave the "Say something nice..." field empty.
  4. Click the "Support $5" button without inputting any details.
- **Expected Results:** 
  An error message should appear requesting the user to fill in the necessary fields or indicate why a name is not needed.

### Test Case 2
- **Description:** Test maximum input limits for the "Name or @yoursocial" field
- **Prerequisites:** Support Modal feature must be enabled on the app
- **Steps:**
  1. Click on the support button to open the Support Modal.
  2. Enter a string of maximum length (e.g., 256 characters) into the "Name or @yoursocial" field.
  3. Enter a simple message in the "Say something nice..." field.
  4. Click the "Support $5" button.
- **Expected Results:** 
  The Modal should handle the maximum input without crashing or truncating. The support is successfully submitted.

### Test Case 3 
- **Description:** Test SQL Injection in the "Name or @yoursocial" field
- **Prerequisites:** Support Modal feature must be enabled on the app
- **Steps:**
  1. Click on the support button to open the Support Modal.
  2. Enter a common SQL injection string like `'; DROP TABLE Users; --` in the "Name or @yoursocial" field.
  3. Enter a simple message in the "Say something nice..." field.
  4. Click the "Support $5" button.
- **Expected Results:** 
  The application should sanitize inputs and reject harmful scripts, displaying an error message if necessary but not breaking functionality.

### Test Case 4
- **Description:** Verify special characters are properly handled in the "Say something nice..." text
- **Prerequisites:** Support Modal feature must be enabled on the app
- **Steps:**
  1. Click on the support button to open the Support Modal.
  2. Enter a valid name in the "Name or @yoursocial" field.
  3. Enter a text string containing special characters like `<script>test</script>` in the "Say something nice..." field.
  4. Click the "Support $5" button.
- **Expected Results:** 
  The Modal should sanitize special characters to prevent XSS and display the text as plain text without executing it.

### Test Case 5
- **Description:** Test the Support Modal's behavior under intermittent network conditions
- **Prerequisites:** Support Modal feature must be enabled, and network throttling tools should be available
- **Steps:**
  1. Click on the support button to open the Support Modal.
  2. Enter the appropriate details in both fields.
  3. Enable network throttling or disconnect the network intermittently.
  4. Click the "Support $5" button.
- **Expected Results:** 
  The app should handle the intermittent network gracefully, possibly showing a loading indicator or retry option without losing the entered data.

### Test Case 6 
- **Description:** Check for proper validation and error messages under unusual input combinations
- **Prerequisites:** Support Modal feature must be enabled on the app
- **Steps:**
  1. Click on the support button to open the Support Modal.
  2. Enter a mix of valid and invalid strings in the "Name or @yoursocial" field (e.g., "John123 @example.com").
  3. Enter an empty string in the "Say something nice..." field.
  4. Click the "Support $5" button.
- **Expected Results:** 
  The Modal should validate the input correctly and show appropriate error messages indicating which field is incorrect or if the message field is required.

### Test Case 7 
- **Description:** Test the Support Modal for Cross-Site Request Forgery (CSRF) prevention
- **Prerequisites:** Support Modal feature must be enabled and the backend should have CSRF protection mechanisms
- **Steps:**
  1. Open the Support Modal.
  2. Using browser developer tools, attempt to intercept and alter the request token or send a request from an unauthorized site.
  3. Submit the support request.
- **Expected Results:** 
  The request should be rejected if CSRF validation fails, ensuring unauthorized actions cannot be performed.

These exploratory tests cover a range of unusual and potentially disruptive workflow scenarios aimed at ensuring the Support Modal is robust against common issues and security vulnerabilities.

0 bugs
0 senseless