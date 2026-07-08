---
title : "Environment & Source Code Preparation"
date : 2024-01-01 
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---

### Environment & Source Code Preparation

Before starting, ensure the following resources are ready:

1. **AWS Account:** You must have access to the AWS Management Console with sufficient permissions to create ECR, ECS, CodeBuild, and CodePipeline.
2. **Application Source Code:** A basic Web application (e.g., React, Next.js, or Spring Boot) with a `Dockerfile` in the root directory.
3. **Existing ECS Environment:** To focus on CI/CD, assume you have already created an ECS Cluster (Fargate type) and an ECS Service running a basic Task Definition.

**Add `buildspec.yml` to the source code:**
You need to create a file named `buildspec.yml` in the root directory of your code to instruct AWS CodeBuild on how to build the application. Sample content:

```yaml
version: 0.2
phases:
  pre_build:
    commands:
      - echo Logging into Amazon ECR...
      - aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com
      - REPOSITORY_URI=$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME
      - COMMIT_HASH=$(echo $CODEBUILD_RESOLVED_SOURCE_VERSION | cut -c 1-7)
      - IMAGE_TAG=${COMMIT_HASH:=latest}
  build:
    commands:
      - echo Build started on `date`
      - echo Building the Docker image...
      - docker build -t $REPOSITORY_URI:latest .
      - docker tag $REPOSITORY_URI:latest $REPOSITORY_URI:$IMAGE_TAG
  post_build:
    commands:
      - echo Pushing the Docker image to ECR...
      - docker push $REPOSITORY_URI:latest
      - docker push $REPOSITORY_URI:$IMAGE_TAG
      - echo Writing imagedefinitions.json file...
      - printf '[{"name":"my-app-container","imageUri":"%s"}]' $REPOSITORY_URI:$IMAGE_TAG > imagedefinitions.json
artifacts:
  files: imagedefinitions.json
```
