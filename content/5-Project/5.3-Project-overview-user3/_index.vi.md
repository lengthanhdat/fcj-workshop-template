---
title : "Tổng quan dự án và các chức năng dành cho người dùng phần 3"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

#### 5.Tổng quan về giao diện trang Ngân hàng đề thi, trang tài liệu học tập, trang thông báo và trang Hồ sơ cá nhân của hệ thống: 


<div align="center">

![Hình 5.1: Giao diện trang Ngân hàng đề thi của hệ thống](image.png)

**Hình 5.1. Giao diện trang Ngân hàng đề thi của hệ thống**

</div>


**5.1.1. Mô tả giao diện Hình 5.1**

1. Khu vực Banner chính (Khung màu xanh trên cùng)

- Thông tin hiển thị:
  - Tiêu đề lớn: "Ngân hàng Đề thi" và đoạn text mô tả bên dưới.
  - 3 Thẻ thống kê (Nền trắng): "0 Tổng đề", "23 Môn học", "0 Chuyên đề".

- Các nút tương tác (Buttons):
  - Nút Icon Danh sách (Cạnh nút Lịch sử làm bài): Có thể dùng để mở menu phụ hoặc thu gọn banner.
  - Nút "Lịch sử làm bài" (Có icon biểu đồ): Bấm vào chuyển hướng sang trang xem lại các đề đã làm.

2. Khu vực 3 Thẻ tính năng (Feature Cards)

- Thông tin hiển thị:
  - 3 thẻ nằm ngang gồm "Tìm đề nhanh", "Ôn theo chuyên đề", "Đề phổ biến" cùng text mô tả phụ.

- Các nút tương tác:
  - Bản thân 3 thẻ này hoạt động như các nút (Tabs/Filters).
  - Hành vi mong đợi: Bấm vào thẻ nào, bộ lọc hoặc giao diện bên dưới sẽ thay đổi tương ứng (VD: Bấm "Ôn theo chuyên đề" thì cột bên trái đổi từ danh sách Môn học sang danh sách Chuyên đề).

3. Khu vực Thanh Tìm kiếm & Bộ lọc (Search & Filter Bar)

- Các nút tương tác & Nhập liệu:
  - Ô tìm kiếm (Input field): Có placeholder "Tìm đề thi theo tên...". Cho phép nhập text để tìm đề thi (Enter để tìm hoặc tự động lọc Real-time).
  - Nút "Đề yêu thích" (Icon trái tim): Hoạt động như nút Bật/Tắt (Toggle). Bấm vào để chỉ hiển thị các đề đã đánh dấu sao/lưu lại.
  - Nút "0 đề thi" (Nền xanh đậm): Hoạt động như "Giỏ đề thi". Bấm vào mở ra popup/drawer danh sách các đề đang được chọn.

4. Khu vực Nội dung chính (Chia làm 3 cột)

**Cột trái: Danh mục MÔN HỌC**

- Thông tin hiển thị:
  - Tiêu đề "MÔN HỌC". Danh sách 8 môn học đầu tiên (Toán học, Ngữ văn, Tiếng Việt...) đi kèm icon.

- Các nút tương tác:
  - Các hàng môn học: Bấm vào một môn học sẽ làm nổi bật môn đó (Active state) và cột giữa chỉ hiển thị đề thi của môn tương ứng.
  - Nút "Xem thêm 15 môn" (Icon mũi tên xuống): Bấm vào xổ dọc (Expand) danh sách để hiển thị các môn đang bị ẩn. Sau khi xổ, nút đổi thành "Thu gọn" kèm mũi tên lên.

**Cột giữa: Vùng hiển thị Kết quả (Đang ở trạng thái Trống)**

- Thông tin hiển thị:
  - Nhãn "0 đề thi" ở góc trên cùng bên trái vùng này.
  - Hình ảnh minh họa trống (Empty state icon).
  - Dòng chữ "Không tìm thấy đề phù hợp" và hướng dẫn "Thử thay đổi từ khoá tìm kiếm".

