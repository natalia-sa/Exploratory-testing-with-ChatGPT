### Exploratory Test Cases for Download Button Functionality

#### Test Case 1
- **Description:** Verify that clicking the "Download" button without any edits downloads the default README file.
- **Prerequisites:** Access to the readme.so editor page.
- **Steps:**
  1. Open the readme.so editor page in Firefox browser.
  2. Without making any edits, click the "Download" button.
  3. Check the downloads folder.
- **Expected results:** A README file with default content is downloaded successfully.

#### Test Case 2
- **Description:** Verify that clicking the "Download" button after editing sections downloads the updated README file.
- **Prerequisites:** Access to the readme.so editor page.
- **Steps:**
  1. Open the readme.so editor page in Chrome browser.
  2. Add or edit a section (e.g., change the project title).
  3. Click the "Download" button.
  4. Check the downloads folder.
  5. Open the downloaded README file and verify the contents.
- **Expected results:** The README file is downloaded with the updated content.

#### Test Case 3
- **Description:** Verify that "Download" button works when sections have been added and removed.
- **Prerequisites:** Access to the readme.so editor page.
- **Steps:**
  1. Open the readme.so editor page in Firefox browser.
  2. Add several sections (e.g., Acknowledgements, API Reference).
  3. Remove some of the added sections.
  4. Click the "Download" button.
  5. Check the downloads folder.
  6. Open the downloaded README file and verify the contents.
- **Expected results:** The README file reflects the current state with the sections correctly added and removed.

#### Test Case 4
- **Description:** Verify that "Download" button functions correctly with non-English characters.
- **Prerequisites:** Access to the readme.so editor page.
- **Steps:**
  1. Open the readme.so editor page in Chrome browser.
  2. Change the language to a non-English language (e.g., French or Spanish) using the language dropdown.
  3. Add or edit a section with content in the selected language.
  4. Click the "Download" button.
  5. Check the downloads folder.
  6. Open the downloaded README file and verify the contents.
- **Expected results:** The README file downloaded with the content in the selected language displays correctly.

#### Test Case 5
- **Description:** Verify that clicking the "Download" button twice in quick succession does not cause any issues.
- **Prerequisites:** Access to the readme.so editor page.
- **Steps:**
  1. Open the readme.so editor page in Firefox browser.
  2. Click the "Download" button twice quickly.
  3. Check the downloads folder.
- **Expected results:** Two README files are downloaded without any issues. Both files should have the same content.

#### Test Case 6
- **Description:** Verify the behavior of the "Download" button with different sections order.
- **Prerequisites:** Access to the readme.so editor page.
- **Steps:**
  1. Open the readme.so editor page in Chrome browser.
  2. Add multiple sections (e.g., Title and Description, API Reference, Acknowledgements).
  3. Change the order of the sections.
  4. Click the "Download" button.
  5. Check the downloads folder.
  6. Open the downloaded README file and verify the contents and order.
- **Expected results:** The README file is downloaded, and the sections are in the updated order.

#### Test Case 7
- **Description:** Verify that "Download" button handles special characters.
- **Prerequisites:** Access to the readme.so editor page.
- **Steps:**
  1. Open the readme.so editor page in Firefox browser.
  2. Add or edit a section, including special characters (e.g., #, &, %, $).
  3. Click the "Download" button.
  4. Check the downloads folder.
  5. Open the downloaded README file and verify the contents.
- **Expected results:** The README file is downloaded, and special characters are displayed correctly in the file.

#### Test Case 8
- **Description:** Verify "Download" button functionality after performing a "Reset" action.
- **Prerequisites:** Access to the readme.so editor page.
- **Steps:**
  1. Open the readme.so editor page in Chrome browser.
  2. Add or edit sections and make changes.
  3. Click the "Reset" button to clear all changes.
  4. Click the "Download" button.
  5. Check the downloads folder.
  6. Open the downloaded README file and verify the contents.
- **Expected results:** The README file is downloaded with the default content after resetting.

By conducting these tests, you'll cover various scenarios, including edge cases, to ensure the "Download" button works as expected.

