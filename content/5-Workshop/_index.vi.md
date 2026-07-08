---
title: "Workshop"
date: 2024-01-01
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# Triển khai CI/CD Pipeline cho ứng dụng Web trên AWS

#### Tổng quan

Trong quá trình phát triển dự án phần mềm, việc tự động hóa quy trình xây dựng (build), kiểm thử (test) và triển khai (deploy) là vô cùng quan trọng. 

Trong bài lab này, chúng ta sẽ học cách thiết lập một **CI/CD Pipeline** hoàn chỉnh trên AWS sử dụng bộ công cụ Developer Tools (AWS CodeCommit, CodeBuild, CodePipeline) để triển khai tự động một ứng dụng web (dưới dạng Docker container) lên dịch vụ **Amazon ECS (Fargate)**.

Bằng cách này, mỗi khi có thay đổi code mới được đẩy lên repository, hệ thống sẽ tự động đóng gói và cập nhật phiên bản mới nhất của ứng dụng lên môi trường production mà không cần thao tác thủ công, giúp giảm thiểu sai sót và tăng tốc độ phát hành tính năng.

#### Nội dung

1. [Tổng quan về kiến trúc CI/CD](5.1-Workshop-overview/)
2. [Chuẩn bị môi trường & Source Code](5.2-Prerequiste/)
3. [Tạo Repository với AWS CodeCommit](5.3-CodeCommit/)
4. [Đóng gói ứng dụng với AWS CodeBuild & ECR](5.4-CodeBuild/)
5. [Tự động hóa với AWS CodePipeline](5.5-CodePipeline/)
6. [Dọn dẹp tài nguyên](5.6-Cleanup/)
