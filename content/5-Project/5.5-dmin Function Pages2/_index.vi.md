---
title : "Các trang chức năng của Admin phần 2"
date : 2024-01-01
weight : 5
chapter : false
pre : " <b> 5.5. </b> "
---

#### 5.Tổng quan về giao diện trang Quản trị kì thi và báo cáo , trang Biên soạn đề thi,... của hệ thống khi đăng nhập bằng tài khoản admin: 


<div align="center">

![Hình 5.1: Giao diện trang Quản trị kì thi và báo cáo của hệ thống](image.png)

**Hình 5.1. Giao diện trang Quản trị kì thi và báo cáo của hệ thống**

</div>


#### 5.1.1 Mô tả giao diện của ảnh 5.1
1. Khu vực thanh điều hướng trên cùng (Top Header)
 * Thông tin hiển thị:
   * Tiêu đề khu vực: "ADMIN / ADMIN PANEL".
   * Thời gian thực: "06:53 Thứ Sáu, 10 tháng 7".
   * Trạng thái hệ thống: Nhãn "SYSTEM ONLINE" (kèm chấm xanh lá).
 * Các nút tương tác:
   * Nút Menu (Icon 3 gạch): Thu/phóng thanh Sidebar.
   * Ô tìm kiếm toàn cục: Khung nhập liệu "Tìm kiếm người dùng, bài thi...".
   * Cụm icon tiện ích: Nút Theme (Sáng/Tối), Thông báo (Chuông), Cài đặt (Bánh răng) và Avatar Admin.
2. Khu vực Menu chức năng bên trái (Admin Sidebar)
 * Thông tin hiển thị:
   * Logo dự án Aura Academic.
   * Các nhóm chức năng: TỔNG QUAN, QUẢN LÝ, BẢO MẬT, HỆ THỐNG.
   * Thông tin tài khoản góc dưới: "System Admin - SUPER ADMIN".
 * Các nút tương tác:
   * Danh sách tab điều hướng: Tab "Quản lý Bài thi" đang được chọn (Active - nền xanh đậm, icon bài kiểm tra).
   * Nút Đăng xuất: Nằm cạnh thông tin Admin ở góc dưới cùng bên phải.
3. Khu vực Banner & Tiêu đề trang (Hero Banner)
 * Thông tin hiển thị:
   * Nền xanh gradient nổi bật để nhấn mạnh tầm quan trọng của trang.
   * Tiêu đề chính: "Quản trị Kỳ thi & Giám sát" (kèm icon chiếc khiên bảo mật).
   * Tiêu đề phụ: "Trang điều khiển dành cho Admin để giám sát, can thiệp đóng/mở phòng thi và quản lý tất cả phiên làm bài thi trên toàn hệ thống."
 * Các nút tương tác:
   * Nút "Làm mới dữ liệu" (Refresh button): Nằm bên phải banner, dùng để gọi lại API cập nhật trạng thái realtime của các phòng thi mà không cần load lại cả trang web.
4. Khu vực Thẻ thống kê tổng quan (Status Summary Cards)
 * Thông tin hiển thị: Gồm 5 thẻ thống kê số lượng phòng thi chia theo trạng thái (kèm mã màu trực quan):
   * TỔNG PHÒNG THI: 15
   * ĐANG DIỄN RA (LIVE): 3 (Màu xanh lá)
   * SẴN SÀNG (SCHEDULED): 7 (Màu xanh dương)
   * ĐANG SOẠN (DRAFT): 4 (Màu cam)
   * ĐÃ KẾT THÚC: 1 (Màu xám)
 * Các nút tương tác: Các thẻ này có thể được thiết kế như những nút bấm; khi click vào một thẻ, hệ thống sẽ tự động áp dụng bộ lọc trạng thái tương ứng cho danh sách bài thi ở dưới.
5. Khu vực Tìm kiếm & Bộ lọc (Search & Filters)
 * Thông tin hiển thị: Không có thông tin tĩnh.
 * Các nút tương tác:
   * Ô tìm kiếm (Search input): "Tìm theo mã phòng hoặc tên bài..." dùng để tra cứu nhanh.
   * Các nút lọc trạng thái (Pill buttons): Tất cả (đang active), Đang diễn ra, Sẵn sàng, Bản nháp, Đã kết thúc. Bấm vào để lọc các thẻ bài thi bên dưới.
