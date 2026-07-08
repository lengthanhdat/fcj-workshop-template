---
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
