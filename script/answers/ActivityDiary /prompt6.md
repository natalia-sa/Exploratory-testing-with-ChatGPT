Here are the test cases for the "update Location Service" feature in the ActivityDiary app, formatted according to the specified structure:

### Test Case 1
- **Description**: Verify that the user can select the “off” option for Location Service.
- **Prerequisites**: The app is installed and opened on an Android cell phone.
- **Steps**:
  1. Open the ActivityDiary app.
  2. Navigate to the Settings section.
  3. Locate the “Location Service” setting.
  4. Select the “off” option.
- **Expected Result**: The Location Service is set to "off" and no other options for updating period and distance information are presented.

### Test Case 2
- **Description**: Verify that the user can select the “network” option for Location Service.
- **Prerequisites**: The app is installed and opened on an Android cell phone.
- **Steps**:
  1. Open the ActivityDiary app.
  2. Navigate to the Settings section.
  3. Locate the “Location Service” setting.
  4. Select the “network” option.
- **Expected Result**: The Location Service is set to "network" and options for updating “period” and “distance” become available for editing.

### Test Case 3
- **Description**: Verify that the user can select the “GPS” option for Location Service.
- **Prerequisites**: The app is installed and opened on an Android cell phone.
- **Steps**:
  1. Open the ActivityDiary app.
  2. Navigate to the Settings section.
  3. Locate the “Location Service” setting.
  4. Select the “GPS” option.
- **Expected Result**: The Location Service is set to "GPS" and options for updating “period” and “distance” become available for editing.

### Test Case 4
- **Description**: Verify that the user can update the “period” when Location Service is set to “network”.
- **Prerequisites**: The app is installed and opened on an Android cell phone, with Location Service set to “network”.
- **Steps**:
  1. Select the “network” option for Location Service.
  2. Locate and select the “Update period” option.
  3. Change the update period.
  4. Save the settings.
- **Expected Result**: The update period is changed successfully. The new period is displayed correctly.

### Test Case 5
- **Description**: Verify that the user can update the “distance” when Location Service is set to “network”.
- **Prerequisites**: The app is installed and opened on an Android cell phone, with Location Service set to “network”.
- **Steps**:
  1. Select the “network” option for Location Service.
  2. Locate and select the “Update distance” option.
  3. Change the update distance.
  4. Save the settings.
- **Expected Result**: The update distance is changed successfully. The new distance is displayed correctly.

### Test Case 6
- **Description**: Verify that the user can update the “period” when Location Service is set to “GPS”.
- **Prerequisites**: The app is installed and opened on an Android cell phone, with Location Service set to “GPS”.
- **Steps**:
  1. Select the “GPS” option for Location Service.
  2. Locate and select the “Update period” option.
  3. Change the update period.
  4. Save the settings.
- **Expected Result**: The update period is changed successfully. The new period is displayed correctly.

### Test Case 7
- **Description**: Verify that the user can update the “distance” when Location Service is set to “GPS”.
- **Prerequisites**: The app is installed and opened on an Android cell phone, with Location Service set to “GPS”.
- **Steps**:
  1. Select the “GPS” option for Location Service.
  2. Locate and select the “Update distance” option.
  3. Change the update distance.
  4. Save the settings.
- **Expected Result**: The update distance is changed successfully. The new distance is displayed correctly.

### Test Case 8
- **Description**: Check that update period and distance values persist after restarting the app when Location Service is set to "network".
- **Prerequisites**: The app is installed and opened on an Android cell phone, with Location Service set to “network”. Update period and distance values are set.
- **Steps**:
  1. Set the update period and distance values.
  2. Restart the app.
  3. Navigate back to Settings to check the “Location Service” options.
- **Expected Result**: The previously set update period and distance values should persist even after restarting the app.

### Test Case 9
- **Description**: Check that update period and distance values persist after restarting the app when Location Service is set to "GPS".
- **Prerequisites**: The app is installed and opened on an Android cell phone, with Location Service set to “GPS”. Update period and distance values are set.
- **Steps**:
  1. Set the update period and distance values.
  2. Restart the app.
  3. Navigate back to Settings to check the “Location Service” options.
- **Expected Result**: The previously set update period and distance values should persist even after restarting the app.

### Test Case 10
- **Description**: Verify boundary values for “update period” when Location Service is set to “network”.
- **Prerequisites**: The app is installed and opened on an Android cell phone, with Location Service set to “network”.
- **Steps**:
  1. Select the “network” option for Location Service.
  2. Change the update period to the minimum acceptable value.
  3. Change the update period to the maximum acceptable value.
- **Expected Result**: The app should accept both the minimum and maximum values for update period and validate accordingly.

### Test Case 11
- **Description**: Verify boundary values for “update distance” when Location Service is set to “network”.
- **Prerequisites**: The app is installed and opened on an Android cell phone, with Location Service set to “network”.
- **Steps**:
  1. Select the “network” option for Location Service.
  2. Change the update distance to the minimum acceptable value.
  3. Change the update distance to the maximum acceptable value.
- **Expected Result**: The app should accept both the minimum and maximum values for update distance and validate accordingly.

### Test Case 12
- **Description**: Verify boundary values for “update period” when Location Service is set to “GPS”.
- **Prerequisites**: The app is installed and opened on an Android cell phone, with Location Service set to “GPS”.
- **Steps**:
  1. Select the “GPS” option for Location Service.
  2. Change the update period to the minimum acceptable value.
  3. Change the update period to the maximum acceptable value.
- **Expected Result**: The app should accept both the minimum and maximum values for update period and validate accordingly.

### Test Case 13
- **Description**: Verify boundary values for “update distance” when Location Service is set to “GPS”.
- **Prerequisites**: The app is installed and opened on an Android cell phone, with Location Service set to “GPS”.
- **Steps**:
  1. Select the “GPS” option for Location Service.
  2. Change the update distance to the minimum acceptable value.
  3. Change the update distance to the maximum acceptable value.
- **Expected Result**: The app should accept both the minimum and maximum values for update distance and validate accordingly.

### Test Case 14
- **Description**: Check for unexpected app behavior when switching rapidly between “off”, “network”, and “GPS” options for Location Service.
- **Prerequisites**: The app is installed and opened on an Android cell phone.
- **Steps**:
  1. Switch between “off”, “network”, and “GPS” options rapidly.
  2. Ensure each switch registers before moving to the next setting.
- **Expected Result**: The app should accommodate rapid switching without crashing or showing unexpected behavior.

### Test Case 15 2 bugs
- **Description**: Verify app stability when inputting extreme or invalid values for “update period” and “update distance”.
- **Prerequisites**: The app is installed and opened on an Android cell phone.
- **Steps**:
  1. Set Location Service to “network” or “GPS”.
  2. Input extreme or invalid values for “update period” (e.g., negative numbers, excessively high values).
  3. Input extreme or invalid values for “update distance” (e.g., negative numbers, non-numeric inputs).
- **Expected Result**: The app should handle invalid inputs gracefully, providing appropriate error messages and preventing invalid data from being saved.

These test cases cover a range of scenarios, including standard functionality, edge cases, and potential areas for bugs or unexpected behavior in the update Location Service feature of the ActivityDiary app.