6. Khu vực Danh sách Thẻ Bài thi (Exam Data Cards)
 * Thông tin hiển thị (Trên mỗi thẻ/Card):
   * Nhãn trạng thái (Badge): VD: "ĐANG DIỄN RA" (Xanh lá), "BẢN NHÁP" (Cam), "SẴN SÀNG" (Xanh dương). Một số bài thi có thêm nhãn "GIÁM SÁT AI".
   * Mã phòng thi: Nằm ở góc phải thẻ (VD: 450130, 12148E, E9212C).
   * Tên bài thi: Tiêu đề in đậm (VD: TEST, Lí).
   * Thông số cơ bản: Hình thức thi (Thi tự do hoặc theo Lớp), Số câu hỏi, Thời gian làm bài (VD: 1 câu hỏi / 60 phút).
   * Người tạo: Tên giáo viên/admin tạo đề (VD: Đạt lê, Huy Trương).
   * Trạng thái realtime (dành riêng cho phòng đang diễn ra): Dòng cảnh báo "Hết giờ làm bài" hoặc số lượng học sinh đang trong phòng (VD: "0 học sinh đang làm bài").
 * Các nút tương tác (Rất quan trọng cho luồng xử lý - Workflow):
   * Nút "Vào giám sát" (Nút xanh lá): Ở thẻ phòng đang diễn ra. Click vào sẽ chuyển Admin sang màn hình Dashboard giám sát trực tiếp (xem log học sinh, xem cảnh báo gian lận AI).
   * Nút "Đóng phòng" (Nút chữ đỏ): Nút hành động nguy hiểm. Cần gọi API kết thúc phiên thi ngay lập tức, thường sẽ hiện một Modal xác nhận trước khi thực thi để tránh ấn nhầm.
   * Nút "Bắt đầu thi" (Nút màu xanh dương): Ở thẻ bản nháp hoặc sẵn sàng. Dùng để mở/kích hoạt phòng thi, cho phép học sinh bắt đầu nhập mã vào.
   * Nút "Xóa" (Icon thùng rác): Ở thẻ bản nháp. Dùng để xóa vĩnh viễn đề thi chưa diễn ra. Tương tự nút Đóng phòng, thường sẽ yêu cầu popup xác nhận (Confirm Delete).


--------------------------------------------------------------------------------------------------------------

<div align="center">

![Hình 5.2: Giao diện trang Biên soạn đề thi của hệ thống](image-1.png)

**Hình 5.2. Giao diện trang Biên soạn đề thi của hệ thống**

</div>


#### 5.1.2 Mô tả giao diện của ảnh 5.2
Đặc biệt lưu ý: Trong ảnh này có một số lỗi hiển thị (bug UI) ở thanh cài đặt bên phải liên quan đến đa ngôn ngữ (i18n). Bạn nên ghi chú lại điểm này để báo team Dev fix trước khi đem đi demo trong workshop nhé!
1. Khu vực thanh điều hướng trên cùng (Top Header)
 * Thông tin hiển thị:
   * Tiêu đề: "ADMIN / ADMIN PANEL".
   * Thời gian thực: "06:54 Thứ Sáu, 10 tháng 7".
   * Trạng thái: "SYSTEM ONLINE".
 * Các nút tương tác:
   * Nút Menu (Icon 3 gạch): Thu/phóng thanh Sidebar.
   * Ô tìm kiếm toàn cục: Khung nhập liệu tìm kiếm.
   * Cụm icon tiện ích: Theme, Thông báo, Cài đặt, Avatar Admin.
2. Khu vực Menu chức năng bên trái (Admin Sidebar)
 * Thông tin hiển thị: Menu tiêu chuẩn của hệ thống.
 * Các nút tương tác:
   * Danh sách tab điều hướng: Tab "Thiết kế & Kho đ..." (Thiết kế & Kho đề thi) đang được chọn (Active - nền xanh đậm).
   * Nút Đăng xuất: Nằm góc dưới cùng bên phải.
3. Khu vực Tiêu đề trang & Thanh công cụ tạo đề (Page Header & Methods)
 * Thông tin hiển thị:
   * Breadcrumb (Đường dẫn): "KHO ĐỀ > BIÊN SOẠN".
   * Tiêu đề chính: "Biên soạn đề thi".
   * Nhãn (Badge) trạng thái: Nút pill màu nâu/vàng với dòng chữ "AI đang hoạt động", cho biết core AI tạo đề đã sẵn sàng.
   * Khung cảnh báo (Màu vàng): "Lưu ý quan trọng: Công cụ này sử dụng AI để phân tích tài liệu. Xin vui lòng kiểm tra lại chất lượng câu hỏi trước khi xuất bản."
 * Các nút tương tác:
   * 3 Tab chọn phương thức tạo đề: * "Tạo bằng AI" (Đang active - màu xanh).
     * "Nhập từ file" (Click để upload file Word/PDF/Excel có sẵn).
     * "Tạo thủ công" (Click để mở form tự gõ từng câu hỏi).