**Cột phải: Mục PHỔ BIẾN**

- Thông tin hiển thị:
  - Tiêu đề "PHỔ BIẾN" (kèm icon ngọn lửa).
  - Khung hiển thị trạng thái trống với dòng chữ mờ "Chưa có dữ liệu" (Do hệ thống chưa có đề thi nào để thống kê lượng người làm).


--------------------------------------------------------------------------------------------------------------

<div align="center">

![Hình 5.2: Giao diện trang Tài liệu học tập của hệ thống](image-1.png)

**Hình 5.2. Giao diện trang Tài liệu học tập của hệ thống**

</div>


**5.1.2. Mô tả giao diện Hình 5.2**
1. Khu vực Banner chính (Khung trên cùng)

- Thông tin hiển thị:
  - Nhãn (Tag): "[Icon quyển sách] KHO TÀI LIỆU" màu xanh.
  - Tiêu đề lớn: "Tài liệu học tập".
  - Đoạn văn bản mô tả: "Khám phá và tải xuống các tài liệu học tập, bài giảng và tài liệu tham khảo được cung cấp bởi giáo viên."
  - 4 Thẻ thống kê (Stats Cards) xếp thành lưới 2x2:
    - Thẻ 1: Icon thư mục - "0 TÀI LIỆU".
    - Thẻ 2: Icon mũ cử nhân - "0 MÔN HỌC".
    - Thẻ 3: Icon tải xuống - "0 LƯỢT TẢI".
    - Thẻ 4: Icon huy hiệu - "0 MỚI TUẦN NÀY".

- Hành vi mong đợi:
  - Các thẻ thống kê phải hiển thị chính xác số liệu tổng hợp từ dữ liệu của học sinh.
  - Khi di chuột (hover) vào các thẻ có thể có hiệu ứng sáng lên hoặc nổi lên nhẹ.

2. Khu vực Thanh Tìm kiếm & Bộ lọc (Search & Filter Bar)

- Các nút tương tác & Nhập liệu:
  - Ô tìm kiếm (Search Input):
    - Thông tin: Có icon kính lúp và placeholder chữ mờ "Tìm kiếm theo tên tài liệu, môn học, từ khóa...".
    - Hành vi mong đợi: Cho phép nhập văn bản. Khi gõ phím Enter hoặc gõ xong (sau một khoảng delay ngắn), hệ thống sẽ lọc kết quả bên dưới tương ứng với từ khóa.

  - Dropdown Lọc (Đang hiển thị "Tất cả"):
    - Hành vi mong đợi: Bấm vào sẽ xổ xuống danh sách các tiêu chí lọc (Ví dụ: lọc theo Môn học, Lớp hoặc Loại tài liệu như PDF/Word/Video). Khi chọn một mục, danh sách bên dưới lập tức cập nhật.

  - Dropdown Sắp xếp (Đang hiển thị "Mới nhất"):
    - Hành vi mong đợi: Bấm vào sẽ xổ xuống các tiêu chí sắp xếp (Sort). Ví dụ: Mới nhất, Cũ nhất, Tên A-Z, Tên Z-A, Xem nhiều nhất. Chọn xong tự động sắp xếp lại dữ liệu.

3. Khu vực Danh sách tài liệu (Data Section)

- Phần Tiêu đề danh sách:
  - Thông tin hiển thị: Tiêu đề "Tất cả tài liệu" ở bên trái và một nhãn (badge) xám ghi "0 tài liệu" ở bên phải.
  - Hành vi mong đợi: Nhãn số lượng phải cập nhật linh hoạt (Dynamic) dựa trên kết quả của bộ lọc phía trên (Ví dụ: Lọc môn Toán ra 5 bài thì nhãn hiển thị "5 tài liệu").

- Phần Nội dung (Đang hiển thị Trạng thái trống):
  - Thông tin hiển thị: Một khung xám lớn, chính giữa có icon (kính lúp/ổ khóa mờ) và dòng chữ "Không tìm thấy tài liệu phù hợp".
  - Hành vi mong đợi: Trạng thái này phải luôn xuất hiện khi kho tài liệu thực sự trống hoặc khi học sinh tìm kiếm/lọc nhưng không có kết quả nào khớp. Khối thông báo cần được căn giữa hoàn hảo, không bị xô lệch layout của toàn trang.

