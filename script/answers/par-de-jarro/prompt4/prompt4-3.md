1. **Test Logout from Profile Page**
   - **Description:** Verify that the user can successfully log out from the Profile Page.
   - **Prerequisites:** User must be logged in and on the Profile Page.
   - **Steps:**
     1. Navigate to the Profile Page.
     2. Click on the Logout button (if available).
   - **Expected results:** User is successfully logged out and redirected to the login page.

2. **Test Logout During Profile Edit**
   - **Description:** Verify that the user can successfully log out while editing their profile.
   - **Prerequisites:** User must be logged in and on the Profile Page in edit mode.
   - **Steps:**
     1. Navigate to the Profile Page.
     2. Click the "Editar" (Edit) button to enable edit mode.
     3. Without saving changes, click on the Logout button.
   - **Expected results:** User is successfully logged out, any unsaved changes are discarded, and the user is redirected to the login page.

3. **Test Logout without Profile Data**
   - **Description:** Verify that the user can logout even if some profile fields are absent or left empty.
   - **Prerequisites:** User must be logged in and able to edit their profile.
   - **Steps:**
     1. Navigate to the Profile Page.
     2. Click the "Editar" (Edit) button to enable edit mode.
     3. Delete data from one or more fields, but do not save.
     4. Click on the Logout button.
   - **Expected results:** User is successfully logged out, with or without completed profile data, and redirected to the login page.

4. **Test Logout Upon Network Disconnect** SENSELESS
   - **Description:** Verify how the app handles logout when there is a network disconnection.
   - **Prerequisites:** User must be logged in and on the Profile Page.
   - **Steps:**
     1. Disconnect the network or disable internet access on the device.
     2. Attempt to click the Logout button.
   - **Expected results:** User should receive an appropriate error message indicating a network issue, and after re-establishing the connection, be able to logout successfully.

5. **Test Logout Button UI/UX Responsiveness**
   - **Description:** Verify the responsiveness and user feedback of the Logout button.
   - **Prerequisites:** User must be logged in and on the Profile Page.
   - **Steps:**
     1. Navigate to the Profile Page.
     2. Click the Logout button multiple times quickly.
   - **Expected results:** The Logout button should respond promptly to the click event, process the logout action only once, and redirect the user to the login page without multiple redirects or errors.

6. **Test Session Timeout While on Profile Page**
   - **Description:** Verify the functionality of the Logout feature if the session times out while the user is on the Profile Page.
   - **Prerequisites:** User must be logged in and on the Profile Page.
   - **Steps:**
     1. Wait for the user session to time out while on the Profile Page.
     2. After session timeout, click on the Logout button.
   - **Expected results:** The user should be redirected to the login page or receive a prompt that the session has expired, and they should re-login.

7. **Test Logout Functionality via Browser Back Button**
   - **Description:** Test the Logout functionality using the browser's back button.
   - **Prerequisites:** User must be logged in and on the Profile Page.
   - **Steps:**
     1. Navigate to the Profile Page.
     2. Click on the Logout button to logout and be redirected to the login page.
     3. Click the browser's back button.
   - **Expected results:** User should not be able to access the Profile Page again without logging in, and should be redirected to the login page or an appropriate message should be displayed.

8. **Test Simultaneous Logouts from Multiple Devices**
   - **Description:** Verify if logging out from one device logs out the user from other devices.
   - **Prerequisites:** User must be logged in on multiple devices.
   - **Steps:**
     1. Log in to the Profile Page on two different devices or browser tabs.
     2. Logout from one device/tab.
     3. Attempt to perform actions on the Profile Page from the second device/tab.
   - **Expected results:** Logging out from one device/tab should log out the user from the other device/tab as well, and actions attempted on the second device/tab should prompt for re-login.

   1 senseless
   0 bugs