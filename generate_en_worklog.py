import os
from datetime import datetime, timedelta

def get_dates(start_date, week_num):
    week_start = start_date + timedelta(days=(week_num - 1) * 7)
    days = []
    for i in range(5):  # Mon to Fri
        day = week_start + timedelta(days=i)
        days.append(day.strftime("%d/%m/%Y"))
    return days

start_date = datetime(2026, 4, 20)

weekly_data = [
    {
        "week": "1.1-Week1",
        "goals": [
            "Familiarize with the First Cloud Journey internship process and rules.",
            "Grasp fundamental Cloud Computing concepts and the AWS ecosystem.",
            "Create and secure an AWS Free Tier account (IAM, MFA, Billing Alarm).",
            "Hold the first team meeting and brainstorm project ideas."
        ],
        "tasks": [
            "- Attend FCJ Orientation.<br>- Read guidelines and weekly report requirements.<br>- Get to know team members.",
            "- Learn Cloud Computing overview (IaaS, PaaS, SaaS).<br>- Create AWS Free Tier account.<br>- Enable Multi-Factor Authentication (MFA).",
            "- Set up AWS Budgets and CloudWatch Alarms to receive email alerts for costs over $1.",
            "- Explore AWS Management Console.<br>- Deep dive into AWS IAM.<br>- Practice creating IAM Users, Groups, and Roles with Least Privilege.",
            "- Hold team kick-off meeting via Google Meet/Zoom.<br>- Brainstorm final project ideas.<br>- Agree on: AI-powered proctoring platform (AuraAcademic)."
        ],
        "eval": "- Successfully onboarded to AWS and secured the account.\n- Built initial engagement with team members.\n- Established clear project goals."
    },
    {
        "week": "1.2-Week2",
        "goals": [
            "Master Amazon EC2 compute service and related concepts (AMI, EBS).",
            "Understand and deploy AWS VPC network infrastructure (Subnets, Route Tables, IGW).",
            "Finalize the Project Proposal and assign team roles."
        ],
        "tasks": [
            "- Study Amazon Virtual Private Cloud (VPC), CIDR blocks, Public/Private Subnets, IGW, and NAT Gateway.<br>- Draw a basic network architecture.",
            "- Practice deploying a Custom VPC via AWS Console.<br>- Configure Route Tables to route traffic to the Internet for the Public Subnet.",
            "- Launch an Amazon EC2 instance (Linux AMI) in the Public Subnet.<br>- Configure Security Groups to open port 22 (SSH) and 80 (HTTP).<br>- Connect via SSH.",
            "- Install Apache/Nginx on EC2 to host a basic static website.<br>- Learn how to attach an Elastic IP.<br>- Explore Amazon EBS and mount volumes.",
            "- Finalize AuraAcademic core features.<br>- Draft the Project Proposal.<br>- Officially take on the role of Fullstack Team Leader."
        ],
        "eval": "- Mastered AWS networking and virtual servers.\n- Completed a high-quality Project Proposal and effectively assigned team tasks."
    },
    {
        "week": "1.3-Week3",
        "goals": [
            "Research and practice AWS S3 storage service.",
            "Analyze and select a database (Amazon RDS vs DynamoDB).",
            "Finalize the System Architecture for AuraAcademic."
        ],
        "tasks": [
            "- Study Amazon S3 (Buckets, Objects, Storage Classes).<br>- Practice creating S3 Buckets, Bucket Policies, and CORS.<br>- Demo Static Website Hosting.",
            "- Research Relational Database Amazon RDS (MySQL/PostgreSQL) and Multi-AZ features.",
            "- Research NoSQL Amazon DynamoDB.<br>- Analyze project data requirements.<br>- Decide to use MongoDB Atlas combined with S3 for media storage.",
            "- Use Draw.io to design the overall System Architecture Diagram.<br>- Break down the system into modules: Frontend, Core API, and AI Processing.",
            "- Hold a team meeting to review the architecture.<br>- Address technical questions from AI and Frontend members."
        ],
        "eval": "- Understand S3 and Database operations well.\n- Designed a clear, logical architecture, giving the team a holistic view of the project."
    },
    {
        "week": "1.4-Week4",
        "goals": [
            "Deep dive into AWS CloudFront (CDN) and Amazon Route 53 (DNS).",
            "Finalize the Tech Stack and list the Backlog.",
            "Design the Database Schema."
        ],
        "tasks": [
            "- Study Amazon CloudFront operations.<br>- Practice integrating CloudFront with S3 Buckets for low-latency static content delivery.",
            "- Learn Amazon Route 53: Domain registration, Hosted Zones, and Routing Policies.",
            "- Finalize Tech Stack: Next.js (Frontend), Spring Boot (Backend), MongoDB Atlas (Database), FastAPI (AI).",
            "- Design detailed Database Schema for Collections: Users, Exams, Questions, Submissions.<br>- Define relationships and indexes.",
            "- Create a workspace on Jira/Trello.<br>- Add features to the Product Backlog.<br>- Plan details for initial Sprints."
        ],
        "eval": "- Ready with advanced AWS networking theory (CDN, DNS).\n- Prepared all project management infrastructure for the team to start coding."
    },
    {
        "week": "1.5-Week5",
        "goals": [
            "Finalize UI/UX design on Figma.",
            "Initialize the Repository and set up Coding Conventions.",
            "Build the Boilerplate for both Frontend and Backend."
        ],
        "tasks": [
            "- Collaborate with the Frontend team to finalize UI/UX on Figma for Login, Admin Dashboard, and Exam Interface.",
            "- Create a Github Repository.<br>- Set up Git Flow and branch protection.<br>- Configure ESLint, Prettier, and Husky for code quality.",
            "- Initialize the Frontend base project using Next.js (App Router).<br>- Install Tailwind CSS and Shadcn UI.<br>- Build the main Layout and Navbar.",
            "- Initialize the Backend base project using Spring Boot.<br>- Connect to MongoDB Atlas via secure URI.<br>- Create standard MVC folder structure.",
            "- Sprint Planning Meeting: Assign initial coding modules to members.<br>- Guide the team on checking out branches, committing, and creating PRs."
        ],
        "eval": "- Set up the project professionally from the start.\n- Built a solid boilerplate that helps members easily start coding."
    },
    {
        "week": "1.6-Week6",
        "goals": [
            "Integrate Authentication and Authorization.",
            "Work with Amazon Cognito for user identity management.",
            "Complete Login/Register functionalities."
        ],
        "tasks": [
            "- Deep dive into Amazon Cognito.<br>- Configure Cognito User Pool, set required attributes, and create an App Client.",
            "- Integrate AWS Amplify / Cognito SDK into the Next.js app to handle Login, Signup, and Forgot Password flows.",
            "- On the Spring Boot side: Implement Spring Security.<br>- Write custom filters to intercept requests and validate JWT tokens issued by Cognito.",
            "- Build an API to fetch the current user's Profile.<br>- Connect Frontend to call Backend APIs with Bearer Tokens.<br>- Configure Axios Interceptors.",
            "- Review team Pull Requests.<br>- Pair-program with members struggling with API calls or React state."
        ],
        "eval": "- Successfully deployed a comprehensive security flow from Frontend to Backend using AWS Cognito.\n- Managed the team effectively through thorough code reviews."
    },
    {
        "week": "1.7-Week7",
        "goals": [
            "Develop core APIs for the Exam Management module.",
            "Finalize the Dashboard UI for Instructors/Proctors.",
            "Optimize source code and provide technical support."
        ],
        "tasks": [
            "- Code CRUD APIs in Spring Boot for entities: Course, Exam, and Question.<br>- Apply DTOs to map data between Controllers and Services.",
            "- Implement logic to import multiple-choice questions from Excel/CSV to MongoDB using Apache POI.",
            "- On Frontend: Complete the Proctor Dashboard UI.<br>- Use React Query / SWR to fetch exam lists and display them in a Data Table.",
            "- Create 'Create Exam' forms with comprehensive Validation (React Hook Form + Zod).<br>- Handle complex components like Date/Time Pickers.",
            "- Database Optimization: Create MongoDB Indexes for frequently queried fields.<br>- Sprint review meeting to evaluate progress."
        ],
        "eval": "- Completed the core business logic of the application (Exam Management).\n- Achieved high coding productivity and maintained clean architectures."
    },
    {
        "week": "1.8-Week8",
        "goals": [
            "Integrate Amazon S3 to store multimedia data (Avatars, Evidence Videos).",
            "Finalize the Exam Room UI for students.",
            "Process the exam submission and auto-grading flow."
        ],
        "tasks": [
            "- Integrate AWS SDK for Java into Spring Boot.<br>- Write an API to generate S3 Presigned URLs for direct, secure file uploads from Frontend to S3.",
            "- Configure Next.js to handle webcam captures and upload them to S3 using the received Presigned URLs.",
            "- Build the Exam Interface: Display questions sequentially, include a Countdown Timer synced with the server.",
            "- Implement auto-submit logic when time runs out.<br>- Write Backend APIs to receive answers, compare them with correct answers, and calculate scores.",
            "- Coordinate with the AI team member: Discuss WebSockets/API standards to receive fraud warnings from the YOLOv8 model."
        ],
        "eval": "- Solved static file storage effectively using S3 Presigned URLs, offloading the Backend server.\n- Completed the most complex module of the project."
    },
    {
        "week": "1.9-Week9",
        "goals": [
            "Dockerize the application.",
            "Configure and test deploying the Backend to Amazon ECS Fargate.",
            "Resolve network, CORS, and security issues."
        ],
        "tasks": [
            "- Write optimized Dockerfiles (Multi-stage builds) for Spring Boot and Next.js.",
            "- Write docker-compose.yml to run Frontend, Backend, and MongoDB locally for comprehensive testing.",
            "- Initialize Amazon ECR.<br>- Build and push Docker images to the ECR repository via AWS CLI.",
            "- Configure Amazon ECS using Fargate (Serverless).<br>- Create Task Definitions, define CPU/Memory, and set Environment Variables.",
            "- Create ECS Cluster and Service.<br>- Troubleshoot Load Balancer (ALB) configs and fully resolve CORS errors."
        ],
        "eval": "- Upgraded DevOps skills: Successfully transitioned the project from running locally to a containerized architecture on AWS ECS Fargate."
    },
    {
        "week": "1.10-Week10",
        "goals": [
            "Complete Frontend deployment on AWS (S3 + CloudFront).",
            "Perform End-to-End (E2E) Testing.",
            "Outline ideas and prepare documentation for the personal Workshop."
        ],
        "tasks": [
            "- Build the Next.js app into static HTML/JS files.<br>- Deploy to an Amazon S3 Bucket and use CloudFront CDN for global distribution.",
            "- Configure SSL/TLS Certificates (ACM) on CloudFront and ALB to support HTTPS securely.",
            "- Organize a User Acceptance Testing (UAT) session with all team members.<br>- Simulate Proctor and Student roles.",
            "- Review Amazon CloudWatch logs, identify bottlenecks, and fix bugs (mostly mobile UI and S3 image display issues).",
            "- Start drafting the outline for the personal technical Workshop: Chose the topic 'Deploying CI/CD with AWS CodePipeline'."
        ],
        "eval": "- The AuraAcademic system is fully operational and smooth on the Production Cloud environment.\n- Demonstrated thoroughness in testing and bug fixing."
    },
    {
        "week": "1.11-Week11",
        "goals": [
            "Automate the entire deployment process (CI/CD Pipeline).",
            "Perform Load Testing on the system.",
            "Continue finalizing the Workshop content."
        ],
        "tasks": [
            "- Explore AWS Developer Tools.<br>- Set up AWS CodeCommit to track source code changes.",
            "- Write a buildspec.yml file to configure AWS CodeBuild: Auto-build Spring Boot, package the Docker image, and push it to ECR.",
            "- Set up AWS CodePipeline connecting Source -> Build -> Deploy.<br>- Automate ECS Service updates when valid code is merged into main.",
            "- Use Apache JMeter for Load Testing: Simulate 200 students logging in and taking exams simultaneously.<br>- Evaluate CloudWatch metrics.",
            "- Take screenshots of CI/CD setups and write detailed explanations for the personal Workshop."
        ],
        "eval": "- The CI/CD system runs smoothly, automating release workflows.\n- Ensured the system handles real-world exam loads effectively."
    },
    {
        "week": "1.12-Week12",
        "goals": [
            "Wrap up the internship and finalize the Worklog report.",
            "100% complete the Workshop documentation and Project Demo.",
            "Prepare presentation slides for Demo Day."
        ],
        "tasks": [
            "- Compile and update the entire 12-week Worklog into the personal report repository (Hugo Template).",
            "- Review the 'Deploying CI/CD Pipeline on AWS' Workshop.<br>- Edit Markdown formatting, add alerts, and double-check illustrations.",
            "- Record a Demo video of the AuraAcademic project in action (From creating an exam to a student taking it and AI detecting fraud).",
            "- Design presentation slides for Demo Day with the team.<br>- Conduct a dry-run meeting, assign speakers, and prepare for Q&A.",
            "- Package all source code, design documents, and personal reports to submit to First Cloud Journey organizers before the deadline."
        ],
        "eval": "- Successfully achieved all goals and deliverables of the internship program.\n- Grew significantly in Cloud (AWS) skills, Fullstack Development, and Leadership."
    }
]

