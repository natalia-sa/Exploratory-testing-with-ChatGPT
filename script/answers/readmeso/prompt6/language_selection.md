## Test 1
- **Description:** Verify language selection dropdown functionality.
- **Prerequisites:** Access to the readme generator app on either Firefox or Chrome.
- **Steps:**
  1. Open the readme generator app in the browser (Firefox or Chrome).
  2. Click on the language selection dropdown in the top-right corner.
  3. Scroll through the list of available languages.
  4. Close the dropdown by clicking outside it or on the dropdown icon again.
- **Expected results:** 
  - The dropdown should display a list of all supported languages.
  - The list should be scrollable if it does not fit in the view.
  - The dropdown should close when clicking outside it or on the icon again.

## Test 2 - BUG
- **Description:** Verify language change functionality.
- **Prerequisites:** Access to the readme generator app on either Firefox or Chrome.
- **Steps:**
  1. Open the readme generator app in the browser (Firefox or Chrome).
  2. Click on the language selection dropdown in the top-right corner.
  3. Select a language from the list (e.g., Français).
- **Expected results:** 
  - The app interface should change to the selected language (e.g., all labels, buttons, and texts should be displayed in French).

## Test 3
- **Description:** Verify persistence of language selection after refresh.
- **Prerequisites:** Access to the readme generator app on either Firefox or Chrome.
- **Steps:**
  1. Open the readme generator app in the browser (Firefox or Chrome).
  2. Select a different language (e.g., Español) from the language dropdown.
  3. Refresh the page.
- **Expected results:** 
  - The app should maintain the selected language (Español) after the page refresh.

## Test 4 
- **Description:** Verify switching back to default language (English).
- **Prerequisites:** Access to the readme generator app on either Firefox or Chrome.
- **Steps:**
  1. Open the readme generator app in the browser (Firefox or Chrome).
  2. Change the language to another language (e.g., Arabic).
  3. Change the language back to English.
- **Expected results:** 
  - The app interface should revert to English.

## Test 5
- **Description:** Verify UI elements' alignment and responsiveness after language change.
- **Prerequisites:** Access to the readme generator app on either Firefox or Chrome.
- **Steps:**
  1. Open the readme generator app in the browser (Firefox or Chrome).
  2. Select different languages from the language dropdown.
  3. Observe the alignment and layout of UI elements after each language change.
- **Expected results:** 
  - All UI elements should remain properly aligned and responsive regardless of the selected language.

## Test 6
- **Description:** Verify unsupported language handling.
- **Prerequisites:** Access to the readme generator app on either Firefox or Chrome.
- **Steps:**
  1. Attempt to select a language that is not listed (e.g., a custom script through developer console).
- **Expected results:** 
  - The app should either ignore the unsupported language input or display a default fallback language (e.g., English).

## Test 7
- **Description:** Verify language dropdown accessibility.
- **Prerequisites:** Access to the readme generator app on either Firefox or Chrome.
- **Steps:**
  1. Open the readme generator app in the browser (Firefox or Chrome).
  2. Navigate to the language selection dropdown using only the keyboard (e.g., tab key).
  3. Open and select a language using the keyboard.
- **Expected results:** 
  - The language dropdown and its options should be fully accessible and navigable using the keyboard.

## Test 8
- **Description:** Verify error handling for language selection.
- **Prerequisites:** Access to the readme generator app on either Firefox or Chrome.
- **Steps:**
  1. Open the readme generator app in the browser (Firefox or Chrome).
  2. Simulate a failure during the language change (e.g., disconnect internet, then select a language).
- **Expected results:** 
  - The app should display an appropriate error message indicating the failure to change the language, and the UI should remain stable.

These exploratory test cases cover various aspects of the language selection functionality, including basic operations, edge cases, and error scenarios.

