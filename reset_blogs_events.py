import os
import shutil

# Reset 3-BlogsTranslated
blogs_dir = r'd:\fcj-workshop-template\content\3-BlogsTranslated'
for item in os.listdir(blogs_dir):
    item_path = os.path.join(blogs_dir, item)
    if os.path.isdir(item_path):
        shutil.rmtree(item_path)

with open(os.path.join(blogs_dir, '_index.vi.md'), 'w', encoding='utf-8') as f:
    f.write("""---
title: "Các bài blogs đã dịch"
date: 2024-01-01
weight: 3
chapter: false
pre: " <b> 3. </b> "
---

# Danh sách các bài blog AWS đã dịch

*(Bạn hãy xóa dòng này và liệt kê các bài blog mà bạn đã dịch trong khuôn khổ chương trình First Cloud Journey vào đây).*

1. [Tiêu đề bài blog 1] - [Link bài viết]
2. [Tiêu đề bài blog 2] - [Link bài viết]
""")

# Reset 4-EventParticipated
events_dir = r'd:\fcj-workshop-template\content\4-EventParticipated'
for item in os.listdir(events_dir):
    item_path = os.path.join(events_dir, item)
    if os.path.isdir(item_path):
        shutil.rmtree(item_path)

with open(os.path.join(events_dir, '_index.vi.md'), 'w', encoding='utf-8') as f:
    f.write("""---
title: "Các events đã tham gia"
date: 2024-01-01
weight: 4
chapter: false
pre: " <b> 4. </b> "
---

# Danh sách các sự kiện đã tham gia

*(Bạn hãy liệt kê các sự kiện AWS, hội thảo, hoặc các buổi meet-up mà bạn đã tham gia ở đây).*

1. **Sự kiện A** - Ngày DD/MM/YYYY
   - Nội dung học được: ...

2. **Sự kiện B** - Ngày DD/MM/YYYY
   - Nội dung học được: ...
""")

print("Cleaned up Blogs and Events.")
