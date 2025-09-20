File mô tả UML Lab 03 – Zalo Mini App
1. Đối tượng tham gia (Actors & Components)
Student (Học sinh)
-Đăng nhập vào Zalo Mini App.
-Tham gia làm bài thi trắc nghiệm và tự luận.
-Xem điểm, giải thích và thứ hạng.
-Nhận nhắc lịch học, lịch kiểm tra.
Teacher (Giáo viên)
-Đăng nhập vào Zalo Mini App.
-Tạo đề thi, chỉnh sửa và lên lịch thi.
-Chấm điểm tự luận.
-Xem thống kê điểm số, độ khó câu hỏi.
-Nhận nhắc lịch chấm, lịch thi.
Zalo Platform
-Cung cấp cơ chế OAuth để xác thực tài khoản người dùng.
-Là môi trường chạy Mini App.
Backend API (NodeJS/Express)
-Xử lý nghiệp vụ chính: lấy đề thi, ghi nhận bài làm, chấm tự động MCQ, lưu kết quả.
-Giao tiếp giữa Zalo Mini App và Firebase.
Firebase (Firestore/Storage)
-Lưu trữ dữ liệu: Users, Exams, Questions, Attempts, Transactions, Leaderboards.
-Cung cấp dữ liệu thống kê cho giáo viên.
Notification Service (Zalo OA/ZNS/Cloud Functions)
-Gửi thông báo nhắc lịch học/thi.
-Gửi thông báo kết quả điểm thi.
2. Thông điệp trao đổi (Messages)
Use Case chính
1.Đăng nhập Zalo OAuth:
Student/Teacher → Zalo Platform → Backend API xác thực và khởi tạo user trong Firebase.
2.Tạo/Lên lịch đề thi (Teacher):
Teacher → Mini App → Backend API → Firebase (lưu đề thi, câu hỏi, lịch).
3.Làm bài thi (Student):
Student → Mini App → Backend API → Firebase (tải đề, gửi câu trả lời).
4.Chấm điểm:
Tự động MCQ: Backend API xử lý, so sánh với đáp án.
Tự luận: Teacher vào grading queue để chấm, lưu kết quả.
5.Xem kết quả & xếp hạng:
Student → Mini App → Backend API → Firebase (lấy điểm, bảng xếp hạng).
6.Thống kê kết quả (Teacher):
Teacher → Mini App → Backend API → Firebase (lấy dữ liệu phân tích).
7.Nhắc lịch/Thông báo:
Backend API/Cloud Function → Notification Service → Student/Teacher.
