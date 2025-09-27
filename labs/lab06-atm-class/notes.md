## 1. Class Diagram – Mini App Học Tập & Thi Trực Tuyến
### Thành phần chính
- **User (Student)**  
  - Thuộc tính: userId, name, email, role  
  - Phương thức: đăng nhập, xem đề thi, làm bài thi, nộp bài.  
  - Nhiệm vụ: đại diện cho học sinh tham gia vào hệ thống.  

- **Teacher**  
  - Thuộc tính: teacherId, name, email, department  
  - Phương thức: đăng nhập, tạo đề thi, quản lý câu hỏi, xem kết quả.  
  - Nhiệm vụ: đại diện cho giáo viên quản lý bài thi và câu hỏi.  

- **Exam**  
  - Thuộc tính: examId, title, startTime, endTime  
  - Phương thức: addQuestion(), publish(), getResult()  
  - Nhiệm vụ: quản lý các bài thi trực tuyến.  

- **Question**  
  - Thuộc tính: questionId, content, type, options, correctAnswer  
  - Nhiệm vụ: quản lý câu hỏi cho các bài thi.  

- **Attempt**  
  - Thuộc tính: attemptId, userId, examId, startTime, submitTime  
  - Nhiệm vụ: ghi lại lần làm bài của học sinh.  

- **Answer**  
  - Thuộc tính: answerId, attemptId, questionId, selectedOption  
  - Nhiệm vụ: lưu đáp án học sinh chọn.  

- **Result**  
  - Thuộc tính: resultId, attemptId, score, feedback  
  - Nhiệm vụ: lưu điểm và phản hồi cho lần thi của học sinh.  

### Quan hệ
- User **thực hiện** Attempt trên Exam.  
- Teacher **tạo** Exam và Question.  
- Exam **bao gồm** nhiều Question.  
- Attempt **chứa** nhiều Answer.  
- Result **liên kết** Attempt để tính điểm.  
---
## 2. Package Diagram – Mini App Học Tập & Thi Trực Tuyến
### Các Package
- **UI Layer (Zalo Mini App)**  
  - Thành phần: StudentUI, TeacherUI, AuthUI  
  - Nhiệm vụ: giao diện cho học sinh và giáo viên thao tác.  

- **API Layer (NodeJS/Express)**  
  - Thành phần: AuthService, ExamService, QuestionService, AttemptService, AnswerService, ResultService, ImportService, StatisticsService, NotificationOrchestrator  
  - Nhiệm vụ: xử lý nghiệp vụ chính, cầu nối giữa UI và dữ liệu.  

- **Data Layer (Firestore/Storage)**  
  - Thành phần: UsersCollection, ExamsCollection, QuestionsCollection, AttemptsCollection, AnswersCollection, ResultsCollection, QuestionBankCollection, AttachmentsStorage, Leaderboards  
  - Nhiệm vụ: lưu trữ dữ liệu về người dùng, bài thi, câu hỏi, kết quả.  

- **Infra/External Services**  
  - Thành phần: ZaloOAuth, ZaloNotification, CloudFunctions, Workers  
  - Nhiệm vụ: cung cấp xác thực OAuth, gửi thông báo Zalo OA/ZNS, chạy các tác vụ nền như auto-save, auto-submit.  

### Quan hệ chính
- **UI → API**:  
  - StudentUI gọi ExamService, AttemptService, ResultService.  
  - TeacherUI gọi ExamService, QuestionService, ImportService, StatisticsService.  
  - AuthUI gọi AuthService.  

- **API → Data**:  
  - Các service đọc/ghi dữ liệu từ Firestore/Storage Collections.  

- **API → External**:  
  - AuthService kết nối ZaloOAuth để xác thực người dùng.  
  - NotificationOrchestrator gọi ZaloNotification để gửi nhắc nhở, thông báo kết quả.  

- **CloudFunctions** & **Workers**:  
  - Chạy nền các tác vụ tự động như auto-save, auto-submit, batch compute thống kê.  


## 3. Kết luận
- **Class Diagram** cho thấy cách tổ chức lớp, thuộc tính, phương thức và mối quan hệ cho nghiệp vụ học và thi trực tuyến.  
- **Package Diagram** cho thấy kiến trúc module/tầng, thể hiện luồng dữ liệu và dịch vụ giữa các thành phần.  
- Hai sơ đồ này giúp minh họa và chuẩn hóa kiến trúc của hệ thống trước khi triển khai.  
