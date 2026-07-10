---
title : "Các trang chức năng của Admin"
date : 2024-01-01
weight : 4
chapter : false
pre : " <b> 5.4. </b> "
---

#### 5.Tổng quan về giao diện trang dashboard thống kê báo cáo và trang lớp học của hệ thống khi đăng nhập bằng tài khoản admin: 


<div align="center">

![Hình 5.1: Giao diện trang tổng quan quản trị của hệ thống](image.png)

**Hình 5.1. Giao diện trang tổng quan quản trị của hệ thống**

</div>


#### 5.1.1 Mô tả giao diện của ảnh 5.1
1. Khu vực thanh điều hướng trên cùng (Top Header)
 * Thông tin hiển thị:
   * Tiêu đề khu vực: "ADMIN / ADMIN PANEL".
   * Thời gian thực và Trạng thái hệ thống: "SYSTEM ONLINE" (kèm chấm xanh lá biểu thị hệ thống đang hoạt động bình thường).
 * Các nút tương tác:
   * Ô tìm kiếm toàn cục (Global Search): Nơi gõ từ khóa tìm kiếm nhanh người dùng, bài thi... trên toàn hệ thống.
   * Nút Theme (Icon mặt trời): Chuyển đổi giao diện Sáng/Tối.
   * Nút Thông báo (Icon chuông): Xem các cảnh báo, log hoặc thông báo mới của hệ thống.
   * Nút Tài khoản (Avatar góc phải): Truy cập nhanh cài đặt cá nhân của Admin.
2. Khu vực Menu chức năng bên trái (Admin Sidebar)
 * Thông tin hiển thị:
   * Logo dự án Aura Academic.
   * Các tiêu đề phân nhóm chức năng: TỔNG QUAN, QUẢN LÝ, BẢO MẬT, HỆ THỐNG.
   * Thông tin tài khoản Admin đang đăng nhập ở dưới cùng (Avatar và chữ "System Admin").
 * Các nút tương tác:
   * Tab điều hướng: Có rất nhiều tab nghiệp vụ sâu như Người dùng, Phân quyền RBAC, Quản lý Bài thi, Ngân hàng đề thi, Audit Logs, Cấu hình AI Hub... Lúc này tab Dashboard đang được chọn (Active).
   * Nút Thu gọn/Mở rộng Sidebar (nếu có, thường nằm ngay cạnh logo hoặc icon avatar dưới cùng).
3. Khu vực Tiêu đề trang & Thao tác nhanh (Page Header & Actions)
 * Thông tin hiển thị:
   * Tiêu đề chính: "Tổng quan quản trị hệ thống".
   * Tiêu đề phụ: "Kiểm soát và quản trị toàn bộ tài nguyên nền tảng AuraAcademic".
 * Các nút tương tác:
   * Nút "Làm mới" (Refresh icon): Click để gọi lại API, cập nhật số liệu thống kê mới nhất mà không cần tải lại toàn bộ trang web.
   * Nút "+ Thêm người dùng" (Nút xanh đậm): Thường sẽ mở ra một Modal (hộp thoại pop-up) hoặc chuyển sang trang form điền thông tin để tạo mới một tài khoản (Học sinh/Giáo viên/Admin).
4. Khu vực Thẻ thống kê tổng quan (Summary Stats Cards)
 * Thông tin hiển thị: Bao gồm 8 thẻ dữ liệu mang tính sống còn của hệ thống:
   * Tổng người dùng: 9
   * Giáo viên hệ thống: 2
   * Tổng số học sinh: 6
   * Bài thi đang chạy: 0
   * Tổng lượt nộp bài: 3
   * Email đã xác thực: 9
   * Tổng kho đề thi: 15
   * Chờ duyệt xác thực: 0
 * Các nút tương tác: Thông thường, thiết kế bảng điều khiển Admin cho phép click trực tiếp vào từng thẻ (Card) này để chuyển hướng nhanh đến trang danh sách tương ứng (VD: Bấm vào thẻ "Chờ duyệt xác thực" sẽ nhảy sang danh sách user cần duyệt).
