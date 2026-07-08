import os
from datetime import datetime, timedelta

def get_dates(start_date, week_num):
    # week_num is 1-indexed
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
            "Làm quen với môi trường thực tập và các thành viên.",
            "Tìm hiểu tổng quan về Điện toán đám mây và AWS.",
            "Biết cách tạo tài khoản AWS và quản lý chi phí.",
            "Phân chia nhóm và thảo luận ý tưởng dự án."
        ],
        "tasks": [
            "- Làm quen với các thành viên FCJ<br>- Đọc và tìm hiểu nội quy",
            "- Tạo tài khoản AWS Free Tier<br>- Thiết lập AWS Budgets",
            "- Khám phá AWS Management Console<br>- Tìm hiểu giao diện các dịch vụ",
            "- Tìm hiểu cơ chế phân quyền AWS IAM<br>- Tạo IAM User",
            "- Họp nhóm đầu tiên<br>- Thảo luận ý tưởng hệ thống thi trắc nghiệm"
        ]
    },
    {
        "week": "1.2-Week2",
        "goals": [
            "Tìm hiểu và thực hành dịch vụ tính toán Amazon EC2.",
            "Hiểu kiến trúc mạng VPC (Virtual Private Cloud).",
            "Chốt ý tưởng và phân công vai trò trong nhóm."
        ],
        "tasks": [
            "- Tìm hiểu kiến trúc VPC, Subnet, Route Table",
            "- Thực hành tạo VPC (Public/Private Subnet)",
            "- Khởi tạo máy chủ Amazon EC2<br>- Cài đặt Web Server cơ bản",
            "- SSH vào EC2 và quản lý Security Group",
            "- Họp nhóm chốt dự án AuraAcademic<br>- Phân công vai trò Trưởng nhóm Fullstack"
        ]
    },
    {
        "week": "1.3-Week3",
        "goals": [
            "Tìm hiểu các dịch vụ lưu trữ: Amazon S3, EBS.",
            "Nghiên cứu cơ sở dữ liệu: Amazon RDS, DynamoDB.",
            "Bắt đầu thiết kế kiến trúc hệ thống cho dự án."
        ],
        "tasks": [
            "- Tìm hiểu và thực hành lưu trữ tĩnh với Amazon S3",
            "- Tìm hiểu CSDL quan hệ Amazon RDS",
            "- So sánh RDS và DynamoDB cho dự án<br>- Quyết định dùng MongoDB",
            "- Phác thảo sơ đồ kiến trúc hệ thống (Architecture Diagram)",
            "- Review tiến độ nhóm và giải đáp thắc mắc kỹ thuật"
        ]
    },
    {
        "week": "1.4-Week4",
        "goals": [
            "Nghiên cứu AWS CloudFront và Route53.",
            "Chốt danh sách công nghệ (Tech Stack) cho dự án.",
            "Thiết kế cơ sở dữ liệu (Database Schema)."
        ],
        "tasks": [
            "- Tìm hiểu CDN với CloudFront",
            "- Tìm hiểu quản lý tên miền với Amazon Route53",
            "- Chốt Tech Stack: Next.js, Spring Boot, MongoDB, ECS",
            "- Thiết kế Database Schema cho Quản lý Kỳ thi",
            "- Lập kế hoạch chi tiết (Jira/Trello) cho các Sprint tiếp theo"
        ]
    },
    {
        "week": "1.5-Week5",
        "goals": [
            "Khởi tạo Repository và thiết lập chuẩn code.",
            "Bắt đầu phát triển Frontend với Next.js.",
            "Xây dựng khung (boilerplate) cho Backend Spring Boot."
        ],
        "tasks": [
            "- Khởi tạo Git Repo<br>- Thiết lập ESLint, Prettier",
            "- Xây dựng bộ khung Frontend (Next.js, TailwindCSS)",
            "- Dựng base project Spring Boot<br>- Kết nối MongoDB",
            "- Tạo các UI components cơ bản (Button, Input, Layout)",
            "- Phân chia task code Frontend/Backend cho thành viên"
        ]
    },
    {
        "week": "1.6-Week6",
        "goals": [
            "Tích hợp xác thực người dùng với Amazon Cognito.",
            "Phát triển các tính năng đăng nhập/đăng ký.",
            "Hỗ trợ giải quyết các bug phát sinh của nhóm."
        ],
        "tasks": [
            "- Tìm hiểu và cấu hình Amazon Cognito User Pool",
            "- Tích hợp Cognito vào Frontend Next.js",
            "- Viết API xác thực JWT Token trên Spring Boot",
            "- Ghép nối giao diện Login/Register với Backend",
            "- Review code (Pull Requests) của các thành viên"
        ]
    },
    {
        "week": "1.7-Week7",
        "goals": [
            "Phát triển API cốt lõi cho Quản lý Kỳ thi.",
            "Thiết kế UI Dashboard cho sinh viên và giám thị.",
            "Tối ưu hóa các câu truy vấn MongoDB."
        ],
        "tasks": [
            "- Viết API CRUD cho Module Kỳ thi và Câu hỏi",
            "- Xây dựng giao diện Dashboard bằng Next.js",
            "- Xử lý luồng lấy dữ liệu (Fetch API) hiển thị lên biểu đồ",
            "- Tối ưu hóa Index trong MongoDB để tăng tốc query",
            "- Họp nhóm tổng kết Sprint, lên kế hoạch Sprint mới"
        ]
    },
    {
        "week": "1.8-Week8",
        "goals": [
            "Tích hợp lưu trữ hình ảnh/video bằng Amazon S3.",
            "Đảm bảo luồng dữ liệu (Data flow) thông suốt.",
            "Xử lý chức năng nộp bài thi."
        ],
        "tasks": [
            "- Cấu hình AWS SDK trong Spring Boot để upload file",
            "- Tích hợp tính năng upload avatar và bài làm lên S3",
            "- Xây dựng UI làm bài thi trắc nghiệm (Timer, Auto-submit)",
            "- Xử lý API nộp bài và tính điểm tự động",
            "- Hỗ trợ thành viên team AI đẩy kết quả xử lý về Backend"
        ]
    },
    {
        "week": "1.9-Week9",
        "goals": [
            "Đóng gói ứng dụng bằng Docker.",
            "Chuẩn bị triển khai Backend lên Amazon ECS.",
            "Xử lý triệt để các vấn đề CORS và bảo mật API."
        ],
        "tasks": [
            "- Viết Dockerfile cho Next.js và Spring Boot",
            "- Test chạy ứng dụng qua Docker Compose dưới local",
            "- Đẩy image lên Amazon ECR (Elastic Container Registry)",
            "- Fix các lỗi CORS khi gọi API từ nhiều origin",
            "- Rà soát lại bảo mật các endpoint quan trọng"
        ]
    },
    {
        "week": "1.10-Week10",
        "goals": [
            "Triển khai Frontend lên S3/CloudFront và Backend lên ECS Fargate.",
            "Kiểm thử toàn bộ hệ thống (E2E Testing).",
            "Bắt đầu lên ý tưởng cho Workshop cá nhân."
        ],
        "tasks": [
            "- Triển khai Spring Boot lên ECS Fargate",
            "- Build Next.js static, host lên S3 + CloudFront",
            "- Tiến hành End-to-End Testing luồng thi trực tuyến",
            "- Fix các bug phát sinh khi chạy trên môi trường Cloud",
            "- Lên kịch bản và chuẩn bị tài liệu cho Workshop CI/CD"
        ]
    },
    {
        "week": "1.11-Week11",
        "goals": [
            "Tự động hóa triển khai (CI/CD) với AWS CodePipeline.",
            "Thực hiện Load Test nhẹ trên ECS.",
            "Hoàn thiện các tài liệu kỹ thuật."
        ],
        "tasks": [
            "- Cấu hình AWS CodeBuild và CodePipeline",
            "- Thiết lập CI/CD tự động deploy ECS khi push code",
            "- Dùng JMeter thực hiện Load Test giả lập 100 User",
            "- Phân tích log CloudWatch và tinh chỉnh cấu hình Task",
            "- Viết tài liệu Workshop: Triển khai CI/CD Pipeline"
        ]
    },
    {
        "week": "1.12-Week12",
        "goals": [
            "Hoàn thiện báo cáo thực tập tổng kết.",
            "Kiểm tra chéo (Cross-check) nội dung trong nhóm.",
            "Chuẩn bị cho buổi báo cáo cuối kỳ (Demo Day)."
        ],
        "tasks": [
            "- Tổng hợp Worklog 12 tuần vào Repo cá nhân",
            "- Hoàn thiện toàn bộ bài viết Workshop",
            "- Cập nhật các bài dịch Blog và Sự kiện đã tham gia",
            "- Họp nhóm chạy thử Demo, chuẩn bị slide thuyết trình",
            "- Đóng gói báo cáo và gửi cho Mentor review"
        ]
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

### Kết quả đạt được:
- Hoàn thành các mục tiêu đề ra đúng thời hạn.
- Đảm bảo tiến độ chung của toàn dự án.

---

### Tự đánh giá:
- Chủ động tìm hiểu và áp dụng công nghệ mới.
- Khả năng quản lý team và xử lý technical issue tốt.
"""
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Successfully generated detailed worklogs with tables and dates.")
