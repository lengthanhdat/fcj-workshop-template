---
title : "Tổng quan về kiến trúc CI/CD"
date : 2024-01-01 
weight : 1
chapter : false
pre : " <b> 5.1. </b> "
---

### Tổng quan về kiến trúc CI/CD

Để tự động hóa việc phát hành một ứng dụng Web (được đóng gói bằng Docker) lên môi trường Amazon ECS Fargate, chúng ta cần xây dựng một chuỗi CI/CD (Continuous Integration / Continuous Deployment). 

Trong Workshop này, chúng ta sẽ sử dụng bộ công cụ dành cho Developer của AWS:
1. **AWS CodeCommit (hoặc GitHub):** Nơi lưu trữ mã nguồn (Source).
2. **AWS CodeBuild:** Dịch vụ dùng để kéo code về, chạy lệnh build Docker image, và đẩy (push) image đó lên kho chứa Amazon ECR.
3. **AWS CodePipeline:** Dịch vụ điều phối tự động. Khi có code mới đẩy lên nhánh `main`, CodePipeline sẽ tự động gọi CodeBuild, sau đó tự động kích hoạt Amazon ECS để kéo image mới về và cập nhật ứng dụng (Rolling Update) mà không làm gián đoạn hệ thống.

![CI/CD Architecture](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169ce0d2faea7cd5a546d15a/2021/05/26/fargate-cicd-1.jpg)
