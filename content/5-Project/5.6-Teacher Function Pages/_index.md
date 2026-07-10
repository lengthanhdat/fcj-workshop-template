---
title: "Teacher Function Pages"
date: 2024-01-01
weight: 6
chapter: false
pre: " <b> 5.6. </b> "
---

#### 5. Overview of the Teacher dashboard, exam authoring page, my question bank, exam room and monitoring, class management, shared question bank, teaching materials, analytics report, notifications, and profile pages:


<div align="center">

![Figure 5.1: Teacher dashboard page](image.png)

**Figure 5.1. Teacher dashboard page**

</div>

#### 5.1.1 Description of Figure 5.1
1. Top Header area
 * Displayed information:
	 * Real-time clock (07:12, Friday, 10/07).
 * Interactive controls:
	 * Menu button (hamburger icon): Collapses or expands the sidebar.
	 * Right-side icon group: Theme toggle (light/dark), Notifications (bell), and User avatar (showing the name "2783_ Dau Dai Tai" with a dropdown user menu).
2. Left navigation menu (Teacher Sidebar)
 * Displayed information:
	 * Aura Academic logo.
 * Interactive controls:
	 * Navigation tabs: The "Dashboard" tab is active (dark blue text). The teacher-specific features include Exam Design, My Question Bank, Exam Management, Classes, Question Bank, Teaching Materials, Analytics Reports, Notifications, and Personal Profile.
	 * Logout button: Located at the bottom-left corner.
3. Account warning area (Trial/Verification Banner)
 * Displayed information:
	 * A light-yellow warning banner: "Account is in trial mode" with the limitation text "Maximum 2 classes - Shared question bank access unlocked".
 * Interactive controls:
	 * "Verify now ->" button (green outline): A call-to-action that takes the teacher to the document/evidence submission flow for upgrading to a verified account.
4. Welcome and overview area (Welcome Banner)
 * Displayed information:
	 * A visually prominent light-blue gradient background.
	 * Greeting text: "Good morning, 2783_ Dau Dai Tai 👋" and a short description.
	 * Quick stats: "0 TOTAL QUESTIONS" and "0 CLASSES".
 * Interactive controls:
	 * "✨ Create New Exam" button (dark blue): The main primary action in this section. Clicking it starts the exam creation flow using AI, file upload, or manual input.
5. Quick Actions area
 * Displayed information: Title "Quick Actions" with a lightning icon.
 * Interactive controls: This section contains four shortcut cards leading to the most frequently used features:
	 * "Create with AI"
	 * "Teaching materials"
	 * "Analytics report"
	 * "Question Bank"
6. My Data sections
 * "My question bank" panel:
	 * Displayed information: Empty state text "Your question bank is empty" with an icon and guidance.
	 * Interactive controls: A text link "View all" at the top-right and a green outlined "Design exam" button in the middle of the panel to start creating content.
 * "My classes" panel:
	 * Displayed information: Empty state text "You have not managed any classes yet".
	 * Interactive controls: A plus icon at the top-right and a "Create new class ->" text link in the middle.
7. Floating button
 * Interactive controls: A green circular chat button in the bottom-right corner of the screen, used to open the support chat or live chat dialog.



--------------------------------------------------------------------------------------------------------------

<div align="center">

![Figure 5.2: Exam authoring page](image-1.png)

**Figure 5.2. Exam authoring page**

</div>


#### 5.1.2 Description of Figure 5.2
1. Top Header area
 * Displayed information:
	 * Real-time clock: "07:13 Friday, 10/07".
 * Interactive controls:
	 * Menu button (hamburger icon): Collapses or expands the left sidebar.
	 * Right-side icon group: Theme toggle, Notifications (bell), and User avatar showing the name "2783_ Dau Dai Tai".
2. Left navigation menu (Teacher Sidebar)
 * Displayed information:
	 * Aura Academic logo.
 * Interactive controls:
	 * Navigation tabs: In the teacher flow, the "Exam Design" tab is active (dark blue background, white text).
	 * Logout button: Located at the bottom-left corner.
3. Page Header and creation methods
 * Displayed information:
	 * Breadcrumb: "QUESTION BANK > AUTHORING".
	 * Main title: "Exam authoring".
	 * Status badge: A brown/yellow button labeled "✨ AI is active", indicating the AI server is ready.
	 * Warning banner (yellow): "Important note: This tool uses AI to analyze documents. Please review the question quality before publishing."
 * Interactive controls (Creation mode selection):
	 * Three method tabs:
		 * "✨ Create with AI" (active - blue text with underline).
		 * "Import from file" (upload Word/PDF/Excel files).
		 * "Manual creation" (enter questions one by one).
