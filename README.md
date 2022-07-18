# DoDat-VNPT  
I. Nhiệm vụ:  
Ngày | Nhiệm Vụ
-----|---------
Thứ 2|Tìm hiểu và áp dụng framework flask
Thứ 3|Tìm hiểu và áp dụng framework flask
Thứ 4|Viết API sử dụng Flask để gửi mail
Thứ 5|Tìm hiểu và chạy thử dự án nhỏ kết hợp Flask với SQLite
Thứ 6|Tìm hiểu và chạy thử dự án nhỏ kết hợp Flask với SQLite

II. Nội dung:
1.	Tìm hiểu và áp dụng framework flask:
1.1.	Tìm hiểu:
-	Flask là một Web Framework rất nhẹ của Python, dễ dàng giúp người mới bắt đầu học Python có thể tạo ra website nhỏ. Flask cũng dễ mở rộng để xây dựng các ứng dụng web phức tạp.
-	Được ứng dụng trong thiết kế website đơn giản và tạo lập các ứng dụng cho những trang web lớn và phức tạp. 

1.2.	Áp dụng framework Flask:
-	Cài đặt thư viện: pipenv install flask
2.	Viết API sử dụng flask để gửi mail:
-	Cài đặt thư viện: 	pipenv install flask
                      pipenv install flask-mail
![image](https://user-images.githubusercontent.com/106945207/179439445-d02941bd-43af-44b1-908a-3458ff3d941b.png)

3.	Tìm hiểu và chạy thử dự án kết hợp Flask với SQLite:  
1.	Yêu cầu dự án:  
Tạo 1 bảng dữ liệu bao gồm:  
NHANVIEN  
idNhanVien (string) suggest sử dụng uuidv4  
tenNhanVien (string)  
CCCD (string) <- unique (duy nhất)  
email (string) <- unique (duy nhất)  
phone (string) <- unique (duy nhất)  
		Đầu ra: 5 APIs  
			API danh sách nhân viên Method: GET  
API tạo nhân viên: POST -> tạo thành công thì gửi email thông báo đến nhân viên đó  
API cập nhật nhân viên Method: POST / PUT  
API thông tin nhân viên Method: GET  
API xóa nhân viên Method: DELETE  
2.	Kết quả đạt được:  
-	Create database:  
![image](https://user-images.githubusercontent.com/106945207/179439690-74b9e41c-aa0a-430d-8d79-146b1a059ea7.png)

- Giao diện:  
![image](https://user-images.githubusercontent.com/106945207/179439744-6868a097-ca2e-49c5-b761-31d05cf9fe83.png)

- Danh sách nhân viện:  
![image](https://user-images.githubusercontent.com/106945207/179439762-0878a2b4-40b6-4ab3-b8e6-1c285f75fb92.png)

- Thêm mới nhân viên:  
![image](https://user-images.githubusercontent.com/106945207/179439792-63214a32-b949-4440-b928-6e0233e659d3.png)

- Thông tin nhân viện:  
![image](https://user-images.githubusercontent.com/106945207/179439826-9a8a29ff-a4ea-4f62-9772-3e075ee44db0.png)

- Cập nhật nhân viện:  
![image](https://user-images.githubusercontent.com/106945207/179439846-4ac55290-fc35-4d7b-a3bf-e6fa274322e7.png)

- Xoá nhân viện:  
![image](https://user-images.githubusercontent.com/106945207/179439867-c278eda5-6533-48e4-9654-d3267007a4fd.png)




