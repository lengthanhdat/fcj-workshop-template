---
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