4. Khu vực Làm việc chính: Tạo đề bằng AI (AI Prompting Area)
 * Thông tin hiển thị:
   * Khung hướng dẫn "Hướng dẫn chi tiết tạo đề bằng AI": Cung cấp công thức viết yêu cầu (Prompt) chuẩn và các ví dụ minh họa trực quan cho giáo viên.
 * Các nút tương tác:
   * 2 Tab nguồn dữ liệu AI: "Tạo từ chủ đề" (Đang active - AI tự suy luận) và "Tạo từ tài liệu" (Có thể là tính năng RAG, cho phép AI đọc file tài liệu riêng để ra đề).
   * Các thẻ gợi ý nhanh (Suggestion Chips): "Toán 12 - Tích phân", "Vật lý 11 - Điện từ học"... Click vào để điền nhanh nội dung vào ô mô tả bên dưới.
   * Ô nhập liệu (Text Area): "MÔ TẢ YÊU CẦU ĐỀ THI". Nơi giáo viên gõ prompt để ra lệnh cho AI (VD: Đề thi môn Toán lớp 12 chương...).
   * Các Dropdown cấu hình câu hỏi: * ĐỘ KHÓ: Chọn Mức độ (VD: Trung bình, Khó, Dễ).
     * NGÔN NGỮ: Chọn ngôn ngữ xuất đề (VD: Tiếng Việt).
     * SỐ CÂU: Ô nhập số lượng câu hỏi muốn AI tạo ra (Đang điền số 10).
   * Nút Action chính (Màu tím/xanh lớn): "Aura AI - Biên soạn đề thi ngay". Bấm vào để gửi request lên server AI bắt đầu quá trình sinh (generate) đề thi.
5. Khu vực Thanh cài đặt bài thi bên phải (Settings Sidebar - CHÚ Ý LỖI UI)
 * Thông tin hiển thị:
   * Khu vực này đang bị lỗi chưa load được file ngôn ngữ (Missing i18n keys). Thay vì hiện text tiếng Việt, nó đang hiện các biến code như: TeacherExams.sidebar.title, TeacherExams.sidebar.label..., TeacherExams.sidebar.SUMMARY.
 * Các nút tương tác (Luồng thiết lập bài thi):
   * Các ô Input Text (Bị lỗi key): Có vẻ là ô nhập Tên bài thi, Mô tả bài thi.
   * Bộ chọn ngày giờ (Date Picker): "BẮT ĐẦU TỰ ĐỘNG (TÙY CHỌN)" - Click để cài đặt thời gian hẹn giờ mở phòng thi tự động.
   * Dropdown ĐỘ KHÓ TỔNG THỂ: Đang chọn "Trung bình".
   * Công tắc (Toggle) Trộn đề: Nút bật/tắt tính năng đảo thứ tự câu hỏi/đáp án (Hiện key TeacherExams.sidebar.shuffle...).
   * Công tắc (Toggle) AI Proctoring: Bật/tắt tính năng giám sát thi bằng AI.
   * Nút Action (Bị lỗi key): Nút màu xanh TeacherExams.sidebar.btn_publish (Đoán là nút "Lưu và Xuất bản").
   * Nút "Lưu bản nháp": Lưu lại trạng thái thiết lập hiện tại nhưng chưa phát hành.


--------------------------------------------------------------------------------------------------------------

<div align="center">

![Hình 5.3: Giao diện trang Ngân hàng đề thi của hệ thống](image-2.png)

**Hình 5.3. Giao diện trang Ngân hàng đề thi của hệ thống**

</div>


#### 5.1.3 Mô tả giao diện của ảnh 5.3

1. Khu vực thanh điều hướng trên cùng (Top Header)
 * Thông tin hiển thị:
   * Tiêu đề: "ADMIN / ADMIN PANEL".
   * Thời gian thực: "06:54 Thứ Sáu, 10 tháng 7".
   * Trạng thái hệ thống: Nhãn "SYSTEM ONLINE" (kèm chấm xanh lá).
 * Các nút tương tác:
   * Nút Menu (Icon 3 gạch): Thu gọn/mở rộng thanh Sidebar.
   * Ô tìm kiếm toàn cục: Khung "Tìm kiếm người dùng, bài thi...".
   * Cụm icon góc phải: Nút Theme (Sáng/Tối), Thông báo, Cài đặt và Avatar Admin.
