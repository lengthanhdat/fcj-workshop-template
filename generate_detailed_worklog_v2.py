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
            "Làm quen với quy trình thực tập First Cloud Journey và các quy định của chương trình.",
            "Nắm vững các khái niệm cơ bản về Cloud Computing và hệ sinh thái AWS.",
            "Tạo và bảo mật tài khoản AWS Free Tier (Thiết lập IAM, MFA, Billing Alarm).",
            "Tổ chức họp nhóm đầu tiên, khởi động quá trình brainstorm ý tưởng dự án."
        ],
        "tasks": [
            "- Tham gia buổi định hướng (Orientation) của chương trình FCJ.<br>- Đọc kỹ các tài liệu hướng dẫn, nội quy và yêu cầu báo cáo thực tập hàng tuần.<br>- Giao lưu và làm quen với các thành viên trong nhóm.",
            "- Tìm hiểu tổng quan về Cloud Computing (IaaS, PaaS, SaaS).<br>- Tạo tài khoản AWS Free Tier.<br>- Kích hoạt Multi-Factor Authentication (MFA) cho tài khoản Root để tăng cường bảo mật.",
            "- Thiết lập AWS Budgets và cấu hình CloudWatch Alarm để nhận thông báo qua email khi chi phí vượt quá 1 USD (Tránh rủi ro phát sinh chi phí ngoài ý muốn).",
            "- Khám phá AWS Management Console.<br>- Tìm hiểu sâu về AWS IAM (Identity and Access Management).<br>- Thực hành tạo IAM User, Group, Role và gán các Policy theo nguyên tắc đặc quyền tối thiểu (Least Privilege).",
            "- Tổ chức buổi họp nhóm (Kick-off meeting) qua Google Meet/Zoom.<br>- Bắt đầu thảo luận các ý tưởng dự án cuối khóa.<br>- Thống nhất hướng đi: Xây dựng nền tảng thi trực tuyến có giám sát AI (AuraAcademic)."
        ],
        "eval": "- Đã làm quen với môi trường AWS và thiết lập bảo mật an toàn cho tài khoản.\n- Xây dựng được sự gắn kết ban đầu với các thành viên trong nhóm.\n- Xác định được mục tiêu dự án rõ ràng."
    },
    {
        "week": "1.2-Week2",
        "goals": [
            "Làm chủ dịch vụ tính toán Amazon EC2 và các khái niệm liên quan (AMI, EBS).",
            "Hiểu và tự tay triển khai hạ tầng mạng ảo AWS VPC (Subnets, Route Tables, IGW).",
            "Hoàn thiện bản đề xuất dự án (Project Proposal) và chốt vai trò thành viên."
        ],
        "tasks": [
            "- Tìm hiểu lý thuyết về Amazon Virtual Private Cloud (VPC), CIDR block, Public/Private Subnet, Internet Gateway (IGW) và NAT Gateway.<br>- Vẽ sơ đồ mạng cơ bản cho hệ thống.",
            "- Thực hành triển khai một Custom VPC hoàn chỉnh thông qua AWS Console.<br>- Cấu hình Route Table để định tuyến traffic ra Internet cho Public Subnet.",
            "- Khởi tạo máy chủ ảo Amazon EC2 (Linux AMI) nằm trong Public Subnet.<br>- Cấu hình Security Group mở port 22 (SSH) và 80 (HTTP).<br>- Kết nối SSH vào EC2 instance từ máy local sử dụng key pair (.pem).",
            "- Cài đặt Apache/Nginx trên EC2 để host một trang web tĩnh cơ bản.<br>- Tìm hiểu cách gán Elastic IP cho EC2.<br>- Tìm hiểu về Amazon EBS (Elastic Block Store) và cách mount volume vào EC2.",
            "- Cùng nhóm chốt lại các tính năng cốt lõi của AuraAcademic.<br>- Soạn thảo file Proposal cho dự án.<br>- Phân công vai trò chính thức: Đảm nhận vị trí Trưởng nhóm kiêm Fullstack Developer."
        ],
        "eval": "- Nắm vững kiến thức mạng và máy chủ ảo trên AWS, có khả năng tự triển khai hạ tầng cơ bản.\n- Đã hoàn thành bản Proposal dự án chất lượng, phân công công việc hợp lý cho nhóm."
    },
    {
        "week": "1.3-Week3",
        "goals": [
            "Nghiên cứu và thực hành các dịch vụ lưu trữ AWS S3.",
            "Tìm hiểu và phân tích lựa chọn cơ sở dữ liệu (Amazon RDS vs DynamoDB).",
            "Chốt kiến trúc hệ thống (System Architecture) cho dự án AuraAcademic."
        ],
        "tasks": [
            "- Tìm hiểu Amazon S3 (Buckets, Objects, Storage Classes, Versioning).<br>- Thực hành tạo S3 Bucket, cấu hình Bucket Policy và CORS.<br>- Demo tính năng Static Website Hosting trên S3.",
            "- Nghiên cứu về Cơ sở dữ liệu quan hệ Amazon RDS (MySQL/PostgreSQL) và các tính năng Multi-AZ, Read Replicas.",
            "- Nghiên cứu NoSQL Database - Amazon DynamoDB.<br>- Phân tích yêu cầu dữ liệu của dự án AuraAcademic: Cần lưu trữ log bài thi linh hoạt.<br>- Cùng nhóm ra quyết định sử dụng MongoDB Atlas kết hợp S3 để lưu hình ảnh/video.",
            "- Sử dụng công cụ Draw.io để vẽ Sơ đồ kiến trúc tổng thể (Architecture Diagram).<br>- Phân rã hệ thống thành các module: Frontend (UI), Core API, và AI Processing (YOLOv8).",
            "- Họp nhóm review sơ đồ kiến trúc.<br>- Giải đáp các thắc mắc về kỹ thuật cho các thành viên phụ trách mảng AI và Frontend."
        ],
        "eval": "- Đã hiểu rõ cách vận hành của S3 và RDS/DynamoDB.\n- Thiết kế kiến trúc tổng thể rõ ràng, logic, giúp cả team hình dung được bức tranh toàn cảnh của dự án."
    },
    {
        "week": "1.4-Week4",
        "goals": [
            "Tìm hiểu sâu về AWS CloudFront (CDN) và Amazon Route 53 (DNS).",
            "Chốt toàn bộ Tech Stack và lên danh sách các công việc (Backlog).",
            "Thiết kế Cơ sở dữ liệu (Database Schema)."
        ],
        "tasks": [
            "- Nghiên cứu cách hoạt động của Amazon CloudFront (Edge Locations, Caching, TTL).<br>- Thực hành kết hợp CloudFront với S3 Bucket để phân phối nội dung tĩnh với độ trễ thấp.",
            "- Tìm hiểu Amazon Route 53: Cách đăng ký domain, quản lý Hosted Zones, và các chiến lược định tuyến (Routing Policies).",
            "- Thống nhất Tech Stack cuối cùng: Next.js (Frontend), Spring Boot (Backend API), MongoDB Atlas (Database), FastAPI (AI/WebSockets).",
            "- Thiết kế Database Schema chi tiết cho các Collection: Users, Exams, Questions, Submissions.<br>- Xác định rõ các Relationship và Index cần thiết để tối ưu query.",
            "- Tạo không gian làm việc trên Trello/Jira.<br>- Đưa các tính năng vào Product Backlog.<br>- Lên kế hoạch chi tiết cho các Sprint đầu tiên (Thiết kế UI & Setup Project)."
        ],
        "eval": "- Đã sẵn sàng về mặt lý thuyết mạng AWS nâng cao (CDN, DNS).\n- Chuẩn bị đầy đủ cơ sở hạ tầng quản lý dự án (Schema, Jira) để team bắt tay vào code."
    },
    {
        "week": "1.5-Week5",
        "goals": [
            "Hoàn thiện thiết kế giao diện UI/UX trên Figma.",
            "Khởi tạo Repository và thiết lập các tiêu chuẩn lập trình (Coding Convention).",
            "Xây dựng khung (Boilerplate) cho cả Frontend và Backend."
        ],
        "tasks": [
            "- Cùng team Frontend hoàn thiện thiết kế UI/UX trên Figma cho các màn hình: Đăng nhập, Dashboard Giám thị, và Giao diện làm bài thi.",
            "- Tạo Github Repository cho dự án (phân chia folder cấu trúc Monorepo hoặc Multi-repo).<br>- Thiết lập Git Flow, branch protection rule.<br>- Cấu hình ESLint, Prettier, và Husky (pre-commit hooks) để đảm bảo chất lượng code.",
            "- Khởi tạo base project Frontend bằng Next.js (App Router).<br>- Cài đặt và cấu hình Tailwind CSS, Shadcn UI.<br>- Xây dựng Layout tổng thể và thanh điều hướng (Sidebar/Navbar).",
            "- Khởi tạo base project Backend bằng Spring Boot (Spring Web, Spring Data MongoDB).<br>- Thiết lập kết nối đến MongoDB Atlas qua URI bảo mật.<br>- Tạo cấu trúc thư mục Controller, Service, Repository chuẩn MVC.",
            "- Họp Sprint Planning: Phân chia các module code đầu tiên cho từng thành viên.<br>- Hướng dẫn team cách checkout branch, commit và tạo Pull Request (PR) đúng chuẩn."
        ],
        "eval": "- Setup dự án cực kỳ bài bản và chuyên nghiệp ngay từ đầu.\n- Xây dựng được nền móng vững chắc (boilerplate) giúp các thành viên bắt đầu code dễ dàng."
    },
    {
        "week": "1.6-Week6",
        "goals": [
            "Tích hợp xác thực và phân quyền (Authentication/Authorization).",
            "Làm việc với Amazon Cognito để quản lý định danh người dùng.",
            "Hoàn thành các chức năng Đăng nhập/Đăng ký."
        ],
        "tasks": [
            "- Tìm hiểu sâu về Amazon Cognito.<br>- Cấu hình Cognito User Pool, thiết lập các thuộc tính bắt buộc (Email, Custom Attributes) và App Client.",
            "- Tích hợp AWS Amplify / Cognito SDK vào ứng dụng Next.js để xử lý luồng Login, Signup, và Forgot Password.",
            "- Ở phía Spring Boot Backend: Triển khai Spring Security.<br>- Viết custom filter chặn request, giải mã và xác thực JWT token được cấp bởi Cognito (sử dụng JWK Set).",
            "- Xây dựng API lấy thông tin Profile người dùng hiện tại.<br>- Ghép nối Frontend gọi API Backend kèm theo Bearer Token ở Header.<br>- Cấu hình Axios Interceptors để tự động handle refresh token hoặc redirect khi hết hạn.",
            "- Review Pull Requests của team.<br>- Pair-programming với các thành viên đang gặp khó khăn khi gọi API hoặc xử lý state trong React."
        ],
        "eval": "- Triển khai thành công luồng bảo mật toàn diện từ Frontend đến Backend bằng AWS Cognito.\n- Quản lý team hiệu quả thông qua việc review code kỹ lưỡng."
    },
    {
        "week": "1.7-Week7",
        "goals": [
            "Phát triển các API cốt lõi cho module Quản lý Kỳ thi.",
            "Hoàn thiện giao diện Dashboard dành cho Giảng viên/Giám thị.",
            "Tiếp tục tối ưu mã nguồn và hỗ trợ kỹ thuật cho team."
        ],
        "tasks": [
            "- Lập trình các API CRUD trên Spring Boot cho các entity: Course, Exam, và Question.<br>- Áp dụng DTO (Data Transfer Object) để map dữ liệu giữa Controller và Service.",
            "- Xử lý logic import danh sách câu hỏi trắc nghiệm từ file Excel/CSV vào MongoDB.<br>- Sử dụng thư viện Apache POI trên Java.",
            "- Ở Frontend: Hoàn thiện UI màn hình Dashboard Giám thị.<br>- Sử dụng React Query / SWR để fetch danh sách các kỳ thi và hiển thị lên Data Table.",
            "- Tạo các form tạo mới Kỳ thi với đầy đủ Validation (React Hook Form + Zod).<br>- Xử lý các component phức tạp như Date Picker, Time Picker chọn thời gian thi.",
            "- Tối ưu hóa Database: Tạo Index trên MongoDB cho các trường thường xuyên truy vấn (như examId, userId).<br>- Họp tổng kết Sprint, đánh giá tiến độ so với kế hoạch ban đầu."
        ],
        "eval": "- Đã hoàn thiện xong phần core business logic của ứng dụng (Quản lý kỳ thi).\n- Năng suất code cao, kiến trúc codebase Frontend/Backend gọn gàng, dễ bảo trì."
    },
    {
        "week": "1.8-Week8",
        "goals": [
            "Tích hợp Amazon S3 để lưu trữ dữ liệu multimedia (Avatar, Video bằng chứng).",
            "Hoàn thiện giao diện Phòng thi dành cho sinh viên.",
            "Xử lý luồng nộp bài và tính điểm tự động."
        ],
        "tasks": [
            "- Tích hợp AWS SDK for Java vào Spring Boot.<br>- Viết API tạo S3 Presigned URL để Frontend có thể upload file trực tiếp lên S3 bucket một cách bảo mật mà không qua Backend trung gian.",
            "- Cấu hình Frontend Next.js xử lý việc chụp ảnh xác thực từ Webcam và upload lên S3 sử dụng Presigned URL nhận được.",
            "- Xây dựng giao diện Làm bài thi: Hiển thị câu hỏi tuần tự, có đồng hồ đếm ngược (Countdown Timer) đồng bộ với thời gian server.",
            "- Xử lý logic auto-submit: Tự động thu bài khi hết giờ.<br>- Viết API Backend nhận danh sách câu trả lời, so sánh với đáp án chuẩn và tính điểm tự động.",
            "- Phối hợp với thành viên phụ trách AI: Thảo luận về chuẩn giao tiếp (WebSockets/API) để nhận kết quả cảnh báo gian lận từ model YOLOv8 gửi về Frontend."
        ],
        "eval": "- Giải quyết triệt để bài toán lưu trữ file tĩnh bằng S3 Presigned URL, giảm tải cho Backend server.\n- Hoàn thành module Phòng thi phức tạp nhất của dự án."
    },
    {
        "week": "1.9-Week9",
        "goals": [
            "Đóng gói ứng dụng thành các container (Dockerization).",
            "Cấu hình triển khai thử nghiệm Backend lên Amazon ECS Fargate.",
            "Khắc phục các sự cố về mạng, CORS và bảo mật."
        ],
        "tasks": [
            "- Viết Dockerfile tối ưu (Multi-stage build) cho dự án Spring Boot (sử dụng JRE nhẹ) và dự án Next.js (Standalone mode).",
            "- Viết file docker-compose.yml để chạy đồng thời Frontend, Backend và kết nối MongoDB dưới local network để kiểm thử toàn diện.",
            "- Khởi tạo Amazon ECR (Elastic Container Registry).<br>- Build và push các Docker image lên ECR repository thông qua AWS CLI.",
            "- Cấu hình Amazon ECS (Elastic Container Service) theo mô hình Fargate (Serverless).<br>- Tạo Task Definition, định nghĩa CPU/Memory và thiết lập Environment Variables (DB URI, Secrets).",
            "- Tạo ECS Cluster và Service.<br>- Khắc phục các lỗi cấu hình Load Balancer (ALB), Target Groups và xử lý triệt để lỗi CORS khi Frontend ở một domain khác gọi vào ECS API."
        ],
        "eval": "- Nâng cấp kỹ năng DevOps: Chuyển đổi thành công dự án từ chạy local sang kiến trúc container hóa trên AWS ECS Fargate."
    },
    {
        "week": "1.10-Week10",
        "goals": [
            "Hoàn tất triển khai Frontend lên hạ tầng AWS (S3 + CloudFront).",
            "Thực hiện kiểm thử toàn hệ thống (End-to-End Testing).",
            "Lên khung ý tưởng và chuẩn bị tài liệu cho Workshop cá nhân."
        ],
        "tasks": [
            "- Build ứng dụng Next.js ra các file static HTML/JS.<br>- Triển khai bộ source này lên Amazon S3 Bucket và dùng CloudFront CDN để phân phối đến người dùng toàn cầu.",
            "- Cấu hình SSL/TLS Certificate (ACM) trên CloudFront và ALB để hỗ trợ giao thức HTTPS an toàn cho toàn bộ hệ thống.",
            "- Tổ chức phiên kiểm thử toàn hệ thống (UAT - User Acceptance Testing) với tất cả các thành viên trong nhóm.<br>- Giả lập vai trò Giám thị tạo đề và Sinh viên làm bài thi.",
            "- Rà soát log trên Amazon CloudWatch, xác định các nút thắt cổ chai (bottleneck) và sửa các bugs (phần lớn là lỗi UI trên thiết bị di động và lỗi hiển thị hình ảnh S3).",
            "- Bắt đầu phác thảo đề cương cho Workshop kỹ thuật cá nhân theo yêu cầu thực tập: Chọn chủ đề 'Triển khai CI/CD với AWS CodePipeline'."
        ],
        "eval": "- Hệ thống AuraAcademic đã chạy hoàn chỉnh và mượt mà trên môi trường Production Cloud.\n- Thể hiện sự chỉn chu trong khâu kiểm thử và fix bug."
    },
    {
        "week": "1.11-Week11",
        "goals": [
            "Tự động hóa toàn bộ quy trình triển khai (CI/CD Pipeline).",
            "Kiểm tra khả năng chịu tải của hệ thống (Load Testing).",
            "Tiếp tục hoàn thiện nội dung Workshop."
        ],
        "tasks": [
            "- Tìm hiểu bộ công cụ AWS Developer Tools.<br>- Thiết lập AWS CodeCommit (hoặc kết nối Github) để theo dõi thay đổi mã nguồn.",
            "- Viết file buildspec.yml để cấu hình AWS CodeBuild: Tự động build source code Spring Boot, đóng gói Docker image, và push image mới lên ECR.",
            "- Thiết lập AWS CodePipeline kết nối Source -> Build -> Deploy.<br>- Tự động cập nhật ECS Service (Blue/Green Deploy) mỗi khi có code mới hợp lệ được merge vào branch main.",
            "- Sử dụng Apache JMeter thiết lập kịch bản Load Test: Mô phỏng 200 sinh viên cùng đăng nhập và làm bài thi cùng lúc.<br>- Đánh giá Metrics CPU/RAM của ECS Fargate qua CloudWatch.",
            "- Chụp màn hình các bước thiết lập CI/CD, viết tài liệu giải thích chi tiết cho Workshop cá nhân."
        ],
        "eval": "- Hệ thống CI/CD hoạt động trơn tru giúp tự động hóa khâu release.\n- Đảm bảo hệ thống có khả năng chịu tải tốt trong điều kiện thi cử thực tế."
    },
    {
        "week": "1.12-Week12",
        "goals": [
            "Tổng kết toàn bộ quá trình thực tập, hoàn thiện báo cáo Worklog.",
            "Hoàn thiện 100% tài liệu Workshop và Project Demo.",
            "Chuẩn bị tài liệu thuyết trình (Slide) và bảo vệ dự án cuối khóa."
        ],
        "tasks": [
            "- Tổng hợp và cập nhật toàn bộ nhật ký công việc (Worklog 12 tuần) vào Repository báo cáo cá nhân (Hugo Template).",
            "- Rà soát lại bài Workshop 'Triển khai CI/CD Pipeline trên AWS'.<br>- Chỉnh sửa format Markdown, thêm alert và kiểm tra lại toàn bộ hình ảnh minh họa.",
            "- Quay video Demo quá trình hoạt động của dự án AuraAcademic (Từ lúc tạo kỳ thi đến lúc sinh viên làm bài và AI bắt gian lận).",
            "- Cùng nhóm thiết kế Slide thuyết trình cho Demo Day.<br>- Họp nhóm chạy thử chương trình (Dry-run), phân công người nói và chuẩn bị phần Q&A.",
            "- Đóng gói toàn bộ mã nguồn, tài liệu thiết kế, báo cáo cá nhân và gửi nộp cho ban tổ chức First Cloud Journey đúng deadline."
        ],
        "eval": "- Hoàn thành xuất sắc mọi mục tiêu và deliverables của chương trình thực tập.\n- Trưởng thành vượt bậc về kỹ năng Cloud (AWS), Fullstack Development và kỹ năng lãnh đạo nhóm (Teamwork/Leadership)."
    }
]

