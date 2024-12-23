1.  SENSELESS
- Description: Verify that the user can add a new tag to a note.
- Prerequisites: The app is installed and the user is logged in. The user has navigated to the 'Add note' page.
- Steps: 
  1. Tap on the 'Tags+' icon.
  2. In the 'Add tag' popup, enter a valid tag name in the 'Tag name' field.
  3. Tap on the 'OK' button.
- Expected results: The tag should be added to the note and displayed in the list of tags.

2. SENSELESS
- Description: Verify that the user can cancel adding a new tag.
- Prerequisites: The app is installed and the user is logged in. The user has navigated to the 'Add note' page.
- Steps: 
  1. Tap on the 'Tags+' icon.
  2. In the 'Add tag' popup, enter a valid tag name in the 'Tag name' field.
  3. Tap on the 'Cancel' button.
- Expected results: The tag entry should be cancelled and no new tag should be added to the note.

3. SENSELESS
- Description: Verify that an error message is shown when adding an empty tag name.
- Prerequisites: The app is installed and the user is logged in. The user has navigated to the 'Add note' page.
- Steps: 
  1. Tap on the 'Tags+' icon.
  2. In the 'Add tag' popup, leave the 'Tag name' field empty.
  3. Tap on the 'OK' button.
- Expected results: An error message should be displayed indicating that the tag name cannot be empty.

4. SENSELESS
- Description: Verify that duplicate tags cannot be added.
- Prerequisites: The app is installed and the user is logged in. The user has navigated to the 'Add note' page. A tag (e.g. "study") is already added to the note.
- Steps: 
  1. Tap on the 'Tags+' icon.
  2. In the 'Add tag' popup, enter the same tag name (e.g. "study") that is already added.
  3. Tap on the 'OK' button.
- Expected results: An error message should be displayed indicating that the tag already exists.

5. SENSELESS
- Description: Verify the functionality of the search bar in the 'Tags' area.
- Prerequisites: The app is installed and the user is logged in. The user has navigated to the 'Add note' page. There are multiple tags added to the note.
- Steps: 
  1. Tap on the search icon in the 'Tags' section.
  2. Enter a tag name in the search bar.
- Expected results: The tags list should be filtered according to the search term, displaying only matching tags.

6. SENSLESS
- Description: Verify the responsive layout of the 'Add tag' popup on different screen sizes.
- Prerequisites: The app is installed and the user is logged in. The user has navigated to the 'Add note' page.
- Steps: 
  1. Tap on the 'Tags+' icon.
  2. Observe the layout and appearance of the 'Add tag' popup on different device screen sizes and orientations (e.g. portrait, landscape).
- Expected results: The 'Add tag' popup should be properly aligned and all elements should be correctly visible and functional regardless of the screen size or orientation.