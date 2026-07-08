---
title: "Proposal"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# AuraAcademic

## AI-Powered Online Examination and Proctoring Platform on AWS

### 1. Executive Summary

AuraAcademic is an online multiple-choice examination platform integrated with AI Proctoring to ensure fairness and transparency for remote exams. The system utilizes the YOLOv8 model for real-time fraud detection via webcam. By combining AWS architecture (CloudFront, ECS Fargate, EC2 GPU Spot) with a Serverless/Managed Services model, AuraAcademic provides an automated, low-latency, and cost-optimized monitoring solution (reducing operational costs by up to 70% via Spot Instances), catering to the online testing needs of educational institutions.

### 2. Problem Statement

**Current Problem**  
Existing online testing platforms lack effective automated proctoring mechanisms, making it easy for cheating to occur. Commercial AI proctoring solutions (like ProctorU, Respondus) often come with expensive licensing fees, complex integration processes, and demand significant bandwidth or massive server resources.

**Solution**  
AuraAcademic solves this problem by building a complete system:

- **Frontend (Next.js)** statically hosted on Amazon S3 and distributed globally via CloudFront, providing a seamless experience.
- **Backend Core API (Spring Boot)** running on ECS Fargate Spot to handle exam logic, submissions, and authentication.
- **AI Proctoring (FastAPI + YOLOv8)** running on EC2 GPU instances (G4dn series) processing real-time WebSockets streams from students to detect cheating behaviors (e.g., looking away, multiple faces, leaving the frame).
- **Video Evidence** is saved to S3 via a NAT Instance to serve as evidence of security violations.
- **Authentication and Security** uses Amazon Cognito, combined with AWS WAF and IAM.

**Benefits and Return on Investment (ROI)**  
The system automates the proctoring process, minimizing traditional human invigilation. By utilizing Spot Instances for both ECS Fargate and EC2 GPUs, the infrastructure costs are reduced by up to 70% compared to On-Demand pricing. The total cost to maintain the system at a testing/small scale is only around $26 - $30/month. This solution allows schools and educational organizations to easily access advanced exam proctoring technology at a reasonable cost, enhancing the credibility of online exams.

### 3. Solution Architecture

AuraAcademic applies a Microservices architecture on AWS, clearly decoupling the Core API and AI Processing.

**AWS Services Used**

- **Amazon S3 & CloudFront**: Global storage and CDN delivery for the Frontend web app (Next.js) and video evidence storage.
- **Amazon Cognito**: User authentication management via JWT.
- **ALB (Application Load Balancer)**: Routing REST API requests to ECS and WebSockets to the EC2 GPU.
- **Amazon ECS (Fargate Spot)**: Running the Spring Boot Backend container.
- **Amazon EC2 (G4dn Spot)**: Running FastAPI and the YOLOv8 model for real-time video processing.
- **AWS WAF**: Web Application Firewall protecting the app from malicious attacks.
- **Amazon SES**: Sending notification emails and OTPs.
- **VPC, Public/Private Subnets & NAT Instance**: Ensuring internal network isolation and secure outbound Internet access.
- **External Services**: MongoDB Atlas (Database), Google Gemini API (Automated Question Generation).

**Component Design**

- **Web Interface**: Students take exams and stream their cameras; Instructors manage exams and view violation reports.
- **Core API**: Handles exam logic, asynchronous processing (@Async) for exam parsing using Gemini, and saves results.
- **AI Engine**: Receives camera streams via WebSockets, detects cheating using YOLOv8, and automatically uploads violation videos to S3.

### 4. Technical Implementation

**Implementation Phases (3-month Internship Project)**

- **Month 1 (Initiation & Design)**: Analyze VPC architecture, design MongoDB database, prepare the YOLOv8 model.
- **Month 2 (Backend & AI Development)**: Code the Spring Boot API, integrate Gemini for question parsing. Build FastAPI to handle camera WebSockets.
- **Month 3 (Finalization & Deployment)**: Build the Next.js UI, deploy the system to AWS (S3, CloudFront, ECS, EC2 Spot). Conduct testing and write the final internship report.

**Technical Requirements**

- **Frontend**: Next.js, WebSockets client, in-browser video recording.
- **Backend**: Spring Boot, Spring Security, MongoDB Atlas connection.
- **AI**: FastAPI, OpenCV, YOLOv8 object detection, video streaming processing.
- **DevOps/AWS**: Docker, VPC (Public/Private Subnets, NAT Instance).

### 5. Roadmap & Milestones

- **Weeks 1-2**: System analysis, UI/UX design, and code repository setup.
- **Weeks 3-5**: Develop core features (Exam Management) and Gemini-based question parsing.
- **Weeks 6-9**: Integrate AI YOLOv8 for real-time camera stream detection.
- **Weeks 10-12**: Deploy to AWS, test the fault tolerance of Spot Instances, and finalize the internship report documentation.

### 6. Estimated Budget

Using a cost-optimized model with Spot Instances, estimated for a Test/Small Scale environment (~100 concurrent students):

- **Frontend (S3 + CloudFront)**: ~$0.00/month (Free Tier).
- **ECS Fargate Spot (Backend)**: ~$4.00 - $6.00/month.
- **EC2 GPU Spot (AI Engine - g4dn.xlarge)**: ~$3.00/month (Only powered on during exams, ~$0.15/hour).
- **NAT Instance (t4g.nano)**: ~$2.50/month.
- **Application Load Balancer (ALB)**: ~$16.00/month.
- **MongoDB Atlas**: ~$0.00/month (M0 Free Tier).
- **SES & Others**: ~$2.00/month.
  **Total Estimate:** Approximately $28 - $30/month (Can be fully covered by AWS Credits).

### 7. Risk Assessment

**Risk Matrix**

- **Sudden Spot Instance Termination**: High impact, medium probability. (AWS can reclaim Spot instances at any time).
- **High Camera Network Latency**: Medium impact, high probability. (Depends on the student's network connection).
- **Billing Overage**: Medium impact, low probability. (If someone forgets to stop the EC2 GPU).

**Mitigation Strategies**

- **Spot Instance**: Configure an Auto Scaling group or use automated scripts to fallback to On-Demand instances if Spot capacity is unavailable.
- **Latency**: Optimize the video resolution sent to the server (e.g., 480p instead of 1080p), compress video before sending.
- **Cost**: Set up AWS Budgets Alarms to send email alerts when costs exceed $10 and $20 thresholds.

### 8. Expected Outcomes

- **Technical Improvement**: Deliver a real-time, automated AI proctoring solution with a highly available Cloud-Native architecture, optimizing bandwidth through WebSockets.
- **Long-term Value**: The platform can be packaged as a SaaS solution sold to universities/training centers, solving the online cheating problem with significantly lower operating costs than current solutions.
