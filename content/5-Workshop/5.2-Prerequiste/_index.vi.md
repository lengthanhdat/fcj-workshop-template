---
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
