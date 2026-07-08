import os

workshop_dir = r'd:\fcj-workshop-template\content\5-Workshop'

sections = {
    '5.1-Workshop-overview': """---
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
""",

    '5.2-Prerequiste': """---
title : "Chuẩn bị môi trường & Source Code"
date : 2024-01-01 
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---

### Chuẩn bị môi trường & Source Code

Trước khi bắt đầu, bạn cần đảm bảo các tài nguyên sau đã sẵn sàng:

1. **Tài khoản AWS:** Bạn phải có quyền truy cập vào AWS Management Console với đủ quyền để tạo ECR, ECS, CodeBuild và CodePipeline.
2. **Mã nguồn ứng dụng:** Một ứng dụng Web cơ bản (Ví dụ: React, Next.js, hoặc Spring Boot) đã có sẵn file `Dockerfile` ở thư mục gốc (root directory).
3. **Môi trường ECS có sẵn:** Để tập trung vào CI/CD, giả định rằng bạn đã tạo sẵn một ECS Cluster (chế độ Fargate) và một ECS Service đang chạy một Task Definition cơ bản.

**Thêm file `buildspec.yml` vào mã nguồn:**
Bạn cần tạo một file có tên `buildspec.yml` ở thư mục gốc của code để hướng dẫn AWS CodeBuild cách build ứng dụng. Nội dung mẫu:

```yaml
version: 0.2
phases:
  pre_build:
    commands:
      - echo Đăng nhập vào Amazon ECR...
      - aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com
      - REPOSITORY_URI=$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME
      - COMMIT_HASH=$(echo $CODEBUILD_RESOLVED_SOURCE_VERSION | cut -c 1-7)
      - IMAGE_TAG=${COMMIT_HASH:=latest}
  build:
    commands:
      - echo Build bắt đầu vào `date`
      - echo Build Docker image...
      - docker build -t $REPOSITORY_URI:latest .
      - docker tag $REPOSITORY_URI:latest $REPOSITORY_URI:$IMAGE_TAG
  post_build:
    commands:
      - echo Đẩy Docker image lên ECR...
      - docker push $REPOSITORY_URI:latest
      - docker push $REPOSITORY_URI:$IMAGE_TAG
      - echo Ghi file imagedefinitions.json...
      - printf '[{"name":"my-app-container","imageUri":"%s"}]' $REPOSITORY_URI:$IMAGE_TAG > imagedefinitions.json
artifacts:
  files: imagedefinitions.json
```
""",

    '5.3-CodeCommit': """---
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
""",

    '5.4-CodeBuild': """---
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
""",

    '5.5-CodePipeline': """---
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
""",

    '5.6-Cleanup': """---
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
"""
}

for folder, content in sections.items():
    file_path = os.path.join(workshop_dir, folder, '_index.vi.md')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Workshop content has been fully generated.")
