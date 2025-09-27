# Final Report: Mini hỗ trợ học tập và thi trực tuyến

## 1. Giới thiệu

* Lý do chọn đề tài
* Mục tiêu của hệ thống (hỗ trợ học tập, làm bài thi trực tuyến, quản lý học sinh – giáo viên)
* Đối tượng sử dụng chính (sinh viên, giáo viên, admin)
* Công nghệ sử dụng (ngôn ngữ lập trình, framework, MySQL, công cụ UML, …)

---

## 2. Mô hình UML

* Use Case Diagram (vai trò: Học sinh, Giáo viên, Admin, chức năng chính)
![Use Case học sinh](https://github.com/1yn3r/software-engineering-lab/blob/bc52245931fba87d32cd15d9a08a4aa049641219/labs/lab10-final-demo/final-report/Use%20Cases/h%E1%BB%8Dc%20sinh.jpg)
![Use Case Giáo Viên](https://github.com/1yn3r/software-engineering-lab/blob/1c9969ad95aaa989d819b157e89c145f71fd1992/labs/lab02-usecase/NewUC/giaovien.jpg)
![Use Case Admin + Hệ thống](https://github.com/1yn3r/software-engineering-lab/blob/1c9969ad95aaa989d819b157e89c145f71fd1992/labs/lab02-usecase/NewUC/admin%2Bhethong.jpg)


* Class Diagram (cấu trúc đối tượng, quan hệ giữa các class)
![Class diagram](https://github.com/1yn3r/software-engineering-lab/blob/1c9969ad95aaa989d819b157e89c145f71fd1992/labs/lab06-atm-class/Class%20diagram.png)
*Package Diagram:  

![Package Diagram](https://github.com/1yn3r/software-engineering-lab/blob/1c9969ad95aaa989d819b157e89c145f71fd1992/labs/lab06-atm-class/Package_Diagram.png)
* Sequence Diagram (luồng thực hiện ví dụ: đăng nhập, làm bài thi, chấm điểm tự động)
* Đối với giảng viên
  ![Sequence Giảng Viên](https://github.com/1yn3r/software-engineering-lab/blob/6279ebd0e6bbbef10d77fdce993835011fb2c52e/labs/lab03-UML/Gi%E1%BA%A3ng%20Vi%C3%AAn.png)
* Đối với học sinh
 ![Sequence Học Viên](https://github.com/1yn3r/software-engineering-lab/blob/6279ebd0e6bbbef10d77fdce993835011fb2c52e/labs/lab03-UML/Student.png)
* Sơ đồ luồng (quy trình làm bài và nộp bài)
![UC ](https://github.com/1yn3r/software-engineering-lab/blob/6279ebd0e6bbbef10d77fdce993835011fb2c52e/labs/lab03-UML/AnhPhanTichNghiepVu1ChucNang.png)
---

## 3. Database & Code minh họa

### 3.1 Database
* ERD (Entity Relationship Diagram)
 ![ERD](https://github.com/1yn3r/software-engineering-lab/blob/6279ebd0e6bbbef10d77fdce993835011fb2c52e/labs/lab05/ERDForMiniAPP.png)
* Mô tả các bảng chính (Users, Subjects, Exams, Questions, Attempts, Results, …)
Ừ được chứ 👍. Bạn có thể bỏ markdown heading `##` và bullet `*` đi, chỉ để plain text thôi. Ví dụ như này:

---

1. **Users**
   Gồm các trường: user_id (PK), user_name, user_email, user_password, user_role, created_at, status.
   Đại diện cho người dùng hệ thống (học sinh, giáo viên, admin).

2. **Subjects**
   Gồm subject_id (PK), subject_name.
   Môn học, có thể chứa nhiều topic (chủ đề) và nhiều kỳ thi.

3. **Topics**
   Gồm topic_id (PK), topic_name, topic_subject_id (FK → Subjects.subject_id).
   Mỗi môn học có nhiều chủ đề (1-n).

4. **Questions**
   Gồm question_id (PK), question_text, question_topic_id (FK → Topics.topic_id), question_type_id (FK → QuestionTypes.question_type_id), question_difficulty.
   Câu hỏi được gắn với một topic và có một loại (MCQ, tự luận...).

5. **Answers**
   Gồm answer_id (PK), answer_text, answer_question_id (FK → Questions.question_id), is_correct.
   Mỗi câu hỏi có nhiều đáp án (1-n).

6. **Exams**
   Gồm exam_id (PK), exam_title, exam_subject_id (FK → Subjects.subject_id), exam_date, exam_duration, total_marks.
   Kỳ thi thuộc về một môn học.

7. **ExamQuestions** (bảng trung gian)
   Gồm exam_question_id (PK), exam_question_exam_id (FK → Exams.exam_id), exam_question_question_id (FK → Questions.question_id).
   Thể hiện quan hệ n-n giữa Exams và Questions.

8. **UserExams**
   Gồm user_exam_id (PK), user_exam_user_id (FK → Users.user_id), user_exam_exam_id (FK → Exams.exam_id), user_exam_score.
   Ghi nhận mỗi học sinh tham gia một kỳ thi.

9. **ExamResults**
   Gồm exam_result_id (PK), exam_result_user_exam_id (FK → UserExams.user_exam_id), exam_result_question_id (FK → Questions.question_id), exam_result_selected_answer_id (FK → Answers.answer_id).
   Lưu chi tiết kết quả làm bài.

---

**Quan hệ chính**

* Users – UserExams – Exams: quan hệ n-n (nhiều học sinh có thể thi nhiều kỳ thi).
* Exams – ExamQuestions – Questions: quan hệ n-n (một kỳ thi gồm nhiều câu hỏi, một câu hỏi có thể tái sử dụng ở nhiều kỳ thi).
* Questions – Answers: quan hệ 1-n.
* Subjects – Topics – Questions: quan hệ 1-n.
* UserExams – ExamResults: quan hệ 1-n.

### 3.2 Login form + Chức năng demo

* Đăng nhập/Đăng ký
  ![Login](https://github.com/1yn3r/software-engineering-lab/blob/a7203e2732188ed0f1c0d87c405463fcc9c3ecd9/labs/lab04-login-form/loginform_image.png)
* Tạo đề thi và câu hỏi
* Làm bài & nộp bài thi
* Chấm điểm tự động & lưu kết quả
    ![Result](https://github.com/1yn3r/software-engineering-lab/blob/7fc96f4f434db71cb7bca4483003f1909dd35748/labs/lab07/z7057178444065_1b7446cad25de483feaa08054af5242f.jpg)

---

## 4. Kết quả test & Sprint report

### 4.1 Kết quả test

* Unit test (kiểm tra các module)
 ![Kiểm tra module](https://github.com/1yn3r/software-engineering-lab/blob/7fc96f4f434db71cb7bca4483003f1909dd35748/labs/lab08/UnitTest.png)
* Integration test (tương tác giữa backend – database – frontend)
  ![Kiểm tra module](https://github.com/1yn3r/software-engineering-lab/blob/main/labs/lab08/%E1%BA%A2nh%20pass&fail.png?raw=true)

### 4.2 Sprint report

* Số sprint đã thực hiện
* Công việc hoàn thành trong từng sprint
* Đánh giá tiến độ 

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


