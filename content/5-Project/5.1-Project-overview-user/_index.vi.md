---
title : "Tổng quan dự án và các chức năng của user phần 1"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 5.1. </b> "
---

#### 5.Tổng quan về giao diện của hệ thống: 

<div align="center">

![Hình 5.1: Giao diện Dashboard của hệ thống](image.png)

**Hình 5.1. Giao diện Dashboard của hệ thống**

</div>


#### 5.1.1 Mô tả giao diện ảnh 5.1

1. Khu vực thanh điều hướng trên cùng (Header)
 Thông tin hiển thị:
 Thời gian thực (04:27 Thứ 6, 10/07).
 Các nút tương tác (Buttons):
 Nút Menu (Icon 3 gạch ngang) để mở/thu gọn thanh bên trái.
 Nút Theme (Icon mặt trời) để đổi giao diện Sáng/Tối.
 Nút Thông báo (Icon cái chuông, đang có thông báo số ⁠3⁠ màu đỏ).
 Nút Tài khoản người dùng (Hiển thị Avatar chữ ⁠Đ⁠ và tên ⁠2783_ Đậu Đại Tài⁠).
2. Khu vực Menu chức năng bên trái (Sidebar)
 Thông tin hiển thị:
 Logo dự án (Aura Academic).
 Các nút tương tác (Buttons):
 Danh sách tab điều hướng: Bảng điều khiển (đang chọn), Thi trực tuyến, Kết quả thi, Lớp học, Ngân hàng đề, Tài liệu học, Thông báo, Hồ sơ Cá nhân.
 Nút Đăng xuất (ở góc dưới cùng).
3. Khu vực Lời chào & Vào thi nhanh
 Thông tin hiển thị:
 Câu chào mừng: "Xin chào, 2783_ Đậu Đại Tài!" kèm đoạn mô tả ngắn.
 Thẻ thông tin tài khoản: "toilatai2004@gmail.com - Tài khoản học sinh".
 Các nút tương tác (Buttons/Inputs):
 Ô nhập liệu (Input field): Nơi để gõ mã bài thi (Có chữ mờ "VD: AURA25").
 Nút "-> Vào": Bấm để xác nhận tham gia bài thi.
4. Khu vực 4 Thẻ thống kê (Stats Cards)
Khu vực này chủ yếu là Thông tin hiển thị, nhưng bản thân mỗi thẻ cũng có thể là một nút nhấn (nếu bạn có code cho nó click được).
 Thẻ 1: Điểm trung bình (Hiển thị số ⁠6.7⁠ & mô tả "Cao nhất 6.7/10").
 Thẻ 2: Bài thi đã nộp (Hiển thị số ⁠1⁠ & mô tả "100% đạt từ 5 điểm").
 Thẻ 3: Lớp đang học (Hiển thị số ⁠1⁠ & mô tả "Cập nhật theo lớp thật").
 Thẻ 4: Lượt luyện tập (Hiển thị số ⁠0⁠ & mô tả "Chưa luyện tập").
5. Khu vực Bảng dữ liệu (Data Sections)
 Khung "Kết quả bài thi gần đây":
 Thông tin hiển thị: Bảng kết quả gồm Bài thi (Test - Mã đề 101), Thời gian (10/7/2026), Trạng thái (Hoàn thành - tag màu xanh), Điểm (6.7/10).
 Các nút tương tác: Nút text "Xem tất cả ->".
 Khung "Tổng quan học tập":
 Thông tin hiển thị: Thanh tiến trình (Progress bar) đạt 100%, Thẻ "Đã đạt" (1), Thẻ "Tổng điểm" (6.7/10).
 Khung "Lớp học của tôi":
 Thông tin hiển thị: Thẻ hiển thị lớp học ("Lớp 12 - Chưa có môn học - Đạt lệ").
 Các nút tương tác: Nút text "Mở lớp học ->" và Nút mũi tên ⁠>⁠ nằm trong thẻ Lớp 12.
 Khung "Luyện tập gần đây":
 Thông tin hiển thị: Trạng thái trống (Dòng chữ "Chưa có kết quả luyện tập.").
 Các nút tương tác: Nút text "Xem".