2. Khu vực Menu chức năng bên trái (Admin Sidebar)
 * Thông tin hiển thị:
   * Logo Aura Academic.
   * Các nhóm chức năng hệ thống.
   * Thông tin tài khoản góc dưới: "System Admin - SUPER ADMIN".
 * Các nút tương tác:
   * Danh sách tab điều hướng: Tab "Ngân hàng đ..." (Ngân hàng đề thi) đang được chọn (Active - nền xanh đậm, icon hình tòa nhà ngân hàng/thư viện).
   * Nút Đăng xuất: Nằm góc dưới cùng bên phải.
3. Khu vực Banner chính & Thống kê (Hero Banner & Stats)
 * Thông tin hiển thị:
   * Nền xanh gradient đặc trưng.
   * Tiêu đề chính: "Ngân hàng Đề thi" (kèm icon tòa nhà).
   * Đoạn mô tả: "Quản lý toàn bộ đề luyện tập trong hệ thống, nhập đề mới, đồng bộ từ Kho đề và kiểm soát nội dung công khai cho học sinh ôn tập."
   * 3 Thẻ thống kê mini: Hiển thị dữ liệu tổng quan "0 Tổng đề", "0 Môn học", "0 Người đăng". (Do ngân hàng đang trống nên các chỉ số đều là 0).
 * Các nút tương tác (Hành động chính):
   * Nút "Upload PDF/DOCX" (Nút nền trắng): Mở form hoặc hộp thoại (Modal) để Admin/Giáo viên tải file tài liệu từ máy tính cá nhân lên hệ thống.
   * Nút "Thêm từ Kho đề" (Nút nền xanh viền nhạt): Cho phép chọn và đồng bộ các đề thi đã được tạo sẵn từ "Kho đề biên soạn" sang "Ngân hàng đề công khai" cho học sinh luyện tập.
4. Khu vực Thẻ tính năng nổi bật (Feature Highlight Cards)
 * Thông tin hiển thị: Gồm 3 thẻ mô tả nhanh các tính năng chính của trang:
   * "Upload nhanh": Nhập PDF/DOCX và lưu thẳng vào ngân hàng đề.
   * "Đồng bộ Kho đề": Chọn đề mẫu sẵn có để công khai cho luyện tập.
   * "Lọc chính xác": Tìm theo tên đề, người đăng và từng môn học.
 * Các nút tương tác: Các thẻ này có thể chỉ mang tính chất hướng dẫn hiển thị (Info cards), hoặc cũng có thể là các nút bấm thay thế (Shortcuts) dẫn thẳng đến tính năng tương ứng.
5. Khu vực Tìm kiếm & Bộ lọc (Search & Filters)
 * Thông tin hiển thị: Không có thông tin tĩnh.
 * Các nút tương tác:
   * Ô nhập liệu (Search Box): "Tìm theo tên đề thi..." để gõ từ khóa.
   * Dropdown "Tất cả người đăng": Lọc đề thi theo giáo viên/admin đã tải đề lên.
   * Dropdown "Tất cả môn học": Lọc đề thi theo môn học cụ thể (Toán, Lý, Hóa...).
   * Nút/Nhãn "0 đề thi" (Màu xanh đậm): Đóng vai trò là nút Submit để áp dụng bộ lọc, hoặc chỉ là bộ đếm hiển thị tổng số kết quả sau khi lọc.
6. Khu vực Danh sách dữ liệu (Data List / Empty State)
 * Thông tin hiển thị: * Do chưa có dữ liệu, khu vực này đang hiển thị Trạng thái trống (Empty State) rất trực quan.
   * Icon tài liệu trống.
   * Tiêu đề: "Ngân hàng chưa có đề thi nào".
   * Ghi chú hướng dẫn: "Admin và Giáo viên có thể Upload hoặc Tạo đề thi ngay tại đây."
 * Các nút tương tác: Hiện tại không có nút bấm, nhưng nếu có dữ liệu, đây sẽ là nơi hiển thị danh sách các thẻ bài thi (Card) hoặc dạng bảng (Table), kèm theo các nút thao tác như Xem chi tiết, Chỉnh sửa, hoặc Xóa.


--------------------------------------------------------------------------------------------------------------

<div align="center">

![Hình 5.4: Giao diện trang Quản lý tài liệu của hệ thống](image-3.png)

**Hình 5.4. Giao diện trang Quản lý tài liệu của hệ thống**

</div>


