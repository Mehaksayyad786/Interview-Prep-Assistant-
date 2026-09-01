import os
import json
import time
from dotenv import load_dotenv
import google.generativeai as genai

# Load env variables from backend folder
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment or .env file.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-3.5-flash")

ROLES = ["Python Developer", "Java Developer", "Data Analyst", "Data Scientist", "Machine Learning Engineer", "AI Engineer"]
TYPES = ["Technical", "HR", "Behavioral"]
DIFFICULTIES = ["Easy", "Medium", "Hard"]

ROLE_SKILLS = {
    "Python Developer": [
        "Core Python (GIL, memory models, garbage collection, OOP, decorators, generators)",
        "Web Frameworks & APIs (FastAPI, Django, Flask, Asyncio, RESTful API design)",
        "Databases & ORMs (SQL, NoSQL, migrations, SQLAlchemy, Django ORM)",
        "Testing & Software Engineering Tools (pytest, mocking, Git, Docker, CI/CD)",
        "Concurrency & Workers (multiprocessing, multithreading, Celery, task queues)"
    ],
    "Java Developer": [
        "Core Java (JVM internals, memory models, Garbage Collection, generics, Lambdas, Streams)",
        "Spring Boot & Spring Framework (IoC, DI, Spring Security, Spring MVC)",
        "ORM & Databases (JPA, Hibernate, SQL queries, transaction management, connection pools)",
        "Testing & Build Tools (JUnit, Mockito, Maven, Gradle)",
        "Deployment & Microservices Architecture (Docker, Git, REST API design)"
    ],
    "Data Analyst": [
        "Data Querying & Processing (SQL Window Functions, CTEs, Joins, Excel pivot tables, Lookup formulas)",
        "Data Programming (Python Pandas, NumPy, or R)",
        "BI & Visualization (Tableau, Power BI, Matplotlib, Seaborn)",
        "Statistics & Analysis (Descriptive statistics, A/B testing, distributions, probability)",
        "Data Warehousing & ETL (Schemas, ETL pipelines, cleaning dirty/missing data)"
    ],
    "Data Scientist": [
        "Programming & Data Wrangling (Python, SQL, Pandas, NumPy, Git)",
        "Statistical Modeling & Hypothesis Testing (Regression analysis, experimental design, Bayesian statistics)",
        "Machine Learning Algorithms (Regression, Classification, Clustering, metrics like ROC-AUC, F1)",
        "Feature Engineering & Processing (Outliers, scaling, PCA, t-SNE)",
        "Advanced Analytics & Communication (Presenting complex concepts to business stakeholders)"
    ],
    "Machine Learning Engineer": [
        "ML Algorithms & Deep Learning (Tree models, SVMs, Neural Networks, PyTorch, TensorFlow)",
        "MLOps & Pipelines (Docker, Kubernetes, DVC, MLflow, Airflow, Prefect)",
        "Software Engineering (Clean code, Git, automated pipeline testing)",
        "Deployment & Inference (FastAPI, Triton, BentoML, ONNX, quantization, model serving)"
    ],
    "AI Engineer": [
        "Generative AI & LLMs (Prompt engineering, fine-tuning, LoRA, Vector DBs like Pinecone/Chroma, RAG)",
        "Frameworks & Agents (LangChain, LlamaIndex, Transformers, multi-agent orchestration)",
        "Neural Architectures (Transformers, self-attention, CNNs, Diffusion models)",
        "System Design & APIs (FastAPI, function calling, structured output generation, semantic search)",
        "LLM Evaluation & Optimization (Ragas, TruLens, latency/cost optimization, semantic caching)"
    ]
}

