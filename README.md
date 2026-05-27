Tích chập (Convolution)
1. Lý thuyết

Tích chập là phép toán dùng một ma trận nhỏ gọi là kernel K để quét qua ảnh I và tạo ảnh mới.

Mục đích:

làm mượt ảnh

giảm nhiễu

phát hiện biên

làm sắc nét

2. Các kernel và công dụng
   
A. Mean Filter (Lọc trung bình)

1/9 * [
 [1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]
]

	​
Công dụng

làm mượt ảnh

giảm nhiễu nhẹ

làm mờ ảnh

Ý tưởng

Lấy trung bình các pixel xung quanh.

Nhược điểm

làm mất chi tiết

ảnh bị blur





B. Gaussian Filter

Kernel
1/16 * [
 [1, 2, 1],
 [2, 4, 2],
 [1, 2, 1]
]

	​
Công dụng

giảm nhiễu

làm mượt tốt hơn Mean Filter

giữ biên tốt hơn

Ý tưởng

Pixel gần trung tâm có trọng số lớn hơn.

Ứng dụng

tiền xử lý ảnh

xử lý ảnh y tế











C. Sobel Filter

Sobel X
	​
[
 [-1, 0, 1],
 [-2, 0, 2],
 [-1, 0, 1]
]
	​

Công dụng

phát hiện biên dọc

tìm thay đổi theo trục x


Sobel Y
	​

[
 [-1, -2, -1],
 [ 0,  0,  0],
 [ 1,  2,  1]
]

	​

Công dụng

phát hiện biên ngang

tìm thay đổi theo trục y

Ý tưởng Sobel

Nếu độ sáng thay đổi mạnh:

→ xuất hiện cạnh (edge)

D. Laplacian Filter

[
 [ 0, -1,  0],
 [-1,  4, -1],
 [ 0, -1,  0]
]

	​

Công dụng

phát hiện biên mọi hướng

làm nổi cạnh

Đặc điểm

Nhạy với nhiễu nên thường: kết hợp Gaussian trước

E. Sharpen Filter (Làm sắc nét)

Kernel
	​
[
 [ 0, -1,  0],
 [-1,  5, -1],
 [ 0, -1,  0]
]
	​

	​

Công dụng

tăng độ sắc nét

làm rõ chi tiết

Ý tưởng

Tăng khác biệt giữa pixel trung tâm và vùng xung quanh.

	​

	​

