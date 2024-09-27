Sure, here are a set of test cases for the Logout feature in the app “Par de Jarro”:

---

**Test Case 1**
- **Description:** Verify that a user can successfully log out from the profile page.
- **Prerequisites:** User must be logged in and on the profile page.
- **Steps:**
  1. Navigate to the profile page.
  2. Click on the logout button/icon.
- **Expected Results:** The user should be redirected to the login page.

---

**Test Case 2** - SENSELESS
- **Description:** Verify that the logout option is available and clickable on every main user interface page.
- **Prerequisites:** User must be logged in and navigate through various main pages.
- **Steps:**
  1. Navigate to profile page.
  2. Ensure the logout button/icon is visible and clickable.
  3. Repeat step 1 and 2 for other main pages (e.g., dashboard, settings, messages, etc.).
- **Expected Results:** The logout option should be visible and clickable on every main page and should log the user out when clicked.

---

**Test Case 3**
- **Description:** Verify that the user session is cleared after logout.
- **Prerequisites:** User must be logged in.
- **Steps:**
  1. Click on the logout button/icon.
  2. Try accessing the user profile URL directly from the browser after logging out.
- **Expected Results:** The user should be redirected to the login page when attempting to access secured pages directly after logout.

---

**Test Case 4**
- **Description:** Verify login page displays appropriate confirmation message after logout.
- **Prerequisites:** User must be logged in.
- **Steps:**
  1. Click on the logout button/icon.
  2. Observe the feedback message on the login page.
- **Expected Results:** A confirmation message such as "You have successfully logged out" should be displayed on the login page.

---

**Test Case 5**
- **Description:** Verify logout functionality when there are unsaved changes in the profile.
- **Prerequisites:** User must be logged in and make unsaved changes in the profile.
- **Steps:**
  1. Make changes in the profile (e.g., change email, phone, etc.) but do not save.
  2. Click on the logout button/icon.
- **Expected Results:** The user should either receive a warning about unsaved changes or the changes should be discarded upon logging out. The user should be redirected to the login page.

---

**Test Case 6** SENSELESS
- **Description:** Verify logout functionality in case of network failure during logout process.
- **Prerequisites:** User must be logged in.
- **Steps:**
  1. Disconnect the network or simulate a network failure.
  2. Click on the logout button/icon.
- **Expected Results:** User should receive an error message indicating network issues and should remain on the same page.

---

**Test Case 7**
- **Description:** Verify that the user remains logged out after closing and reopening the app following logout.
- **Prerequisites:** User must be logged in.
- **Steps:**
  1. Click on the logout button/icon.
  2. Close the app.
  3. Reopen the app and attempt to navigate to the profile page.
- **Expected Results:** The user should be prompted to log in again upon reopening the app.

---

**Test Case 8**
- **Description:** Verify multiple login sessions and logout on one device.
- **Prerequisites:** The user must have their credentials and an additional device.
- **Steps:**
  1. Login on Device A.
  2. Login on Device B.
  3. Logout from Device A.
  4. Attempt to access protected content on Device B.
- **Expected Results:** The user should still be logged in on Device B and able to access protected content. 

---

These test cases aim to cover different potential scenarios, including edge cases, to ensure the logout functionality works correctly under various conditions.

2 senseless
0 bugs