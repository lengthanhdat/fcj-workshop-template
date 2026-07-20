---
title: "Tuần 9"
date: 2026-04-22
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

# Nhật Ký Thực Tập Tuần 9

**Thời gian:** 15/06/2026-21/06/2026

Báo cáo tiến độ và chi tiết các công việc đã thực hiện trong tuần 9 của kỳ thực tập tại AWS (Dự án Aura Academic).

### Chi Tiết Công Việc

| STT | Nội Dung Công Việc | Ngày Thực Hiện | Tình Trạng | Tài Liệu Tham Khảo |
| --- | --- | --- | --- | --- |
| 1 | Triển khai giám sát ứng dụng Aura Academic với Amazon CloudWatch: Cấu hình CloudWatch Logs để thu thập và quản lý log tập trung từ các container Spring Boot Backend (chạy trên ECS Fargate) và các máy ảo EC2 GPU Instances. Thiết lập hệ thống cảnh báo (CloudWatch Alarms) khi các chỉ số tài nguyên vượt ngưỡng an toàn để kịp thời phát hiện sự cố hệ thống. | Trong tuần | ✅ Hoàn thành | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 2 | Quản lý hiệu năng và độ trễ của cụm AI liên kết: Theo dõi sát sao thời gian phản hồi (latency) của luồng API Inbound đi qua Application Load Balancer (ALB) đến Backend, cũng như luồng xử lý AI cục bộ (EC2 GPU chạy YOLOv8) và luồng gọi API GenAI bên ngoài (Google Gemini, Groq API). | Trong tuần | ✅ Hoàn thành | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |


---

### Kết Quả Đạt Được
- Hoàn thành xuất sắc toàn bộ các mục tiêu đề ra trong tuần.
- Đảm bảo tiến độ dự án thực tập Aura Academic.
