---
title: "Week9"
date: 2026-04-24
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

### Mục tiêu tuần 9:

- Đóng gói ứng dụng thành các container (Dockerization).
- Cấu hình triển khai thử nghiệm Backend lên Amazon ECS Fargate.
- Khắc phục các sự cố về mạng, CORS và bảo mật.

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Viết Dockerfile tối ưu (Multi-stage build) cho dự án Spring Boot (sử dụng JRE nhẹ) và dự án Next.js (Standalone mode). | 15/06/2026 | 15/06/2026 | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 3 | - Viết file docker-compose.yml để chạy đồng thời Frontend, Backend và kết nối MongoDB dưới local network để kiểm thử toàn diện. | 16/06/2026 | 16/06/2026 | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 4 | - Khởi tạo Amazon ECR (Elastic Container Registry).<br>- Build và push các Docker image lên ECR repository thông qua AWS CLI. | 17/06/2026 | 17/06/2026 | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 5 | - Cấu hình Amazon ECS (Elastic Container Service) theo mô hình Fargate (Serverless).<br>- Tạo Task Definition, định nghĩa CPU/Memory và thiết lập Environment Variables (DB URI, Secrets). | 18/06/2026 | 18/06/2026 | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 6 | - Tạo ECS Cluster và Service.<br>- Khắc phục các lỗi cấu hình Load Balancer (ALB), Target Groups và xử lý triệt để lỗi CORS khi Frontend ở một domain khác gọi vào ECS API. | 19/06/2026 | 19/06/2026 | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |


---

### Tự đánh giá vai trò Trưởng nhóm & Fullstack Developer:

- Nâng cấp kỹ năng DevOps: Chuyển đổi thành công dự án từ chạy local sang kiến trúc container hóa trên AWS ECS Fargate.