def generate_questions_for_role_and_type(role, itype, model_name):
    model = genai.GenerativeModel(model_name)
    skills_list = ROLE_SKILLS.get(role, [])
    skills_text = ", ".join(skills_list)
    
    if itype == "Technical":
        prompt = f"""You are a professional technical interviewer. Generate a batch of technical interview questions for a candidate applying for the role: '{role}'.
You must generate exactly 20 questions for EACH of the three difficulty levels: 'Easy', 'Medium', and 'Hard' (total of 60 questions).
Ensure the questions test different skills/topics: {skills_text}.
For each difficulty level (Easy, Medium, Hard):
- Easy: simple/basic questions.
- Medium: standard mid-level topics.
- Hard: complex, advanced, in-depth technical/design scenarios.

Format Requirements for each difficulty level's list of 20 questions:
- Questions 1, 3, 6, 8, 11, 13, 16, 18 MUST be of type 'mcq' (Multiple Choice Question) with 4 options and a correct_answer letter ('A', 'B', 'C', or 'D').
- Questions 2, 4, 7, 9, 12, 14, 17, 19 MUST be of type 'fib' (Fill in the Blank) with a correct_answer word or short phrase.
- Questions 5, 10, 15, 20 MUST be of type 'descriptive' (open-ended description) with a correct_answer containing key concepts expected in a good answer.

You MUST return your output in this EXACT JSON structure:
{{
  "Easy": [
    {{
      "question_number": 1,
      "question": "...",
      "type": "mcq",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "correct_answer": "C"
    }},
    ...
  ],
  "Medium": [
    ...
  ],
  "Hard": [
    ...
  ]
}}
"""
    else:
        # HR or Behavioral
        prompt = f"""You are a professional HR and Behavioral interviewer. Generate a batch of '{itype}' interview questions for a candidate applying for the role: '{role}'.
You must generate exactly 20 questions for EACH of the three difficulty levels: 'Easy', 'Medium', and 'Hard' (total of 60 questions).
For each difficulty level (Easy, Medium, Hard):
- Easy: Junior/Entry-level questions.
- Medium: Mid-level questions.
- Hard: Senior/Lead-level leadership scenarios.
The questions must be custom-tailored to the professional background, projects, and challenges expected of a '{role}'.

Format Requirements for each difficulty level's list of 20 questions:
- Questions 1, 3, 6, 8, 11, 13, 16, 18 MUST be of type 'mcq' (Multiple Choice Question) with 4 options representing different professional/behavioral decisions and a correct_answer letter ('A', 'B', 'C', or 'D').
- Questions 2, 4, 7, 9, 12, 14, 17, 19 MUST be of type 'fib' (Fill in the Blank) regarding soft skill terms or alignment concepts, with a correct_answer word or phrase.
- Questions 5, 10, 15, 20 MUST be of type 'descriptive' (open-ended situational description) asking the candidate to describe an experience, with a correct_answer containing key traits expected in a good answer.

You MUST return your output in this EXACT JSON structure:
{{
  "Easy": [
    {{
      "question_number": 1,
      "question": "...",
      "type": "mcq",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "correct_answer": "C"
    }},
    ...
  ],
  "Medium": [
    ...
  ],
  "Hard": [
    ...
  ]
}}
"""

    for attempt in range(4):
        try:
            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    response_mime_type="application/json"
                ),
                request_options={"timeout": 180}
            )
            data = json.loads(response.text.strip())
            
            # Validation check
            valid = True
            for diff in DIFFICULTIES:
                if diff not in data or not isinstance(data[diff], list) or len(data[diff]) != 20:
                    valid = False
                    break
            
            if valid:
                print(f"  [SUCCESS] Generated 60 questions for {role} - {itype}")
                return data
            else:
                print(f"  [RETRY] Validation failed for {role} - {itype} (attempt {attempt + 1}).")
        except Exception as e:
            print(f"  [RETRY] API call failed for {role} - {itype} on attempt {attempt + 1}: {e}")
            time.sleep(20)
            
    # Fallback default lists if all retries fail
    print(f"  [FALLBACK] Using defaults for {role} - {itype}")
    fallback_data = {}
    for diff in DIFFICULTIES:
        fallback_data[diff] = []
        for q_idx in range(1, 21):
            q_type = "mcq" if q_idx in [1, 3, 6, 8, 11, 13, 16, 18] else ("fib" if q_idx in [2, 4, 7, 9, 12, 14, 17, 19] else "descriptive")
            options = ["Opt A", "Opt B", "Opt C", "Opt D"] if q_type == "mcq" else []
            correct = "A" if q_type == "mcq" else ("fallback term" if q_type == "fib" else "concepts")
            fallback_data[diff].append({
                "question_number": q_idx,
                "question": f"Fallback: Test question {q_idx} for {role} {itype} {diff}.",
                "type": q_type,
                "options": options,
                "correct_answer": correct
            })
    return fallback_data