5. Khu vực Biểu đồ phân tích (Charts & Graphs)
 * Thông tin hiển thị:
   * Phân bổ vai trò: Hiển thị trực quan dưới dạng thanh ngang (Progress bar) tỷ lệ % của 3 nhóm: Học sinh (67%), Giáo viên (22%), Quản trị viên (11%).
   * Hoạt động hệ thống 7 ngày qua: Khung chuẩn bị render biểu đồ (Line chart hoặc Bar chart) theo các thứ trong tuần.
 * Các nút tương tác:
   * Nút dropdown "Lượt đăng nhập hàng ngày": Nằm trong khung Hoạt động hệ thống. Bấm vào sẽ xổ ra các tùy chọn để đổi bộ lọc biểu đồ (VD: Đổi sang xem lượt thi, lượt nộp bài...).
6. Khu vực Bảng dữ liệu (Data Table - Quản lý người dùng)
 * Thông tin hiển thị:
   * Các tab phụ: "Quản lý tập trung người dùng" (Đang active) và "Phân tích cơ sở".
   * Đoạn text thống kê bộ lọc: "9 tài khoản được tìm thấy".
   * Bảng dữ liệu gồm các cột: Người dùng, Thông tin Email, Phân quyền vai trò, Xác thực Email, Thời gian đăng ký, Tác vụ quản lý.
   * Nhãn trạng thái màu xanh lá: "Đã xác thực".
 * Các nút tương tác:
   * Ô tìm kiếm nội bộ (Search input): "Tìm theo tên, email...".
   * Các nút lọc nhanh (Pill buttons): Tất cả, Học sinh, Giáo viên, Admin.
   * Dropdown "Phân quyền vai trò": (Đang hiển thị chữ "Học sinh" kèm mũi tên chỉ xuống). Admin có thể click vào đây để thay đổi trực tiếp quyền (Role) của user ngay tại bảng mà không cần vào trang chi tiết.
   * Tác vụ quản lý: (Tuy phần này đang bị khuất/chưa có icon trong ảnh, nhưng trong workshop bạn có thể đề cập đây là nơi đặt các nút như Edit (Sửa), Delete (Xóa), Khóa tài khoản (Ban/Block)).


--------------------------------------------------------------------------------------------------------------

<div align="center">

![Hình 5.2: Giao diện trang Thống kê & báo cáo của hệ thống](image-1.png)

**Hình 5.2. Giao diện trang Thống kê & báo cáo của hệ thống**

</div>

#### 5.1.2 Mô tả giao diện của ảnh 5.2
1. Khu vực thanh điều hướng trên cùng (Top Header)
 * Thông tin hiển thị:
   * Tiêu đề khu vực: "ADMIN / ADMIN PANEL".
   * Thời gian thực: "06:50 Thứ Sáu, 10 tháng 7".
   * Trạng thái hệ thống: Nhãn "SYSTEM ONLINE" (kèm chấm xanh lá).
 * Các nút tương tác:
   * Nút Menu (Icon 3 gạch): Thu gọn/mở rộng thanh Sidebar.
   * Ô tìm kiếm (Search input): "Tìm kiếm người dùng, bài thi..." có icon kính lúp.
   * Nút Theme (Icon mặt trời): Chuyển đổi giao diện Sáng/Tối.
   * Nút Thông báo (Icon chuông): Xem thông báo hệ thống.
   * Nút Cài đặt (Icon bánh răng): Truy cập nhanh vào cấu hình hệ thống (Đây là điểm mới so với giao diện của học sinh).
   * Nút Tài khoản (Avatar chữ Đ): Mở menu lối tắt tài khoản.
