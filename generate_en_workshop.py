import os

workshop_dir = r'd:\fcj-workshop-template\content\5-Workshop'

sections = {
    '5.1-Workshop-overview': """---
title : "Overview of CI/CD Architecture"
date : 2024-01-01 
weight : 1
chapter : false
pre : " <b> 5.1. </b> "
---

### Overview of CI/CD Architecture

To automate the release process of a Web application (containerized with Docker) to Amazon ECS Fargate, we need to build a Continuous Integration / Continuous Deployment (CI/CD) pipeline.

In this Workshop, we will use AWS Developer Tools:
1. **AWS CodeCommit (or GitHub):** The source code repository.
2. **AWS CodeBuild:** The service that pulls the code, runs the Docker build command, and pushes the image to Amazon ECR.
3. **AWS CodePipeline:** The automation orchestrator. When new code is pushed to the `main` branch, CodePipeline automatically triggers CodeBuild, then triggers Amazon ECS to pull the new image and perform a Rolling Update without causing system downtime.

![CI/CD Architecture](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169ce0d2faea7cd5a546d15a/2021/05/26/fargate-cicd-1.jpg)
""",

    '5.2-Prerequiste': """---
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
""",

    '5.3-CodeCommit': """---
title : "Create Repository with AWS CodeCommit"
date : 2024-01-01 
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

### Create Repository with AWS CodeCommit

For CodePipeline to automatically detect new code, we need to push our code to AWS CodeCommit (you can also use GitHub or Bitbucket).

**Steps:**
1. Log in to the **AWS Management Console** and search for **CodeCommit**.
2. Click **Create repository**.
3. Enter the name `MyWebApp-Repo` and add a description (optional), then click **Create**.
4. Get the Clone URL. You will need to set up HTTPS Git credentials for your IAM User to push code.
5. Locally, open your Terminal at the current code directory and run:
   ```bash
   git init
   git remote add origin <CLONE_URL>
   git add .
   git commit -m "Initial commit with buildspec"
   git push -u origin main
   ```
After this step, your source code (including `Dockerfile` and `buildspec.yml`) is safely stored on AWS CodeCommit.
""",

    '5.4-CodeBuild': """---
title : "Package Application with AWS CodeBuild"
date : 2024-01-01 
weight : 4
chapter : false
pre : " <b> 5.4. </b> "
---

### Package Application with AWS CodeBuild & ECR

In this step, we will create an Image repository (ECR) and configure CodeBuild to read the `buildspec.yml` file.

#### 1. Create an ECR Repository
1. Navigate to **Amazon Elastic Container Registry (ECR)**.
2. Click **Create repository** and name it `my-web-app-repo`.
3. Click **Create**. Note down the URI of this repository (e.g., `123456789.dkr.ecr.us-east-1.amazonaws.com/my-web-app-repo`).

#### 2. Create an AWS CodeBuild Project
1. Switch to the **CodeBuild** service, click **Create build project**.
2. Project name: `my-web-app-build`.
3. Source Configuration: Choose AWS CodeCommit and select the `MyWebApp-Repo` you just created.
4. Environment:
   - Choose **Managed Image** -> **Ubuntu** -> **Standard** -> **aws/codebuild/standard:5.0** (or latest).
   - Check the **Privileged** box (Required for CodeBuild to run the `docker build` command).
5. Buildspec: Choose **Use a buildspec file** (CodeBuild will look for `buildspec.yml` in your code).
6. Click **Create build project**.

*Important note:* You must go to the IAM Role of the newly created CodeBuild project and attach the `AmazonEC2ContainerRegistryPowerUser` policy so that CodeBuild has permission to push images to ECR.
""",

    '5.5-CodePipeline': """---
title : "Automation with AWS CodePipeline"
date : 2024-01-01 
weight : 5
chapter : false
pre : " <b> 5.5. </b> "
---

### Automation with AWS CodePipeline

This is the final step to connect everything together.

1. Navigate to **CodePipeline** and click **Create pipeline**.
2. Name: `MyWebApp-Pipeline`. Select **New service role** and click Next.
3. **Source Stage:**
   - Source Provider: **AWS CodeCommit** (or GitHub).
   - Repository: `MyWebApp-Repo`.
   - Branch: `main`.
   - Detection options: Amazon CloudWatch Events (Recommended). Click Next.
4. **Build Stage:**
   - Build Provider: **AWS CodeBuild**.
   - Project name: Select `my-web-app-build` created in the previous step. Click Next.
5. **Deploy Stage:**
   - Deploy Provider: **Amazon ECS**.
   - Cluster: Select your ECS Cluster.
   - Service: Select your ECS Service.
   - Image definitions file: Enter `imagedefinitions.json`. Click Next.
6. Review all configurations and click **Create pipeline**.

As soon as it's created, the Pipeline will automatically run for the first time. From now on, whenever you `git push` new code to the `main` branch, CodePipeline will automatically trigger CodeBuild to build the new Docker Image, and ECS will automatically pull that Image, replacing the old running Image without any application downtime (Zero-downtime).
""",

    '5.6-Cleanup': """---
title : "Resource Cleanup"
date : 2024-01-01 
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

### Resource Cleanup

After completing the Workshop, to avoid unexpected AWS charges, you need to delete the created resources in the following order:

1. **ECS Service and Cluster:** Go to the ECS console, select your Cluster, select the Service, and click Delete. After the Service is deleted, you can Delete the Cluster.
2. **AWS CodePipeline:** Go to CodePipeline, select `MyWebApp-Pipeline`, and click Delete.
3. **AWS CodeBuild:** Go to CodeBuild, select `my-web-app-build`, and click Delete.
4. **AWS CodeCommit:** Go to CodeCommit, delete the repository `MyWebApp-Repo`.
5. **Amazon ECR:** Go to ECR, delete all images inside the `my-web-app-repo` repository, then delete the repository itself.

🎉 **Congratulations on completing the AWS CI/CD Workshop!**
"""
}

for folder, content in sections.items():
    file_path = os.path.join(workshop_dir, folder, '_index.md') # Writing to English file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("English Workshop content has been fully generated.")