def main():
    print("Starting generation of 1,080 questions via Gemini (Batched, Rate-Limited & Model-Cycled)...")
    questions_data = {}
    
    MODELS = [
        "gemini-flash-lite-latest", 
        "gemini-3.6-flash", 
        "gemini-3.5-flash-lite",
        "gemini-3.1-flash-lite"
    ]
    
    combo_idx = 0
    for role in ROLES:
        print(f"Generating for Role: {role}...")
        questions_data[role] = {}
        for itype in TYPES:
            model_name = MODELS[combo_idx % len(MODELS)]
            print(f"  Category: {itype} using model {model_name}...")
            batch = generate_questions_for_role_and_type(role, itype, model_name)
            questions_data[role][itype] = batch
            combo_idx += 1
            time.sleep(15) # Sleep 15 seconds to keep request rate below 5 Requests Per Minute (Free Tier limit)
                
    # Format the entire content to write to questions_bank.py
    file_content = f"""# Predefined Questions Bank for MockAI (Auto-Generated)
# Contains 20 distinct questions for each combination of role, type, and difficulty.
# Total Questions: 1,080

QUESTIONS_DATA = {json.dumps(questions_data, indent=4)}

def get_predefined_question_base(job_role: str, interview_type: str, difficulty: str = "Medium", question_number: int = 1) -> dict:
    idx = (question_number - 1) % 20
    
    role_data = QUESTIONS_DATA.get(job_role)
    if role_data:
        type_data = role_data.get(interview_type)
        if type_data:
            level_questions = type_data.get(difficulty)
            if level_questions and len(level_questions) > idx:
                return level_questions[idx]
                
    # Extreme fallback if role not found
    q_type = "mcq" if question_number in [1, 3, 6, 8, 11, 13, 16, 18] else ("fib" if question_number in [2, 4, 7, 9, 12, 14, 17, 19] else "descriptive")
    return {{
        "question_number": question_number,
        "question": f"Fallback question {{question_number}} for {{job_role}} {{interview_type}} {{difficulty}}.",
        "type": q_type,
        "options": ["A", "B", "C", "D"] if q_type == "mcq" else [],
        "correct_answer": "A" if q_type == "mcq" else "term"
    }}

def seed_questions(db_instance):
    questions_collection = db_instance["questions"]
    
    # Drop existing collections to replace
    questions_collection.delete_many({{}})
    
    print("Seeding predefined questions database collection...")
    all_questions = []
    
    roles = {list(ROLES)}
    types = {list(TYPES)}
    difficulties = {list(DIFFICULTIES)}
    
    for role in roles:
        for itype in types:
            for diff in difficulties:
                for qnum in range(1, 21):
                    base_q_obj = get_predefined_question_base(role, itype, diff, qnum)
                    
                    all_questions.append({{
                        "job_role": role,
                        "interview_type": itype,
                        "difficulty": diff,
                        "question_number": qnum,
                        "question": base_q_obj["question"],
                        "type": base_q_obj["type"],
                        "options": base_q_obj.get("options", []),
                        "correct_answer": base_q_obj["correct_answer"]
                    }})
                    
    questions_collection.insert_many(all_questions)
    print(f"Successfully seeded {{len(all_questions)}} questions into the 'questions' collection.")
"""

    output_path = os.path.join(os.path.dirname(__file__), "questions_bank.py")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(file_content)
    print(f"Successfully wrote 1,080 questions to {output_path}")

if __name__ == "__main__":
    main()
