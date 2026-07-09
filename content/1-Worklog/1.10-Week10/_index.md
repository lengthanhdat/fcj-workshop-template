---
title: "Week 10"
date: 2026-04-22
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

# Internship Worklog - Week 10

**Timeframe:** 22/06/2026 - 26/06/2026

Progress report and details of tasks completed during week 10 of the internship at AWS (Aura Academic Project).

### Task Details

| No. | Task Description | Date | Status | Reference |
| --- | --- | --- | --- | --- |
| 1 | Deploy Aura Academic Core Backend system to the Cloud: Officially deploy the Spring Boot Backend Docker Image to the Amazon ECS cluster combined with AWS Fargate. Configure Task Definitions and set up an Application Load Balancer (ALB) to distribute traffic evenly across Availability Zones (AZ A and AZ B). | 22/06/2026 | ✅ Completed | [AWS Docs](https://cloudjourney.awsstudygroup.com/) |
| 2 | Configure secure network infrastructure (VPC & Subnets): Establish the Amazon VPC virtual network environment. Configure Internet Gateway (IGW) for Inbound/Outbound flows, coordinated with NAT Gateways in Public Subnets to allow containers residing in Private Subnets to securely connect to the internet to call external services. | 23/06/2026 | ✅ Completed | [AWS Docs](https://cloudjourney.awsstudygroup.com/) |
| 3 | Set up a specialized AI computing cluster (EC2 GPU Instances): Configure the environment and deploy Docker Images containing the YOLOv8 model along with LiteLLM onto EC2 GPU Instances. Establish an Auto Scaling Group mechanism to ensure the system automatically scales the number of virtual machines based on the volume of AI exercises to process. | 24/06/2026 | ✅ Completed | [AWS Docs](https://cloudjourney.awsstudygroup.com/) |
| 4 | Integration test interconnected data flows: Check and configure AWS IAM permissions for services to interact securely. Test the interface source code synchronization flow from GitHub Actions via S3/CloudFront and verify the data storage connection from the Backend to the external MongoDB Atlas database. | 25/06/2026 | ✅ Completed | [AWS Docs](https://cloudjourney.awsstudygroup.com/) |

---

### Achievements
- Successfully accomplished all goals set for the week.
- Ensured the Aura Academic internship project stays on schedule.
