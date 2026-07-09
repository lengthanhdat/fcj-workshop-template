---
title: "Tuần 9"
date: 2026-04-22
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

# Nhật Ký Thực Tập Tuần 9

**Thời gian:** 15/06/2026 - 19/06/2026

Báo cáo tiến độ và chi tiết các công việc đã thực hiện trong tuần 9 của kỳ thực tập tại AWS (Dự án Aura Academic).

### Chi Tiết Công Việc

| STT | Nội Dung Công Việc | Ngày Thực Hiện | Tình Trạng | Tài Liệu Tham Khảo |
| --- | --- | --- | --- | --- |
| 1 | Triển khai giám sát ứng dụng Aura Academic với Amazon CloudWatch: Cấu hình CloudWatch Logs để thu thập và quản lý log tập trung từ các container Spring Boot Backend (chạy trên ECS Fargate) và các máy ảo EC2 GPU Instances. Thiết lập hệ thống cảnh báo (CloudWatch Alarms) khi các chỉ số tài nguyên vượt ngưỡng an toàn để kịp thời phát hiện sự cố hệ thống. | 15/06/2026 | ✅ Hoàn thành | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 2 | Quản lý hiệu năng và độ trễ của cụm AI liên kết: Theo dõi sát sao thời gian phản hồi (latency) của luồng API Inbound đi qua Application Load Balancer (ALB) đến Backend, cũng như luồng xử lý AI cục bộ (EC2 GPU chạy YOLOv8) và luồng gọi API GenAI bên ngoài (Google Gemini, Groq API). Tiến hành phân tích để tối ưu hóa tốc độ xử lý các tính năng chấm điểm và phân tích bài học IELTS. | 16/06/2026 | ✅ Hoàn thành | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 3 | Tối ưu hóa ngân sách hệ thống với AWS Budgets: Sử dụng công cụ AWS Budgets để thiết lập các hạn mức cảnh báo chi phí theo thời gian thực (real-time notification). Hành động này giúp kiểm soát chặt chẽ tiến độ tiêu hao tài nguyên trong quá trình thử nghiệm hệ thống Hybrid Cloud, đảm bảo số dư $200 credit luôn nằm trong phạm vi an toàn. | 17/06/2026 | ✅ Hoàn thành | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 4 | Thực hành quản trị và dọn dẹp tài nguyên rác: Tiến hành rà soát định kỳ trên toàn bộ hệ thống console, thực hiện xóa bỏ các Docker Image phiên bản cũ không dùng tới trên ECR, các ổ đĩa EBS ở trạng thái mồ côi hoặc các bản sao lưu cấu hình cũ nhằm tối ưu hóa không gian lưu trữ và triệt tiêu hoàn toàn các chi phí phát sinh ẩn. | 18/06/2026 | ✅ Hoàn thành | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |

---

### Kết Quả Đạt Được
- Hoàn thành xuất sắc toàn bộ các mục tiêu đề ra trong tuần.
- Đảm bảo tiến độ dự án thực tập Aura Academic.