6. Nút thả nổi (Floating Button)
 Các nút tương tác: Nút hình tròn màu xanh có icon Tin nhắn ở góc dưới cùng bên phải màn hình.



--------------------------------------------------------------------------------------------------------------




<div align="center">

![Hình 5.2: Giao diện Trang thi trực tuyến của hệ thống](image-1.png)

**Hình 5.2. Giao diện Trang thi trực tuyến của hệ thống**
</div>

#### 5.1.2 Mô tả giao diện của ảnh 5.2: 
1. Phân tích các chức năng hiện tại
 Khu vực điều hướng (Sidebar & Header): * Sidebar trái chứa đầy đủ các module cần thiết của một hệ sinh thái học tập (E-learning): Thi trực tuyến, Kết quả thi, Lớp học, Ngân hàng đề, Tài liệu học, Thông báo. Các icon đi kèm trực quan và dễ nhận biết.
 Header làm tốt vai trò cung cấp tiện ích nhanh: hiển thị thời gian thực, nút chuyển đổi giao diện Sáng/Tối (Dark/Light mode) rất bắt trend, chuông thông báo và góc quản lý tài khoản người dùng (Profile).
 Chức năng truy cập nhanh "Vào bài thi":
 Đây là một chức năng rất thực tế. Việc cho phép học sinh nhập mã phòng thi (ví dụ: AURA25) để tham gia ngay lập tức giúp tối ưu hóa luồng thao tác (user flow), thay vì phải lướt tìm trong danh sách các kỳ thi đang diễn ra.
 Các thẻ thống kê tổng quan (Statistics Cards):
 4 thẻ (Điểm trung bình, Bài thi đã nộp, Lớp đang học, Lượt luyện tập) mang lại cái nhìn bao quát về tiến độ học tập ngay khi vừa đăng nhập. Màu sắc của từng thẻ (Xanh dương, Xanh lá, Vàng, Hồng) giúp phân biệt tốt các luồng thông tin khác nhau.
 Bảng dữ liệu chi tiết (Data Tables & Cards):
 Kết quả bài thi gần đây: Hiển thị dưới dạng bảng rất rõ ràng với các trường thông tin quan trọng (Tên/Mã đề, Thời gian, Trạng thái, Điểm). Nút "Xem tất cả" được bố trí hợp lý.
 Tổng quan học tập & Luyện tập gần đây: Giúp theo dõi tỉ lệ đạt và kết quả ôn luyện.



--------------------------------------------------------------------------------------------------------------

<div align="center">

![Hình 5.3: Giao diện nhập mã phòng thi của hệ thống](image-2.png)

**Hình 5.3. Giao diện nhập mã phòng thi của hệ thống**
</div>

--------------------------------------------------------------------------------------------------------------

<div align="center">

![Hình 5.4: Giao diện sau khi nhấn làm bài thi của hệ thống](image-3.png)

**Hình 5.4. Giao diện sau khi nhấn làm bài thi của hệ thống**
</div>

--------------------------------------------------------------------------------------------------------------<div align="center">

![Hình 5.5: Giao diện làm bài thi của hệ thống](image-4.png)

**Hình 5.5. Giao diện làm bài thi của hệ thống**
</div>

--------------------------------------------------------------------------------------------------------------

<div align="center">

![Hình 5.6: Giao diện xác nhận nộp bài thi của hệ thống](image-5.png)

**Hình 5.6.  Giao diện xác nhận nộp bài thi của hệ thống**
</div>

--------------------------------------------------------------------------------------------------------------

<div align="center">

![Hình 5.7: Giao diện hoàn thành bài thi của hệ thống](image-6.png)

**Hình 5.7.  Giao diện hoàn thành bài thi của hệ thống**
</div>

--------------------------------------------------------------------------------------------------------------
