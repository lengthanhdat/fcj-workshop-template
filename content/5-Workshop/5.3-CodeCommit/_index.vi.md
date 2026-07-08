---
title : "Tạo Repository với AWS CodeCommit"
date : 2024-01-01 
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

### Tạo Repository với AWS CodeCommit

Để CodePipeline có thể tự động bắt sự kiện khi có code mới, chúng ta cần đẩy code lên AWS CodeCommit (bạn cũng có thể dùng GitHub hoặc Bitbucket).

**Các bước thực hiện:**
1. Truy cập **AWS Management Console**, tìm kiếm dịch vụ **CodeCommit**.
2. Nhấn nút **Create repository**.
3. Nhập tên là `MyWebApp-Repo` và thêm mô tả (nếu cần), sau đó nhấn **Create**.
4. Lấy link Clone URL. Bạn sẽ cần thiết lập HTTPS Git credentials cho IAM User của bạn để có quyền push code.
5. Ở dưới local, mở Terminal tại thư mục code hiện tại và chạy các lệnh:
   ```bash
   git init
   git remote add origin <URL_VỪA_CLONE>
   git add .
   git commit -m "Initial commit with buildspec"
   git push -u origin main
   ```
Sau bước này, source code của bạn (bao gồm cả `Dockerfile` và `buildspec.yml`) đã nằm an toàn trên AWS CodeCommit.
