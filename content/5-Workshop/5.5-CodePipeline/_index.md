---
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
