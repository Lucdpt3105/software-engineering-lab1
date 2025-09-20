sequenceDiagram
    autonumber
    participant S as Student (Zalo App)
    participant Z as Zalo Platform
    participant A as Zalo Mini App (UI)
    participant B as Backend API (NodeJS)
    participant F as Firebase (Firestore/Storage)
    participant N as Notification Service

    Note over S,Z: Mo Mini App va dang nhap (Zalo OAuth)
    S->>Z: Open Mini App
    Z->>A: Launch + OAuth token
    A->>B: Verify token / get profile
    B->>F: GetOrCreate(Student)
    F-->>B: Student record
    B-->>A: Auth OK + exam list

    Note over S,A: Chon bai thi
    S->>A: Select exam
    A->>B: GET /exams/{id}
    B->>F: Read exam + questions
    F-->>B: Exam + questions
    B-->>A: Exam content

    Note over S,A: Lam bai (MCQ & Tu luan)
    loop For each question
        S->>A: Send answer
        A->>B: POST /attempts/{examId}/answers
        B->>F: Save temp answer
        F-->>B: OK
        B-->>A: Ack
    end

    Note over S,A: Nop bai
    S->>A: Submit
    A->>B: POST /attempts/{examId}/submit
    B->>F: Load answers
    alt Co MCQ
        B->>B: Auto grade MCQ
    end
    alt Co tu luan
        B->>F: Mark essay pending review
    end
    B->>F: Save attempt (score_mcq, status)
    F-->>B: OK
    B-->>A: Return preliminary score

    Note over A,N: Thong bao
    A->>N: Notify result (optional)
    N-->>S: Zalo message

    Note over S: Xem diem cuoi & xep hang
    S->>A: View result
    A->>B: GET /attempts/{examId}/me
    B->>F: Read final score + rank
    F-->>B: Score + rank
    B-->>A: Show final score, rank, explanations