base_dir = r'd:\fcj-workshop-template\content\1-Worklog'
doc_link = "https://cloudjourney.awsstudygroup.com/"

for idx, data in enumerate(weekly_data):
    week_num = idx + 1
    dates = get_dates(start_date, week_num)
    
    week_dir = os.path.join(base_dir, data['week'])
    index_file = os.path.join(week_dir, '_index.md') # Writing to the English file
    
    if not os.path.exists(week_dir):
        os.makedirs(week_dir)
        
    goals_md = "\n".join([f"- {g}" for g in data['goals']])
    
    table_md = "| Day | Task | Start Date | End Date | Resource |\n"
    table_md += "| --- | --- | --- | --- | --- |\n"
    
    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    for i in range(5):
        table_md += f"| {days_of_week[i]} | {data['tasks'][i]} | {dates[i]} | {dates[i]} | [AWS Docs]({doc_link}) |\n"
    
    content = f"""---
title: "Week{week_num}"
date: 2026-04-24
weight: {week_num}
chapter: false
pre: " <b> 1.{week_num}. </b> "
---

### Week {week_num} Objectives:

{goals_md}

---

### Tasks to be implemented this week:

{table_md}

---

### Self-evaluation as Team Leader & Fullstack Developer:

{data['eval']}
"""
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Successfully generated English worklogs.")
