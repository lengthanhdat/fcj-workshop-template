---
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
