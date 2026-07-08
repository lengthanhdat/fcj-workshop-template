---
title: "Week6"
date: 2026-04-24
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

### Mục tiêu tuần 6:

- Tích hợp xác thực và phân quyền (Authentication/Authorization).
- Làm việc với Amazon Cognito để quản lý định danh người dùng.
- Hoàn thành các chức năng Đăng nhập/Đăng ký.

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Tìm hiểu sâu về Amazon Cognito.<br>- Cấu hình Cognito User Pool, thiết lập các thuộc tính bắt buộc (Email, Custom Attributes) và App Client. | 25/05/2026 | 25/05/2026 | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 3 | - Tích hợp AWS Amplify / Cognito SDK vào ứng dụng Next.js để xử lý luồng Login, Signup, và Forgot Password. | 26/05/2026 | 26/05/2026 | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 4 | - Ở phía Spring Boot Backend: Triển khai Spring Security.<br>- Viết custom filter chặn request, giải mã và xác thực JWT token được cấp bởi Cognito (sử dụng JWK Set). | 27/05/2026 | 27/05/2026 | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 5 | - Xây dựng API lấy thông tin Profile người dùng hiện tại.<br>- Ghép nối Frontend gọi API Backend kèm theo Bearer Token ở Header.<br>- Cấu hình Axios Interceptors để tự động handle refresh token hoặc redirect khi hết hạn. | 28/05/2026 | 28/05/2026 | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 6 | - Review Pull Requests của team.<br>- Pair-programming với các thành viên đang gặp khó khăn khi gọi API hoặc xử lý state trong React. | 29/05/2026 | 29/05/2026 | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |


---

### Tự đánh giá vai trò Trưởng nhóm & Fullstack Developer:

- Triển khai thành công luồng bảo mật toàn diện từ Frontend đến Backend bằng AWS Cognito.
- Quản lý team hiệu quả thông qua việc review code kỹ lưỡng.
