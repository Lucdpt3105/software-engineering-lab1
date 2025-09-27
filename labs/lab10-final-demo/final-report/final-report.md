# Final Report: Mini hỗ trợ học tập và thi trực tuyến

## 1. Giới thiệu

* Lý do chọn đề tài
* Mục tiêu của hệ thống (hỗ trợ học tập, làm bài thi trực tuyến, quản lý học sinh – giáo viên)
* Đối tượng sử dụng chính (sinh viên, giáo viên, admin)
* Công nghệ sử dụng (ngôn ngữ lập trình, framework, MySQL, công cụ UML, …)

---

## 2. Mô hình UML

* Use Case Diagram (vai trò: Học sinh, Giáo viên, Admin, chức năng chính)
![alt text](https://github.com/1yn3r/software-engineering-lab/blob/bc52245931fba87d32cd15d9a08a4aa049641219/labs/lab10-final-demo/final-report/Use%20Cases/h%E1%BB%8Dc%20sinh.jpg)

* Class Diagram (cấu trúc đối tượng, quan hệ giữa các class)
* Sequence Diagram (luồng thực hiện ví dụ: đăng nhập, làm bài thi, chấm điểm tự động)
* Activity Diagram (quy trình làm bài và nộp bài)

---

## 3. Database & Code minh họa

### 3.1 Database

* Mô tả các bảng chính (Users, Subjects, Exams, Questions, Attempts, Results, …)
* ERD (Entity Relationship Diagram)
* Giải thích ràng buộc khóa chính, khóa ngoại, quan hệ 1-n, n-n

### 3.2 Code minh họa

* Đăng nhập/Đăng ký
* Tạo đề thi và câu hỏi
* Làm bài & nộp bài thi
* Chấm điểm tự động & lưu kết quả

---

## 4. Kết quả test & Sprint report

### 4.1 Kết quả test

* Unit test (kiểm tra các module)
* Integration test (tương tác giữa backend – database – frontend)
* Test case tiêu biểu (đăng nhập sai mật khẩu, làm bài quá thời gian, …)

### 4.2 Sprint report

* Số sprint đã thực hiện
* Công việc hoàn thành trong từng sprint
* Đánh giá tiến độ (theo Agile/Scrum nếu có)

---

## 5. Kết luận & Định hướng mở rộng

* Tổng kết ưu điểm của hệ thống
* Hạn chế hiện tại (giao diện, bảo mật, tối ưu database, …)
* Đề xuất cải tiến:

  * Thêm AI chấm tự động câu hỏi tự luận
  * Thêm chức năng phòng thi ảo với giám thị online
  * Tích hợp app mobile
  * Phân tích dữ liệu học tập để gợi ý cá nhân hóa

---

## 6. Tài liệu tham khảo (nếu cần)

* Tài liệu kỹ thuật, framework, DBMS
* Các nghiên cứu liên quan đến hệ thống thi trực tuyến

