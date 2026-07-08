---
title : "Đóng gói ứng dụng với AWS CodeBuild"
date : 2024-01-01 
weight : 4
chapter : false
pre : " <b> 5.4. </b> "
---

### Đóng gói ứng dụng với AWS CodeBuild & ECR

Trong bước này, chúng ta sẽ tạo một kho lưu trữ Image (ECR) và cấu hình CodeBuild để đọc file `buildspec.yml`.

#### 1. Tạo kho lưu trữ ECR
1. Truy cập **Amazon Elastic Container Registry (ECR)**.
2. Chọn **Create repository**, đặt tên là `my-web-app-repo`.
3. Nhấn **Create**. Ghi chú lại URI của kho lưu trữ này (Ví dụ: `123456789.dkr.ecr.us-east-1.amazonaws.com/my-web-app-repo`).

#### 2. Tạo AWS CodeBuild Project
1. Chuyển sang dịch vụ **CodeBuild**, chọn **Create build project**.
2. Đặt tên Project: `my-web-app-build`.
3. Cấu hình Source: Chọn AWS CodeCommit và chọn repository `MyWebApp-Repo` bạn vừa tạo.
4. Môi trường (Environment):
   - Chọn **Managed Image** -> **Ubuntu** -> **Standard** -> **aws/codebuild/standard:5.0** (hoặc mới nhất).
   - Đánh dấu tick vào ô **Privileged** (Bắt buộc phải check để CodeBuild có thể chạy lệnh `docker build`).
5. Ở phần Buildspec: Chọn **Use a buildspec file** (CodeBuild sẽ tự tìm file `buildspec.yml` trong code của bạn).
6. Nhấn **Create build project**.

*Lưu ý quan trọng:* Bạn phải vào phần IAM Role của CodeBuild vừa được tạo, và gắn thêm Policy `AmazonEC2ContainerRegistryPowerUser` để CodeBuild có quyền đẩy image lên ECR.