--------------------------------------------------------------------------------------------------------------

<div align="center">

![Hình 5.3: Giao diện trang Thông báo của hệ thống](image-2.png)

**Hình 5.3.  Giao diện trang Thông báo của hệ thống**

</div>


**5.1.3. Mô tả giao diện Hình 5.3**
1. Khu vực Banner chính (Khung trên cùng)

- Thông tin hiển thị:
  - Nhãn (Tag): "[Icon chuông] TRUNG TÂM THÔNG BÁO HỌC SINH" nền xanh nhạt.
  - Tiêu đề lớn: "Thông báo hệ thống".
  - Dòng trạng thái thống kê: "Bạn có 0 thông báo chưa đọc" (Số 0 được bôi đậm màu xanh).

- Hành vi mong đợi:
  - Con số ở dòng trạng thái phải đồng bộ tuyệt đối với số thông báo chưa đọc hiển thị trên Header (icon chuông đỏ). Khi có thông báo mới hoặc người dùng "đánh dấu đã đọc", con số này phải thay đổi ngay lập tức.

2. Khu vực Thanh Tìm kiếm & Bộ lọc (Search & Filter Bar)

- Các nút tương tác & Nhập liệu:
  - Ô tìm kiếm (Input field):
    - Thông tin: Có icon kính lúp và placeholder chữ mờ "Tìm kiếm thông báo...".
    - Hành vi mong đợi: Cho phép gõ văn bản để tìm theo tiêu đề hoặc nội dung thông báo.

  - Dropdown "Tất cả loại":
    - Hành vi mong đợi: Bấm vào sẽ xổ xuống danh sách các loại thông báo (VD: Từ lớp học, Từ kỳ thi, Từ hệ thống). Chọn để lọc.

  - Dropdown "Tất cả trạng thái":
    - Hành vi mong đợi: Bấm vào xổ ra các trạng thái (VD: Đã đọc, Chưa đọc).

  - Nút "Lọc" (Nền xám nhạt):
    - Hành vi mong đợi: Bấm vào để áp dụng các điều kiện tìm kiếm/lọc ở 3 ô bên trái. (Lưu ý cho tester: Cần kiểm tra xem hệ thống có bắt buộc phải bấm nút này mới lọc, hay chỉ cần đổi dropdown là dữ liệu đã tự động load lại (Auto-submit).)

3. Khu vực Danh sách thông báo (Khung hiển thị dữ liệu)

- Thông tin hiển thị (Trạng thái trống):
  - Hình ảnh minh họa: Icon chiếc chuông bị gạch chéo màu xám mờ.
  - Tiêu đề chính: "Không có thông báo nào được tìm thấy."
  - Dòng mô tả phụ: "Các thông báo mới từ lớp học, kỳ thi và hệ thống sẽ xuất hiện tại đây."

- Hành vi mong đợi:
  - Giao diện này phải xuất hiện khi người dùng chưa có bất kỳ thông báo nào hoặc khi sử dụng bộ lọc (ví dụ lọc thông báo "Chưa đọc") mà không có kết quả phù hợp. Toàn bộ khối thông báo này cần được căn giữa hoàn hảo trong khung trắng.


  --------------------------------------------------------------------------------------------------------------

<div align="center">

![Hình 5.4: Giao diện trang Hồ sơ cá nhân của hệ thống](image-3.png)

**Hình 5.4.  Giao diện trang Hồ sơ cá nhân của hệ thống**

</div>


**5.1.4. Mô tả giao diện Hình 5.4**

Trang này hiện đang hiển thị trạng thái đã có dữ liệu (Populated State).

1. Khu vực Tiêu đề Hồ sơ (Profile Header)

