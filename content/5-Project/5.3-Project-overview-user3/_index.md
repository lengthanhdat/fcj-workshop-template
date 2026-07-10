---
title : "Project Overview and User Features Part 3"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

#### 5. Overview of the system's Exam Bank, Learning Materials, Notifications, and Personal Profile pages:


<div align="center">

![Figure 5.1: Exam Bank page of the system](image.png)

**Figure 5.1. Exam Bank page of the system**

</div>


**5.1.1. Description of Figure 5.1**

1. Main Banner section (Blue area at the top)

- Display information:
	- Large title: "Exam Bank" with descriptive text below.
	- 3 statistic cards (white background): "0 Total exams", "23 Subjects", "0 Topics".

- Interactive buttons:
	- List icon button (next to the History button): Can be used to open a side menu or collapse the banner.
	- "History" button (with chart icon): Navigates to the page for reviewing completed exams.

2. Feature Cards section

- Display information:
	- 3 horizontal cards: "Quick Search", "Practice by Topic", and "Popular Exams", each with supporting text.

- Interactive buttons:
	- Each of the 3 cards works as a button (Tabs/Filters).
	- Expected behavior: Clicking a card changes the filter or the content below accordingly (for example, clicking "Practice by Topic" switches the left column from the subject list to the topic list).

3. Search & Filter Bar section

- Interactive controls and input fields:
	- Search input: Placeholder text is "Search exams by name...". Users can type to search exams (press Enter to search or filter in real time).
	- "Favorites" button (heart icon): Works as a toggle. Click it to show only exams that have been starred or saved.
	- "0 exams" button (dark blue background): Acts as the "exam cart". Click it to open a popup/drawer showing the selected exams.

4. Main content section (3 columns)

**Left column: SUBJECTS list**

- Display information:
	- Title "SUBJECTS". The first 8 subjects (Mathematics, Literature, Vietnamese, etc.) are shown with icons.

- Interactive controls:
	- Subject rows: Clicking a subject highlights it (active state) and the middle column shows only exams for that subject.
	- "Show 15 more subjects" button (down arrow icon): Expands the list to show the hidden subjects. After expanding, the button changes to "Collapse" with an up arrow.

**Middle column: Results area (currently empty state)**

- Display information:
	- "0 exams" label at the top-left of the area.
	- Empty-state illustration.
	- Text "No matching exams found" and guidance "Try changing the search keyword".

**Right column: POPULAR section**

- Display information:
	- Title "POPULAR" (with a flame icon).
	- Empty-state container with faint text "No data yet" (because the system does not yet have any exams to calculate popularity statistics from).


--------------------------------------------------------------------------------------------------------------

<div align="center">

![Figure 5.2: Learning Materials page of the system](image-1.png)

**Figure 5.2. Learning Materials page of the system**

</div>


**5.1.2. Description of Figure 5.2**
1. Main Banner section (Top area)

- Display information:
	- Tag: "[Book icon] MATERIAL LIBRARY" in blue.
	- Large title: "Learning Materials".
	- Description text: "Explore and download learning materials, lecture notes, and reference documents provided by teachers."
	- 4 statistic cards arranged in a 2x2 grid:
		- Card 1: Folder icon - "0 MATERIALS".
		- Card 2: Graduation cap icon - "0 SUBJECTS".
		- Card 3: Download icon - "0 DOWNLOADS".
		- Card 4: Badge icon - "0 THIS WEEK".

- Expected behavior:
	- The statistic cards must display aggregated values correctly from student data.
	- Hovering over the cards may produce a glow or slight lift effect.

2. Search & Filter Bar section

- Interactive controls and input fields:
	- Search input:
		- Information: Includes a magnifying-glass icon and placeholder text "Search by material name, subject, keywords...".
		- Expected behavior: Users can type text. When pressing Enter or after typing stops for a short delay, the system filters the results below accordingly.

	- Filter dropdown (currently showing "All"):
		- Expected behavior: Clicking opens a list of filtering criteria (for example, by subject, grade, or material type such as PDF/Word/Video). Selecting an item updates the list immediately.

	- Sort dropdown (currently showing "Newest"):
		- Expected behavior: Clicking opens sorting criteria. Examples: Newest, Oldest, Name A-Z, Name Z-A, Most viewed. After selection, the data is sorted automatically.

3. Materials list section (Data Section)

- List header:
	- Display information: Title "All materials" on the left and a gray badge showing "0 materials" on the right.
	- Expected behavior: The count badge should update dynamically based on the filtered results above (for example, if filtering Mathematics returns 5 items, the badge shows "5 materials").

