Sure! Here are the test cases for the Create Note feature in the Omni-Notes app:

### Test Case 1
- **Description**: Create a simple text note.
- **Prerequisites**: The Omni-Notes app must be installed, and the user should be on the note creation screen.
- **Steps**:
  1. Open the Omni-Notes app.
  2. Tap on the "Create Note" (+) button.
  3. Enter text into the "Título" (Title) field.
  4. Enter text into the "Conteúdo" (Content) field.
- **Expected results**: The note is created and saved automatically. Returning to the main screen should display the new note with the entered title and content.

### Test Case 2 BUG
- **Description**: Add an image to the note using the camera.
- **Prerequisites**: The Omni-Notes app must be installed, the camera must be in working condition, and the user should be on the note creation screen.
- **Steps**:
  1. Open the Omni-Notes app.
  2. Tap on the "Create Note" (+) button.
  3. Tap on the camera icon (first icon in the drop-down menu).
  4. Take a picture with the camera.
  5. Confirm the captured image.
- **Expected results**: The image is attached to the note and saved automatically.

### Test Case 3 BUG
- **Description**: Record a video and attach it to the note.
- **Prerequisites**: The Omni-Notes app must be installed, the camera must be in working condition, and the user should be on the note creation screen.
- **Steps**:
  1. Open the Omni-Notes app.
  2. Tap on the "Create Note" (+) button.
  3. Tap on the video camera icon (second icon in the drop-down menu).
  4. Record a video.
  5. Confirm the recorded video.
- **Expected results**: The video is attached to the note and saved automatically.

### Test Case 4
- **Description**: Add an audio recording to the note.
- **Prerequisites**: The Omni-Notes app must be installed, and the user should be on the note creation screen.
- **Steps**:
  1. Open the Omni-Notes app.
  2. Tap on the "Create Note" (+) button.
  3. Tap on the microphone icon (fifth icon in the drop-down menu).
  4. Record the audio.
  5. Stop and confirm the audio recording.
- **Expected results**: The audio recording is attached to the note and saved automatically.

### Test Case 5
- **Description**: Add a sketch to the note.
- **Prerequisites**: The Omni-Notes app must be installed, and the user should be on the note creation screen.
- **Steps**:
  1. Open the Omni-Notes app.
  2. Tap on the "Create Note" (+) button.
  3. Tap on the sketch icon (sixth icon in the drop-down menu).
  4. Draw a simple sketch.
  5. Save the sketch.
- **Expected results**: The sketch is attached to the note and saved automatically.

### Test Case 6 BUG
- **Description**: Add a location to the note.
- **Prerequisites**: The Omni-Notes app must be installed, and GPS/location services must be enabled on the Android device. The user should be on the note creation screen.
- **Steps**:
  1. Open the Omni-Notes app.
  2. Tap on the "Create Note" (+) button.
  3. Tap on the location icon (seventh icon in the drop-down menu).
  4. Confirm the current location.
- **Expected results**: The location is attached to the note and saved automatically.

### Test Case 7
- **Description**: Attach a file to the note.
- **Prerequisites**: The Omni-Notes app must be installed, and the user should be on the note creation screen. There should be files stored on the device.
- **Steps**:
  1. Open the Omni-Notes app.
  2. Tap on the "Create Note" (+) button.
  3. Tap on the file icon (fourth icon in the drop-down menu).
  4. Browse for and select a file to attach.
- **Expected results**: The file is attached to the note and saved automatically.

### Test Case 8 BUG
- **Description**: Add a reminder to the note.
- **Prerequisites**: The Omni-Notes app must be installed, and the user should be on the note creation screen.
- **Steps**:
  1. Open the Omni-Notes app.
  2. Tap on the "Create Note" (+) button.
  3. Tap on "Adicionar lembrete" (Add reminder).
  4. Set a reminder for the note.
  5. Save the reminder.
- **Expected results**: The reminder is added, and the note is saved along with the reminder.

### Test Case 9
- **Description**: Create a note with a very long title and content.
- **Prerequisites**: The Omni-Notes app must be installed, and the user should be on the note creation screen.
- **Steps**:
  1. Open the Omni-Notes app.
  2. Tap on the "Create Note" (+) button.
  3. Enter a very long text into the "Título" (Title) field.
  4. Enter a very long text into the "Conteúdo" (Content) field.
- **Expected results**: The note is created and saved automatically with all the text correctly displayed in the note list.

### Test Case 10 maybe senseless
- **Description**: Customize the appearance of the note with different fonts and colors.
- **Prerequisites**: The Omni-Notes app must be installed, and the user should be on the note creation screen.
- **Steps**:
  1. Open the Omni-Notes app.
  2. Tap on the "Create Note" (+) button.
  3. Customize the note by changing the font and background colors (if such options exist within the app).
- **Expected results**: The note customization is applied and saved automatically.

These tests cover various functionalities and edge cases for the Create Note feature in the Omni-Notes app on an Android device.