- Thông tin hiển thị:
  - Ảnh đại diện (Avatar) lớn: Hiển thị chữ "Đ" trên nền nâu.
  - Nhãn (Tag): "HỒ SƠ HỌC SINH" màu xanh nhỏ.
  - Tên hiển thị: "2783_ Đậu Đại Tài".

- Các nút tương tác:
  - Nút "Sửa hồ sơ" (Icon cây bút):
    - Hành vi mong đợi: Bấm vào sẽ mở ra một Form (Modal/Popup hoặc chuyển trang) cho phép người dùng cập nhật thông tin cá nhân (đổi tên, đổi avatar, ngày sinh...).

2. Khu vực Thống kê tổng quan (Stats Cards)

- Thông tin hiển thị:
  - Thẻ 1: "BÀI THI ĐÃ LÀM" - Số 1 (Màu xanh).
  - Thẻ 2: "ĐIỂM TRUNG BÌNH" - Số 6.7 (Màu xanh đậm/tím).
  - Thẻ 3: "ĐIỂM CAO NHẤT" - Số 6.7 (Màu xanh lá).
  - Thẻ 4: "TỈ LỆ ĐẠT" - Tỉ lệ 1/1 (Màu đỏ).

- Hành vi mong đợi:
  - Dữ liệu số phải được tính toán và lấy chính xác từ lịch sử làm bài của học sinh.

3. Khu vực Dữ liệu chi tiết (Chia làm 2 cột)

**Cột trái: Thông tin & Lịch sử**

- Khung "Thông tin cá nhân":
  - Thông tin hiển thị:
    - Email tài khoản (toilatai2004@gmail.com).
    - Thời gian "ĐĂNG NHẬP GẦN NHẤT" (21:07:07 9/7/2026).
  - Hành vi mong đợi:
    - Thời gian đăng nhập phải được cập nhật đúng mỗi khi user tạo session mới.

- Khung "Kết quả gần đây":
  - Thông tin hiển thị:
    - Bảng liệt kê các bài thi mới làm (Bài thi: Test, Điểm: 6.7, Nộp lúc: 04:22:29 10/7/2026, Trạng thái: nhãn "Đạt" màu xanh lá).
  - Hành vi mong đợi:
    - Dữ liệu khớp với thẻ thống kê ở trên.
    - Hiển thị đúng tối đa số dòng quy định (VD: 5 bài gần nhất).

**Cột phải: Khung "Bảo mật" (Security Settings)**

- Thông tin trạng thái tĩnh:
  - Mục Email: Trạng thái "Đã xác minh" (Chữ xanh lá).
  - Mục Đăng nhập: Phương thức "Google" (Chữ xanh lá).

- Các nút tương tác & Nhập liệu:
  - Mục 2FA (Xác thực 2 bước):
    - Thông tin: Đang ở trạng thái "Chưa bật".
    - Nút "Gửi mã bật":
      - Hành vi mong đợi: Bấm vào sẽ gửi một mã OTP về email toilatai2004@gmail.com và mở ra ô nhập mã OTP để xác nhận bật 2FA.

  - Khung "Thiết lập mật khẩu":
    - Thông tin:
      - Đoạn text giải thích việc tạo mật khẩu phụ.
      - Ô nhập "MẬT KHẨU MỚI" và "XÁC NHẬN MẬT KHẨU".
    - Hành vi mong đợi:
      - Văn bản nhập vào bị mã hóa thành dấu chấm/sao (***).
      - Có Icon con mắt ở góc phải. Khi bấm vào Icon con mắt, mật khẩu sẽ hiển thị dạng text rõ ràng (Toggle show/hide password).
    - Nút "Thiết lập mật khẩu":
      - Hành vi mong đợi: Nút này chỉ sáng lên (Enable) khi người dùng đã nhập đủ cả 2 ô. Nếu bấm vào mà 2 ô không khớp nhau, phải báo lỗi "Mật khẩu xác nhận không khớp". Nếu khớp và thỏa mãn quy tắc mật khẩu (độ dài, ký tự...), hệ thống lưu mật khẩu và báo thành công.