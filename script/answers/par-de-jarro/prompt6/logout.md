Sure! Here's a list of exploratory test cases for the logout feature in the Par de Jarro app:

### Test Case 1
- **Test Number:** TC001
- **Description:** Test logout functionality from the profile page.
- **Prerequisites:** User is logged in and on the Profile page.
- **Steps:**
  1. Navigate to `localhost:3000/userConfig`.
  2. Click on the "Deslogar" (Logout) button.
- **Expected Results:** User is logged out and redirected to the login page at `localhost:3000/signIn`.

### Test Case 2
- **Description:** Test logout functionality on different browser (Chrome).
- **Prerequisites:** User is logged in on Chrome and on the Profile page.
- **Steps:**
  1. Open Chrome, navigate to `localhost:3000/userConfig`.
  2. Click on the "Deslogar" button.
- **Expected Results:** User is logged out and redirected to the login page at `localhost:3000/signIn`.

### Test Case 3
- **Description:** Test if logout stops user from navigating to a protected page directly afterward.
- **Prerequisites:** User is logged in and on the Profile page.
- **Steps:**
  1. Navigate to `localhost:3000/userConfig`.
  2. Click on the "Deslogar" button.
  3. After being redirected to the login page, enter URL `localhost:3000/userConfig` directly in the address bar and press Enter.
- **Expected Results:** User remains on the login page and is not navigated to the profile page or any other protected pages.

### Test Case 4 - NONSENSICAL
- **Description:** Test logout functionality when network disconnects immediately after clicking logout.
- **Prerequisites:** User is logged in and on the Profile page.
- **Steps:**
  1. Navigate to `localhost:3000/userConfig`.
  2. Click on the "Deslogar" button.
  3. Immediately disconnect the internet.
- **Expected Results:** Appropriate error message should be displayed or process handled gracefully. Once the connection is restored, the user should be logged out and redirected to the login page.

### Test Case 5
- **Description:** Test multiple tabs handling for logout.
- **Prerequisites:** User is logged in and has multiple tabs open within the app.
- **Steps:**
  1. Open multiple tabs and navigate to different pages of the app.
  2. In one of the tabs, navigate to `localhost:3000/userConfig`.
  3. Click on the "Deslogar" button.
- **Expected Results:** User should be logged out from all the opened tabs and redirected to the login page when interactions are attempted on any tab.

### Test Case 6 
- **Description:** Test logout functionality for a session timeout scenario.
- **Prerequisites:** User is logged in and on any page of the app.
- **Steps:**
  1. Keep the user session alive until timeout.
  2. Try interacting with various elements in the app.
  3. Now click on the "Deslogar" button.
- **Expected Results:** The session should be invalidated, and the user should be redirected to the login page, with a proper timeout message.

### Test Case 7 - NONSENSICAL
- **Description:** Test logout security by checking cookie/session deletion.
- **Prerequisites:** User is logged in and on the Profile page.
- **Steps:**
  1. Open browser developer tools and go to the application tab.
  2. Navigate to `localhost:3000/userConfig`.
  3. Observe cookie/session storage.
  4. Click on the "Deslogar" button.
- **Expected Results:** Relevant session cookies should be deleted or expired.

### Test Case 8
- **Description:** Verify logout under high load conditions.
- **Prerequisites:** Multiple users logged in the system simultaneously.
- **Steps:**
  1. Simulate multiple users logging in.
  2. Log out from one of the user accounts by navigating to `localhost:3000/userConfig` and clicking on "Deslogar".
- **Expected Results:** User should be successfully logged out and redirected to the login page without performance degradation or errors.

### Test Case 9
- **Description:** Test logout functionality with browser back button after logout.
- **Prerequisites:** User is logged in and on the Profile page.
- **Steps:**
  1. Navigate to `localhost:3000/userConfig`.
  2. Click on the "Deslogar" button.
  3. Click on the browser back button.
- **Expected Results:** User should remain logged out and redirected back to the login page, not to the previous logged-in state.

### Test Case 10
- **Description:** Test logout functionality while performing a critical operation.
- **Prerequisites:** User is logged in and performing some operation.
- **Steps:**
  1. Start a transaction or operation (like adding a new location).
  2. While the operation is ongoing, navigate to `localhost:3000/userConfig`.
  3. Click on the "Deslogar" button.
- **Expected Results:** User should be prompted to confirm logging out and warned about unsaved changes.

By following these test cases, you can ensure that the logout functionality in the Par de Jarro app is robust, secure, and behaves as expected under various conditions.

