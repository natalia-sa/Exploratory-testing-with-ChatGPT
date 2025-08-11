## Exploratory Test Cases for Update Location Service in ActivityDiary App

### Test Case 1:
- **Test Number**: 1
- **Description**: Verify that when the Location Service is set to "OFF", location tracking is disabled.
- **Prerequisites**: The app is installed and opened on the device.
- **Steps**: 
  1. Navigate to the "Settings" screen in the app.
  2. Select the "Location Service" field.
  3. Choose the "OFF" option.
  4. Attempt to access the "Update period" and "Update distance" fields.
- **Expected Results**: 
  - The "Location Service" setting should display "User location not tracked at all."
  - The "Update period" and "Update distance" fields should be disabled/greyed out.

### Test Case 2:
- **Test Number**: 2
- **Description**: Verify that when the Location Service is set to "Network", the user can update the "period" and "distance" settings.
- **Prerequisites**: The app is installed and opened on the device.
- **Steps**: 
  1. Navigate to the "Settings" screen in the app.
  2. Select the "Location Service" field.
  3. Choose the "Network" option.
  4. Attempt to update the "Update period" to a different value.
  5. Attempt to update the "Update distance" to a different value.
- **Expected Results**: 
  - The "Location Service" setting should display "Network used to track device location."
  - The "Update period" and "Update distance" fields should be enabled and the new values should be saved correctly.

### Test Case 3:
- **Test Number**: 3
- **Description**: Verify that when the Location Service is set to "GPS", the user can update the "period" and "distance" settings.
- **Prerequisites**: The app is installed and opened on the device.
- **Steps**: 
  1. Navigate to the "Settings" screen in the app.
  2. Select the "Location Service" field.
  3. Choose the "GPS" option.
  4. Attempt to update the "Update period" to a different value.
  5. Attempt to update the "Update distance" to a different value.
- **Expected Results**: 
  - The "Location Service" setting should display "GPS used to track device location."
  - The "Update period" and "Update distance" fields should be enabled and the new values should be saved correctly.

### Test Case 4:
- **Test Number**: 4
- **Description**: Verify the app's behavior when rapidly toggling between "OFF", "Network", and "GPS" options.
- **Prerequisites**: The app is installed and opened on the device.
- **Steps**: 
  1. Navigate to the "Settings" screen in the app.
  2. Quickly toggle the "Location Service" between "OFF", "Network", and "GPS" multiple times.
  3. Check the status of the "Update period" and "Update distance" fields after each toggle.
- **Expected Results**: 
  - The app should correctly update the "Location Service" status.
  - The "Update period" and "Update distance" fields should be enabled/disabled correspondingly without glitches or crashes.

### Test Case 5:
- **Test Number**: 5
- **Description**: Verify that valid values are accepted and saved for "Update period" and "Update distance".
- **Prerequisites**: The app is installed and opened on the device, Location Service is set to either "Network" or "GPS".
- **Steps**: 
  1. Navigate to the "Settings" screen in the app.
  2. Select the "Location Service" field and choose either "Network" or "GPS."
  3. Update the "Update period" to valid values within the accepted range (e.g., 1 minute, 10 minutes).
  4. Update the "Update distance" to valid values within the accepted range (e.g., 10 meters, 100 meters).
- **Expected Results**: 
  - The new values should be saved correctly and displayed after navigating away and returning to the settings.

### Test Case 6: - 2 BUGS
- **Test Number**: 6
- **Description**: Verify that invalid values are not accepted for "Update period" and "Update distance".
- **Prerequisites**: The app is installed and opened on the device, Location Service is set to either "Network" or "GPS".
- **Steps**: 
  1. Navigate to the "Settings" screen in the app.
  2. Select the "Location Service" field and choose either "Network" or "GPS."
  3. Attempt to update the "Update period" with invalid values (e.g., negative value, 0, text input).
  4. Attempt to update the "Update distance" with invalid values (e.g., negative value, 0, text input).
- **Expected Results**: 
  - An error message or validation feedback should be displayed, and the invalid values should not be accepted or saved.

### Test Case 7:
- **Test Number**: 7
- **Description**: Verify the UI elements and text are correctly displayed and aligned.
- **Prerequisites**: The app is installed and opened on the device.
- **Steps**: 
  1. Navigate to the "Settings" screen in the app.
  2. Observe the "Location Service," "Update period," and "Update distance" fields.
  3. Check text alignment, font size, and color consistency.
- **Expected Results**: 
  - All UI elements and text should be correctly displayed, properly aligned, and consistent in font size and color as per design specifications.

### Test Case 8:
- **Test Number**: 8
- **Description**: Verify behavior when the device is offline and user attempts to update location settings.
- **Prerequisites**: The app is installed and opened on the device. The device is set to airplane mode (offline).
- **Steps**: 
  1. Navigate to the "Settings" screen in the app.
  2. Select the "Location Service" field.
  3. Attempt to choose "Network" or "GPS" options.
  4. Attempt to update "Update period" and "Update distance."
- **Expected Results**: 
  - The app should either prevent changing location settings or show appropriate error messages indicating the device is offline.

### Test Case 9:
- **Test Number**: 9
- **Description**: Verify location updates are correctly handled when switching from "Network" to "GPS."
- **Prerequisites**: The app is installed and opened on the device, Location Service is set to "Network."
- **Steps**: 
  1. Navigate to the "Settings" screen in the app.
  2. Set the "Location Service" to "Network."
  3. Update "Update period" and "Update distance."
  4. Switch "Location Service" to "GPS."
  5. Check if the updated values for "Update period" and "Update distance" persist.
- **Expected Results**: 
  - The app should retain the updated values for "Update period" and "Update distance" and appropriately apply them when switching from "Network" to "GPS."

By conducting these tests, potential edge cases and unusual flows will be covered, and any possible bugs related to updating location services in the ActivityDiary app will be identified.