2. Khu vực Menu chức năng bên trái (Admin Sidebar)
 * Thông tin hiển thị:
   * Logo Aura Academic.
   * Các nhóm chức năng: TỔNG QUAN, QUẢN LÝ, BẢO MẬT (bị khuất một phần).
   * Thanh cuộn (Scrollbar): Cho thấy danh sách menu còn kéo dài xuống dưới.
   * Thông tin tài khoản góc dưới: "System Admin - SUPER ADMIN".
 * Các nút tương tác:
   * Danh sách tab điều hướng: Tab "Thống kê & Báo cáo" đang được chọn (Active - nền xanh đậm, có icon biểu đồ). Các tab khác bao gồm: Dashboard, Hỗ trợ trực tuyến, Người dùng, Xác thực giáo viên, Phân quyền RBAC, Quản lý Bài thi, Thiết kế & Kho đề..., Ngân hàng đề thi, Tài liệu hệ thống, Nội dung & Media.
   * Nút Đăng xuất (Icon mũi tên hướng ra cửa): Nằm cạnh thông tin System Admin ở góc dưới cùng.
3. Khu vực Tiêu đề trang & Thao tác nhanh (Page Header)
 * Thông tin hiển thị:
   * Tiêu đề chính: "Thống kê & Báo cáo".
   * Tiêu đề phụ: "Dữ liệu thống kê từ hệ thống — cập nhật theo thời gian thực".
 * Các nút tương tác:
   * Nút "Làm mới" (Refresh button): Có icon mũi tên xoay vòng, dùng để gọi lại API cập nhật số liệu mới nhất trên trang.
4. Khu vực Thẻ thống kê tổng quan (Summary Cards)
 * Thông tin hiển thị: Gồm 4 thẻ chứa các tiêu đề:
   * Tổng người dùng (Icon nhóm người).
   * Tổng bài thi (Icon bài kiểm tra).
   * Lượt nộp bài (Icon check hoàn thành).
   * Đã xác thực email (Icon huy hiệu check).
   * Lưu ý UI/UX để test: Hiện tại 4 thẻ này đang không hiển thị con số dữ liệu (có thể đang ở trạng thái loading hoặc thiếu data trả về từ API). Đây là một điểm đáng chú ý khi demo trong workshop.
 * Các nút tương tác: Tùy thuộc vào thiết kế, các thẻ này có thể click được để chuyển hướng đến trang danh sách chi tiết tương ứng.
5. Khu vực Biểu đồ & Phân tích chi tiết (Charts & Analytics)
 * Khung "Lượt đăng nhập 7 ngày":
   * Thông tin hiển thị: Chữ "Dữ liệu mẫu" (mờ ở góc phải). Dưới đó là các con số (38, 62, 55...) tương ứng với các thứ trong tuần (T2, T3, T4... CN). Đây là khu vực chờ render biểu đồ (Line/Bar chart).
 * Khung "Phân bổ người dùng":
   * Thông tin hiển thị:
     * Các thanh tiến trình (Progress bars) thể hiện tỷ lệ của: Học sinh (6), Giáo viên (2), Admin (1).
     * Các chỉ số phụ ở dưới: Đã xác thực email, Tài khoản bị khoá (0 - màu đỏ), Bài thi đang hoạt động (0 - màu xanh lá).
   * Các nút tương tác: Khu vực này mang tính chất trực quan hóa dữ liệu, thường không có nút bấm tương tác trực tiếp.
6. Khu vực Trạng thái (System Alerts)
 * Thông tin hiển thị:
   * Tiêu đề: "Cảnh báo hệ thống".
   * Khung thông báo (Màu xanh nhạt ngọc bích): Kèm icon dấu check và dòng chữ "Hệ thống đang hoạt động bình thường".
 * Các nút tương tác: Không có. Đây là thành phần UI để thông báo tình trạng sức khỏe (health check) của server/hệ thống.

--------------------------------------------------------------------------------------------------------------

<div align="center">

![Hình 5.3: Giao diện trang Trung tâm hỗ trợ Trực tuyến của hệ thống](image-2.png)

**Hình 5.3. Giao diện trang Trung tâm hỗ trợ Trực tuyến của hệ thống**

</div>

#### 5.1.3 Mô tả giao diện của ảnh 5.3
1. Khu vực thanh điều hướng trên cùng (Top Header)
 * Thông tin hiển thị:
   * Tiêu đề khu vực: "ADMIN / ADMIN PANEL".
   * Thời gian thực: "06:50 Thứ Sáu, 10 tháng 7".
   * Trạng thái: Nhãn "SYSTEM ONLINE" (kèm chấm xanh lá).
 * Các nút tương tác:
   * Nút Menu (Icon 3 gạch): Thu gọn/mở rộng thanh Sidebar.
   * Ô tìm kiếm toàn cục: "Tìm kiếm người dùng, bài thi...".
   * Cụm icon tiện ích: Nút Theme (Sáng/Tối), Thông báo (Chuông), Cài đặt (Bánh răng) và Avatar Tài khoản Admin.