4. Main working area: AI-based exam creation
 * Displayed information:
	 * A light-blue instruction panel titled "Detailed guide for AI exam creation", which includes a ready-made formula and examples (subject + grade/level + specific requirements) to help teachers prompt the AI effectively.
 * Interactive controls (AI input flow):
	 * Two data source tabs: "Create from topic" (active - AI infers from general knowledge) and "Create from document" (teacher uploads a document for the AI to read and generate questions from).
	 * Quick suggestion chips: "Math 12 - Integration", "Physics 11 - Electromagnetism", "IELTS English 6.0"... Clicking a chip auto-fills the description box below.
	 * Text area: "EXAM REQUIREMENTS DESCRIPTION". This is where the teacher enters a detailed prompt.
	 * Configuration dropdowns and inputs:
		 * DIFFICULTY: Select level (currently "Medium").
		 * LANGUAGE: Select language (currently "Vietnamese").
		 * NUMBER OF QUESTIONS: Enter quantity (currently "10").
	 * Main action button: "✨ Aura AI - Generate exam now".
		 * Note: This button is currently gray (disabled). In the intended UX, it becomes enabled only when the teacher has entered content in the "Exam requirements description" box.
5. Floating button
 * Interactive controls: A green circular chat button in the bottom-right corner of the screen.


--------------------------------------------------------------------------------------------------------------

<div align="center">

![Figure 5.3: My question bank page](image-2.png)

**Figure 5.3. My question bank page**

</div>


#### 5.1.3 Description of Figure 5.3
1. Top Header area
 * Displayed information:
	 * Real-time clock: "07:13 Friday, 10/07".
 * Interactive controls:
	 * Menu button (hamburger icon): Collapses or expands the left sidebar.
	 * Utility icons on the right: Theme toggle, Notifications (bell), and User avatar showing the name "2783_ Dau Dai Tai".
2. Left navigation menu (Teacher Sidebar)
 * Displayed information:
	 * Aura Academic logo.
 * Interactive controls:
	 * Navigation tabs: On this screen, the "My Question Bank" tab is active (dark blue background, white text, folder icon). Other tabs such as Dashboard, Exam Design, and Classes remain visible.
	 * Logout button: Located at the bottom-left corner.
3. Main hero banner
 * Displayed information:
	 * A dark-blue rounded banner.
	 * Main title: "My Question Bank" (with a folder icon).
	 * Usage description: "Store the exam templates you designed yourself. Click 'Use' to configure, clone, and assign tests to classes."
 * Interactive controls:
	 * "✨ Design exam" button (white background, blue text): The primary call-to-action. Clicking it navigates the teacher back to the Exam Authoring page to start creating a new set of questions.
4. Search and display toolbar
 * Displayed information:
	 * Record counter: "0 templates" at the top-right.
 * Interactive controls:
	 * Search box: Placeholder "Search templates..." with a search icon, used to quickly find created question sets.
	 * View toggle buttons: Two icons for switching between List view and Grid view. At the moment, List view is active (blue).
5. Data area / empty state
 * Displayed information:
	 * Since no question sets have been saved yet, this area shows an empty state.
	 * A faded folder icon.
	 * Title: "Empty question bank".
	 * Helper text: "Design an exam and click 'Save to question bank' to store your templates here."
 * Interactive controls: There are currently no direct buttons inside this empty panel. If data exists, the area will display question set cards with important actions such as "Use/Assign", "Edit", "Clone", or "Delete".
6. Floating button
 * Interactive controls: A green circular chat button in the bottom-right corner of the screen, used to open live chat or AI support.


--------------------------------------------------------------------------------------------------------------

<div align="center">

![Figure 5.4: Exam room & monitoring page](image-3.png)

**Figure 5.4. Exam room & monitoring page**

</div>


#### 5.1.4 Description of Figure 5.4
1. Top Header area
 * Displayed information:
	 * Real-time clock: "07:13 Friday, 10/07".
 * Interactive controls:
	 * Menu button (hamburger icon): Collapses or expands the left sidebar.
	 * Utility icons on the right: Theme toggle, Notifications (bell), and User avatar showing the name "2783_ Dau Dai Tai".
