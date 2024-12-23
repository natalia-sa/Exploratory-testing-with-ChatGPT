## Prompt 6.11

“
From the point of view of a tester who will perform an exploratory testing session, give me test cases to the Toggle between light and dark modes in the readme generator app. Please consider that to carry out these tests you only have access to the Linux operating system, and the Firefox and Chrome browsers. This app does not have a connection to any type of database and there are no user registration and login options. Consider potential edge cases, unusual flows and try to find possible bugs. I will provide screenshots of the app GUI. The test cases should follow the structure below:

[test number]
-Description: The test case description
-Prerequisites: specifies the conditions that must be met before executing the test steps
-Steps: Enumerated steps to execute the test
-Expected results: The expected test result
”

## Images

readme1.png, readme2.png

## Answer

### Test Case 1
#### - Description:
Verify toggling between "Preview" and "Raw" view using Firefox on Linux.

#### - Prerequisites:
- Access to a Linux system.
- Firefox web browser installed.

#### - Steps:
1. Open Firefox and navigate to the readme generator app.
2. Click on "Get Started" to access the editor.
3. Enter some text in the editor area under "Title and Description".
4. Click on the "Preview" tab.
5. Observe the content displayed in the preview panel.
6. Click on the "Raw" tab.
7. Observe the content displayed in the raw panel.
8. Switch back to "Preview" tab.

#### - Expected Results:
- The tab content updates should be smooth and should display the appropriate content based on the mode (formatted for Preview and raw markdown for Raw).

---

### Test Case 2
#### - Description:
Verify toggling between "Preview" and "Raw" view using Chrome on Linux.

#### - Prerequisites:
- Access to a Linux system.
- Chrome web browser installed.

#### - Steps:
1. Open Chrome and navigate to the readme generator app.
2. Click on "Get Started" to access the editor.
3. Enter some text in the editor area under "Title and Description".
4. Click on the "Preview" tab.
5. Observe the content displayed in the preview panel.
6. Click on the "Raw" tab.
7. Observe the content displayed in the raw panel.
8. Switch back to "Preview" tab.

#### - Expected Results:
- The tab content updates should be smooth and should display the appropriate content based on the mode (formatted for Preview and raw markdown for Raw).

---

### Test Case 3
#### - Description:
Verify the behavior when switching tabs rapidly using Firefox on Linux.

#### - Prerequisites:
- Access to a Linux system.
- Firefox web browser installed.

#### - Steps:
1. Open Firefox and navigate to the readme generator app.
2. Click on "Get Started" to access the editor.
3. Enter some text in the editor area under "Title and Description".
4. Rapidly click between "Preview" and "Raw" tabs multiple times (at least 10 times).
5. Observe the stability and responsiveness of the app.

#### - Expected Results:
- The app should not crash or become unresponsive.
- The content should correctly switch between modes without any display issues.

---

### Test Case 4
#### - Description:
Verify the behavior when switching tabs rapidly using Chrome on Linux.

#### - Prerequisites:
- Access to a Linux system.
- Chrome web browser installed.

#### - Steps:
1. Open Chrome and navigate to the readme generator app.
2. Click on "Get Started" to access the editor.
3. Enter some text in the editor area under "Title and Description".
4. Rapidly click between "Preview" and "Raw" tabs multiple times (at least 10 times).
5. Observe the stability and responsiveness of the app.

#### - Expected Results:
- The app should not crash or become unresponsive.
- The content should correctly switch between modes without any display issues.

---

### Test Case 5 - SENSELESS
#### - Description:
Verify if the content remains unsaved and accessible when switching between "Preview" and "Raw" views in Firefox on Linux.

#### - Prerequisites:
- Access to a Linux system.
- Firefox web browser installed.

#### - Steps:
1. Open Firefox and navigate to the readme generator app.
2. Click on "Get Started" to access the editor.
3. Enter some text in the editor area under "Title and Description".
4. Click on the "Preview" tab to view preview.
5. Click on the "Raw" tab.
6. Edit the content in the raw view and switch back to "Preview" view.
7. Observe if the changes made in raw view reflect in preview.
8. Repeat steps 4-7 multiple times.

#### - Expected Results:
- The app should maintain the same content across both views.
- Edits made in raw view should be reflected in the preview view.

---

### Test Case 6 - SENSELESS
#### - Description:
Verify if the content remains unsaved and accessible when switching between "Preview" and "Raw" views in Chrome on Linux.

#### - Prerequisites:
- Access to a Linux system.
- Chrome web browser installed.

#### - Steps:
1. Open Chrome and navigate to the readme generator app.
2. Click on "Get Started" to access the editor.
3. Enter some text in the editor area under "Title and Description".
4. Click on the "Preview" tab to view preview.
5. Click on the "Raw" tab.
6. Edit the content in the raw view and switch back to "Preview" view.
7. Observe if the changes made in raw view reflect in preview.
8. Repeat steps 4-7 multiple times.

#### - Expected Results:
- The app should maintain the same content across both views.
- Edits made in raw view should be reflected in the preview view.

---

### Test Case 7
#### - Description:
Check if non-standard characters and emojis are maintained correctly when toggling between views on Firefox.

#### - Prerequisites:
- Access to a Linux system.
- Firefox web browser installed.

#### - Steps:
1. Open Firefox and navigate to the readme generator app.
2. Click on "Get Started" to access the editor.
3. Enter text containing non-standard characters and emojis in the editor.
4. Click on the "Preview" tab and observe.
5. Click on the "Raw" tab and observe.
6. Switch back to "Preview" tab again.

#### - Expected Results:
- Both views should correctly display non-standard characters and emojis without corruption or loss.

---

### Test Case 8
#### - Description:
Check if non-standard characters and emojis are maintained correctly when toggling between views on Chrome.

#### - Prerequisites:
- Access to a Linux system.
- Chrome web browser installed.

#### - Steps:
1. Open Chrome and navigate to the readme generator app.
2. Click on "Get Started" to access the editor.
3. Enter text containing non-standard characters and emojis in the editor.
4. Click on the "Preview" tab and observe.
5. Click on the "Raw" tab and observe.
6. Switch back to "Preview" tab again.

#### - Expected Results:
- Both views should correctly display non-standard characters and emojis without corruption or loss.

---

### Test Case 9
#### - Description:
Verify functionality when both the "Preview" and "Raw" tabs are left open without interaction for an extended period in Firefox.

#### - Prerequisites:
- Access to a Linux system.
- Firefox web browser installed.

#### - Steps:
1. Open Firefox and navigate to the readme generator app.
2. Click on "Get Started" to access the editor.
3. Enter text in the editor area.
4. Switch to the "Preview" tab.
5. Leave the browser and tab open for at least 30 minutes without any interaction.
6. Switch to "Raw" view after the waiting period.
7. Observe the state of the content and application.

#### - Expected Results:
- The application should remain stable and the content should remain intact after an extended period of inactivity.

---

### Test Case 10
#### - Description:
Verify functionality when both the "Preview" and "Raw" tabs are left open without interaction for an extended period in Chrome.

#### - Prerequisites:
- Access to a Linux system.
- Chrome web browser installed.

#### - Steps:
1. Open Chrome and navigate to the readme generator app.
2. Click on "Get Started" to access the editor.
3. Enter text in the editor area.
4. Switch to the "Preview" tab.
5. Leave the browser and tab open for at least 30 minutes without any interaction.
6. Switch to "Raw" view after the waiting period.
7. Observe the state of the content and application.

#### - Expected Results:
- The application should remain stable and the content should remain intact after an extended period of inactivity.

---

0 bugs
2 senseless