base_dir = r'd:\fcj-workshop-template\content\1-Worklog'
doc_link = "https://cloudjourney.awsstudygroup.com/"

for idx, data in enumerate(weekly_data):
    week_num = idx + 1
    dates = get_dates(start_date, week_num)
    
    week_dir = os.path.join(base_dir, data['week'])
    index_file = os.path.join(week_dir, '_index.vi.md')
    
    if not os.path.exists(week_dir):
        os.makedirs(week_dir)
        
    goals_md = "\n".join([f"- {g}" for g in data['goals']])
    
    table_md = "| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |\n"
    table_md += "| --- | --- | --- | --- | --- |\n"
    
    days_of_week = [2, 3, 4, 5, 6]
    for i in range(5):
        table_md += f"| {days_of_week[i]} | {data['tasks'][i]} | {dates[i]} | {dates[i]} | [Tài liệu AWS]({doc_link}) |\n"
    
    content = f"""---
title: "Week{week_num}"
date: 2026-04-24
weight: {week_num}
chapter: false
pre: " <b> 1.{week_num}. </b> "
---

### Mục tiêu tuần {week_num}:

{goals_md}

---

### Các công việc cần triển khai trong tuần này:

{table_md}

---

### Tự đánh giá vai trò Trưởng nhóm & Fullstack Developer:

{data['eval']}
"""
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Successfully generated ULTRA detailed worklogs with tables and dates.")
