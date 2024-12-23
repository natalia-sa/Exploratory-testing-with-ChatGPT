1.
- Description: Verify that the app correctly enables and disables crash reporting.
- Prerequisites: App must be installed and running. User must be on the "Settings" screen.
- Steps:
  1. Navigate to the "Settings" menu in the app.
  2. Locate the "Crash Reporting" toggle switch.
  3. Toggle the switch to the off position.
  4. Verify that crash reporting is disabled.
  5. Toggle the switch to the on position.
  6. Verify that crash reporting is enabled.
- Expected results: The "Crash Reporting" toggle should enable and disable report sending as expected.

2.
- Description: Validate that the "Location Service" functionality is working properly.
- Prerequisites: App must be installed and running. User must be on the "Settings" screen. GPS must be enabled on the device.
- Steps:
  1. Navigate to the "Settings" menu in the app.
  2. Verify that the "Location Service" setting is present.
  3. Toggle the "Location Service" on/off if applicable.
  4. Verify the app requests and tracks location updates according to the "Update period" and "Update distance" settings.
- Expected results: The app should appropriately request and use the device's location services.

3.
- Description: Verify that the "Update period" setting adjusts the frequency of location updates.
- Prerequisites: App must be installed and running. User must be on the "Settings" screen. 
- Steps:
  1. Navigate to the "Settings" menu in the app.
  2. Locate the "Update period" setting.
  3. Change the update period to a different value (e.g., 10 minutes).
  4. Perform activities that require location updates.
  5. Observe if the app requests location updates based on the new frequency setting.
- Expected results: The app should request location updates according to the new update period value.

4.
- Description: Verify that changing the "Update distance" setting updates the distance requirement for location updates.
- Prerequisites: App must be installed and running. User must be on the "Settings" screen.
- Steps:
  1. Navigate to the "Settings" menu in the app.
  2. Locate the "Update distance" setting.
  3. Change the update distance to a different value (e.g., 100 meters).
  4. Perform activities that involve moving distances.
  5. Observe if the app requests location updates based on the new distance setting.
- Expected results: The app should request location updates according to the new update distance value.

5.
- Description: Validate that the "Picture Storage Folder" setting specifies the correct directory for storing photos.
- Prerequisites: App must be installed and running. User must be on the "Settings" screen.
- Steps:
  1. Navigate to the "Settings" menu in the app.
  2. Locate the "Picture Storage Folder" setting.
  3. Confirm the directory is set to "ActivityDiary" or change it.
  4. Take a photo using the app.
  5. Check the specified directory to confirm the photo is stored there.
- Expected results: The photo should be stored in the specified directory defined by the "Picture Storage Folder" setting.