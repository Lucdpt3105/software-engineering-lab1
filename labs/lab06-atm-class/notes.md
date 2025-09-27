## 1. Class Diagram
### 1.1 Danh sách Class
#### **User (Base Class)**
- **Attributes**
  - `userId: String`
  - `name: String`
  - `email: String`
  - `role: String (STUDENT | TEACHER | ADMIN)`
- **Methods**
  - `loginWithZalo(token: String): AuthResult`
  - `updateProfile(data: Map): void`
#### **Teacher (extends User)**
- **Attributes**
  - `teacherId: String` (alias `userId`)
  - `department: String`
- **Methods**
  - `createExam(examDTO): Exam`
  - `editExam(examId: String, examDTO): Exam`
  - `addQuestion(examId: String, questionDTO): Question`
  - `importFromExcel(examId: String, fileUrl: String): ImportResult`
  - `gradeEssay(attemptId: String, questionId: String, score: float, feedback: String): void`
  - `viewStatistics(examId: String): Statistics`

#### **Student (extends User)**
- **Attributes**
  - `studentId: String` (alias `userId`)
  - `classId: String` hoặc `classIds: List<String>`
- **Methods**
  - `viewExamList(filter: Map): List<Exam>`
  - `startExam(examId: String): Attempt`
  - `resumeExam(attemptId: String): Attempt`
  - `submitAnswer(attemptId: String, questionId: String, answer: AnswerPayload): void`
  - `submitExam(attemptId: String): Result`
  - `viewResult(attemptId: String): Result`
#### **Exam**
- **Attributes**
  - `examId: String`
  - `title: String`
  - `subject: String`
  - `type: String (MCQ | ESSAY | MIXED)`
  - `durationMinutes: int`
  - `startAt: DateTime`
  - `endAt: DateTime`
  - `status: String (DRAFT | PUBLISHED | CLOSED)`
  - `questionIds: List<String>`
  - `config: Map` (immediateResult, allowReview, maxAttempts, shuffleQuestions)
- **Methods**
  - `addQuestion(q: Question): void`
  - `validate(): ValidationResult`
  - `publish(): void`
  - `archive(): void`
#### **QuestionBank**
- **Attributes**
  - `bankId: String`
  - `ownerId: String`
  - `name: String`
  - `meta: Map`
- **Methods**
  - `search(criteria: Map): List<Question>`
  - `addQuestion(q: Question): Question`
  - `importQuestions(fileUrl: String): ImportResult`
#### **Question**
- **Attributes**
  - `questionId: String`
  - `examId: String` (nullable nếu thuộc QuestionBank)
  - `content: String` (text/HTML/Markdown)
  - `mediaUrl: List<String>`
  - `type: String (MCQ | ESSAY)`
  - `choices?: List<Choice>`
  - `weight: float`
  - `difficulty: String (EASY | MEDIUM | HARD)`
- **Methods**
  - `getChoices(): List<Choice>`
  - `isAutoMarkable(): boolean`
#### **Choice**
- **Attributes**
  - `choiceId: String`
  - `questionId: String`
  - `text: String`
  - `isCorrect: boolean`
- **Methods**
  - (Value object – không có method phức tạp)
#### **Attempt**
- **Attributes**
  - `attemptId: String`
  - `examId: String`
  - `studentId: String`
  - `startedAt: DateTime`
  - `lastSavedAt: DateTime`
  - `finishedAt?: DateTime`
  - `status: String (IN_PROGRESS | PAUSED | SUBMITTED | AUTO_SUBMITTED)`
  - `score?: float`
  - `timeRemainingSeconds?: int`
- **Methods**
  - `saveTempAnswer(questionId: String, answerPayload: AnswerPayload): void`
  - `autoSave(): void`
  - `finalizeAndScore(): Result`
  - `resume(): Attempt`
