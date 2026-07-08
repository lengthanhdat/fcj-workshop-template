---
title: "Week8"
date: 2026-04-24
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

### Mục tiêu tuần 8:

- Tích hợp Amazon S3 để lưu trữ dữ liệu multimedia (Avatar, Video bằng chứng).
- Hoàn thiện giao diện Phòng thi dành cho sinh viên.
- Xử lý luồng nộp bài và tính điểm tự động.

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Tích hợp AWS SDK for Java vào Spring Boot.<br>- Viết API tạo S3 Presigned URL để Frontend có thể upload file trực tiếp lên S3 bucket một cách bảo mật mà không qua Backend trung gian. | 08/06/2026 | 08/06/2026 | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 3 | - Cấu hình Frontend Next.js xử lý việc chụp ảnh xác thực từ Webcam và upload lên S3 sử dụng Presigned URL nhận được. | 09/06/2026 | 09/06/2026 | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 4 | - Xây dựng giao diện Làm bài thi: Hiển thị câu hỏi tuần tự, có đồng hồ đếm ngược (Countdown Timer) đồng bộ với thời gian server. | 10/06/2026 | 10/06/2026 | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 5 | - Xử lý logic auto-submit: Tự động thu bài khi hết giờ.<br>- Viết API Backend nhận danh sách câu trả lời, so sánh với đáp án chuẩn và tính điểm tự động. | 11/06/2026 | 11/06/2026 | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 6 | - Phối hợp với thành viên phụ trách AI: Thảo luận về chuẩn giao tiếp (WebSockets/API) để nhận kết quả cảnh báo gian lận từ model YOLOv8 gửi về Frontend. | 12/06/2026 | 12/06/2026 | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |


---

### Tự đánh giá vai trò Trưởng nhóm & Fullstack Developer:

- Giải quyết triệt để bài toán lưu trữ file tĩnh bằng S3 Presigned URL, giảm tải cho Backend server.
- Hoàn thành module Phòng thi phức tạp nhất của dự án.