2. Left navigation menu (Teacher Sidebar)
 * Displayed information:
	 * Project logo.
 * Interactive controls:
	 * Navigation tabs: The "Exam Management" tab is active (dark blue background, white text, clipboard/test icon).
	 * Logout button: Located at the bottom-left corner.
3. Main hero banner
 * Displayed information:
	 * A striking blue gradient banner.
	 * Main title: "Exam room & monitoring" (with a network/connection icon).
	 * Description: "Real-time online exam room monitoring dashboard. Track participating students, control room open/close states, and analyze exam reports."
 * Interactive controls:
	 * "Design new exam" button (white background, blue text): The primary call-to-action. Clicking it navigates the teacher to the Exam Authoring page to set up a new exam room.
4. Status summary cards
 * Displayed information: Five room-status cards, all currently at 0, with clear color coding:
	 * TOTAL ROOMS: 0
	 * LIVE: 0 (green)
	 * SCHEDULED: 0 (blue)
	 * DRAFT: 0 (orange)
	 * COMPLETED: 0 (gray)
 * Interactive controls: Similar to the admin view, these cards can act as filters; clicking one filters the room list below by the corresponding status.
5. Search and filters
 * Displayed information: None.
 * Interactive controls:
	 * Search box: Placeholder "Search exam, room code..." with a search icon.
	 * Status pills: All (active, dark blue), Live, Scheduled, Draft, Completed. Clicking one narrows the results below.
6. Data area / empty state
 * Displayed information:
	 * No exam rooms have been created yet, so this area shows an empty state.
	 * A faded folder icon.
	 * Title: "No exam rooms found".
	 * Helper text: "You do not have any exams matching the current search filter. Design an exam and schedule a new session!"
 * Interactive controls: There are no direct buttons in this empty panel. In practice, once data exists, this area will show room cards with actions such as "Monitor", "Close room", or "Start exam".
7. Floating button
 * Interactive controls: A green circular chat button in the bottom-right corner of the screen, used to open the support chat window.

--------------------------------------------------------------------------------------------------------------

<div align="center">

![Figure 5.5: Class management page](image-4.png)

**Figure 5.5. Class management page**

</div>


#### 5.1.5 Description of Figure 5.5
1. Top Header area
 * Displayed information:
	 * Real-time clock: "07:14 Friday, 10/07".
 * Interactive controls:
	 * Menu button (hamburger icon): Collapses or expands the left sidebar.
	 * Utility icons on the right: Theme toggle, Notifications (bell), and User avatar showing the name "2783_ Dau Dai Tai".
2. Left navigation menu (Teacher Sidebar)
 * Displayed information:
	 * Aura Academic logo.
 * Interactive controls:
	 * Navigation tabs: On this screen, the "Classes" tab is active (dark blue background, white text, graduation-cap icon).
	 * Logout button: Located at the bottom-left corner.
3. Main hero banner
 * Displayed information:
	 * A modern blue gradient banner.
	 * Main title: "Class management" (with a graduation-cap icon).
	 * Description: "Track and manage students, approve member lists, and control dedicated learning spaces for each class."
 * Interactive controls (Class creation flow):
	 * "+ Create new class" button (white background, blue text): The primary action. When clicked, the system typically opens a modal asking for basic information such as class name, subject, and grade level. After successful creation, the system generates a Class Code for the teacher to share with students.
4. Class list / empty state
 * Displayed information:
	 * Since this account has not created any classes yet, this area shows an empty state.
	 * A faded graduation-cap icon.
	 * Title: "No classes yet".
	 * Helper text: "Start by creating your first class to connect with students."
 * Interactive controls: There are currently no direct buttons in this empty panel.
	 * Demo note when data exists: Once the teacher creates classes, this area becomes a list of Class Cards. The teacher can click a class card to open the class details page (which contains the student list, assigned tasks, and class score table) or use secondary actions such as "Edit class information", "Lock class", or "Delete class".
5. Floating button
 * Interactive controls: A green circular chat button in the bottom-right corner of the screen, used to open support chat or quick messaging.

--------------------------------------------------------------------------------------------------------------

<div align="center">

![Figure 5.6: Question bank page](image-5.png)

**Figure 5.6. Question bank page**

</div>


#### 5.1.6 Description of Figure 5.6
1. Top Header area
 * Displayed information:
	 * Real-time clock: "07:14 Friday, 10/07".
 * Interactive controls:
	 * Menu button (hamburger icon): Collapses or expands the left sidebar.
	 * Utility icons on the right: Theme toggle, Notifications (bell), and User avatar showing the name "2783_ Dau Dai Tai".