#### **Answer**
- **Attributes**
  - `answerId: String`
  - `attemptId: String`
  - `questionId: String`
  - `response: String | List<String>`
  - `updatedAt: DateTime`
  - `isAutoMarked: boolean`
  - `autoMarkScore?: float`
  - `manualScore?: float`
  - `feedback?: String`
- **Methods**
  - `markAuto(correct: boolean): float`
  - `applyManualScore(score: float, feedback: String): void`
#### **Result**
- **Attributes**
  - `resultId: String`
  - `attemptId: String`
  - `totalScore: float`
  - `rank?: int`
  - `generatedAt: DateTime`
  - `breakdown?: Map<questionId, score>`
- **Methods**
  - `computeRank(context): int`
  - `publish(): void`
#### **Notification**
- **Attributes**
  - `notificationId: String`
  - `userId: String`
  - `type: String (REMINDER | RESULT | SCHEDULE | SYSTEM)`
  - `content: String`
  - `status: String (PENDING | SENT | FAILED)`
  - `sentAt: DateTime`
- **Methods**
  - `send(): void`
---
### 1.2 Relationships
- `Teacher` **extends** `User`.
- `Student` **extends** `User`.
- `Teacher` **creates** `Exam` → `Exam` **aggregates** `Question`.
- `Exam` **uses** `QuestionBank` để import câu hỏi.
- `Question` **aggregates** `Choice`.
- `Student` **starts** `Attempt` → `Attempt` **aggregates** `Answer`.
- `Result` **belongs to** `Attempt`.
- `Notification` **sent to** `User`.
- `Teacher` **grades** `Answer` trong `Attempt`.
---
## 2. Package Diagram
### 2.1 Danh sách Package & Components
#### **UI Layer (Zalo Mini App)**
- **Components**
  - `StudentUI`
  - `TeacherUI`
  - `AuthUI`
- **Nhiệm vụ**
  - Hiển thị giao diện cho học sinh & giáo viên.
  - Gửi yêu cầu đến Backend API.
#### **API Layer (NodeJS/Express Services)**
- **Components**
  - `AuthService`
  - `ExamService`
  - `QuestionService`
  - `AttemptService`
  - `AnswerService`
  - `ResultService`
  - `ImportService`
  - `StatisticsService`
  - `NotificationOrchestrator`
- **Nhiệm vụ**
  - Xử lý nghiệp vụ chính.
  - Kết nối UI và Data Layer.
  - Gửi thông báo qua Notification Service.
#### **Data Layer (Firestore/Storage)**
- **Collections**
  - `UsersCollection`
  - `ExamsCollection`
  - `QuestionsCollection`
  - `ChoicesCollection`
  - `AttemptsCollection`
  - `AnswersCollection`
  - `ResultsCollection`
  - `QuestionBankCollection`
  - `AttachmentsStorage`
  - `Leaderboards`
- **Nhiệm vụ**
  - Lưu trữ dữ liệu người dùng, bài thi, câu hỏi, kết quả.
#### **Infra/External Services**
- **Components**
  - `ZaloOAuth`
  - `ZaloNotification`
  - `CloudFunctions`
  - `Workers`
- **Nhiệm vụ**
  - Xác thực OAuth.
  - Gửi thông báo OA/ZNS.
  - Xử lý tác vụ nền.
---
### 2.2 Relationships giữa các Package
- **UI → API**:
  - `StudentUI` gọi `ExamService`, `AttemptService`, `ResultService`.
  - `TeacherUI` gọi `ExamService`, `QuestionService`, `ImportService`, `StatisticsService`.
  - `AuthUI` gọi `AuthService`.
- **API → Data**:
  - Các Service đọc/ghi dữ liệu từ Firestore/Storage.
- **API → External Services**:
  - `AuthService` kết nối `ZaloOAuth` để xác thực.
  - `NotificationOrchestrator` gọi `ZaloNotification`.
- **CloudFunctions & Workers**:
  - Auto-save, auto-submit, thống kê.