2. Khu vực Menu chức năng bên trái (Admin Sidebar)
 * Thông tin hiển thị:
   * Logo Aura Academic.
   * Các phân nhóm: TỔNG QUAN, QUẢN LÝ, BẢO MẬT.
   * Thông tin tài khoản góc dưới: "System Admin - SUPER ADMIN".
 * Các nút tương tác:
   * Danh sách tab điều hướng: Tab "Hỗ trợ trực t..." đang được chọn (Active - nền xanh đậm). Bạn có thể thấy thanh cuộn báo hiệu còn nhiều menu bên dưới.
   * Nút Đăng xuất: Nằm cạnh thông tin Admin ở góc dưới cùng.
3. Khu vực Tiêu đề trang & Cấu hình AI (Page Header & AI Config)
 * Thông tin hiển thị:
   * Tiêu đề chính: "Trung tâm Hỗ trợ Trực tuyến" (kèm icon bong bóng chat).
   * Tiêu đề phụ: "PHẢN HỒI & GIẢI ĐÁP CÂU HỎI REALTIME".
   * Khung cấu hình AI: Dòng chữ "AI Tự động trả lời" và mô tả nhỏ "Mô hình Gemini 2.5 & Groq đang trực".
 * Các nút tương tác:
   * Công tắc Bật/Tắt (Toggle Switch): Nằm trong khung cấu hình AI, đang ở trạng thái Bật (màu xanh). Dùng để kích hoạt hoặc tắt bot AI hỗ trợ trả lời tự động cho học sinh.
4. Khu vực Danh sách hội thoại (Chat List - Cột trái)
 * Thông tin hiển thị:
   * Danh sách các thẻ tin nhắn của người dùng: Gồm Tên (VD: 1662_ Vũ Gia Kiệt, 2783_ Đậu Đại Tài...), Vai trò (HỌC SINH), Thời gian nhắn cuối (21:21, 21:07...), và trích đoạn tin nhắn gần nhất.
   * Trạng thái Online/Offline: Chấm xanh lá (Online) hoặc xám (Offline) cạnh avatar. Bạn "Huy Trương" có thêm icon thông báo tin nhắn chưa đọc màu đỏ.
 * Các nút tương tác:
   * Ô tìm kiếm hội thoại: "Tìm tên người dùng hoặc vai trò..." dùng để lọc nhanh người cần chat.
   * Nút Làm mới (Refresh icon): Cập nhật lại danh sách tin nhắn mới nhất.
   * Các thẻ hội thoại (Chat Cards): Click vào từng thẻ (ví dụ thẻ của Vũ Gia Kiệt đang được active viền xanh) để mở chi tiết cuộc trò chuyện sang khung bên phải.
5. Khu vực Khung trò chuyện (Chat Window - Cột phải)
 * Thông tin hiển thị:
   * Header (Phần đầu khung): Hiển thị Avatar, Tên người dùng đang chat ("1662_ Vũ Gia Kiệt"), Chấm xanh trạng thái và Mã định danh "ID PHÒNG: 6A5010CD...".
   * Main body (Phần nội dung): Dòng chữ hiển thị trạng thái trống "Chưa có lịch sử trò chuyện nào trong phòng này."
 * Các nút tương tác:
   * Nút "ĐANG KẾT NỐI LẠI": Ở góc trên cùng bên phải khung chat. Thường là nút tác vụ hoặc nhãn hiển thị trạng thái đường truyền socket của phòng chat đó.
   * Ô nhập liệu tin nhắn (Text Input): Nằm ở dưới đáy, có dòng chữ mờ "Nhập nội dung phản hồi cho 1662_ Vũ Gia Kiệt...".
   * Nút "GỬI": Bấm để gửi tin nhắn đi. Nằm ngay cạnh ô nhập liệu.