2. Left navigation menu (Teacher Sidebar)
 * Displayed information:
	 * Aura Academic logo.
 * Interactive controls:
	 * Navigation tabs: The "Question Bank" tab is active (dark blue background, white text, bank-building icon).
	 * Logout button: Located at the bottom-left corner.
3. Main hero banner and stats
 * Displayed information:
	 * A highly prominent dark-blue banner.
	 * Main title: "Question Bank" (with a building icon).
	 * Description: "Manage practice questions shared in the system and quickly filter by level and subject."
	 * Three mini stats cards:
		 * 0 Total questions: Total number of questions currently available in the bank.
		 * 0 Filtered: Number of questions displayed after applying filters.
		 * 21 Subjects: Indicates that the system has preconfigured data for 21 different subjects.
 * Interactive controls (Question-sharing flow):
	 * "+ Add from my question bank" button (white background, blue text): The primary action. Clicking it opens a popup listing the question sets the teacher has saved in "My Question Bank". The teacher selects a set and confirms to publish it to the shared question bank for students across the school to practice with.
4. Search and filters toolbar
 * Displayed information: None.
 * Interactive controls:
	 * Search box: "Search by exam name..." for quick keyword lookup.
	 * Filter dropdowns: Three detailed filters for large datasets:
		 * All levels (green graduation-cap icon) -> Filter by grade 10, 11, 12, or university.
		 * All subjects (purple molecule icon) -> Filter by Math, Physics, Chemistry, English, etc.
		 * All difficulties (orange chart icon) -> Filter by Easy, Medium, Hard.
	 * View toggle buttons: Switch between List view and Grid view.
	 * "0 questions" label/button (dark blue): Shows the total search/filter result count or acts as a submit button to apply filters.
5. Data area / empty state
 * Displayed information:
	 * The shared bank currently has no questions, so this area shows an empty state with a dashed border.
	 * A faded document icon.
	 * Text: "The question bank is empty".
 * Interactive controls: There are no buttons at the moment. When data exists, this area will show public question sets. Teachers can click a set to preview the structure or view student usage metrics for that set.
6. Floating button
 * Interactive controls: A green circular chat button in the bottom-right corner of the screen.

--------------------------------------------------------------------------------------------------------------

<div align="center">

![Figure 5.7: Teaching materials page](image-6.png)

**Figure 5.7. Teaching materials page**

</div>


#### 5.1.7 Description of Figure 5.7
1. Top Header area
 * Displayed information:
	 * Real-time clock: "07:14 Friday, 10/07".
 * Interactive controls:
	 * Menu button (hamburger icon): Collapses or expands the left sidebar.
	 * Utility icons on the right: Theme toggle, Notifications (bell), and User avatar showing the name "2783_ Dau Dai Tai".
2. Left navigation menu (Teacher Sidebar)
 * Displayed information:
	 * Aura Academic logo.
 * Interactive controls:
	 * Navigation tabs: The "Teaching Materials" tab is active (dark blue background, white text, book/document icon).
	 * Logout button: Located at the bottom-left corner.
3. Header and overview statistics
 * Displayed information:
	 * Small label: "MATERIAL CENTER".
	 * Main title: "Teaching materials".
	 * Description: "Upload, categorize, and track learning materials that students can view in the material library."
	 * Four mini stat cards showing an overview of this teacher's material workflow, all currently at 0:
		 * 0 TOTAL MATERIALS (folder icon)
		 * 0 PUBLISHED (globe icon - materials approved by the admin)
		 * 0 PENDING REVIEW (clock icon - newly uploaded materials waiting for admin processing)
		 * 0 DOWNLOADS (download icon - student interaction statistics)
 * Interactive controls: These stat cards can usually be clicked to quickly filter the list below (for example, click "Pending review" to show files still waiting in the queue).
4. Upload zone and process guide
 * "Upload new materials" panel (left):
	 * Displayed information: Cloud icon. Guidance text: "Drag and drop files here or click to select multiple files at once. PDF, PPTX, DOCX, and Video are supported, with a maximum of 50 MB per file." Supported format badges are shown at the bottom (PDF, PPTX, DOCX, Video).
	 * Interactive controls: The entire dashed panel is a drag-and-drop zone. Teachers can drop files here from their computer or click the area to open the operating system file picker.
 * "Upload workflow" panel (right):
	 * Displayed information: A "0 files waiting" counter in the top-right corner, followed by three clear UX steps:
		 * Choose materials: Upload one or more files...
		 * Add metadata: Set title, subject, category, and tags...
		 * Track status: Valid materials will appear...
	 * Interactive controls: This panel is primarily an information box that helps new users understand the process.
