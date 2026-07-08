---
title: "Workshop"
date: 2024-01-01
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# Deploying CI/CD Pipeline for Web Application on AWS

#### Overview

In the software development process, automating the build, test, and deployment phases is absolutely critical.

In this lab, we will learn how to set up a complete **CI/CD Pipeline** on AWS using Developer Tools (AWS CodeCommit, CodeBuild, CodePipeline) to automatically deploy a web application (as a Docker container) to the **Amazon ECS (Fargate)** service.

By doing this, every time new code changes are pushed to the repository, the system will automatically package and update the latest version of the application to the production environment without manual intervention, minimizing errors and accelerating feature releases.

#### Contents

1. [Overview of CI/CD Architecture](5.1-Workshop-overview/)
2. [Environment & Source Code Preparation](5.2-Prerequiste/)
3. [Create Repository with AWS CodeCommit](5.3-CodeCommit/)
4. [Package Application with AWS CodeBuild & ECR](5.4-CodeBuild/)
5. [Automation with AWS CodePipeline](5.5-CodePipeline/)
6. [Resource Cleanup](5.6-Cleanup/)
