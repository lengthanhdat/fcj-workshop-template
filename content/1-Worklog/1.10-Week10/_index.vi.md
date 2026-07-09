---
title: "Tuần 10"
date: 2026-04-22
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

# Nhật Ký Thực Tập Tuần 10

**Thời gian:** 22/06/2026 - 26/06/2026

Báo cáo tiến độ và chi tiết các công việc đã thực hiện trong tuần 10 của kỳ thực tập tại AWS (Dự án Aura Academic).

### Chi Tiết Công Việc

| STT | Nội Dung Công Việc | Ngày Thực Hiện | Tình Trạng | Tài Liệu Tham Khảo |
| --- | --- | --- | --- | --- |
| 1 | Triển khai hệ thống Core Backend ứng dụng Aura Academic lên Cloud: Tiến hành deploy chính thức Docker Image của Spring Boot Backend lên cụm Amazon ECS kết hợp với AWS Fargate. Cấu hình các Task Definitions và thiết lập bộ cân bằng tải Application Load Balancer (ALB) để phân phối lưu lượng truy cập đồng đều qua các Availability Zone (AZ A và AZ B). | 22/06/2026 | ✅ Hoàn thành | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 2 | Cấu hình hạ tầng mạng bảo mật (VPC & Subnets): Thiết lập môi trường mạng ảo Amazon VPC. Cấu hình Internet Gateway (IGW) cho các luồng Inbound/Outbound, phối hợp với NAT Gateway trong các Public Subnet nhằm cho phép các container nằm trong Private Subnet kết nối ra internet an toàn để gọi các dịch vụ bên ngoài. | 23/06/2026 | ✅ Hoàn thành | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 3 | Thiết lập cụm tính toán AI chuyên biệt (EC2 GPU Instances): Cấu hình môi trường và triển khai Docker Image chứa mô hình YOLOv8 cùng LiteLLM lên các máy ảo EC2 GPU Instances. Thiết lập cơ chế tự động mở rộng Auto Scaling Group để đảm bảo hệ thống tự động tăng giảm số lượng máy ảo dựa trên lượng bài tập AI cần xử lý. | 24/06/2026 | ✅ Hoàn thành | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 4 | Kiểm thử tích hợp luồng dữ liệu liên thông: Kiểm tra và cấu hình phân quyền AWS IAM để các dịch vụ tương tác an toàn. Thực hiện kiểm thử luồng đồng bộ mã nguồn giao diện từ GitHub Actions qua S3/CloudFront và kiểm tra kết nối lưu trữ dữ liệu từ Backend sang cơ sở dữ liệu ngoại vi MongoDB Atlas. | 25/06/2026 | ✅ Hoàn thành | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |

---

### Kết Quả Đạt Được
- Hoàn thành xuất sắc toàn bộ các mục tiêu đề ra trong tuần.
- Đảm bảo tiến độ dự án thực tập Aura Academic.
