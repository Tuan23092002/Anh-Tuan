# Anh-Tuan
Create videos from photos
# Hướng dẫn sử dụng:

## Tạo Video từ Ảnh và Generate.py:

1. **Đảm bảo bạn đã cài đặt các thư viện cần thiết:**
   - OpenCV (cv2)
   - NumPy

2. **Chuẩn bị Ảnh:**
   - Đảm bảo rằng các ảnh bạn muốn sử dụng để tạo video đã được lưu trong thư mục `images/`.

3. **Chỉnh sửa Generate.py (Tuỳ chọn):**
   - Bạn có thể chỉnh sửa Generate.py để điều chỉnh thời gian hiển thị của mỗi ảnh, hiệu ứng chuyển đổi, v.v.

4. **Chạy Generate.py:**
   - Chạy script `generate.py` để tạo video từ ảnh trong thư mục `images/`.
   - Kết quả sẽ được lưu dưới dạng video trong thư mục `output/`.
5. **Chạy app.py*
   - Chạy app.py để demo với 1 web đơn giản
   - Đưa vào ảnh, hoặc tệp nhiều ảnh .zip, file audio
   - Nhận được kết quả là video cùng với nhạc  

## Chuyển Đổi Video sang Chất Lượng 1080p và ConverttoHD:

1. **Cài đặt FFMPEG (nếu chưa có):**
   - Đảm bảo bạn đã cài đặt FFMPEG trên hệ thống của mình.

2. **Chạy ConverttoHD:**
   - Chạy lệnh `converttoHD input_video.mp4 output_video.mp4` để chuyển đổi video sang chất lượng 1080p.

## Đăng Tải Video lên YouTube và Upload.py:

1. **Cấp Quyền Truy Cập YouTube:**
   - Đảm bảo bạn có quyền truy cập đến tài khoản YouTube bạn muốn đăng tải.

2. **Cài đặt Thư Viện:**
   - Cài đặt thư viện `google-auth`, `google-auth-oauthlib`, và `google-auth-httplib2`.

3. **Chỉnh sửa Upload.py:**
   - Điều chỉnh các tham số như tiêu đề, mô tả và thẻ cho video trong tệp `upload.py`.

4. **Chạy Upload.py:**
   - Chạy script `upload.py` để đăng tải video đã được chuyển đổi sang YouTube.

## Lưu Ý:
- Đảm bảo rằng bạn có kết nối Internet ổn định khi đăng tải video lên YouTube.
- Lưu ý về quyền sở hữu và bản quyền khi sử dụng ảnh và video từ nguồn khác nhau.
