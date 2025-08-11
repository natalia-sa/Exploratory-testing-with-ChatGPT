## Test Case 1
- **Test number**: 1
- **Description**: Creating a text note with a title and content
- **Prerequisites**: The app is installed and opened
- **Steps**:
  1. Tap on the "Nota de texto" button.
  2. Enter a title in the "Título" field.
  3. Enter content in the "Conteúdo" field.
- **Expected results**: The note should be created and saved automatically after filling in any field.

## Test Case 2 - BUG
- **Test number**: 2
- **Description**: Creating a text note with an attachment from the camera
- **Prerequisites**: The app is installed and opened
- **Steps**:
  1. Tap on the "Nota de texto" button.
  2. Tap on the attachment icon and select "Câmera".
  3. Capture a photo using the camera.
  4. Ensure the photo is attached to the note.
  5. Enter a title and content.
- **Expected results**: The note should be saved automatically and the captured photo should be attached successfully.

## Test Case 3 - BUG
- **Test number**: 3
- **Description**: Creating a text note with an attachment from video
- **Prerequisites**: The app is installed and opened
- **Steps**:
  1. Tap on the "Nota de texto" button.
  2. Tap on the attachment icon and select "Vídeo".
  3. Record a video using the camera.
  4. Ensure the video is attached to the note.
  5. Enter a title and content.
- **Expected results**: The note should be saved automatically and the recorded video should be attached successfully.

## Test Case 4
- **Test number**: 4
- **Description**: Creating a text note with an attachment from files
- **Prerequisites**: The app is installed and opened, and there are files in the device storage
- **Steps**:
  1. Tap on the "Nota de texto" button.
  2. Tap on the attachment icon and select "Arquivos".
  3. Choose a file from the device storage.
  4. Ensure the file is attached to the note.
  5. Enter a title and content.
- **Expected results**: The note should be saved automatically and the selected file should be attached successfully.

## Test Case 5
- **Test number**: 5
- **Description**: Creating a text note with a voice recording attachment
- **Prerequisites**: The app is installed and opened
- **Steps**:
  1. Tap on the "Nota de texto" button.
  2. Tap on the attachment icon and select "Gravar".
  3. Record a voice memo.
  4. Ensure the voice memo is attached to the note.
  5. Enter a title and content.
- **Expected results**: The note should be saved automatically and the voice recording should be attached successfully.

## Test Case 6
- **Test number**: 6
- **Description**: Creating a text note with a sketch attachment
- **Prerequisites**: The app is installed and opened
- **Steps**:
  1. Tap on the "Nota de texto" button.
  2. Tap on the attachment icon and select "Esboço".
  3. Draw a sketch.
  4. Ensure the sketch is attached to the note.
  5. Enter a title and content.
- **Expected results**: The note should be saved automatically and the sketch should be attached successfully.

## Test Case 7 - BUG
- **Test number**: 7
- **Description**: Creating a text note with a location attachment
- **Prerequisites**: The app is installed and opened, and the device's location services are turned on
- **Steps**:
  1. Tap on the "Nota de texto" button.
  2. Tap on the attachment icon and select "Localização".
  3. Select the current location.
  4. Ensure the location is attached to the note.
  5. Enter a title and content.
- **Expected results**: The note should be saved automatically and the location should be attached successfully.

## Test Case 8 - BUG
- **Test number**: 8
- **Description**: Creating a text note with an attachment from Pushbullet
- **Prerequisites**: The app is installed and opened, and Pushbullet is configured on the device
- **Steps**:
  1. Tap on the "Nota de texto" button.
  2. Tap on the attachment icon and select "Pushbullet".
  3. Choose an item from Pushbullet.
  4. Ensure the item is attached to the note.
  5. Enter a title and content.
- **Expected results**: The note should be saved automatically and the Pushbullet item should be attached successfully.

## Test Case 9
- **Test number**: 9
- **Description**: Creating a note without any content or title
- **Prerequisites**: The app is installed and opened
- **Steps**:
  1. Tap on the "Nota de texto" button.
  2. Leave both the title and content fields empty.
- **Expected results**: The note should not be created, or if it is created, it should be handled gracefully by the app without causing any crashes or unexpected behaviors.

## Test Case 10
- **Test number**: 10
- **Description**: Editing an existing note and verifying automatic save
- **Prerequisites**: A note with a title and content already exists
- **Steps**:
  1. Open the existing note.
  2. Modify the title and content.
- **Expected results**: The changes should be saved automatically without the need to manually save.

## Test Case 11 - BUG
- **Test number**: 11
- **Description**: Test creating a note and use the reminder.
- **Prerequisites**: The app must be able to access device notifications.
- **Steps**:
  1. Open the Omni-Notes app.
  2. Select the Create Note icon.
  3. Provide a title and/or note content.
  4. Choose Add Reminder to set a notification for the note.
- **Expected Results**: The note should be automatically saved with the reminder, displayed in the notes list, and trigger a notification at the scheduled reminder time.

## Test Case 12
- **Test number**: 12
- **Description**: Verifying that the notes are saved across app restarts
- **Prerequisites**: The app is installed and opened
- **Steps**:
  1. Tap on the "Nota de texto" button.
  2. Enter a title and content.
  3. Close the app.
  4. Restart the app.
- **Expected results**: The note created before restarting the app should be present and intact.

