import pymongo
from app.config import settings

client = pymongo.MongoClient(settings.MONGODB_URI)
db = client[settings.DATABASE_NAME]

# Collections
users_collection = db["users"]
interviews_collection = db["interviews"]
questions_answers_collection = db["questions_answers"]
results_collection = db["results"]
questions_collection = db["questions"]

# Setup Indexes
def init_db():
    try:
        # Create unique index on email
        users_collection.create_index("email", unique=True)
        print("MongoDB initialized and indexes created successfully.")
        
        # Seed questions bank once
        from app.questions_bank import seed_questions
        seed_questions(db)
    except Exception as e:
        print(f"Error initializing MongoDB: {e}")