#### 5.1.4 Mô tả giao diện của ảnh 5.4
1. Khu vực thanh điều hướng trên cùng (Top Header)
 * Thông tin hiển thị:
   * Tiêu đề khu vực: "ADMIN / ADMIN PANEL".
   * Thời gian thực: "06:55 Thứ Sáu, 10 tháng 7".
   * Trạng thái hệ thống: Nhãn "SYSTEM ONLINE" (kèm chấm xanh lá).
 * Các nút tương tác:
   * Nút Menu (Icon 3 gạch): Thu gọn/mở rộng thanh Sidebar.
   * Ô tìm kiếm toàn cục: Khung nhập liệu "Tìm kiếm người dùng, bài thi...".
   * Cụm icon góc phải: Nút Theme (đổi giao diện Sáng/Tối), Thông báo (Chuông), Cài đặt (Bánh răng) và Avatar Admin (chữ Đ).
2. Khu vực Menu chức năng bên trái (Admin Sidebar)
 * Thông tin hiển thị:
   * Logo dự án Aura Academic.
   * Các tiêu đề phân nhóm hệ thống: TỔNG QUAN, QUẢN LÝ, BẢO MẬT.
   * Thông tin tài khoản góc dưới: "System Admin - SUPER ADMIN" (kèm avatar chữ S).
 * Các nút tương tác:
   * Danh sách tab điều hướng: Tab "Tài liệu hệ th..." (Tài liệu hệ thống) đang được chọn (Active - nền xanh đậm, icon cuốn sổ/tài liệu).
   * Nút Đăng xuất: Biểu tượng mũi tên hướng ra ngoài nằm góc dưới cùng bên phải.
3. Khu vực Tiêu đề trang (Page Header)
 * Thông tin hiển thị:
   * Tiêu đề chính: "Quản lý tài liệu".
   * Tiêu đề phụ: "Duyệt tài liệu giảng viên và quản lý tài liệu hệ thống."
 * Các nút tương tác: Không có nút bấm ở khu vực này.
4. Khu vực Thẻ thống kê trạng thái (Status Summary Cards)
 * Thông tin hiển thị: Gồm 4 thẻ (Card) tóm tắt số lượng tài liệu theo các trạng thái khác nhau (hiện tại tất cả đều bằng 0):
   * CHỜ DUYỆT: 0 (kèm icon đồng hồ màu vàng).
   * ĐÃ CÔNG KHAI: 0 (kèm icon quả địa cầu màu xanh lá).
   * TỪ CHỐI: 0 (kèm icon dấu X màu đỏ).
   * TỔNG TÀI LIỆU: 0 (kèm icon thư mục màu xanh dương).
 * Các nút tương tác: Trong trải nghiệm UX thực tế, các thẻ này có thể click được để đóng vai trò như một bộ lọc nhanh, giúp Admin xem ngay danh sách tài liệu ứng với trạng thái đó.
5. Khu vực Thanh Tabs Bộ lọc (Filter Tabs)
 * Thông tin hiển thị: Không có thông tin tĩnh.
 * Các nút tương tác:
   * Tab "Chờ duyệt": (Đang active - có gạch chân màu xanh đậm). Bấm vào đây để xem danh sách tài liệu do giáo viên tải lên đang chờ Admin phê duyệt.
   * Tab "Tất cả": (Kèm icon thư mục). Bấm vào để xem toàn bộ danh sách tài liệu trên hệ thống.
   * Tab "Upload hệ thống": (Kèm icon tải lên). Bấm vào đây có thể sẽ mở ra một form/giao diện để chính Admin tải tài liệu trực tiếp lên hệ thống dùng chung.
6. Khu vực Danh sách dữ liệu (Data List / Empty State)
 * Thông tin hiển thị:
   * Do tab "Chờ duyệt" hiện không có dữ liệu (số lượng là 0), khu vực này đang hiển thị Trạng thái trống (Empty State).
   * Bao gồm một icon checkmark đôi màu xám nhạt và dòng chữ: "Không có tài liệu nào cần duyệt."
 * Các nút tương tác: Hiện tại không có nút bấm. Nếu có tài liệu chờ duyệt, khu vực này sẽ hiển thị dạng bảng (Table) hoặc danh sách thẻ (List) kèm theo các nút thao tác cực kỳ quan trọng như Duyệt (Approve), Từ chối (Reject), hoặc Xem trước (Preview) tài liệu.


--------------------------------------------------------------------------------------------------------------

<div align="center">

![Hình 5.5: Giao diện trang Nội dung & Media của hệ thống](image-4.png)

**Hình 5.5. Giao diện trang Nội dung & Media của hệ thống**

</div>


