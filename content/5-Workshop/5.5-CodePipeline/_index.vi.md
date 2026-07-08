---
title : "Tự động hóa với AWS CodePipeline"
date : 2024-01-01 
weight : 5
chapter : false
pre : " <b> 5.5. </b> "
---

### Tự động hóa với AWS CodePipeline

Đây là bước cuối cùng kết nối mọi thứ lại với nhau.

1. Truy cập **CodePipeline** và nhấn **Create pipeline**.
2. Đặt tên: `MyWebApp-Pipeline`. Chọn **New service role** và nhấn Next.
3. **Source Stage:**
   - Source Provider: **AWS CodeCommit** (hoặc GitHub).
   - Repository: `MyWebApp-Repo`.
   - Branch: `main`.
   - Detection options: Amazon CloudWatch Events (Khuyên dùng). Nhấn Next.
4. **Build Stage:**
   - Build Provider: **AWS CodeBuild**.
   - Project name: Chọn `my-web-app-build` vừa tạo ở bài trước. Nhấn Next.
5. **Deploy Stage:**
   - Deploy Provider: **Amazon ECS**.
   - Cluster: Chọn ECS Cluster của bạn.
   - Service: Chọn ECS Service của bạn.
   - Image definitions file: Ghi là `imagedefinitions.json`. Nhấn Next.
6. Xem lại toàn bộ cấu hình và nhấn **Create pipeline**.

Ngay khi tạo xong, Pipeline sẽ tự động chạy lần đầu tiên. Từ bây giờ, bất cứ khi nào bạn `git push` code mới lên nhánh `main`, CodePipeline sẽ tự động kích hoạt CodeBuild để build Docker Image mới và ECS sẽ tự động kéo Image đó về, thay thế cho Image cũ đang chạy mà ứng dụng không hề bị gián đoạn (Zero-downtime).
