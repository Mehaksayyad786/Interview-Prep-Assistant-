# AI Interview Preparation Assistant (MockAI)

MockAI is a full-stack Generative AI application designed to help job seekers and students prepare for professional interviews. The assistant acts as an AI interviewer, dynamically generating questions tailored to a candidate's profile, target role, and interview category. It provides real-time scoring, comprehensive feedback, syllabus weak-topic identification, and a step-by-step personalized learning roadmap.

---

## 🚀 Key Features

* **User Authentication**: Secure user registration, logins, and JWT token authorization.
* **Candidate Profile Manager**: Maintain academic history, target roles, experience levels, and an interactive tags selector to customize skill lists.
* **Interview Setup Wizard**: Configure mock parameters selecting Target Roles, Interview Categories (Technical, HR, Behavioral), and Difficulty Levels (Easy, Medium, Hard).
* **Live Interview Room**: Conducts a text-based 5-question session. Features progress tracking bars, word-count suggestions, and responsive skeleton loader animations.
* **Real-time AI Evaluation**: Uses Gemini's structured JSON outputs to calculate technical correctness, communication clarity, and answer relevance scores.
* **Syllabus Weak-topic Mapping**: Automaticaly tags incorrect details with specific topics (e.g. REST API Design, SQL Joins) needing review.
* **Personalized Improvement Plan**: Generates a step-by-step roadmap checklist tailored to performance scores at the end of the session.
* **Historical Logs Log**: Browse completed or resume active mock interviews with advanced query filter trackers.

---

## 🛠️ Technology Stack

### Frontend
* **Core**: React 19 (TypeScript, Vite framework)
* **Styling**: TailwindCSS v4
* **Icons**: Lucide React
* **Router**: React Router DOM

### Backend
* **Core**: FastAPI (Python 3.13)
* **Validation**: Pydantic v2
* **Authentication**: PyJWT, Passlib (Bcrypt hashing)
* **Database Driver**: PyMongo (MongoDB Client)

### Database
* **Database**: MongoDB (Local Instance)

### AI Client
* **LLM API**: Google Gemini API (`gemini-1.5-flash`)
* **JSON Structured Mode**: Direct generation using JSON schema generation configs

---

## 📂 System Architecture

```text
                    ┌─────────────────────────┐
                    │      React Frontend     │
                    │   (Vite + Tailwind v4)  │
                    └────────────┬────────────┘
                                 │
                            REST API Calls
                                 │
                    ┌────────────▼────────────┐
                    │     FastAPI Backend     │
                    └────────────┬────────────┘
                                 │
             ┌───────────────────┼───────────────────┐
             ▼                   ▼                   ▼
      Authentication          MongoDB             LLM API
       (JWT / Bcrypt)    (Local Port 27017)   (Google Gemini)
                                                     │
                                                     ├─ Question Generation
                                                     ├─ Answer Evaluation
                                                     └─ Improvement plans
```

---

## ⚙️ Installation & Setup

### Pre-requisites
* **Node.js** (v18+)
* **Python** (v3.10+)
* **MongoDB** installed and running on port `27017`

### 1. Backend Configuration
1. Navigate to the `backend` folder:
   ```bash
   cd backend
   ```
2. Activate the pre-configured virtual environment:
   * Windows PowerShell:
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   * Windows Command Prompt:
     ```cmd
     .venv\Scripts\activate.bat
     ```
3. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
4. Configure environment variables in the `.env` template file:
   * Open the `.env` file in the `backend` folder and add your Google Gemini API Key:
     ```env
     MONGODB_URI=mongodb://localhost:27017
     DATABASE_NAME=interview_prep
     SECRET_KEY=4eb806e23214da3108c909623e1f5cd9a77ef797bd3e57620eb583d735cd12fb
     ALGORITHM=HS256
     ACCESS_TOKEN_EXPIRE_MINUTES=1440
     GEMINI_API_KEY=YOUR_GEMINI_API_KEY
     ```
5. Run the FastAPI development server:
   ```bash
   python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
   ```

### 2. Frontend Configuration
1. Open a new terminal and navigate to the `frontend` folder:
   ```bash
   cd frontend
   ```
2. Install npm packages:
   ```bash
   npm install
   ```
3. Launch the Vite development server:
   ```bash
   npm run dev
   ```
4. Access the web dashboard at `http://localhost:5173/`.

---

## 📡 API Endpoints Reference

### Authentication
* `POST /api/auth/register` - Create a new candidate profile credentials
* `POST /api/auth/login` - Authenticate user credentials and retrieve JWT token
* `GET /api/auth/me` - Fetch details of the active authenticated user session

### Profile Settings
* `GET /api/profile` - Fetch candidate educational background, skill chips, and preferred role
* `PUT /api/profile` - Update candidate academic info, experience levels, and skills list

### Mock Lifecycle
* `POST /api/interview/start` - Initiate a mock session; returns unique `interview_id`
* `GET /api/interview/question/{interview_id}` - Fetch the next question (calls Gemini using context of prior questions)
* `POST /api/interview/answer/{interview_id}` - Submit an answer text (triggers Gemini grading; updates scorecard metrics)
* `POST /api/interview/complete/{interview_id}` - Compile overall averages, tag weakness zones, build improvement map, and finalize mock status

### Reports & Logs
* `GET /api/history` - Fetch mock list history for the authenticated profile
* `GET /api/results/{interview_id}` - Retrieve detailed scores, grading feedbacks, and roadmaps for a completed session