- Content area (currently empty state):
	- Display information: A large gray container with a centered icon (magnifying glass / faded lock) and the text "No matching materials found".
	- Expected behavior: This state must appear when the library is truly empty or when searching/filtering yields no results. The message block should be perfectly centered without disturbing the overall page layout.

--------------------------------------------------------------------------------------------------------------

<div align="center">

![Figure 5.3: Notifications page of the system](image-2.png)

**Figure 5.3. Notifications page of the system**

</div>


**5.1.3. Description of Figure 5.3**
1. Main Banner section (Top area)

- Display information:
	- Tag: "[Bell icon] STUDENT NOTIFICATION CENTER" with a light blue background.
	- Large title: "System Notifications".
	- Status line: "You have 0 unread notifications" (the 0 is bold and blue).

- Expected behavior:
	- The number in the status line must stay perfectly in sync with the unread notification count shown in the Header (red bell icon). When new notifications arrive or the user marks items as read, the number must update immediately.

2. Search & Filter Bar section

- Interactive controls and input fields:
	- Search input:
		- Information: Includes a magnifying-glass icon and placeholder text "Search notifications...".
		- Expected behavior: Users can type text to search by notification title or content.

	- Dropdown "All types":
		- Expected behavior: Clicking opens a list of notification types (for example, From class, From exam, From system). Select one to filter.

	- Dropdown "All statuses":
		- Expected behavior: Clicking opens available statuses (for example, Read, Unread).

	- "Filter" button (light gray background):
		- Expected behavior: Applies the search/filter conditions from the three fields on the left. (For testers: check whether the system requires pressing this button to filter, or whether changing the dropdowns automatically reloads the data.)

3. Notifications list section (Data display area)

- Display information (empty state):
	- Illustration: a faded gray crossed-out bell icon.
	- Main title: "No notifications found."
	- Supporting text: "New notifications from class, exams, and the system will appear here."

- Expected behavior:
	- This view must appear when the user has no notifications or when the selected filters (for example, filtering by "Unread") return no results. The entire message block should be perfectly centered inside the white container.


	--------------------------------------------------------------------------------------------------------------

<div align="center">

![Figure 5.4: Personal Profile page of the system](image-3.png)

**Figure 5.4. Personal Profile page of the system**

</div>


**5.1.4. Description of Figure 5.4**

This page is currently shown in a populated state.

1. Profile Header section

- Display information:
	- Large avatar: Shows the letter "Đ" on a brown background.
	- Tag: "STUDENT PROFILE" in small blue text.
	- Display name: "2783_ Đậu Đại Tài".

- Interactive button:
	- "Edit profile" button (pencil icon):
		- Expected behavior: Clicking opens a form (modal/popup or a new page) that allows the user to update personal information (name, avatar, date of birth, etc.).

2. Overview Statistics section

- Display information:
	- Card 1: "EXAMS COMPLETED" - value 1 (blue).
	- Card 2: "AVERAGE SCORE" - value 6.7 (dark blue/purple).
	- Card 3: "HIGHEST SCORE" - value 6.7 (green).
	- Card 4: "PASS RATE" - value 1/1 (red).

- Expected behavior:
	- The numbers must be calculated and retrieved accurately from the student's test history.

3. Detailed data section (2 columns)

**Left column: Information & History**

- "Personal information" panel:
	- Display information:
		- Account email (toilatai2004@gmail.com).
		- "LAST LOGIN" time (21:07:07 9/7/2026).
	- Expected behavior:
		- The login time must update correctly whenever the user starts a new session.

- "Recent results" panel:
	- Display information:
		- A table listing recently taken tests (Test, Score: 6.7, Submitted at: 04:22:29 10/7/2026, Status: green "Passed" label).
	- Expected behavior:
		- Data must match the statistics cards above.
		- Show no more than the configured number of recent rows (for example, the latest 5 tests).

**Right column: Security Settings panel**

- Static status information:
	- Email: "Verified" (green text).
	- Sign-in method: "Google" (green text).

- Interactive controls and input fields:
	- 2FA section (Two-factor authentication):
		- Information: Currently "Not enabled".
		- "Send enable code" button:
			- Expected behavior: Clicking sends an OTP to toilatai2004@gmail.com and opens an input field for entering the OTP to confirm enabling 2FA.

	- "Set password" panel:
		- Information:
			- Explanatory text about creating a secondary password.
			- "NEW PASSWORD" and "CONFIRM PASSWORD" input fields.
		- Expected behavior:
			- Typed text is masked with dots/asterisks (***).
			- An eye icon appears on the right. Clicking it toggles password visibility between masked and plain text.
		- "Set password" button:
			- Expected behavior: The button becomes enabled only when both fields are filled in. If the two passwords do not match, show the error "Confirmation password does not match". If they match and satisfy the password rules (length, characters, etc.), the system saves the password and shows success.