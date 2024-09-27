Let's create exploratory test cases for the Create Text Note feature in the Omni-Notes app.

### Test Case 1
**Description**: Test creating a simple text note with a title and content.
**Prerequisites**: The app should be installed and running on the device.
**Steps**:
1. Open the Omni-Notes app.
2. Tap the "Create Note" icon.
3. Enter a title in the "Título" field.
4. Enter some content in the "Conteúdo" field.
**Expected Results**: The note should be saved automatically and visible in the list of notes.

### Test Case 2
**Description**: Test creation of a note with a title but no content.
**Prerequisites**: The app should be installed and running on the device.
**Steps**:
1. Open the Omni-Notes app.
2. Tap the "Create Note" icon.
3. Enter a title in the "Título" field.
4. Leave the "Conteúdo" field empty.
**Expected Results**: The note should be saved automatically and visible in the list of notes with only the title.

### Test Case 3
**Description**: Test creation of a note with content but no title.
**Prerequisites**: The app should be installed and running on the device.
**Steps**:
1. Open the Omni-Notes app.
2. Tap the "Create Note" icon.
3. Leave the "Título" field empty.
4. Enter some content in the "Conteúdo" field.
**Expected Results**: The note should be saved automatically and visible in the list of notes with only the content.

### Test Case 4 BUG
**Description**: Test adding an image to a note.
**Prerequisites**: The app should have access to the device camera and storage.
**Steps**:
1. Open the Omni-Notes app.
2. Tap the "Create Note" icon.
3. Tap the "Attachment" icon (paperclip).
4. Select "Câmera" and take a photo, or select "Arquivos" to choose an existing image.
5. Enter a title and/or content.
**Expected Results**: The note should be saved automatically with the attached image and visible in the list of notes.

### Test Case 5 BUG
**Description**: Test adding a video to a note.
**Prerequisites**: The app should have access to the device's camera and storage.
**Steps**:
1. Open the Omni-Notes app.
2. Tap the "Create Note" icon.
3. Tap the "Attachment" icon (paperclip).
4. Select "Vídeo" and record a video, or select "Arquivos" to choose an existing video.
5. Enter a title and/or content.
**Expected Results**: The note should be saved automatically with the attached video and visible in the list of notes.

### Test Case 6
**Description**: Test adding an audio recording to a note.
**Prerequisites**: The app should have access to the device's microphone.
**Steps**:
1. Open the Omni-Notes app.
2. Tap the "Create Note" icon.
3. Tap the "Attachment" icon (paperclip).
4. Select "Gravar" and record an audio note.
5. Enter a title and/or content.
**Expected Results**: The note should be saved automatically with the attached audio recording and visible in the list of notes.

### Test Case 7
**Description**: Test adding a sketch to a note.
**Prerequisites**: The app should be installed and running on the device.
**Steps**:
1. Open the Omni-Notes app.
2. Tap the "Create Note" icon.
3. Tap the "Attachment" icon (paperclip).
4. Select "Esboço" and create a sketch.
5. Enter a title and/or content.
**Expected Results**: The note should be saved automatically with the attached sketch and visible in the list of notes.

### Test Case 8 BUG
**Description**: Test adding a location to a note.
**Prerequisites**: The app should have access to the device's location services.
**Steps**:
1. Open the Omni-Notes app.
2. Tap the "Create Note" icon.
3. Tap the "Attachment" icon (paperclip).
4. Select "Localização" and allow location access if prompted.
5. Enter a title and/or content.
**Expected Results**: The note should be saved automatically with the attached location and visible in the list of notes.

### Test Case 9 BUG
**Description**: Test creating a note and using a reminder.
**Prerequisites**: The app should have access to device notifications.
**Steps**:
1. Open the Omni-Notes app.
2. Tap the "Create Note" icon.
3. Enter a title and/or content.
4. Tap "Adicionar lembrete" to set a reminder for the note.
**Expected Results**: The note should be saved automatically with the reminder and visible in the list of notes, and a notification should be sent at the reminder time.

### Test Case 10 BUG
**Description**: Test attaching a file from Pushbullet.
**Prerequisites**: The app should be linked with Pushbullet service.
**Steps**:
1. Open the Omni-Notes app.
2. Tap the "Create Note" icon.
3. Tap the "Attachment" icon (paperclip).
4. Select "Pushbullet" and attach a file from Pushbullet.
5. Enter a title and/or content.
**Expected Results**: The note should be saved automatically with the attached file and visible in the list of notes.

### Edge Case
**Description**: Test creating a note with excessively long text.
**Prerequisites**: The app should be installed and running on the device.
**Steps**:
1. Open the Omni-Notes app.
2. Tap the "Create Note" icon.
3. Enter a very long text in the "Título" and/or "Conteúdo" fields (e.g., 10,000 characters).
**Expected Results**: The app should handle the long text gracefully, saving the note without crashing or slowing down significantly. The note should be visible in the list of notes.