---
title: "Tuần 11"
date: 2026-04-22
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

# Nhật Ký Thực Tập Tuần 11

**Thời gian:** 29/06/2026 - 03/07/2026

Báo cáo tiến độ và chi tiết các công việc đã thực hiện trong tuần 11 của kỳ thực tập tại AWS (Dự án Aura Academic).

### Chi Tiết Công Việc

| STT | Nội Dung Công Việc | Ngày Thực Hiện | Tình Trạng | Tài Liệu Tham Khảo |
| --- | --- | --- | --- | --- |
| 1 | Tối ưu hóa và kiểm thử các tính năng AI cốt lõi trên Cloud: Vận hành và tinh chỉnh luồng xử lý thông minh của Aura Academic. Kiểm thử tính năng phân tích ngôn ngữ lớn bằng cách kết nối Backend với Google Gemini API / Groq API, song song với việc kiểm thử các tính năng nhận diện, chấm điểm cục bộ qua cụm EC2 GPU chạy YOLOv8. | 29/06/2026 | ✅ Hoàn thành | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 2 | Tích hợp luồng dịch vụ thông báo và bảo mật Frontend: Cấu hình luồng gửi Email OTP xác thực cho học viên/giáo viên thông qua Google SMTP kết nối từ hệ thống Cloud. Đồng thời, triển khai cấu hình lớp bảo mật AWS WAF đứng trước CloudFront để chặn các request độc hại tấn công vào giao diện đang lưu trữ trên S3. | 30/06/2026 | ✅ Hoàn thành | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 3 | Thắt chặt bảo mật an toàn thông tin hệ thống: Rà soát lại chính sách bảo mật IAM, thắt chặt Security Groups của cụm ECS Fargate và EC2 GPU. Chỉ cho phép nhận request API hợp lệ điều hướng từ ALB và giới hạn quyền truy cập một chiều từ NAT Gateway ra môi trường internet. | 01/07/2026 | ✅ Hoàn thành | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |
| 4 | Kiểm thử hiệu năng chịu tải hệ thống (Stress Testing): Giả lập lượng lớn request đồng thời (HTTPS Requests) từ người dùng gửi qua CloudFront/ALB. Tiến hành đo lường sức chịu tải của container Spring Boot trên Fargate và tốc độ phản hồi của các cụm máy chủ AI khi xử lý bài thi IELTS cùng lúc. | 02/07/2026 | ✅ Hoàn thành | [Tài liệu AWS](https://cloudjourney.awsstudygroup.com/) |

---

### Kết Quả Đạt Được
- Hoàn thành xuất sắc toàn bộ các mục tiêu đề ra trong tuần.
- Đảm bảo tiến độ dự án thực tập Aura Academic.