--------------------------------------------------------------------------------------------------------------

<div align="center">

![Hình 5.4: Giao diện trang Quản lý người dùng của hệ thống](image-3.png)

**Hình 5.4.  Giao diện trang Quản lý người dùng của hệ thống**

</div>

#### 5.1.4 Mô tả giao diện của ảnh 5.4
1. Khu vực thanh điều hướng trên cùng (Top Header)
 * Thông tin hiển thị:
   * Tiêu đề: "ADMIN / ADMIN PANEL".
   * Thời gian thực: "06:51 Thứ Sáu, 10 tháng 7".
   * Trạng thái hệ thống: Nhãn "SYSTEM ONLINE" (kèm chấm xanh lá).
 * Các nút tương tác:
   * Nút Menu (Icon 3 gạch): Thu/phóng thanh Sidebar.
   * Ô tìm kiếm toàn cục: "Tìm kiếm người dùng, bài thi...".
   * Cụm icon tiện ích: Nút Theme (Sáng/Tối), Thông báo (Chuông), Cài đặt (Bánh răng) và Avatar Admin.
2. Khu vực Menu chức năng bên trái (Admin Sidebar)
 * Thông tin hiển thị:
   * Logo Aura Academic.
   * Các nhóm chức năng: TỔNG QUAN, QUẢN LÝ, BẢO MẬT.
   * Thông tin tài khoản góc dưới: "System Admin - SUPER ADMIN".
 * Các nút tương tác:
   * Danh sách tab điều hướng: Tab "Người dùng" đang được chọn (Active - nền xanh đậm).
   * Nút Đăng xuất: Biểu tượng mũi tên hướng ra ngoài nằm cạnh thông tin Admin ở góc dưới cùng.
3. Khu vực Tiêu đề trang & Thao tác chính (Page Header & Main Actions)
 * Thông tin hiển thị:
   * Tiêu đề chính: "Quản lý người dùng".
   * Tiêu đề phụ: "Tra cứu, chỉnh sửa thông tin tài khoản và phân quyền".
 * Các nút tương tác:
   * Nút "Làm mới" (Refresh): Gọi API để tải lại dữ liệu bảng mới nhất.
   * Nút "+ Thêm người dùng" (Màu xanh đậm): Click để mở form/modal tạo tài khoản mới.
4. Khu vực Tìm kiếm và Lọc dữ liệu (Search & Filters)
 * Thông tin hiển thị:
   * Bộ đếm tổng số bản ghi: "9 tài khoản" (hiển thị ở góc phải).
 * Các nút tương tác:
   * Ô nhập liệu (Search Box): "Tìm theo tên, email..." để gõ từ khóa tìm kiếm user cụ thể.
   * Các nút lọc phân quyền (Tabs/Pills): Gồm "Tất cả" (đang active), "Học sinh", "Giáo viên", "Admin". Bấm vào từng nút để lọc nhanh danh sách bên dưới theo nhóm người dùng tương ứng.
5. Khu vực Bảng dữ liệu (Data Table)
 * Thông tin hiển thị:
   * Các tiêu đề cột: NGƯỜI DÙNG, THÔNG TIN EMAIL, PHÂN QUYỀN VAI TRÒ, XÁC THỰC EMAIL, THỜI GIAN ĐĂNG KÝ, TÁC VỤ QUẢN LÝ.
   * Dữ liệu từng dòng (Rows): Hiển thị Avatar (chữ cái đầu), Mã/Tên người dùng (VD: 1662_ Vũ Gia Kiệt), Email, Thời gian đăng ký (09/07/2026).
   * Nhãn trạng thái: "ĐÃ XÁC THỰC" (màu xanh lá) cho thấy email đã được verify.
 * Các nút tương tác:
   * Dropdown "Phân quyền vai trò": (Các nút có chữ "HỌC SINH" viền xanh lá hoặc "GIÁO VIÊN" viền xanh dương kèm mũi tên trỏ xuống). Admin có thể bấm trực tiếp vào đây để đổi quyền (Role) cho người dùng đó ngay lập tức mà không cần mở trang chỉnh sửa chi tiết.
   * Cột "Tác vụ quản lý" (Actions): Hiện tại UI trong cột này đang trống (có thể do chưa code xong hoặc icon bị ẩn). Thông thường, khu vực này sẽ chứa các nút tương tác rất quan trọng như: Sửa (Edit), Xóa (Delete), hoặc Khóa tài khoản (Ban/Block). Bạn nên lưu ý điểm này để nhắc nhở team bổ sung hoặc giải thích trong lúc demo.

