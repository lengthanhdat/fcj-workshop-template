---
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
