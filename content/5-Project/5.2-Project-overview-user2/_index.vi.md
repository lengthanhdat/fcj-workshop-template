---
title : "Tổng quan dự án và các chức năng của user phần 2"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---

#### 5.Tổng quan về giao diện trang kết quả thi và trang lớp học của hệ thống: 


<div align="center">

![Hình 5.1: Giao diện trang Kết Quả thi của hệ thống](image.png)

**Hình 5.1. Giao diện trang Kết Quả thi của hệ thống**

</div>


#### 5.1.1 Mô tả giao diện của ảnh 5.1
1. Khu vực thanh điều hướng trên cùng (Header)
 * Thông tin hiển thị:
   * Thời gian thực (04:29 Thứ 6, 10/07).
 * Các nút tương tác:
   * Nút Menu (Icon 3 gạch ngang) để mở/thu gọn thanh bên trái.
   * Nút Theme (Icon mặt trời) để đổi giao diện Sáng/Tối.
   * Nút Thông báo (Icon chuông, đang có chấm thông báo màu đỏ).
   * Nút Tài khoản người dùng (Hiển thị Avatar chữ Đ và tên 2783_ Đậu Đại Tài).
2. Khu vực Menu chức năng bên trái (Sidebar)
 * Thông tin hiển thị:
   * Logo dự án Aura Academic.
 * Các nút tương tác:
   * Danh sách tab điều hướng. Lúc này tab Kết quả thi đang ở trạng thái được chọn (Active - nền màu xanh đậm). Các tab còn lại: Bảng điều khiển, Thi trực tuyến, Lớp học, Ngân hàng đề, Tài liệu học, Thông báo, Hồ sơ Cá nhân.
   * Nút Đăng xuất ở góc dưới cùng.
3. Khu vực Tiêu đề trang
 * Thông tin hiển thị:
   * Tiêu đề chính: "Kết quả học tập".
   * Tiêu đề phụ: "Theo dõi tiến độ, điểm số và kết quả các bài thi đã tham gia."
 * Các nút tương tác: Không có.
4. Khu vực Thống kê tổng quan (Stats Cards)
 * Thông tin hiển thị: Gồm 4 thẻ chứa dữ liệu tóm tắt:
   * TỔNG BÀI THI: 1
   * ĐIỂM TRUNG BÌNH: 6.70
   * TỶ LỆ ĐẠT: 100%
   * ĐIỂM CAO NHẤT: 6.7
 * Các nút tương tác: Các thẻ này chủ yếu là thông tin tĩnh, thông thường sẽ không có tính năng click.
5. Khu vực Tìm kiếm và Lọc dữ liệu (Search & Filters)
 * Thông tin hiển thị: Placeholder mờ trong ô tìm kiếm.
 * Các nút tương tác:
   * Ô nhập liệu (Search Box): "Tìm kiếm bài thi, mã đề..." có kèm icon kính lúp để gõ từ khóa tìm kiếm.
   * Các nút lọc trạng thái (Pill buttons): Nút Tất cả (đang active màu xanh đậm), Nút Đạt, Nút Không đạt. Click vào để lọc danh sách bài thi tương ứng.
   * Các menu thả xuống (Dropdown): Bộ lọc "Tất cả nguồn" và "Mới nhất" (có icon mũi tên trỏ xuống), click vào sẽ mở ra danh sách các tùy chọn lọc/sắp xếp khác.
6. Khu vực Danh sách kết quả (Data Table/List)
 * Thông tin hiển thị:
   * Tiêu đề bảng: "Danh sách kết quả" kèm bộ đếm "1 kết quả" ở góc phải.
   * Dữ liệu dòng: Tên bài thi ("Test"), Chi tiết ngày giờ ("Mã đề 101 - 04:22 10/07/2026"), Nhãn trạng thái ("KHÁ" - màu xanh lá), Điểm số ("6.7/10").
 * Các nút tương tác:
   * Nút mở rộng (Icon mũi tên v): Nằm ở cuối dòng dữ liệu bài thi. Khi click vào, khả năng cao sẽ xổ ra (expand) chi tiết kết quả của bài thi đó (ví dụ: xem lại câu nào đúng, câu nào sai).
7. Nút thả nổi (Floating Button)
 * Thông tin hiển thị: Không có.
 * Các nút tương tác: Nút hình tròn màu xanh có icon Tin nhắn ở góc dưới cùng bên phải màn hình (để mở chat/hỗ trợ).


