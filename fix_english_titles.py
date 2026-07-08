import os
import re

content_dir = r'd:\fcj-workshop-template\content'

translations = {
    '1-Worklog': ('Nhật ký công việc', 'Worklog'),
    '2-Proposal': ('Bản đề xuất', 'Proposal'),
    '3-BlogsTranslated': ('Các bài blogs đã dịch', 'Translated Blogs'),
    '4-EventParticipated': ('Các events đã tham gia', 'Participated Events'),
    '5-Workshop': ('Workshop', 'Workshop'),
    '6-Self-evaluation': ('Tự đánh giá', 'Self Evaluation'),
    '7-Feedback': ('Chia sẻ, đóng góp ý kiến', 'Feedback')
}

for folder, (vi_title, en_title) in translations.items():
    file_path = os.path.join(content_dir, folder, '_index.md')
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace title in frontmatter
        content = re.sub(r'title\s*:\s*".*?"', f'title: "{en_title}"', content, count=1)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print('Updated English titles in the sidebar.')