5. "My materials" list
 * Displayed information:
	 * Section title: "My materials" with a small summary "(0 materials displayed - 0 materials rejected)".
	 * Empty state: Since no files exist yet, the lower body shows a faded file icon and the text "No materials yet."
 * Interactive controls:
	 * Search box: "Search materials..." for keyword lookup.
	 * Status filter dropdown: Currently set to "All". Teachers can open it to filter by "Approved", "Pending review", or "Rejected".
	 * Demo note: When data exists, the empty area becomes a list of materials (table or cards), with actions such as View details, Edit information, or Delete file.
6. Floating button
 * Interactive controls: A green circular chat button in the bottom-right corner of the screen, used to open support chat.


--------------------------------------------------------------------------------------------------------------

<div align="center">

![Figure 5.8: Analytics report page](image-7.png)

**Figure 5.8. Analytics report page**

</div>

#### 5.1.8 Description of Figure 5.8
Important note for the workshop: this page currently has a serious internationalization (i18n) bug similar to part of the exam-authoring page earlier. The system is not loading Vietnamese text and instead displays raw code variables (keys). Make sure to note this for the dev team to fix urgently.

Below are the screen components in detail:
1. Top Header area
 * Displayed information:
	 * Real-time clock: "07:15 Friday, 10/07".
 * Interactive controls:
	 * Menu button (hamburger icon): Collapses or expands the left sidebar.
	 * Utility icons on the right: Theme toggle, Notifications (bell), and User avatar showing the name "2783_ Dau Dai Tai".
2. Left navigation menu (Teacher Sidebar)
 * Displayed information:
	 * Aura Academic logo.
 * Interactive controls:
	 * Navigation tabs: The "Analytics Reports" tab is active (dark blue background, white text, bar-chart icon).
	 * Logout button: Located at the bottom-left corner.
3. Page title area (currently broken)
 * Displayed information:
	 * Instead of showing the Vietnamese title (for example, "Reports & Statistics"), the page is displaying the code key: TeacherReports.page_title (with a notebook/chart icon).
	 * The subtitle is also broken and shows the code key: TeacherReports.page_desc.
 * Interactive controls: There are no buttons in this area.
4. Main content area (empty state with broken text)
 * Displayed information:
	 * The page is currently in an empty state, but all helper text is broken into keys.
	 * A faded chart icon with a slash indicating no data.
	 * Empty-state title: TeacherReports.no_reports (it should be "No reports yet").
	 * Detailed helper text: TeacherReports.no_reports_desc (it should explain how to organize an exam so that report data is generated).
 * Interactive controls: There are currently no buttons inside this empty panel.
	 * Demo note after the bug is fixed and data is available: This area will render charts showing score distribution, pass/fail ratios for classes, and detailed reports for each exam managed by that teacher.
5. Floating button
 * Interactive controls: A green circular chat button in the bottom-right corner of the screen, used to open chat/support.

--------------------------------------------------------------------------------------------------------------

<div align="center">

![Figure 5.9: Notifications page](image-8.png)

**Figure 5.9. Notifications page**

</div>

#### 5.1.9 Description of Figure 5.9
1. Top Header area
 * Displayed information:
	 * Real-time clock: "07:15 Friday, 10/07".
 * Interactive controls:
	 * Menu button (hamburger icon): Collapses or expands the left sidebar.
	 * Utility icons on the right: Theme toggle, Notifications (bell with a red dot indicating new notifications), and User avatar showing the name "2783_ Dau Dai Tai".
2. Left navigation menu (Teacher Sidebar)
 * Displayed information:
	 * Aura Academic logo.
 * Interactive controls:
	 * Navigation tabs: The "Notifications" tab is active (dark blue background, white text, bell icon).
	 * Logout button: Located at the bottom-left corner.
3. Page header and main action area
 * Displayed information:
	 * Recognition badge: "TEACHER NOTIFICATION CENTER" (teal text).
	 * Main title: "System notifications".
	 * Description/statistic: "You have 3 unread notifications". The number 3 is highlighted in blue.
 * Interactive controls:
	 * "Mark all as read" button (dark blue, on the right): A key UX action. Clicking it calls the API to move all notifications from Unread to Read and removes the red dot from the header bell icon.
