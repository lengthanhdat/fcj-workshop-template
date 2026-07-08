---
title: "Week11"
date: 2026-04-24
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

### Mục tiêu tuần 11:

- Tự động hóa toàn bộ quy trình triển khai (CI/CD Pipeline).
- Kiểm tra khả năng chịu tải của hệ thống (Load Testing).
- Tiếp tục hoàn thiện nội dung Workshop.

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Tìm hiểu bộ công cụ AWS Developer Tools.<br>- Thiết lập AWS CodeCommit (hoặc kết nối Github) để theo dõi thay đổi mã nguồn. | 29/06/2026 | 29/06/2026 | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 3 | - Viết file buildspec.yml để cấu hình AWS CodeBuild: Tự động build source code Spring Boot, đóng gói Docker image, và push image mới lên ECR. | 30/06/2026 | 30/06/2026 | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 4 | - Thiết lập AWS CodePipeline kết nối Source -> Build -> Deploy.<br>- Tự động cập nhật ECS Service (Blue/Green Deploy) mỗi khi có code mới hợp lệ được merge vào branch main. | 01/07/2026 | 01/07/2026 | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 5 | - Sử dụng Apache JMeter thiết lập kịch bản Load Test: Mô phỏng 200 sinh viên cùng đăng nhập và làm bài thi cùng lúc.<br>- Đánh giá Metrics CPU/RAM của ECS Fargate qua CloudWatch. | 02/07/2026 | 02/07/2026 | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 6 | - Chụp màn hình các bước thiết lập CI/CD, viết tài liệu giải thích chi tiết cho Workshop cá nhân. | 03/07/2026 | 03/07/2026 | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |


---

### Tự đánh giá vai trò Trưởng nhóm & Fullstack Developer:

- Hệ thống CI/CD hoạt động trơn tru giúp tự động hóa khâu release.
- Đảm bảo hệ thống có khả năng chịu tải tốt trong điều kiện thi cử thực tế.