#### 5.1.5 Mô tả giao diện của ảnh 5.5
1. Khu vực thanh điều hướng trên cùng (Top Header)
 * Thông tin hiển thị:
   * Tiêu đề khu vực: "ADMIN / ADMIN PANEL".
   * Thời gian thực: "06:55 Thứ Sáu, 10 tháng 7".
   * Trạng thái hệ thống: Nhãn "SYSTEM ONLINE" (kèm chấm xanh lá).
 * Các nút tương tác:
   * Nút Menu (Icon 3 gạch): Thu gọn/mở rộng thanh Sidebar.
   * Ô tìm kiếm toàn cục: Khung nhập liệu "Tìm kiếm người dùng, bài thi...".
   * Cụm icon góc phải: Nút Theme (Sáng/Tối), Thông báo (Chuông), Cài đặt (Bánh răng) và Avatar Admin (chữ Đ).
2. Khu vực Menu chức năng bên trái (Admin Sidebar)
 * Thông tin hiển thị:
   * Logo dự án Aura Academic.
   * Các tiêu đề phân nhóm: TỔNG QUAN, QUẢN LÝ, BẢO MẬT.
   * Thông tin tài khoản góc dưới: "System Admin - SUPER ADMIN" (kèm avatar chữ S).
 * Các nút tương tác:
   * Danh sách tab điều hướng: Tab "Nội dung & ..." (Nội dung & Media) đang được chọn (Active - nền xanh đậm, icon hình tệp tin/bức ảnh).
   * Nút Đăng xuất: Biểu tượng mũi tên hướng ra ngoài nằm góc dưới cùng bên phải.
3. Khu vực Tiêu đề trang & Thao tác chính (Page Header & Actions)
 * Thông tin hiển thị:
   * Tiêu đề chính: "Nội dung & Media".
   * Tiêu đề phụ: "Quản lý nội dung trang chủ và thư viện tệp tin hệ thống".
 * Các nút tương tác:
   * Nút "Tải tệp lên" (Màu xanh đậm, góc phải): Kèm icon upload. Khi click vào sẽ mở ra cửa sổ hệ thống để Admin chọn file (ảnh, video, tài liệu) từ máy tính tải lên server.
4. Khu vực Thanh Tabs Bộ lọc (Content Category Tabs)
 * Thông tin hiển thị: Không có thông tin tĩnh.
 * Các nút tương tác: Gồm 3 tab để chuyển đổi không gian quản lý nội dung:
   * Tab "Thư viện Media": (Đang active - chữ màu xanh ngọc có gạch chân). Nơi quản lý tổng hợp các tệp tin hình ảnh, video, banner của hệ thống.
   * Tab "Trang tĩnh": Bấm vào để sang giao diện quản lý các bài viết tĩnh (ví dụ: Giới thiệu, Điều khoản, Chính sách bảo mật...).
   * Tab "Thông báo chung": Bấm vào để quản lý nội dung các thông báo popup hoặc banner thông báo hiển thị cho toàn bộ user.
5. Khu vực Không gian dữ liệu (Data Area / Empty State)
 * Thông tin hiển thị:
   * Do tab "Thư viện Media" hiện chưa có file nào được tải lên, khu vực này đang hiển thị Trạng thái trống (Empty State).
   * Bao gồm một icon hình thư mục nhỏ và tiêu đề: "Thư viện Media trống".
   * Dòng chữ hướng dẫn: "Hãy tải lên tệp tin ảnh, video, tài liệu đầu tiên của bạn."
 * Các nút tương tác: Hiện tại ở phần khung giữa không có nút bấm. Tuy nhiên, trong thực tế trải nghiệm (UX), người dùng có thể kéo thả (Drag & Drop) trực tiếp file từ máy tính vào vùng trắng này để kích hoạt lệnh tải lên. Nếu có dữ liệu, khu vực này sẽ hiển thị danh sách các file dưới dạng lưới hình ảnh (Grid view) hoặc dạng bảng (List view) kèm các nút như Xem trước, Copy Link, Xóa.


--------------------------------------------------------------------------------------------------------------

<div align="center">

![Hình 5.6: Giao diện trang Audit Logs của hệ thống](image-5.png)

**Hình 5.6. Giao diện trang Audit Logs của hệ thống**

</div>


#### 5.1.6 Mô tả giao diện của ảnh 5.6
1. Khu vực thanh điều hướng trên cùng (Top Header)
 * Thông tin hiển thị:
   * Tiêu đề khu vực: "ADMIN / ADMIN PANEL".
   * Thời gian thực: "06:56 Thứ Sáu, 10 tháng 7".
   * Trạng thái hệ thống: Nhãn "SYSTEM ONLINE" (kèm chấm xanh lá).
 * Các nút tương tác:
   * Nút Menu (Icon 3 gạch): Thu gọn/mở rộng thanh Sidebar.
   * Ô tìm kiếm toàn cục: Khung nhập liệu "Tìm kiếm người dùng, bài thi...".
   * Cụm icon góc phải: Nút Theme (Sáng/Tối), Thông báo (Chuông), Cài đặt (Bánh răng) và Avatar Admin.
