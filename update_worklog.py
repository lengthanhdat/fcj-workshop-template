import os

worklogs = {
    '1.1-Week1': 'Tìm hiểu về Cloud Computing, AWS Free Tier, thiết lập tài khoản và quản lý chi phí (AWS Budgets). Là trưởng nhóm, tiến hành phân chia nhóm và thảo luận ý tưởng ban đầu.',
    '1.2-Week2': 'Học các dịch vụ cơ bản: Amazon EC2, VPC, IAM. Thực hành triển khai máy chủ ảo và thiết lập mạng nội bộ an toàn.',
    '1.3-Week3': 'Nghiên cứu các dịch vụ lưu trữ và Database: Amazon S3, Amazon RDS, DynamoDB. Bắt đầu thiết kế kiến trúc cho dự án AuraAcademic.',
    '1.4-Week4': 'Tìm hiểu AWS CloudFront, Route53 và các kiến trúc chịu lỗi (High Availability). Chốt danh sách công nghệ cho dự án (Next.js, Spring Boot, MongoDB).',
    '1.5-Week5': 'Thiết kế hệ thống và UI/UX cho AuraAcademic. Khởi tạo repository, thiết lập chuẩn code (Coding Convention) và phân chia task cho các thành viên trong nhóm.',
    '1.6-Week6': 'Phát triển Frontend (Next.js) và Backend (Spring Boot). Tích hợp Amazon Cognito để xác thực người dùng. Hỗ trợ các thành viên khác giải quyết bug.',
    '1.7-Week7': 'Thiết kế và triển khai API cho các chức năng cốt lõi (Quản lý kỳ thi, Sinh câu hỏi). Làm việc với MongoDB. Review code của các thành viên (Pull Requests).',
    '1.8-Week8': 'Tích hợp AWS S3 để lưu trữ file và video từ người dùng. Xây dựng UI dashboard cho giám thị và sinh viên. Đảm bảo luồng dữ liệu (Data flow) thông suốt giữa Frontend và Backend.',
    '1.9-Week9': 'Đóng gói ứng dụng bằng Docker. Cấu hình triển khai Backend lên Amazon ECS Fargate. Xử lý các vấn đề về CORS và bảo mật API.',
    '1.10-Week10': 'Kiểm thử toàn bộ hệ thống (End-to-End Testing). Tối ưu hóa hiệu năng truy vấn và tốc độ tải trang. Khởi thảo tài liệu Workshop cá nhân.',
    '1.11-Week11': 'Hoàn thiện kiến trúc triển khai trên AWS. Rà soát bảo mật. Thực hiện load test nhẹ để đảm bảo hệ thống chịu tải tốt. Họp nhóm tổng kết dự án.',
    '1.12-Week12': 'Hoàn thành báo cáo thực tập tổng kết (Worklog, Project, Workshop). Đóng gói toàn bộ tài liệu và chuẩn bị cho buổi báo cáo cuối kỳ (Demo Day).'
}

base_dir = r'd:\fcj-workshop-template\content\1-Worklog'
for week, desc in worklogs.items():
    week_dir = os.path.join(base_dir, week)
    index_file = os.path.join(week_dir, '_index.vi.md')
    if os.path.exists(index_file):
        weight = week.split('-')[0].split('.')[1]
        pre_num = week.split('-')[0]
        title = week.split('-')[1]
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(f"---\ntitle: \"{title}\"\ndate: 2026-04-24\nweight: {weight}\nchapter: false\npre: \" <b> {pre_num}. </b> \"\n---\n\n### Mục tiêu tuần này:\n\n- {desc.split('. ')[0]}.\n- Hoàn thành các lab và nhiệm vụ được giao.\n\n---\n\n### Công việc đã thực hiện:\n\n{desc}\n\n---\n\n### Tự đánh giá vai trò Trưởng nhóm / Fullstack:\n\n- Đã bám sát tiến độ dự án.\n- Hỗ trợ tốt các thành viên trong nhóm.\n- Đảm bảo chất lượng code và kiến trúc tổng thể.\n")

print('Updated all worklogs.')