4. Search and filters
 * Displayed information: None.
 * Interactive controls:
	 * Search box: "Search notifications..." with a search icon.
	 * Dropdown "All types": Filter by notification type such as System, Class, Reminder.
	 * Dropdown "All statuses": Filter by Read or Unread.
	 * "Filter" button (light gray): Applies the selected search and dropdown conditions.
5. Notifications list
 * Displayed information (per notification card):
	 * Unread indicator: Each card has a blue left border and a blue dot in the top-right corner.
	 * Cards 1 and 2: Same topic, "Join class request approved". Details: "You have been approved into class '12A2'" and "class 'Grade 12'". Includes INFO badge and timestamps (6 hours ago, 10 hours ago).
	 * Card 3: Topic "Welcome to AuraAcademic". A welcome message sent to the account. Includes WELCOME badge and timestamp (10 hours ago).
 * Interactive controls:
	 * Clicking a card: Marks the notification as Read (the blue border and dot disappear) and may navigate to the related page, such as the details page for class 12A2.
	 * Delete button (trash icon): Located on the right side of each card. Click to remove that notification from the list.
6. Floating button
 * Interactive controls: A green circular chat button in the bottom-right corner of the screen.

--------------------------------------------------------------------------------------------------------------

<div align="center">

![Figure 5.10: Personal profile page](image-9.png)

**Figure 5.10. Personal profile page**

</div>

#### 5.1.10 Description of Figure 5.10
1. Top Header area
 * Displayed information:
	 * Real-time clock in the top-right corner.
 * Interactive controls:
	 * Menu button (hamburger icon): Collapses or expands the left sidebar.
	 * Utility icons on the right: Theme toggle, Notifications (bell), and Account avatar.
2. Left navigation menu (Teacher Sidebar)
 * Displayed information:
	 * Aura Academic logo.
 * Interactive controls:
	 * Navigation tabs: On this screen, the "Personal Profile" tab near the bottom is active (dark blue background, white text, user icon).
	 * Logout button: Located at the bottom-left corner.
3. Profile identification card
 * Displayed information:
	 * Avatar with the letter "D" and a yellow warning badge (exclamation mark) indicating the account has not been fully verified.
	 * Role label: "TEACHER PROFILE".
	 * Username: "2783_ Dau Dai Tai".
	 * Login email.
	 * Status pill: "Teacher not verified yet" (yellow).
 * Interactive controls:
	 * "Change avatar" button (camera icon): Click to upload a new avatar from the computer.
	 * "Edit profile" button (dark blue, pencil icon): Typically opens a form to update the name, phone number, date of birth, and other personal details.
4. Personal activity statistics
 * Displayed information: Four overview metrics for this teacher account:
	 * CLASSES: 0 (graduation-cap icon)
	 * EXAMS CREATED: 0 (file icon)
	 * ACTIVE: 0 (play icon)
	 * SUBMISSIONS: 0 (check icon)
 * Interactive controls: These cards are mainly static indicators of activity and achievements.
5. Left column (Information and history)
 * "Personal information" panel:
	 * Displayed information: Email and last login time (for example, 00:10:06 on 10/7/2026).
 * "Recent exams" panel:
	 * Displayed information: Empty state text "No exams yet."
6. Right column (Account verification and security)
 This area contains flows that are extremely important for a teacher account:
 * "Account status" panel:
	 * Displayed information: A yellow warning message "Teacher not verified yet" with a request to provide supporting evidence.
	 * Interactive controls: "Verify now" button (dark blue). Clicking it takes the teacher to the flow for uploading a teacher ID card/identity document for admin approval, which unlocks restricted features such as creating more than 2 classes.
 * "Security" panel:
	 * Displayed information: Email (verified - green text), Login (via Google). 2FA status (turned off).
	 * Interactive controls: "Enable code / Enable" button (light blue) to activate two-factor authentication (2FA).
 * "Set password" panel:
	 * Displayed information: An instruction box explaining how to create a password for Google-based login accounts.
	 * Interactive controls:
		 * Two input fields: "New password" and "Confirm new password" (with an eye icon to hide/show the password).
		 * "Set password" button (gray outline): Click to save the new password.
 * "Recent classes" panel:
	 * Displayed information: Empty state text "No classes yet."