2. Khu vực Menu chức năng bên trái (Admin Sidebar)
 * Thông tin hiển thị:
   * Logo dự án Aura Academic.
   * Các tiêu đề phân nhóm: Ở màn hình này ta thấy rõ phần nhóm BẢO MẬT và HỆ THỐNG.
   * Thông tin tài khoản góc dưới: "System Admin - SUPER ADMIN".
 * Các nút tương tác:
   * Danh sách tab điều hướng: Tab "Audit Logs" đang được chọn (Active - nền xanh đậm, icon kính lúp/bảo mật). Dưới đó là tab "Phiên đăng nhập".
   * Nút Đăng xuất: Biểu tượng mũi tên hướng ra ngoài nằm góc dưới cùng bên phải.
3. Khu vực Tiêu đề trang & Thao tác chính (Page Header)
 * Thông tin hiển thị:
   * Tiêu đề chính: "Audit Logs".
   * Tiêu đề phụ: "Toàn bộ hoạt động bảo mật hệ thống — real-time".
 * Các nút tương tác:
   * Nút "Làm mới" (Refresh): Nằm ở góc phải, dùng để tải lại dữ liệu log mới nhất mà không cần F5 toàn bộ trang.
4. Khu vực Thẻ thống kê bảo mật (Security Summary Cards)
 * Thông tin hiển thị: Gồm 4 thẻ thống kê các rủi ro và hoạt động quan trọng:
   * TỔNG SỰ KIỆN: 88 (Icon kính lúp màu tím).
   * ĐĂNG NHẬP THÀNH CÔNG: 34 (Icon login màu xanh lá).
   * ĐĂNG NHẬP THẤT BẠI: 1 (Icon cái khiên màu đỏ - Cảnh báo quan trọng).
   * IP ĐÁNG NGỜ: 1 (Icon vân tay màu vàng/cam).
 * Các nút tương tác: Khi làm workshop, bạn có thể giải thích đây là các thẻ báo cáo nhanh. Tùy thuộc vào thiết kế hệ thống, khi click vào thẻ "Đăng nhập thất bại" hoặc "IP đáng ngờ", bảng bên dưới sẽ tự động lọc ra các dòng log tương ứng để Admin kiểm tra ngay lập tức.
5. Khu vực Tìm kiếm & Lọc Log (Search & Filters)
 * Thông tin hiển thị:
   * Bộ đếm bản ghi: "88 sự kiện" (Nằm ở góc phải ngang hàng với bộ lọc).
 * Các nút tương tác:
   * Ô nhập liệu (Search Box): Có dòng chữ mờ "Email, IP, sự kiện..." giúp Admin tra cứu nhanh dấu vết của một người dùng hoặc một địa chỉ mạng cụ thể.
   * Các nút lọc nhanh (Pill buttons): "Tất cả" (Đang active), "Thất bại", "LOGIN", "REGISTER", "FAILED LOGIN". Nhấn vào để thu hẹp phạm vi tìm kiếm loại log.
6. Khu vực Bảng dữ liệu Nhật ký (Audit Data Table)
 * Thông tin hiển thị:
   * Các tiêu đề cột: SỰ KIỆN, THÔNG TIN EMAIL, IP ADDRESS, THIẾT BỊ & TRÌNH DUYỆT, THỜI GIAN, KẾT QUẢ.
   * Dữ liệu từng dòng (Rows): * Cột Sự kiện hiển thị loại hành động (VD: LOGIN, GOOGLE LOGIN).
     * Cột Email cho biết ai thực hiện (VD: admin@smartex.com, huy12904@gmail.com).
     * Cột IP và Thiết bị lưu lại dấu vết phần cứng/mạng (VD: 183.80.67.146, Chrome on Windows (Desktop), Safari on iOS (Mobile)).
     * Cột Thời gian ghi chú chính xác đến từng giây (VD: 23<:46:832177145488998400>16 9/7/2026).
   * Nhãn kết quả (Badge): "THÀNH CÔNG" (Nền xanh lá).
 * Các nút tương tác: Trong bảng này chủ yếu là dữ liệu dạng Text chỉ đọc (Read-only) nhằm mục đích kiểm toán (Audit). Thường sẽ không có nút "Sửa" hay "Xóa" ở đây để đảm bảo tính minh bạch và toàn vẹn dữ liệu hệ thống. Cùng lắm sẽ có một nút (Icon mắt) ở cuối dòng để xem chi tiết JSON (payload) của sự kiện đó nếu cần.

