flowchart TB
    %% Actors
    student([Student])
    teacher([Teacher])
    zalo([Zalo Platform])
    backend([Backend API])
    firebase([Firebase])
    notify([Notification Service])
    %% System boundary (Zalo Mini App)
    subgraph Zalo_Mini_App["Zalo Mini App (System)"]
        UC_Login(Đăng nhập Zalo OAuth)
        UC_CreateExam(Tạo/Chỉnh sửa đề thi)
        UC_ScheduleExam(Lên lịch thi)
        UC_TakeExam(Làm bài thi MCQ/Tự luận) 
        UC_AutoGrade(Chấm tự động MCQ)
        UC_ManualGrade(GV chấm tự luận)
        UC_ViewResult(Xem điểm & giải thích)
        UC_Leaderboard(Xếp hạng)
        UC_Stats(Thống kê điểm/độ khó)
        UC_Reminder(Nhắc lịch học/thi)
    end
    %% Associations
    student --- UC_Login
    student --- UC_TakeExam
    student --- UC_ViewResult
    student --- UC_Leaderboard
    student --- UC_Reminder
    teacher --- UC_Login
    teacher --- UC_CreateExam
    teacher --- UC_ScheduleExam
    teacher --- UC_ManualGrade
    teacher --- UC_Stats
    teacher --- UC_Reminder
    %% Internal collaborations (dashed)
    UC_Login -.-> zalo
    UC_TakeExam -.-> backend
    UC_CreateExam -.-> backend
    UC_ScheduleExam -.-> backend
    UC_AutoGrade -.-> backend
    UC_ManualGrade -.-> backend
    UC_ViewResult -.-> backend
    UC_Leaderboard -.-> backend
    UC_Stats -.-> backend
    UC_Reminder -.-> notify
    backend -.-> firebase

