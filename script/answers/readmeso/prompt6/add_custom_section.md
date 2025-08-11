### Test Case 1
- **Description:** Adding a basic custom section with non-empty valid title
- **Prerequisites:** Application is opened in either Linux with Firefox or Chrome browser, and the user is on the Editor page.
- **Steps:**
  1. Click on the "Custom Section" button.
  2. Enter the title "My Custom Section" in the input field.
  3. Click on the "Add Section" button.
- **Expected results:** A new section titled "My Custom Section" should be added to the sections list and displayed in the editor.

### Test Case 2 - BUG
- **Description:** Attempting to add a custom section with an empty title
- **Prerequisites:** Application is opened in either Linux with Firefox or Chrome browser, and the user is on the Editor page.
- **Steps:**
  1. Click on the "Custom Section" button.
  2. Leave the title input field empty.
  3. Click on the "Add Section" button.
- **Expected results:** The application should show an error message or prevent adding the section.

### Test Case 3
- **Description:** Attempting to add multiple custom sections with the same title
- **Prerequisites:** Application is opened in either Linux with Firefox or Chrome browser, and the user is on the Editor page.
- **Steps:**
  1. Click on the "Custom Section" button.
  2. Enter the title "Duplicate Section" and click "Add Section".
  3. Repeat steps 1 and 2 to add another section with the same title.
- **Expected results:** Each section titled "Duplicate Section" should be added and displayed in the sections list and editor, or the application should prevent adding duplicate titles.

### Test Case 4
- **Description:** Adding a custom section with special characters in the title
- **Prerequisites:** Application is opened in either Linux with Firefox or Chrome browser, and the user is on the Editor page.
- **Steps:**
  1. Click on the "Custom Section" button.
  2. Enter a title with special characters, e.g., "My @Custom #Section!$".
  3. Click on the "Add Section" button.
- **Expected results:** The section with the special characters should be added and displayed correctly in the sections list and editor.

### Test Case 5 - BUG
- **Description:** Verifying custom section title field input limit
- **Prerequisites:** Application is opened in either Linux with Firefox or Chrome browser, and the user is on the Editor page.
- **Steps:**
  1. Click on the "Custom Section" button.
  2. Enter a very long title (more than 255 characters).
  3. Attempt to submit the form by clicking "Add Section".
- **Expected results:** The application should either prevent entering more than the allowed character limit or not accept the submission if it exceeds the limit, with an appropriate error message.

### Test Case 6
- **Description:** Verifying responsiveness of the "Custom Section" form
- **Prerequisites:** Application is opened in either Linux with Firefox or Chrome browser, and the user is on the Editor page.
- **Steps:**
  1. Click on the "Custom Section" button.
  2. Adjust the browser window size to a very small width and height.
  3. Try to use the "Custom Section" form in this resized window.
- **Expected results:** The "Custom Section" form should be responsive and usable even in a small window size (e.g., no content should be hidden, and buttons should be accessible).

### Test Case 7
- **Description:** Adding a custom section and then navigating to a different functionality
- **Prerequisites:** Application is opened in either Linux with Firefox or Chrome browser, and the user is on the Editor page.
- **Steps:**
  1. Click on the "Custom Section" button.
  2. Enter the title "Another Section".
  3. Click on the "Add Section" button.
  4. Navigate to a different functionality/section of the app.
  5. Return to the Editor page.
- **Expected results:** The newly added custom section "Another Section" should still persist in the sections list and editor.

### Test Case 8
- **Description:** Adding multiple custom sections and verifying the order
- **Prerequisites:** Application is opened in either Linux with Firefox or Chrome browser, and the user is on the Editor page.
- **Steps:**
  1. Add multiple custom sections sequentially titled "Custom Section 1", "Custom Section 2", "Custom Section 3" by following steps 1-3 in Test Case 1.
  2. Observe the order of the sections in the sections list.
- **Expected results:** The sections should be listed in the order they were added: "Custom Section 1", "Custom Section 2", "Custom Section 3".

