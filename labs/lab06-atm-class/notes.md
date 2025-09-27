**Mô tả class diagram
1. Notification

Attributes

notificationId: String

userId: String

type: String — (REMINDER | RESULT | SCHEDULE | SYSTEM)

content: String

status: String — (PENDING | SENT | FAILED)

sentAt: DateTime

Methods

send(): void — gửi notification cho user

2. User (base)

Attributes

userId: String

name: String

email: String

role: String — (STUDENT | TEACHER | ADMIN)

Methods

loginWithZalo(token: String): AuthResult

updateProfile(data: Map): void

3. Teacher (extends User)

Attributes

teacherId: String (alias userId)

department: String

Methods

createExam(examDTO): Exam

editExam(examId: String, examDTO): Exam

addQuestion(examId: String, questionDTO): Question

importFromExcel(examId: String, fileUrl: String): ImportResult

gradeEssay(attemptId: String, questionId: String, score: float, feedback: String): void

viewStatistics(examId: String): Statistics

4. Student (extends User)

Attributes

studentId: String (alias userId)

classId: String (hoặc classIds: List<String>)

Methods

viewExamList(filter: Map): List<Exam>

startExam(examId: String): Attempt

resumeExam(attemptId: String): Attempt

submitAnswer(attemptId: String, questionId: String, answer: AnswerPayload): void

submitExam(attemptId: String): Result

viewResult(attemptId: String): Result

5. Exam

Attributes

examId: String

title: String

subject: String

type: String — (MCQ | ESSAY | MIXED)

durationMinutes: int

startAt: DateTime

endAt: DateTime

status: String — (DRAFT | PUBLISHED | CLOSED)

questionIds: List<String> (ordered)

config: Map — (immediateResult, allowReview, maxAttempts, shuffleQuestions, …)

Methods

addQuestion(q: Question): void

validate(): ValidationResult

publish(): void

archive(): void

6. QuestionBank

Attributes

bankId: String

ownerId: String

name: String

meta: Map

Methods

search(criteria: Map): List<Question>

addQuestion(q: Question): Question

importQuestions(fileUrl: String): ImportResult

7. Question

Attributes

questionId: String

examId: String (nullable nếu lưu trong bank)

content: String (text / HTML / Markdown)

mediaUrl: List<String>

type: String — (MCQ | ESSAY)

choices?: List<Choice> (nếu MCQ)

weight: float (điểm của câu)

difficulty: String — (EASY | MEDIUM | HARD)

Methods

getChoices(): List<Choice>

isAutoMarkable(): boolean

8. Choice

Attributes

choiceId: String

questionId: String

text: String

isCorrect: boolean

Methods

(value object — thường không có method phức tạp)

9. Attempt

Attributes

attemptId: String

examId: String

studentId: String

startedAt: DateTime

lastSavedAt: DateTime

finishedAt?: DateTime

status: String — (IN_PROGRESS | PAUSED | SUBMITTED | AUTO_SUBMITTED)

score?: float

timeRemainingSeconds?: int

Methods

saveTempAnswer(questionId: String, answerPayload: AnswerPayload): void

autoSave(): void

finalizeAndScore(): Result

resume(): Attempt

10. Answer

Attributes

answerId: String

attemptId: String

questionId: String

response: String | List<String>

updatedAt: DateTime

isAutoMarked: boolean

autoMarkScore?: float

manualScore?: float

feedback?: String

Methods

markAuto(correct: boolean): float

applyManualScore(score: float, feedback: String): void

11. Result

Attributes

resultId: String

attemptId: String

totalScore: float

rank?: int

generatedAt: DateTime

breakdown?: Map<questionId, score>

Methods

computeRank(context): int

publish(): void — (notify student/teacher)
