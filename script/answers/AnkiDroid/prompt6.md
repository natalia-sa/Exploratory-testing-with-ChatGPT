### Test Case 1
- **Description:** Add a note with text in both front and back fields.
- **Prerequisites:** AnkiDroid app installed, app opened and navigated to 'Add Note' screen.
- **Steps:**
  1. Select 'Basic' in the 'Type' dropdown.
  2. Select 'Default' in the 'Deck' dropdown.
  3. Enter "Front Text" in the 'Front' field.
  4. Enter "Back Text" in the 'Back' field.
  5. Press the check mark at the top right of the screen to save the note.
- **Expected Results:** The note is saved successfully, and is visible in the 'Default' deck.

### Test Case 2
- **Description:** Add a note with only the front field filled.
- **Prerequisites:** AnkiDroid app installed, app opened and navigated to 'Add Note' screen.
- **Steps:**
  1. Select 'Basic' in the 'Type' dropdown.
  2. Select 'Default' in the 'Deck' dropdown.
  3. Enter "Front Text" in the 'Front' field.
  4. Leave the 'Back' field empty.
  5. Press the check mark at the top right of the screen to save the note.
- **Expected Results:** The note is saved successfully, and is visible in the 'Default' deck.

### Test Case 3
- **Description:** Add a note with special characters in the front and back fields.
- **Prerequisites:** AnkiDroid app installed, app opened and navigated to 'Add Note' screen.
- **Steps:**
  1. Select 'Basic' in the 'Type' dropdown.
  2. Select 'Default' in the 'Deck' dropdown.
  3. Enter "!@#$%^&*()" in the 'Front' field.
  4. Enter "()&*^%$#@!" in the 'Back' field.
  5. Press the check mark at the top right of the screen to save the note.
- **Expected Results:** The note is saved successfully, and special characters are correctly displayed when reviewing the note.

### Test Case 4
- **Description:** Add a note with an image in the front field.
- **Prerequisites:** AnkiDroid app installed, app opened and navigated to 'Add Note' screen, image accessible on the device.
- **Steps:**
  1. Select 'Basic' in the 'Type' dropdown.
  2. Select 'Default' in the 'Deck' dropdown.
  3. Tap the paperclip icon next to the 'Front' field.
  4. Select 'Add image' and choose an image from the gallery.
  5. Fill the 'Back' field with "Back Text".
  6. Press the check mark at the top right of the screen to save the note.
- **Expected Results:** The note is saved successfully with the image visible in the front field and the text visible in the back field during review.

### Test Case 5
- **Description:** Add a note with an audio clip in the back field.
- **Prerequisites:** AnkiDroid app installed, app opened and navigated to 'Add Note' screen, audio clip accessible on the device.
- **Steps:**
  1. Select 'Basic' in the 'Type' dropdown.
  2. Select 'Default' in the 'Deck' dropdown.
  3. Enter "Front Text" in the 'Front' field.
  4. Tap the paperclip icon next to the 'Back' field.
  5. Select 'Add audio clip' and choose an audio clip from the gallery.
  6. Press the check mark at the top right of the screen to save the note.
- **Expected Results:** The note is saved successfully with the text visible in the front field and the audio clip playable in the back field during review.

### Test Case 6
- **Description:** Add a note with recording audio for the back field.
- **Prerequisites:** AnkiDroid app installed, app opened and navigated to 'Add Note' screen.
- **Steps:**
  1. Select 'Basic' in the 'Type' dropdown.
  2. Select 'Default' in the 'Deck' dropdown.
  3. Enter "Front Text" in the 'Front' field.
  4. Tap the paperclip icon next to the 'Back' field.
  5. Select 'Record audio' and record a short audio message.
  6. Press the check mark at the top right of the screen to save the note.
- **Expected Results:** The note is saved successfully with the text visible in the front field and the recorded audio message in the back field during review.

### Test Case 7
- **Description:** Add a note and assign tags.
- **Prerequisites:** AnkiDroid app installed, app opened and navigated to 'Add Note' screen.
- **Steps:**
  1. Select 'Basic' in the 'Type' dropdown.
  2. Select 'Default' in the 'Deck' dropdown.
  3. Enter "Front Text" in the 'Front' field.
  4. Enter "Back Text" in the 'Back' field.
  5. Tap 'Tags' and add a new tag.
  6. Enter "Test Tag" in the 'Tag name' field and press 'OK'.
  7. Press the check mark at the top right of the screen to save the note.
- **Expected Results:** The note is saved successfully with the tag "Test Tag" assigned to it.

### Test Case 8
- **Description:** Add a note with a long text in front and back fields.
- **Prerequisites:** AnkiDroid app installed, app opened and navigated to 'Add Note' screen.
- **Steps:**
  1. Select 'Basic' in the 'Type' dropdown.
  2. Select 'Default' in the 'Deck' dropdown.
  3. Enter a long text (e.g., a paragraph) in the 'Front' field.
  4. Enter a long text (e.g., a paragraph) in the 'Back' field.
  5. Press the check mark at the top right of the screen to save the note.
- **Expected Results:** The note is saved successfully with long texts correctly displayed during review.

### Test Case 9
- **Description:** Add a note with the 'Basic (and reversed card)' type.
- **Prerequisites:** AnkiDroid app installed, app opened and navigated to 'Add Note' screen.
- **Steps:**
  1. Select 'Basic (and reversed card)' in the 'Type' dropdown.
  2. Select 'Default' in the 'Deck' dropdown.
  3. Enter "Front Text" in the 'Front' field.
  4. Enter "Back Text" in the 'Back' field.
  5. Press the check mark at the top right of the screen to save the note.
- **Expected Results:** Two cards are created, one with the front text shown first, and the other with the back text shown first.

### Test Case 10 - NONSENSICAL
- **Description:** Add a note with the 'Basic (and reversed card)' type, enter text only in the front field, then cancel to check if nothing is saved.
- **Prerequisites:** AnkiDroid app installed, app opened and navigated to 'Add Note' screen.
- **Steps:**
  1. Select 'Basic (and reversed card)' in the 'Type' dropdown.
  2. Select 'Default' in the 'Deck' dropdown.
  3. Enter "Front Text" in the 'Front' field.
  4. Leave the 'Back' field empty.
  5. Press the 'Cancel' button.
- **Expected Results:** No cards are created, and nothing is saved in the notes list.