--------------------------------------------------------------------------------------------------------------

<div align="center">

![Hình 5.7: Giao diện trang Quản lý phiên đăng nhập của hệ thống](image-6.png)

**Hình 5.7. Giao diện trang Quản lý phiên đăng nhập**

</div>


#### 5.1.7 Mô tả giao diện của ảnh 5.7
1. Khu vực thanh điều hướng trên cùng (Top Header)
 * Thông tin hiển thị:
   * Tiêu đề khu vực: "ADMIN / ADMIN PANEL".
   * Thời gian thực: "06:56 Thứ Sáu, 10 tháng 7".
   * Trạng thái hệ thống: Nhãn "SYSTEM ONLINE" (kèm chấm xanh lá).
 * Các nút tương tác:
   * Nút Menu (Icon 3 gạch): Thu gọn/mở rộng thanh Sidebar.
   * Ô tìm kiếm toàn cục: Khung nhập liệu "Tìm kiếm người dùng, bài thi...".
   * Cụm icon góc phải: Nút Theme (Sáng/Tối), Thông báo (Chuông), Cài đặt (Bánh răng) và Avatar Admin.
2. Khu vực Menu chức năng bên trái (Admin Sidebar)
 * Thông tin hiển thị:
   * Logo dự án Aura Academic.
   * Các tiêu đề phân nhóm: Đang cuộn tới phần BẢO MẬT và HỆ THỐNG.
   * Thông tin tài khoản góc dưới: "System Admin - SUPER ADMIN".
 * Các nút tương tác:
   * Danh sách tab điều hướng: Tab "Phiên đăng n..." (Phiên đăng nhập) đang được chọn (Active - nền xanh đậm, nằm ngay dưới tab Audit Logs).
   * Nút Đăng xuất: Biểu tượng mũi tên hướng ra ngoài nằm góc dưới cùng bên phải.
3. Khu vực Tiêu đề trang & Thanh công cụ (Page Header & Tools)
 * Thông tin hiển thị:
   * Tiêu đề chính: "Quản lý phiên đăng nhập" (kèm icon thiết bị kết nối).
   * Tiêu đề phụ: "Theo dõi và thu hồi các phiên truy cập đang hoạt động".
 * Các nút tương tác:
   * Ô tìm kiếm cục bộ (Local Search): Khung "Tìm email, tên, IP..." nằm ở góc phải, dùng để lọc nhanh các phiên đăng nhập cụ thể trong trang này.
   * Nút "Làm mới" (Refresh icon): Nằm ngay cạnh ô tìm kiếm, dùng để tải lại danh sách phiên đăng nhập realtime.
4. Khu vực Bảng dữ liệu Phiên hoạt động (Sessions Data Table)
 * Thông tin hiển thị:
   * Các tiêu đề cột: NGƯỜI DÙNG, THIẾT BỊ & TRÌNH DUYỆT, ĐỊA CHỈ IP, THỜI GIAN, TRẠNG THÁI.
   * Dữ liệu từng dòng (Rows):
     * Người dùng: Hiển thị Avatar chữ cái và Email (VD: admin@smartex.com, huy12904@gmail.com, vkey150204@gmail.com...).
     * Thiết bị & Trình duyệt: Kèm icon thiết bị (Desktop/Mobile) và mô tả chi tiết (VD: Chrome on Windows (Desktop), Safari on iOS (Mobile), Microsoft Edge...).
     * Địa chỉ IP: (VD: 183.80.67.146, 171.251.234.222...).
     * Thời gian: Ghi rõ chi tiết giờ/ngày "Bắt đầu" và "Hết hạn" của token/phiên đăng nhập.
   * Nhãn trạng thái (Badge): "Đang hoạt động" (Nền màu xanh ngọc), cho biết user này vẫn đang có token hợp lệ và giữ kết nối với hệ thống.
 * Các nút tương tác (Hành động cực kỳ quan trọng):
   * Nút "Thu hồi / Đăng xuất từ xa" (Icon mũi tên trỏ ra ngoài cửa): Nằm ở cột ngoài cùng bên phải của mỗi dòng. Khi Admin click vào nút này, hệ thống sẽ gọi API xóa token/session của thiết bị đó ngay lập tức, buộc người dùng tương ứng phải đăng nhập lại. Đây là một tính năng bảo mật rất hay để demo trong workshop!