--------------------------------------------------------------------------------------------------------------

<div align="center">

![Hình 5.5: Giao diện trang Xác thực giáo viên của hệ thống](image-4.png)

**Hình 5.5.  Giao diện trang Xác thực giáo viên của hệ thống**

</div>

#### 5.1.5 Mô tả giao diện của ảnh 5.5
1. Khu vực thanh điều hướng trên cùng (Top Header)
 * Thông tin hiển thị:
   * Tiêu đề khu vực: "ADMIN / ADMIN PANEL".
   * Thời gian thực: "06:51 Thứ Sáu, 10 tháng 7".
   * Trạng thái hệ thống: Nhãn "SYSTEM ONLINE" (kèm chấm xanh lá).
 * Các nút tương tác:
   * Nút Menu (Icon 3 gạch): Thu gọn/mở rộng thanh Sidebar.
   * Ô tìm kiếm toàn cục: Khung nhập liệu "Tìm kiếm người dùng, bài thi...".
   * Cụm icon góc phải: Nút Theme (Sáng/Tối), Thông báo (Chuông), Cài đặt (Bánh răng) và Avatar Admin.
2. Khu vực Menu chức năng bên trái (Admin Sidebar)
 * Thông tin hiển thị:
   * Logo dự án Aura Academic.
   * Các tiêu đề phân nhóm: TỔNG QUAN, QUẢN LÝ, BẢO MẬT.
   * Thanh cuộn (Scrollbar) hiển thị danh sách còn dài.
   * Thông tin tài khoản góc dưới: "System Admin - SUPER ADMIN" kèm avatar chữ "S".
 * Các nút tương tác:
   * Danh sách tab điều hướng: Tab "Xác thực giá..." (bị cắt chữ, đầy đủ là Xác thực giáo viên) đang ở trạng thái được chọn (Active - nền xanh đậm).
   * Nút Đăng xuất: Biểu tượng mũi tên hướng ra ngoài nằm góc dưới cùng bên phải của khu vực thông tin Admin.
3. Khu vực Tiêu đề trang & Bộ lọc trạng thái (Page Header & Filters)
 * Thông tin hiển thị:
   * Tiêu đề chính: "Xác thực Giáo viên".
   * Tiêu đề phụ: "Duyệt yêu cầu xác thực từ giáo viên tự do".
 * Các nút tương tác:
   * Các nút Tab lọc trạng thái (Pill/Tab buttons): Gồm các nút "Đang chờ" (hiện đang active với nền xanh đậm), "Đã duyệt", "Đã từ chối", "Chưa gửi". Khi click vào từng tab, hệ thống sẽ gọi API để hiển thị danh sách yêu cầu xác thực tương ứng với trạng thái đó.
4. Khu vực Bảng dữ liệu (Data Table)
 * Thông tin hiển thị:
   * Các tiêu đề cột của bảng: GIÁO VIÊN, LOẠI BẰNG CHỨNG, NGÀY GỬI, TRẠNG THÁI, HÀNH ĐỘNG.
   * Trạng thái trống (Empty State): Do tab "Đang chờ" hiện không có dữ liệu, bảng hiển thị một khoảng trắng lớn với Icon chiếc khiên có dấu tick ở giữa và dòng chữ "Không có yêu cầu nào".
 * Các nút tương tác:
   * Hiện tại bảng đang trống nên không có nút tương tác nào xuất hiện. Tuy nhiên, khi thuyết trình, bạn có thể giải thích thêm: Nếu có dữ liệu, cột "HÀNH ĐỘNG" thường sẽ chứa các nút như "Xem chi tiết", "Duyệt (Approve)" hoặc "Từ chối (Reject)" kèm lý do.


