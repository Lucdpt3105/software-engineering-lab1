# 📘 Project Report – Mini App E-Learning  

## 1. Giới thiệu dự án 🚀
- **Tên**: Mini App E-Learning Hỗ Trợ Học Tập Trực Tuyến 🎓  
- **Mục tiêu**: Xây dựng một ứng dụng mini giúp sinh viên học trực tuyến thông qua quản lý môn học, chủ đề, tài liệu, bài tập, câu hỏi trắc nghiệm, thi thử và thi chính thức. Ứng dụng hỗ trợ giao tiếp (chat, forum), quản lý tiến độ, phản hồi và điểm số.  
- **Quy mô**: Bài tập học tập (lab) – mức độ triển khai cơ bản theo database đã thiết kế.  

---

## 2. Artifacts đã xây dựng 🛠️

### 2.1. Use Case Diagrams 🎯
- **Student**: đăng nhập 🔑, tham gia khóa học 📚, xem tài liệu 📄, làm bài tập/quiz ✏️, thi 📝, xem tiến độ 📊, nhận huy hiệu 🏅.  
- **Teacher**: tạo chủ đề 🗂️, ra đề 📑, quản lý câu hỏi ❓, chấm điểm ✅, tổ chức meeting online 💻.  
- **Admin**: quản lý user 👥, môn học 📖, gói subscription 💳, thống kê 📈.  
- **System**: gửi thông báo 🔔, cập nhật leaderboard 🏆, nhắc deadline ⏰.  
### 2.2. Sequence Diagrams 🔁
#### 2.2.1. Luồng học của Student 👩‍🎓
- Student đăng nhập 🔑  
- Chọn khóa học 📚 và xem tài liệu 📄  
- Làm quiz/thi 📝  
- Nhận điểm và thông báo 📊🔔  
#### 2.2.2. Luồng nộp bài tập ✉️
- Student upload file 📎  
- Backend lưu file + metadata 🗄️  
- Teacher nhận thông báo 👨‍🏫  
- Teacher chấm điểm ✅ và gửi phản hồi 🔔  
#### 2.2.3. Luồng thi chính thức (Exam) 📝
- Student bắt đầu thi 🏁  
- Trả lời câu hỏi ❓  
- Hệ thống lưu kết quả 🗄️  
- Tính điểm và gửi thông báo 📊🔔  
#### 2.2.4. Luồng subscription & thanh toán 💳
- User chọn gói 📦  
- Thanh toán qua Payment Gateway 🧾  
- Backend cập nhật `payments` + `subscriptions` 🗄️  
- Thông báo kích hoạt gói 🔔  
#### 2.2.5. Luồng job hệ thống ⏰
- Cron job kiểm tra deadline ⏳  
- Gửi nhắc nhở 🔔  
- Backup dữ liệu 💾  
- Cập nhật leaderboard 🏆  
### 2.3. Database & ERD 🗄️ 
- **Users** 👤: thông tin tài khoản (student, teacher, admin).  
- **Subjects – Topics – StudyMaterials** 📚: quản lý môn học, chủ đề, tài liệu học.  
- **Questions – Answers – QuestionTypes** ❓: ngân hàng câu hỏi và đáp án.  
- **Exams – ExamQuestions – UserExams – ExamResults** 📝: hệ thống thi & kết quả.  
- **PracticeTests – UserPractices – PracticeResults** 🧑‍🏫: thi thử và kết quả luyện tập.  
- **ProgressTracker – StudySessions – Notes** 📊🗒️: theo dõi tiến độ và thời gian học.  
- **Badges – UserBadges – Leaderboard – DailyChallenges – UserChallenges** 🏅🔥: gamification (huy hiệu, bảng xếp hạng, thử thách hằng ngày).  
- **ChatGroups – ChatMessages – ForumQuestions – ForumAnswers – Meetings** 💬👨‍👩‍👧‍👦: tương tác, trao đổi học tập.  
- **Feedbacks – Announcements – Payments – Subscriptions** 📨📢💳: quản trị hệ thống, gói học, góp ý, thông báo.  
### 2.4. Form Login Code 🔑
- **Frontend**: `index.html`, `styles.css`, `main.js` với form đăng nhập.  
- **Backend**: API xử lý đăng nhập ⚙️, kiểm tra user/password trong bảng `users`.  
- Đã viết **unit test** 🧪 cho module xác thực và **integration test** 🔍 cho form login.
---
## 3. Quy trình làm việc 📋

1. **Phân tích yêu cầu** 🔎  
   - Actor: Student 👩‍🎓, Teacher 👨‍🏫, Admin 👨‍💼, System ⚙️.  
   - Mô hình hóa nghiệp vụ bằng Use Case & Sequence Diagram.  

2. **Thiết kế hệ thống** 🏗️  
   - Dựa trên `DBMiniAppStudy.sql` để dựng ERD.  
   - Xác định các module: User, Course, Exam, Practice, Communication.  

3. **Lập trình & tích hợp** 💻  
   - Xây dựng API CRUD cho users, subjects, exams.  
   - Kết nối login form với backend (Express + MySQL).  
   - Test chức năng exam + practice flow.  

4. **Quản lý source code** 🔐  
   - Dùng Git/GitHub, commit theo module.  
   - Tag phiên bản v1.0.  

5. **Kiểm thử** 🧪  
   - Unit test: xác minh xử lý login, tính điểm.  
   - Integration test: kiểm tra luồng login, làm bài thi.  
   - Manual test: giao diện, database, chat.  

6. **Báo cáo** 📝  
   - Viết báo cáo Markdown, tổng hợp code, test case.  

---

## 4. Hướng dẫn push code & tạo tag version 🌐

```bash
# Cấu hình lần đầu
git config --global user.name "Tên của bạn"
git config --global user.email "email@example.com"

# Thêm remote
git remote add origin https://github.com/1yn3r/software-engineering-lab.git

# Push code
git add .
git commit -m "E-Learning 1.0"
git push origin main

# Tạo tag v1.0
git tag v1.0
git push origin v1.0
