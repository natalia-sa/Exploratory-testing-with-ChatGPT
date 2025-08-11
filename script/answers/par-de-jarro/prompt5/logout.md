Here are some exploratory test cases for the logout feature in the Par de Jarro app:

### Test Case 1

- **Test Number:** TC001
- **Description:** Successful logout
- **Prerequisites:** User must be logged into the application.
- **Steps:**
  1. Navigate to the profile page.
  2. Click on the "Deslogar" (Logout) button.
- **Expected Results:** User is redirected to the login page and is no longer able to access the profile page without logging in again.

### Test Case 2

- **Test Number:** TC002
- **Description:** Attempt to access a secured page after logout
- **Prerequisites:** User must be logged into the application.
- **Steps:**
  1. Navigate to the profile page.
  2. Click on the "Deslogar" (Logout) button.
  3. Attempt to directly access the profile page via the URL.
- **Expected Results:** User is redirected to the login page or receives an unauthorized access message.

### Test Case 3

- **Test Number:** TC003
- **Description:** Logout and back navigation
- **Prerequisites:** User must be logged into the application.
- **Steps:**
  1. Navigate to the profile page.
  2. Click on the "Deslogar" (Logout) button.
  3. Click the browser's back button.
- **Expected Results:** User remains on the login page and does not have access to the profile page.

### Test Case 4

- **Test Number:** TC004
- **Description:** Multiple logout attempts
- **Prerequisites:** User must be logged into the application.
- **Steps:**
  1. Navigate to the profile page.
  2. Click on the "Deslogar" (Logout) button multiple times quickly.
- **Expected Results:** Application handles multiple logout attempts gracefully, and the user is logged out and redirected to the login page without errors.

### Test Case 5

- **Test Number:** TC005
- **Description:** Session expiration and logout
- **Prerequisites:** User must be logged into the application and session expiration must be configured.
- **Steps:**
  1. Wait for the user session to expire.
  2. Try to navigate to any secured page.
  3. Observe if the session expired message is provided or user is logged out automatically.
- **Expected Results:** User is automatically logged out and redirected to the login page when session expires.

### Test Case 6

- **Test Number:** TC006
- **Description:** Logout from different browser tabs/windows
- **Prerequisites:** User must be logged into the application on multiple tabs or windows of the same browser.
- **Steps:**
  1. Open the application in multiple browser tabs or windows.
  2. In one of the tabs (or windows), navigate to the profile page and click on the "Deslogar" (Logout) button.
  3. Try to navigate to a secured page from the other tabs (or windows).
- **Expected Results:** Logout should affect all tabs and windows, redirecting to the login page if a secured page is accessed.

### Test Case 7

- **Test Number:** TC007
- **Description:** Logout when database is not reachable
- **Prerequisites:** User must be logged into the application, and the database must momentarily become unreachable.
- **Steps:**
  1. Simulate database unreachability.
  2. Navigate to the profile page
  3. Click on the "Deslogar" (Logout) button.
- **Expected Results:** The application should handle the error gracefully, provide an appropriate error message, and user should be logged out from the session.

### Test Case 8 - NONSENSICAL

- **Test Number:** TC008
- **Description:** Logout while performing an ongoing action
- **Prerequisites:** User must be logged into the application and performing an action (e.g., updating a profile, sending a request).
- **Steps:**
  1. Initiate an action (e.g., start updating a profile).
  2. While the action is ongoing
  3. Click on the "Deslogar" (Logout) button.
- **Expected Results:** The logout completes successfully, and the user action should be canceled with an appropriate prompt or message.

### Test Case 9

- **Test Number:** TC009
- **Description:** Check for potential security issues - Attempt forceful browsing after logout
- **Prerequisites:** User must be logged into the application and logged out after usage.
- **Steps:**
  1. After logging out, use the browser history to try returning to a previously accessed secured URL.
- **Expected Results:** Application should not allow access to any secured page and should ensure the user is redirected to the login page.

### Test Case 10 - NONSENSICAL

- **Test Number:** TC010 
- **Description:** Logout with network fluctuation
- **Prerequisites:** User must be logged into the application.
- **Steps:**
  1. Simulate unstable network connection.
  2. Navigate to the profile page and click on the "Deslogar" (Logout) button.
- **Expected Results:** The application should handle network fluctuations gracefully, complete the logout process, and redirect the user to the login page.

