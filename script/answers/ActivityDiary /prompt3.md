### Test Case 1
- **Description:** Test the behavior when updating the location service while toggling crash reporting on/off.
- **Prerequisites:** Ensure the app is installed, and the settings page shown in the screenshot is accessible.
- **Steps:**
  1. Open the app.
  2. Navigate to the "Settings" page.
  3. Toggle "Crash Reporting" off.
  4. Change the "Location Service" to another option (e.g., from Network to GPS).
  5. Toggle "Crash Reporting" on.
  6. Change the "Location Service" back to the original setting.
- **Expected results:** The app should allow toggling "Crash Reporting" while changing "Location Service" without any crashes or freezing. Both settings should update correctly according to user selection.

### Test Case 2 - 2 bugs
- **Description:** Test updating the location update period and distance with invalid values.
- **Prerequisites:** Ensure the app is installed, network/GPS is enabled, and the settings page shown in the screenshot is accessible.
- **Steps:**
  1. Open the app.
  2. Navigate to the "Settings" page.
  3. Attempt to set the "Update period" to an invalid value, such as a non-numeric string or negative number.
  4. Attempt to set the "Update distance" to an invalid value, such as a non-numeric string or negative number.
- **Expected results:** The app should validate input and display an error message or prohibit setting invalid values for both "Update period" and "Update distance."

### Test Case 3 SENSELESS
- **Description:** Test the app response when the storage directory for the picture storage folder is not accessible.
- **Prerequisites:** Ensure the app is installed, and the settings page shown in the screenshot is accessible. Restrict access to the directory `/ActivityDiary`.
- **Steps:**
  1. Open the app.
  2. Navigate to the "Settings" page.
  3. Attempt to save a picture in the "Picture Storage Folder" directory.
- **Expected results:** The app should handle the restricted access gracefully by displaying an appropriate error message, and it should not crash.

### Test Case 4
- **Description:** Test the app’s behavior with simultaneous updates to location period and distance.
- **Prerequisites:** Ensure the app is installed, location service is enabled, and the settings page shown in the screenshot is accessible.
- **Steps:**
  1. Open the app.
  2. Navigate to the "Settings" page.
  3. Set the "Update period" to a high-frequency value (e.g., every 1 minute).
  4. Set the "Update distance" to a small value (e.g., every 10 meters).
  5. Observe whether the app tracks location correctly and without any delay or lag.
- **Expected results:** The app should update the location as per the specified period and distance, and it should not affect performance negatively.

### Test Case 5
- **Description:** Test the app behavior when chaotic actions are performed on the settings.
- **Prerequisites:** Ensure the app is installed and the settings page shown in the screenshot is accessible.
- **Steps:**
  1. Open the app.
  2. Navigate to the "Settings" page.
  3. Rapidly toggle "Crash Reporting" on/off multiple times.
  4. Rapidly switch "Location Service" options multiple times.
  5. Quickly update "Update period" and "Update distance" to various valid values within a short span.
- **Expected results:** The app should handle rapid changes correctly without crashing, freezing, or showing erroneous behavior. It should apply the last valid settings correctly.

These exploratory test cases will help uncover potential issues and edge cases within the "ActivityDiary" app, ensuring higher reliability and usability.