--------------------------------------------------------------------------------------------------------------
<div align="center">

![Hình 5.2: Giao diện trang Lớp học của hệ thống](image-1.png)

**Hình 5.2. Giao diện trang Lớp học của hệ thống**

</div>


#### 5.1.2 Mô tả giao diện của ảnh 5.2
1. Khu vực thanh điều hướng trên cùng (Header)
 * Thông tin hiển thị:
   * Thời gian thực (04:30 Thứ 6, 10/07).
 * Các nút tương tác:
   * Nút Menu (Icon 3 gạch ngang) để thu/phóng Sidebar.
   * Nút Theme (Icon mặt trời) để chuyển đổi giao diện Sáng/Tối.
   * Nút Thông báo (Icon chuông, đang có số 2 màu đỏ).
   * Nút Tài khoản người dùng (Hiển thị Avatar chữ Đ và tên 2783_ Đậu Đại Tài).
2. Khu vực Menu chức năng bên trái (Sidebar)
 * Thông tin hiển thị:
   * Logo Aura Academic.
 * Các nút tương tác:
   * Danh sách tab điều hướng. Lúc này tab Lớp học đang ở trạng thái được chọn (Active - nền màu xanh đậm). Các tab còn lại: Bảng điều khiển, Thi trực tuyến, Kết quả thi, Ngân hàng đề, Tài liệu học, Thông báo, Hồ sơ Cá nhân.
   * Nút Đăng xuất ở góc dưới cùng.
3. Khu vực Tiêu đề trang & Hành động chính (Page Title & Call to Action)
 * Thông tin hiển thị:
   * Tiêu đề chính: "Lớp học của tôi".
   * Tiêu đề phụ: "Các lớp học bạn đã tham gia và đang theo học."
 * Các nút tương tác:
   * Nút "Tham gia lớp học" (Nút màu xanh góc phải): Click vào thường sẽ mở ra một Modal (hộp thoại) hoặc trang mới để học sinh nhập mã lớp học do giáo viên cung cấp nhằm mục đích ghi danh vào lớp mới.
4. Khu vực Danh sách Lớp học (Class Cards)
 * Thông tin hiển thị:
   * Thẻ thông tin lớp học (Card) bao gồm:
     * Icon cuốn sách (đại diện cho lớp).
     * Tên lớp: "Lớp 12".
     * Đoạn mô tả: "Không có mô tả chi tiết cho lớp học này."
     * Thông số: Sĩ số ("1 học sinh" kèm icon user), Tên giáo viên ("Giáo viên: Đạt lê").
     * Nhãn trạng thái: "Đã tham gia" (kèm chấm xanh lá).
 * Các nút tương tác:
   * Toàn bộ khối Thẻ Lớp 12 (Class Card): Thường được thiết kế là một nút bấm lớn (hoặc có link bọc bên ngoài). Khi click vào vùng của thẻ này, hệ thống sẽ điều hướng người dùng vào trang chi tiết bên trong của "Lớp 12" (để xem bài tập, danh sách học sinh, tài liệu riêng của lớp đó).
5. Nút thả nổi (Floating Button)
 * Thông tin hiển thị: Không có.
 * Các nút tương tác: Nút hình tròn màu xanh có icon Tin nhắn ở góc dưới cùng bên phải màn hình (để mở khung chat hỗ trợ).

--------------------------------------------------------------------------------------------------------------

<div align="center">

![Hình 5.3: Giao diện trang thành viên lớp học của hệ thống](image-2.png)

**Hình 5.3.  Giao diện trang thành viên lớp học của hệ thống**

</div>

--------------------------------------------------------------------------------------------------------------

<div align="center">

![Hình 5.4: Giao diện phần bài thi được giao cho lớp học của hệ thống](image-3.png)

**Hình 5.4.  Giao diện phần bài thi được giao cho lớp học của hệ thống**

</div>

--------------------------------------------------------------------------------------------------------------

<div align="center">

![Hình 5.5: Giao diện phần bảng điểm của lớp học của hệ thống](image-4.png)

**Hình 5.5.  Giao diện phần bảng điểm của lớp học của hệ thống**

</div>

--------------------------------------------------------------------------------------------------------------

<div align="center">

![Hình 5.6: Giao diện phần thảo luận của lớp học của hệ thống](image-5.png)

**Hình 5.6.  Giao diện phần thảo luận của lớp học của hệ thống**

</div>
