---
title : "Dọn dẹp tài nguyên"
date : 2024-01-01 
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

### Dọn dẹp tài nguyên (Clean up)

Sau khi hoàn thành Workshop, để tránh phát sinh chi phí AWS ngoài ý muốn, bạn cần thực hiện xóa các tài nguyên đã tạo theo thứ tự sau:

1. **ECS Service và Cluster:** Vào màn hình ECS, chọn Cluster của bạn, chọn Service và nhấn Delete. Sau khi Service bị xóa, bạn có thể Delete Cluster.
2. **AWS CodePipeline:** Vào CodePipeline, chọn `MyWebApp-Pipeline` và nhấn Delete.
3. **AWS CodeBuild:** Vào CodeBuild, chọn `my-web-app-build` và Delete.
4. **AWS CodeCommit:** Vào CodeCommit, xóa repository `MyWebApp-Repo`.
5. **Amazon ECR:** Vào ECR, xóa toàn bộ image bên trong repository `my-web-app-repo`, sau đó xóa repository.

🎉 **Chúc mừng bạn đã hoàn thành Workshop về CI/CD trên AWS!**