--------------------------------------------------------------------------------------------------------------

<div align="center">

![Hình 5.6: Giao diện trang Phân quyền của hệ thống](image-5.png)

**Hình 5.6. Giao diện trang  Phân quyền của hệ thống**

</div>

#### 5.1.6 Mô tả giao diện của ảnh 5.6
1. Khu vực thanh điều hướng trên cùng (Top Header)
 * Thông tin hiển thị:
   * Tiêu đề khu vực: "ADMIN / ADMIN PANEL".
   * Thời gian thực: "06:52 Thứ Sáu, 10 tháng 7".
   * Trạng thái hệ thống: Nhãn "SYSTEM ONLINE" (kèm chấm xanh lá).
 * Các nút tương tác:
   * Nút Menu (Icon 3 gạch): Thu gọn/mở rộng thanh Sidebar.
   * Ô tìm kiếm toàn cục: Khung nhập liệu "Tìm kiếm người dùng, bài thi...".
   * Cụm icon góc phải: Nút Theme (Sáng/Tối), Thông báo (Chuông), Cài đặt (Bánh răng) và Avatar Tài khoản Admin.
2. Khu vực Menu chức năng bên trái (Admin Sidebar)
 * Thông tin hiển thị:
   * Logo dự án Aura Academic.
   * Các tiêu đề phân nhóm: TỔNG QUAN, QUẢN LÝ, BẢO MẬT.
   * Thông tin tài khoản góc dưới: "System Admin - SUPER ADMIN" kèm avatar chữ "S".
 * Các nút tương tác:
   * Danh sách tab điều hướng: Tab "Phân quyền ..." (Phân quyền RBAC) đang ở trạng thái được chọn (Active - nền xanh đậm, có icon ổ khóa bảo mật).
   * Nút Đăng xuất: Biểu tượng mũi tên hướng ra ngoài nằm góc dưới cùng bên phải.
3. Khu vực Tiêu đề trang (Page Header)
 * Thông tin hiển thị:
   * Tiêu đề chính: "Phân quyền (RBAC)".
   * Tiêu đề phụ: "Tuỳ chỉnh vai trò và ma trận quyền hạn hệ thống. Các thay đổi được lưu cục bộ."
 * Các nút tương tác: Không có nút thao tác nhanh ở khu vực này.
4. Khu vực Ma trận phân quyền (Role & Permission Cards)
 * Thông tin hiển thị: Gồm 3 thẻ (Card) đại diện cho 3 nhóm quyền chính trong hệ thống, mỗi thẻ có một vạch màu đặc trưng ở trên cùng:
   * Thẻ Quản trị viên (Vạch tím): Hiển thị số lượng "1 người dùng". Danh sách các quyền được tích xanh (cấp phép): Quản lý người dùng, Quản lý bài thi, Xem kết quả thi, Cấu hình hệ thống, Xem Audit Logs. Riêng quyền Làm bài thi bị mờ (không được cấp).
   * Thẻ Giáo viên (Vạch xanh dương): Hiển thị số lượng "2 người dùng". Danh sách các quyền được tích xanh: Quản lý bài thi, Xem kết quả thi. Các quyền khác bị mờ.
   * Thẻ Học sinh (Vạch xanh lá): Hiển thị số lượng "6 người dùng". Danh sách các quyền được tích xanh: Làm bài thi. Các quyền khác bị mờ.
 * Các nút tương tác:
   * Các ô Checkbox (Tích chọn): Hiện tại trên giao diện tổng quan, các ô này mang tính chất hiển thị trạng thái (Read-only).
   * Nút "Chỉnh sửa quyền": Nằm ở dưới đáy của mỗi thẻ. Khi Admin click vào nút này, hệ thống thường sẽ mở ra một Modal (hộp thoại) hoặc chuyển trạng thái các ô Checkbox bên trên thành dạng có thể click (Enable/Disable) để Admin tích chọn lại các quyền mới cho nhóm vai trò đó, sau đó bấm "Lưu".
