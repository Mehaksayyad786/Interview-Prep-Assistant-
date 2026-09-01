# Predefined Questions Bank for MockAI (Auto-Generated)
# Contains 20 distinct questions for each combination of role, type, and difficulty.
# Total Questions: 1,080

QUESTIONS_DATA = {
    "Python Developer": {
        "Technical": {
            "Easy": [
                {
                    "question_number": 1,
                    "question": "Which of the following data types is immutable in Python?",
                    "type": "mcq",
                    "options": [
                        "A) List",
                        "B) Dictionary",
                        "C) Tuple",
                        "D) Set"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 2,
                    "question": "To define a function in Python, the keyword ________ is used.",
                    "type": "fib",
                    "correct_answer": "def"
                },
                {
                    "question_number": 3,
                    "question": "What is the output of the expression `3 * 10 ** 3` in Python?",
                    "type": "mcq",
                    "options": [
                        "A) 3000",
                        "B) 9000",
                        "C) 30",
                        "D) 333"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 4,
                    "question": "In Git, the command used to download a repository from a remote origin is ________.",
                    "type": "fib",
                    "correct_answer": "git clone"
                },
                {
                    "question_number": 5,
                    "question": "Explain the difference between a list and a tuple in Python.",
                    "type": "descriptive",
                    "correct_answer": "Lists are mutable sequences, defined with square brackets [], while tuples are immutable sequences, defined with parentheses (). Lists are generally used for homogeneous data collections that need modification, whereas tuples are used for heterogeneous data where immutability is desired."
                },
                {
                    "question_number": 6,
                    "question": "Which built-in Python function is used to get the length of a string or list?",
                    "type": "mcq",
                    "options": [
                        "A) size()",
                        "B) length()",
                        "C) len()",
                        "D) count()"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 7,
                    "question": "In Django, the file where project-level URL patterns are defined is named ________.py.",
                    "type": "fib",
                    "correct_answer": "urls"
                },
                {
                    "question_number": 8,
                    "question": "How do you start a basic Flask development server in a script?",
                    "type": "mcq",
                    "options": [
                        "A) app.run()",
                        "B) flask.start()",
                        "C) app.serve()",
                        "D) server.run()"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 9,
                    "question": "In pytest, test functions must start with the prefix ________.",
                    "type": "fib",
                    "correct_answer": "test_"
                },
                {
                    "question_number": 10,
                    "question": "What is a virtual environment in Python and why is it used?",
                    "type": "descriptive",
                    "correct_answer": "A virtual environment is a self-contained directory that houses a specific Python installation and its own set of packages. It is used to manage dependencies for different projects independently and avoid version conflicts on the host system."
                },
                {
                    "question_number": 11,
                    "question": "Which SQL statement is used to retrieve data from a database?",
                    "type": "mcq",
                    "options": [
                        "A) GET",
                        "B) SELECT",
                        "C) EXTRACT",
                        "D) FETCH"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "To create a Docker container from an image, the command `docker ________` is used.",
                    "type": "fib",
                    "correct_answer": "run"
                },
                {
                    "question_number": 13,
                    "question": "Which operator is used for identity comparison, checking if two variables point to the exact same object in memory?",
                    "type": "mcq",
                    "options": [
                        "A) ==",
                        "B) equals",
                        "C) is",
                        "D) ==="
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 14,
                    "question": "In Python, exceptions are caught using the `try` and ________ blocks.",
                    "type": "fib",
                    "correct_answer": "except"
                },
                {
                    "question_number": 15,
                    "question": "Describe what a decorator is in Python at a high level.",
                    "type": "descriptive",
                    "correct_answer": "A decorator is a design pattern in Python that allows a user to add new functionality to an existing object (usually a function or method) without modifying its structure. It takes a function as input, extends its behavior, and returns a new function."
                },
                {
                    "question_number": 16,
                    "question": "Which method is commonly used to add an item to the end of a list?",
                    "type": "mcq",
                    "options": [
                        "A) add()",
                        "B) append()",
                        "C) insert()",
                        "D) push()"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "The built-in function used to read input from the user in the console is ________.",
                    "type": "fib",
                    "correct_answer": "input"
                },
                {
                    "question_number": 18,
                    "question": "What keyword is used to handle multiple conditions in a conditional statement after an initial 'if'?",
                    "type": "mcq",
                    "options": [
                        "A) elseif",
                        "B) elsif",
                        "C) elif",
                        "D) else if"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 19,
                    "question": "In SQLAlchemy, the base class used to declare mapped classes is created via `declarative_________()`.",
                    "type": "fib",
                    "correct_answer": "base"
                },
                {
                    "question_number": 20,
                    "question": "Explain the purpose of the `__init__` method in Python classes.",
                    "type": "descriptive",
                    "correct_answer": "The `__init__` method is a constructor method in Python classes. It is automatically called when an instance of a class is created and is used to initialize the object's attributes with passed arguments."
                }
            ],
            "Medium": [
                {
                    "question_number": 1,
                    "question": "What is the primary purpose of the Global Interpreter Lock (GIL) in CPython?",
                    "type": "mcq",
                    "options": [
                        "A) To manage memory allocation and garbage collection.",
                        "B) To prevent multiple native threads from executing Python bytecodes at once.",
                        "C) To optimize multi-core CPU usage for compute-heavy tasks.",
                        "D) To enforce strict type checking across modules."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "Functions that yield values one at a time using the `yield` keyword are known as ________.",
                    "type": "fib",
                    "correct_answer": "generators"
                },
                {
                    "question_number": 3,
                    "question": "In FastAPI, how do you declare a query parameter that has a default value and validation rules?",
                    "type": "mcq",
                    "options": [
                        "A) Using Query(...) from fastapi",
                        "B) Using Field(...) from pydantic",
                        "C) Using Param(...) from typing",
                        "D) Using Arg(...) from fastapi"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 4,
                    "question": "In Django ORM, to optimize queries involving ForeignKeys and avoid the N+1 query problem, the ________ method is used.",
                    "type": "fib",
                    "correct_answer": "select_related"
                },
                {
                    "question_number": 5,
                    "question": "Explain how context managers work in Python and name the two magic methods required to implement a custom context manager.",
                    "type": "descriptive",
                    "correct_answer": "Context managers allow setup and teardown actions to be cleanly executed around a block of code using the `with` statement. The two magic methods required are `__enter__` (which sets up the context and returns the resource) and `__exit__` (which handles cleanup, exception handling, and resource teardown)."
                },
                {
                    "question_number": 6,
                    "question": "What is the main difference between multithreading and multiprocessing in Python?",
                    "type": "mcq",
                    "options": [
                        "A) Multithreading uses separate processes, while multiprocessing uses threads within a single process.",
                        "B) Multiprocessing bypasses the GIL by using separate memory spaces and processes, whereas multithreading shares memory and is bound by the GIL.",
                        "C) Multithreading is faster for CPU-bound tasks, while multiprocessing is only for I/O tasks.",
                        "D) There is no functional difference; they are interchangeable aliases."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "To mock an external API call or object in pytest, the `unittest.________` module is commonly used.",
                    "type": "fib",
                    "correct_answer": "mock"
                },
                {
                    "question_number": 8,
                    "question": "Which of the following best describes the role of Celery in a Python architecture?",
                    "type": "mcq",
                    "options": [
                        "A) An ORM for managing NoSQL databases.",
                        "B) A distributed task queue that handles asynchronous background jobs.",
                        "C) An ASGI web server similar to Uvicorn.",
                        "D) A testing framework for concurrent code."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "In an asynchronous Python function (`async def`), code pauses execution until an awaitable completes using the `________` keyword.",
                    "type": "fib",
                    "correct_answer": "await"
                },
                {
                    "question_number": 10,
                    "question": "Describe how database migrations work in SQLAlchemy (typically via Alembic) and why they are important.",
                    "type": "descriptive",
                    "correct_answer": "Database migrations track changes to the database schema over time. Tools like Alembic compare the current SQLAlchemy model definitions against the existing database state and auto-generate migration scripts containing upgrade and downgrade paths. They are important for safely deploying schema updates across different environments (development, staging, production) without losing data."
                },
                {
                    "question_number": 11,
                    "question": "What does the method resolution order (MRO) determine in Python?",
                    "type": "mcq",
                    "options": [
                        "A) The order in which exception handlers are evaluated.",
                        "B) The order in which base classes are searched when looking for a method or attribute in multiple inheritance.",
                        "C) The order in which decorators are applied to a function.",
                        "D) The memory allocation priority for objects."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "In Docker, the file used to define multi-container Docker applications is named `docker-compose.________`.",
                    "type": "fib",
                    "correct_answer": "yml"
                },
                {
                    "question_number": 13,
                    "question": "Which of the following describes a RESTful API best practice for resource naming?",
                    "type": "mcq",
                    "options": [
                        "A) Use verbs for endpoints, such as `/getUserData`.",
                        "B) Use plural nouns for resource collections, such as `/users`.",
                        "C) Mix uppercase and lowercase letters freely.",
                        "D) Always include the database table name as a prefix."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "In Git, to discard local changes in a tracked file, you can use `git checkout --` or `git ________`.",
                    "type": "fib",
                    "correct_answer": "restore"
                },
                {
                    "question_number": 15,
                    "question": "Explain what Pydantic is and how it is used in modern Python web frameworks like FastAPI.",
                    "type": "descriptive",
                    "correct_answer": "Pydantic is a data validation and settings management library using Python type annotations. It enforces type constraints at runtime, serializes models to JSON or dicts, and provides clear validation errors. FastAPI uses Pydantic models to validate incoming request bodies, query parameters, and serialize response data automatically."
                },
                {
                    "question_number": 16,
                    "question": "What is the primary purpose of SQLAlchemy Session in an application?",
                    "type": "mcq",
                    "options": [
                        "A) To manage HTTP user sessions in a web app.",
                        "B) To act as a workspace/unit of work for model objects, tracking changes and managing database transactions.",
                        "C) To create database tables automatically on startup.",
                        "D) To handle connection pooling exclusively."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "In pytest, fixtures can specify their lifecycle scope. A fixture that runs once per test session uses `scope=________`.",
                    "type": "fib",
                    "correct_answer": "session"
                },
                {
                    "question_number": 18,
                    "question": "Which of the following is true regarding Python's garbage collection?",
                    "type": "mcq",
                    "options": [
                        "A) Python relies solely on manual memory management (`free()`).",
                        "B) Python uses reference counting primarily, supplemented by a cyclic garbage collector to detect reference cycles.",
                        "C) Garbage collection runs only when the program terminates.",
                        "D) Memory is never reclaimed until the OS reboots."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "To specify type hints for optional values that could be None in Python 3.10+, you can use the pipe operator (`| ________`).",
                    "type": "fib",
                    "correct_answer": "None"
                },
                {
                    "question_number": 20,
                    "question": "Describe the concept of dependency injection in the context of FastAPI.",
                    "type": "descriptive",
                    "correct_answer": "Dependency injection is a design pattern where a system's components are provided with their dependencies rather than creating them internally. In FastAPI, dependency injection is implemented using `Depends()`. It allows clean code reuse for tasks like database sessions, authentication, and request validation by injecting dependencies into path operation functions."
                }
            ],
            "Hard": [
                {
                    "question_number": 1,
                    "question": "How does CPython handle memory fragmentation and allocation for small objects, and what mechanism does it use internally?",
                    "type": "mcq",
                    "options": [
                        "A) It delegates all memory allocations directly to the OS `malloc` without caching.",
                        "B) It uses a specialized memory allocator called pymalloc, which manages arenas, pools, and blocks for small objects to reduce overhead and fragmentation.",
                        "C) It uses a compacting mark-and-compact garbage collector that moves object memory addresses constantly.",
                        "D) It stores all objects in a contiguous statically allocated array."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "In Python metaclasses, the method responsible for creating a new class instance (the class itself) is `____________`.",
                    "type": "fib",
                    "correct_answer": "new"
                },
                {
                    "question_number": 3,
                    "question": "When working with SQLAlchemy and async drivers (like `asyncpg`), how must database sessions be managed to prevent blocking the event loop?",
                    "type": "mcq",
                    "options": [
                        "A) Use standard synchronous sessions inside `run_in_executor`.",
                        "B) Use `AsyncSession` with an async engine and `await` database operations.",
                        "C) Disable connection pooling entirely.",
                        "D) Use threading.Thread for every query."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "In Python's `asyncio`, an object that represents the result of an asynchronous operation and can be awaited is called a ________.",
                    "type": "fib",
                    "correct_answer": "future"
                },
                {
                    "question_number": 5,
                    "question": "Explain how reference cycles are detected and collected by Python's cyclic garbage collector, and explain the generation-based threshold mechanism.",
                    "type": "descriptive",
                    "correct_answer": "Python's cyclic GC handles reference cycles (objects referencing each other, preventing ref count from hitting zero). It maintains doubly linked lists of container objects across three generations (0, 1, 2). Generation 0 is checked most frequently. When allocations minus deallocations exceed a threshold, a collection run identifies objects with reference counts equal to their internal container references, isolates them, and sweeps them. Surviving objects are promoted to older generations."
                },
                {
                    "question_number": 6,
                    "question": "What is the primary behavior of Python descriptors (implementing `__get__`, `__set__`, or `__delete__`), and what distinguishes data descriptors from non-data descriptors?",
                    "type": "mcq",
                    "options": [
                        "A) Data descriptors implement `__set__` or `__delete__` and take precedence over instance dictionaries; non-data descriptors only implement `__get__` and can be shadowed by instance attributes.",
                        "B) Non-data descriptors are thread-safe, while data descriptors are not.",
                        "C) Data descriptors are only used in Django models, while non-data descriptors are used in FastAPI.",
                        "D) There is no distinction; all descriptors behave identically."
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 7,
                    "question": "In Celery, when tasks need to be executed after a specific delay or at a specific ETA, the method used is `task.apply_________()`.",
                    "type": "fib",
                    "correct_answer": "async"
                },
                {
                    "question_number": 8,
                    "question": "How does `__slots__` optimize memory usage in a Python class?",
                    "type": "mcq",
                    "options": [
                        "A) By compressing all string attributes into byte arrays.",
                        "B) By preventing the creation of an instance `__dict__` and allocating a fixed-size array for attributes.",
                        "C) By enabling multithreading support for class attributes.",
                        "D) By caching method return values automatically."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "In a distributed Python microservices setup, circuit breaking patterns are often implemented using libraries like ________ to prevent cascade failures.",
                    "type": "fib",
                    "correct_answer": "pybreaker"
                },
                {
                    "question_number": 10,
                    "question": "Design a resilient worker architecture using Celery and Redis. Explain how you would handle task retries, dead-letter queues, and idempotency.",
                    "type": "descriptive",
                    "correct_answer": "A resilient architecture configures Celery with Redis as the broker and result backend. Task retries are handled via `self.retry(exc=..., countdown=...)` with exponential backoff and jitter to prevent thundering herd. Dead-letter queues are implemented by routing persistently failing tasks to a separate failure queue after max retries are exhausted. Idempotency is crucial: workers must ensure tasks can be executed multiple times safely (e.g., using unique transaction IDs, upsert logic, or distributed locks in Redis) without causing duplicate side effects."
                },
                {
                    "question_number": 11,
                    "question": "What is the difference between `asyncio.gather()` and `asyncio.as_completed()` when running concurrent tasks?",
                    "type": "mcq",
                    "options": [
                        "A) `gather` runs tasks sequentially, while `as_completed` runs them concurrently.",
                        "B) `gather` returns results as a list in the order of input once all tasks finish, whereas `as_completed` returns an iterator yielding futures as they complete.",
                        "C) `gather` is for multithreading, while `as_completed` is for multiprocessing.",
                        "D) There is no functional difference."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "In Python abstract base classes (ABCs), methods can be forced to be implemented in subclasses using the `@abstract________` decorator.",
                    "type": "fib",
                    "correct_answer": "method"
                },
                {
                    "question_number": 13,
                    "question": "What is the key mechanism behind monkey patching in Python, and why is it often considered a dangerous practice?",
                    "type": "mcq",
                    "options": [
                        "A) It modifies bytecode compiled files on disk, which can corrupt the operating system.",
                        "B) It dynamically alters classes or modules at runtime, which can lead to unpredictable behavior, hidden side effects, and hard-to-debug maintenance issues.",
                        "C) It encrypts source code to prevent reverse engineering.",
                        "D) It forces the interpreter to ignore the GIL entirely."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "When profiling Python memory leaks, tools like `tracemalloc` or `________` can be used to trace object allocations back to their source lines.",
                    "type": "fib",
                    "correct_answer": "objgraph"
                },
                {
                    "question_number": 15,
                    "question": "Describe how you would design a custom caching decorator in Python that supports time-to-live (TTL) expiration and thread-safe operations.",
                    "type": "descriptive",
                    "correct_answer": "A robust TTL caching decorator would maintain an internal dictionary storing cached results along with their expiration timestamps (`time.time() + ttl`). To ensure thread safety across multiple threads, access to the cache dictionary must be synchronized using a `threading.Lock`. The wrapper function checks if the key exists and has not expired; if valid, it returns the cached value, otherwise it computes the result, updates the cache (with eviction policies if size is capped), and returns it."
                },
                {
                    "question_number": 16,
                    "question": "What happens under the hood when a Python generator function encounters a `yield from` expression?",
                    "type": "mcq",
                    "options": [
                        "A) It delegates part of its operations to a sub-generator, establishing a transparent bi-directional channel for values and exceptions between the caller and the sub-generator.",
                        "B) It exits the generator immediately and returns a list.",
                        "C) It spawns a separate OS thread to evaluate the sub-generator.",
                        "D) It converts the generator into an asynchronous coroutine."
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 17,
                    "question": "In advanced database indexing with PostgreSQL and SQLAlchemy, a B-tree index can be complemented by GiST or ________ indexes for JSON or spatial data.",
                    "type": "fib",
                    "correct_answer": "gin"
                },
                {
                    "question_number": 18,
                    "question": "Which of the following describes the execution model of Python's `asyncio` event loop?",
                    "type": "mcq",
                    "options": [
                        "A) Preemptive multitasking using OS kernel thread interrupts.",
                        "B) Cooperative multitasking where tasks explicitly yield control using `await`, running on a single thread.",
                        "C) Distributed computing across multiple network nodes.",
                        "D) Hardware-level parallel instruction execution."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "In pytest, to parameterize test functions with multiple input data sets, the decorator `@pytest.mark.________` is used.",
                    "type": "fib",
                    "correct_answer": "parametrize"
                },
                {
                    "question_number": 20,
                    "question": "Discuss the architectural challenges of scaling a monolithic Django or Flask application to a microservices architecture, and how database transactions spanning multiple services are typically handled (e.g., Saga pattern).",
                    "type": "descriptive",
                    "correct_answer": "Scaling a monolith to microservices introduces challenges such as distributed data management, network latency, service discovery, and complex debugging. In a monolith, ACID transactions span multiple tables easily via the ORM. In microservices with database-per-service, traditional ACID transactions across services are impractical. The Saga pattern is commonly used to manage distributed transactions as a sequence of local transactions, where each step updates data within a service and publishes events or messages, triggering the next step, along with compensating transactions to handle rollbacks if a step fails."
                }
            ]
        },
        "HR": {
            "Easy": [
                {
                    "question_number": 1,
                    "question": "You discover a minor bug in your Python code just 10 minutes before the daily standup meeting. What is the most professional initial response?",
                    "type": "mcq",
                    "options": [
                        "Hide the issue and fix it quietly without telling anyone.",
                        "Mention the bug during standup, present a proposed fix, and update your estimated completion time.",
                        "Blame the bug on unclear requirements from the product manager.",
                        "Ignore the bug since it is minor and push the code to production anyway."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "Proactively asking a senior developer for guidance after spending more than two hours stuck on a complex Python module demonstrates good time ________.",
                    "type": "fib",
                    "correct_answer": "management"
                },
                {
                    "question_number": 3,
                    "question": "A senior engineer leaves critical feedback on your Django pull request asking you to rewrite a view using class-based views. How should you react?",
                    "type": "mcq",
                    "options": [
                        "Take it personally and argue that your initial solution works fine.",
                        "Ignore the comments and merge the pull request without changes.",
                        "Review the feedback objectively, ask clarifying questions if needed, and update the pull request to follow team standards.",
                        "Complain to the HR team about harsh code review practices."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 4,
                    "question": "Adhering to community standards like PEP 8 when writing Python code shows respect for code ________ and maintainability.",
                    "type": "fib",
                    "correct_answer": "readability"
                },
                {
                    "question_number": 5,
                    "question": "Describe a scenario where you had to quickly learn a new Python library or framework (e.g., Pandas, FastAPI, or Celery) to complete a project task. How did you approach the learning process?",
                    "type": "descriptive",
                    "correct_answer": "Key traits: Proactive learning strategy, resourcefulness, effective time allocation, practical application of new technical concepts, and seeking peer feedback."
                },
                {
                    "question_number": 6,
                    "question": "You are assigned a task involving a third-party Python SDK you have never used before. What is the best initial step?",
                    "type": "mcq",
                    "options": [
                        "Ask a teammate to write the code for you.",
                        "Read the official documentation, experiment with simple test scripts, and plan your implementation.",
                        "Inform your manager that you cannot complete the task because you lack experience with the SDK.",
                        "Copy random snippets from online forums directly into production."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "Taking immediate ownership when your Python script accidentally breaks a shared development environment reflects personal ________.",
                    "type": "fib",
                    "correct_answer": "accountability"
                },
                {
                    "question_number": 8,
                    "question": "A non-technical project manager asks how your Python script automates a manual data entry process. How should you explain it?",
                    "type": "mcq",
                    "options": [
                        "Use complex technical terms like list comprehensions, decorators, and GIL to sound knowledgeable.",
                        "Explain high-level concepts using simple analogies without getting bogged down in low-level code mechanics.",
                        "Tell them that technical details are too complex for non-developers to understand.",
                        "Send them the raw Python source code file and tell them to read the comments."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "Consistently writing unit tests using tools like `unittest` or `pytest` helps maintain overall software ________.",
                    "type": "fib",
                    "correct_answer": "quality"
                },
                {
                    "question_number": 10,
                    "question": "Describe a time when you made a mistake in your Python code that caused an error in the staging environment. How did you handle it and what did you learn?",
                    "type": "descriptive",
                    "correct_answer": "Key traits: Honesty, accountability, quick root-cause analysis, effective communication under pressure, and implementing preventive measures."
                },
                {
                    "question_number": 11,
                    "question": "Two senior developers give you conflicting suggestions on how to structure a Python script during a pull request review. What should you do?",
                    "type": "mcq",
                    "options": [
                        "Pick the solution that takes the least effort without telling either developer.",
                        "Respectfully bring both developers together in a brief discussion or thread to reach a clear consensus.",
                        "Implement both suggestions in different parts of the script to appease both.",
                        "Ignore both comments and ask a third developer to approve the pull request."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "Participating constructively during sprint planning by providing realistic task estimates requires honest ________.",
                    "type": "fib",
                    "correct_answer": "communication"
                },
                {
                    "question_number": 13,
                    "question": "You finish your assigned Python development tasks two days before the end of the sprint. What is the best action to take?",
                    "type": "mcq",
                    "options": [
                        "Take a break and stay idle until the next sprint begins.",
                        "Inform your team lead, offer help to peers, or pick up technical debt/backlog items.",
                        "Start refactoring random parts of the codebase without consulting the team.",
                        "Keep your completion secret so team expectations stay low for future sprints."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "Being open to revising your Python code structure based on constructive review comments demonstrates cognitive ________.",
                    "type": "fib",
                    "correct_answer": "flexibility"
                },
                {
                    "question_number": 15,
                    "question": "Describe how you prioritize your daily workload when you have multiple bug fixes and feature requests assigned in Python.",
                    "type": "descriptive",
                    "correct_answer": "Key traits: Task prioritization criteria (severity/impact), time management, stakeholder communication, and balance between short-term fixes and long-term goals."
                },
                {
                    "question_number": 16,
                    "question": "You notice that a Python dependency your feature relies on has a known open-source security advisory. What is your immediate action?",
                    "type": "mcq",
                    "options": [
                        "Ignore it if your code runs fine without crashing.",
                        "Notify the team, assess the vulnerability impact, and look for an updated version or alternative library.",
                        "Delete the library and rewrite the entire functionality from scratch without informing anyone.",
                        "Wait until security audit tools fail in production."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "Sharing progress updates regularly on complex Python integration tasks builds team ________.",
                    "type": "fib",
                    "correct_answer": "trust"
                },
                {
                    "question_number": 18,
                    "question": "You are struggling to understand legacy Python code written by a former developer. How do you handle this issue?",
                    "type": "mcq",
                    "options": [
                        "Complain about the quality of the legacy code during team meetings.",
                        "Step through the code using debugging tools, read available docs, and draft documentation as you figure it out.",
                        "Demand that the management assign you a completely new codebase.",
                        "Rewrite the entire legacy script without verifying its edge cases."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "Showing enthusiasm to learn core Python concepts like async IO or type hinting reflects a continuous growth ________.",
                    "type": "fib",
                    "correct_answer": "mindset"
                },
                {
                    "question_number": 20,
                    "question": "Describe a situation where you had to balance writing clean, readable Python code with meeting an urgent deadline.",
                    "type": "descriptive",
                    "correct_answer": "Key traits: Pragmatic trade-offs, code quality commitment, post-deadline cleanup plan, clear communication, and risk management."
                }
            ],
            "Medium": [
                {
                    "question_number": 1,
                    "question": "You realize that refactoring a legacy Python service will improve performance by 40%, but product management wants new business features released first. How do you resolve this?",
                    "type": "mcq",
                    "options": [
                        "Refactor the code secretly while working on the features, risking deadline delays.",
                        "Present metrics and a business case to product management, proposing an incremental refactoring plan alongside feature delivery.",
                        "Concede completely and abandon technical debt improvements indefinitely.",
                        "Refuse to work on new features until refactoring is prioritized."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "Providing clear, actionable feedback during pull request reviews for junior Python developers fosters team ________.",
                    "type": "fib",
                    "correct_answer": "growth"
                },
                {
                    "question_number": 3,
                    "question": "A high-traffic Python Web API experiences a memory leak during peak hours. As a mid-level engineer leading the investigation, what is your initial step?",
                    "type": "mcq",
                    "options": [
                        "Restart the production servers periodically without investigating the cause.",
                        "Blame the infrastructure team for under-provisioning RAM.",
                        "Analyze memory profiling data, identify leaking objects/tasks, communicate status to stakeholders, and deploy a targeted fix.",
                        "Rewrite the service in another language immediately."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 4,
                    "question": "Aligning data models between a Python backend service and a frontend framework requires effective cross-functional ________.",
                    "type": "fib",
                    "correct_answer": "collaboration"
                },
                {
                    "question_number": 5,
                    "question": "Describe a time when you mentored a junior Python developer. How did you identify their areas for improvement and guide their growth?",
                    "type": "descriptive",
                    "correct_answer": "Key traits: Empathy, active listening, structured mentoring techniques, constructive feedback, patience, and encouraging self-reliance."
                },
                {
                    "question_number": 6,
                    "question": "A product owner requests an urgent scope change mid-sprint that requires restructuring your team's Python database models. What should you do?",
                    "type": "mcq",
                    "options": [
                        "Accept the request immediately without assessing technical impact on current sprint goals.",
                        "Evaluate the architectural impact, communicate risks and effort estimates to the product owner, and negotiate trade-offs.",
                        "Reject the request rudely, citing strict adherence to Agile rules.",
                        "Implement the change quickly by bypassing code reviews and automated tests."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "Balancing urgent Python hotfixes with planned project deliverables requires effective work ________.",
                    "type": "fib",
                    "correct_answer": "prioritization"
                },
                {
                    "question_number": 8,
                    "question": "A junior engineer repeatedly submits Python code with missing unit tests and poor exception handling. How should you address this issue?",
                    "type": "mcq",
                    "options": [
                        "Reject all their pull requests without explaining why.",
                        "Schedule a 1-on-1 session to discuss testing expectations, demonstrate proper test patterns, and establish standard guidelines.",
                        "Write the tests for them every time to save time.",
                        "Report their incompetence to the engineering manager immediately."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "Taking ownership of a production bug caused by an edge case in your Python service demonstrates high professional ________.",
                    "type": "fib",
                    "correct_answer": "integrity"
                },
                {
                    "question_number": 10,
                    "question": "Tell me about a technical disagreement you had with another developer regarding Python architecture (e.g., synchronous vs asynchronous paradigms). How did you reach a resolution?",
                    "type": "descriptive",
                    "correct_answer": "Key traits: Data-driven decision making, respectful debate, active listening, willingness to compromise, and prioritizing technical fit over personal preference."
                },
                {
                    "question_number": 11,
                    "question": "Your team is experiencing frequent merge conflicts due to long-lived Python feature branches. What solution do you propose?",
                    "type": "mcq",
                    "options": [
                        "Tell developers to stop working on overlapping files.",
                        "Advocate for trunk-based development or smaller, more frequent pull requests with feature flags.",
                        "Assign single developers to manage all code merges manually.",
                        "Extend sprint lengths to give people more time to resolve conflicts."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "Establishing clear documentation for internal Python microservices enhances developer ________.",
                    "type": "fib",
                    "correct_answer": "onboarding"
                },
                {
                    "question_number": 13,
                    "question": "During a sprint, you discover that an third-party API your Python application relies on will be deprecated next month. How do you handle this?",
                    "type": "mcq",
                    "options": [
                        "Wait until the API officially shuts down before taking action.",
                        "Log the issue, assess the migration effort, raise it to product managers, and plan a transition strategy.",
                        "Monkey-patch the current library to keep it working indefinitely.",
                        "Blame the external vendor during daily standups."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "Explaining complex Python performance bottlenecks to business managers requires translation of technical issues into business ________.",
                    "type": "fib",
                    "correct_answer": "impact"
                },
                {
                    "question_number": 15,
                    "question": "Describe a situation where a production system broke due to an unforeseen Python issue. How did you manage the incident response and post-mortem process?",
                    "type": "descriptive",
                    "correct_answer": "Key traits: Calmness under pressure, systematic troubleshooting, clear communication during crises, blameless post-mortem execution, and preventive action planning."
                },
                {
                    "question_number": 16,
                    "question": "Your team is divided on whether to adopt a new Python framework. As a mid-level developer, how can you help facilitate a decision?",
                    "type": "mcq",
                    "options": [
                        "Push for your favorite framework without testing alternative solutions.",
                        "Build a small proof-of-concept using competing options, evaluate performance and developer experience, and present facts to the team.",
                        "Let the team argue until the manager makes an arbitrary choice.",
                        "Implement the new framework in production without team consensus."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "Automating Python code formatting using CI tools like Black or Flake8 ensures team-wide code ________.",
                    "type": "fib",
                    "correct_answer": "consistency"
                },
                {
                    "question_number": 18,
                    "question": "The QA team reports that a Python worker process is randomly dropping jobs, but they cannot provide reliable reproduction steps. What is your approach?",
                    "type": "mcq",
                    "options": [
                        "Close the bug report as 'Cannot Reproduce' and ignore it.",
                        "Work collaboratively with QA, enhance logging and telemetry in the worker process, and monitor system behavior to catch the root cause.",
                        "Tell QA it is their job to figure out how to reproduce it before you look at it.",
                        "Rewrite the entire background worker code hoping the bug disappears."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "Showing resilience when dealing with shifting priorities across Python services demonstrates professional ________.",
                    "type": "fib",
                    "correct_answer": "adaptability"
                },
                {
                    "question_number": 20,
                    "question": "Describe a time when you had to optimize a slow SQL query execution within a Python ORM (like Django ORM or SQLAlchemy). How did you collaborate with stakeholders during this work?",
                    "type": "descriptive",
                    "correct_answer": "Key traits: Analytical approach, performance profiling, understanding database patterns (N+1 queries, indexing), cross-team collaboration, and benchmarking output."
                }
            ],
            "Hard": [
                {
                    "question_number": 1,
                    "question": "As a Python Lead, executive management asks you to cut automated unit and integration testing by 80% to meet an aggressive product deadline. How do you lead your team through this challenge?",
                    "type": "mcq",
                    "options": [
                        "Comply immediately and order the engineering team to stop writing tests.",
                        "Present data on long-term defect costs, negotiate a reduced feature scope instead, and advocate for core safety net testing.",
                        "Quietly instruct developers to write tests in secret, ignoring the deadline.",
                        "Resign publicly to make a statement about quality standards."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "Fostering an engineering culture where developers feel safe admitting production mistakes in Python applications builds psychological ________.",
                    "type": "fib",
                    "correct_answer": "safety"
                },
                {
                    "question_number": 3,
                    "question": "Two senior architects on your team are in a deadlock over migrating a legacy Python monolithic app to microservices vs modular monolith. How do you resolve this dispute?",
                    "type": "mcq",
                    "options": [
                        "Flip a coin to decide and force the team to follow.",
                        "Establish objective evaluation criteria aligned with business goals, review technical prototypes, and lead a structured decision matrix session.",
                        "Side with the senior engineer who has been at the company longest.",
                        "Delay the decision indefinitely until one architect backs down."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "Developing a multi-year technical roadmap for a company's Python software ecosystem requires strategic technical ________.",
                    "type": "fib",
                    "correct_answer": "vision"
                },
                {
                    "question_number": 5,
                    "question": "Describe a time when you led a major migration of a mission-critical Python system (e.g., Python 2 to 3 migration, or monolith to microservices). How did you manage technical risk and team alignment?",
                    "type": "descriptive",
                    "correct_answer": "Key traits: Strategic planning, risk mitigation, stakeholder management, change management leadership, cross-team coordination, and measurable outcomes."
                },
                {
                    "question_number": 6,
                    "question": "Your engineering team is experiencing severe burnout due to constant hotfixes and high technical debt in legacy Python services. What immediate leadership steps do you take?",
                    "type": "mcq",
                    "options": [
                        "Offer monetary bonuses and urge the team to work harder until the debt is cleared.",
                        "Halt non-essential feature development, dedicate sprint cycles to technical debt reduction, and review workload distributions.",
                        "Replace struggling developers with new hires.",
                        "Ignore the morale issue as long as release commitments are met."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "Guiding senior engineers through complex Python system architectural choices requires strong technical ________.",
                    "type": "fib",
                    "correct_answer": "leadership"
                },
                {
                    "question_number": 8,
                    "question": "A senior Python developer on your team consistently delivers high-quality code but exhibits toxic behavior toward junior developers during code reviews. How do you address this?",
                    "type": "mcq",
                    "options": [
                        "Ignore the behavior because their technical output is critical to the team.",
                        "Address the behavior directly in private 1-on-1s, set clear behavioral expectations, and tie soft skills to performance evaluations.",
                        "Publicly reprimand the senior developer in team meetings.",
                        "Reassign all junior developers so they don't interact with the senior developer."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "Securing buy-in from non-technical C-suite executives for expensive infrastructure upgrades to Python services demands business-aligned stakeholder ________.",
                    "type": "fib",
                    "correct_answer": "management"
                },
                {
                    "question_number": 10,
                    "question": "Describe a situation where an architectural decision you made for a Python application turned out to be wrong. How did you recognize it, pivot, and lead your team out of the situation?",
                    "type": "descriptive",
                    "correct_answer": "Key traits: Vulnerability, decisive leadership, quick course correction, data-driven reevaluation, transparent communication, and post-mortem learning culture."
                },
                {
                    "question_number": 11,
                    "question": "You need to decide whether to build a custom in-house Python task orchestration engine or license an existing enterprise solution. What is your framework for making this decision?",
                    "type": "mcq",
                    "options": [
                        "Always build in-house so your team maintains 100% control over code.",
                        "Conduct a comprehensive Total Cost of Ownership (TCO) and build-vs-buy analysis considering team capability, ongoing maintenance, and core business focus.",
                        "Always buy off-the-shelf software to avoid writing custom code.",
                        "Choose whatever technology is trending on social media."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "Establishing company-wide Python coding standards, security baselines, and review guidelines promotes engineering ________.",
                    "type": "fib",
                    "correct_answer": "excellence"
                },
                {
                    "question_number": 13,
                    "question": "Several development teams are creating duplicated Python utility packages across the company, leading to fragmented efforts. How do you resolve this at an enterprise level?",
                    "type": "mcq",
                    "options": [
                        "Forbid developers from creating utility libraries.",
                        "Form a inner-source guild, centralize common Python shared libraries, establish clear governance, and assign maintainers.",
                        "Force everyone to use one team's codebase without consultation.",
                        "Allow teams to continue duplicating work since autonomy is paramount."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "Mediating high-stakes technical disputes between senior Python leads requires diplomatic consensus ________.",
                    "type": "fib",
                    "correct_answer": "building"
                },
                {
                    "question_number": 15,
                    "question": "Describe your approach to building and scaling a high-performing Python engineering team, from recruitment and interviewing to career growth and retention.",
                    "type": "descriptive",
                    "correct_answer": "Key traits: Structured hiring practices, inclusive culture, career ladder definition, continuous mentoring, retention strategies, and empowering team autonomy."
                },
                {
                    "question_number": 16,
                    "question": "A major client threatens to cancel their contract unless a complex Python feature set is delivered in half the estimated time. How do you respond as an engineering lead?",
                    "type": "mcq",
                    "options": [
                        "Force the engineering team to work 80-hour work weeks to meet the deadline.",
                        "Collaborate with product and sales to define a phased rollout plan, prioritizing MVP requirements while maintaining system stability.",
                        "Promise everything immediately without consulting the engineering team.",
                        "Refuse the client request outright without offering alternative solutions."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "Encouraging team members to experiment with emerging Python tools like Pyodide or Mojo while maintaining core stability requires calculated risk ________.",
                    "type": "fib",
                    "correct_answer": "management"
                },
                {
                    "question_number": 18,
                    "question": "Key senior Python engineers are being actively poached by competitors offering significantly higher compensation. How do you handle retention and risk mitigation?",
                    "type": "mcq",
                    "options": [
                        "Ignore the issue and assume loyalty will keep them at the company.",
                        "Partner with HR/leadership to review compensation structures, foster growth opportunities, and ensure knowledge transfer to eliminate single points of failure.",
                        "Restrict developers from updating their LinkedIn profiles.",
                        "Match every external offer immediately regardless of internal equity."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "Building consistent technical standards across global, remote Python development teams requires intentional culture ________.",
                    "type": "fib",
                    "correct_answer": "building"
                },
                {
                    "question_number": 20,
                    "question": "Describe a scenario where you had to lead your Python team through an organizational restructuring or major strategic shift. How did you maintain productivity and team trust?",
                    "type": "descriptive",
                    "correct_answer": "Key traits: Transparent leadership, empathetic communication, change management, maintaining team focus, psychological support, and strategic realignment."
                }
            ]
        },
        "Behavioral": {
            "Easy": [
                {
                    "question_number": 1,
                    "question": "When you are stuck on a basic Python syntax error and cannot find the solution immediately, what is the best first step?",
                    "type": "mcq",
                    "options": [
                        "A) Rewrite the entire module from scratch.",
                        "B) Read the traceback message carefully and search for similar issues on Stack Overflow or official documentation.",
                        "C) Immediately escalate the issue to the engineering director.",
                        "D) Ignore the error and comment out the failing line."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "The ability to work effectively and harmoniously in a group with other developers and stakeholders is known as _______.",
                    "type": "fib",
                    "correct_answer": "teamwork"
                },
                {
                    "question_number": 3,
                    "question": "You notice that a senior developer used a Python feature you are unfamiliar with during a code review. What should you do?",
                    "type": "mcq",
                    "options": [
                        "A) Ask them to revert the code because you don't understand it.",
                        "B) Quietly ignore it and hope it doesn't break anything.",
                        "C) Politely ask them to explain the feature or point you to relevant documentation so you can learn.",
                        "D) Reject the pull request without explanation."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 4,
                    "question": "Actively listening to others without interrupting and seeking to understand their perspective before responding is an essential part of effective _______.",
                    "type": "fib",
                    "correct_answer": "communication"
                },
                {
                    "question_number": 5,
                    "question": "Describe a time when you had to learn a new Python library or tool quickly for a small task. How did you approach the learning process?",
                    "type": "descriptive",
                    "correct_answer": "Look for resourcefulness, willingness to learn, reading official documentation, and practical application."
                },
                {
                    "question_number": 6,
                    "question": "You are given a bug-fixing task in a Python script that you did not write. How should you approach understanding the code?",
                    "type": "mcq",
                    "options": [
                        "A) Delete the script and write your own version.",
                        "B) Run tests, read existing comments, check version control history, and add print/debug statements to trace execution.",
                        "C) Guess what the bug is and change random variables.",
                        "D) Refuse the task because you didn't write the original code."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "The personal quality of being honest and having strong moral principles, especially regarding code quality and testing, is called _______.",
                    "type": "fib",
                    "correct_answer": "integrity"
                },
                {
                    "question_number": 8,
                    "question": "During a daily standup, you realize you will not finish your assigned Python bug fix by the end of the day. What is the most professional action?",
                    "type": "mcq",
                    "options": [
                        "A) Say nothing and hope nobody notices during the sprint.",
                        "B) Blame your computer setup for the delay.",
                        "C) Inform the team during standup, explain the roadblock, and ask for guidance if needed.",
                        "D) Leave work early so you don't have to report it."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 9,
                    "question": "The capability to adjust to new conditions, such as shifting project requirements or a new Python framework, is known as _______.",
                    "type": "fib",
                    "correct_answer": "adaptability"
                },
                {
                    "question_number": 10,
                    "question": "Describe a situation where you received constructive feedback on your code style (e.g., failing PEP 8 guidelines). How did you react?",
                    "type": "descriptive",
                    "correct_answer": "Look for openness to feedback, lack of defensiveness, and willingness to improve."
                },
                {
                    "question_number": 11,
                    "question": "A QA engineer reports a bug in your Python code, but you cannot reproduce it locally. What is your best response?",
                    "type": "mcq",
                    "options": [
                        "A) Mark the bug as 'Cannot Reproduce' and close it immediately.",
                        "B) Tell the QA engineer they must be using the software incorrectly.",
                        "C) Collaborate with the QA engineer to review their environment, input data, and exact steps to reproduce it.",
                        "D) Ignore the report until it happens to another user."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 12,
                    "question": "Maintaining steady progress and a positive attitude in the face of minor technical setbacks demonstrates emotional _______.",
                    "type": "fib",
                    "correct_answer": "resilience"
                },
                {
                    "question_number": 13,
                    "question": "You notice a typo in the documentation of an open-source Python library you are using. What is the most appropriate action?",
                    "type": "mcq",
                    "options": [
                        "A) Complain about it on social media.",
                        "B) Do nothing since it doesn't affect the code execution.",
                        "C) Submit a quick pull request or issue report to fix the typo.",
                        "D) Stop using the library entirely."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 14,
                    "question": "The ability to manage one's time and tasks efficiently to meet daily development goals is called _______ management.",
                    "type": "fib",
                    "correct_answer": "time"
                },
                {
                    "question_number": 15,
                    "question": "Tell me about a time when you had to balance university coursework or previous job duties with learning a new technical skill. How did you organize your time?",
                    "type": "descriptive",
                    "correct_answer": "Look for organization, prioritization, self-discipline, and effective time management."
                },
                {
                    "question_number": 16,
                    "question": "You finish your assigned Python task early in the sprint and have extra time. What should you do?",
                    "type": "mcq",
                    "options": [
                        "A) Take the rest of the week off without telling anyone.",
                        "B) Play video games at your desk.",
                        "C) Ask the team lead or peers if they need help with testing, documentation, or overflow tasks.",
                        "D) Start rewriting random parts of the codebase without approval."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 17,
                    "question": "Fulfilling promises and completing assigned coding tasks on schedule builds trust and reliability, also known as _______.",
                    "type": "fib",
                    "correct_answer": "accountability"
                },
                {
                    "question_number": 18,
                    "question": "How should you handle constructive criticism from a senior developer regarding your variable naming conventions?",
                    "type": "mcq",
                    "options": [
                        "A) Take it personally and argue that your names are creative.",
                        "B) Accept the feedback, learn the team's naming conventions, and update your code accordingly.",
                        "C) Refuse to change your code because Python allows any variable name.",
                        "D) Ask someone else to merge your code behind their back."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "The drive to continuously improve your Python programming skills and stay updated with industry trends is an example of a growth _______.",
                    "type": "fib",
                    "correct_answer": "mindset"
                },
                {
                    "question_number": 20,
                    "question": "Describe a time when you worked on a group project (coding or otherwise) where a team member was not pulling their weight. How did you handle it?",
                    "type": "descriptive",
                    "correct_answer": "Look for empathy, direct communication, collaborative problem-solving, and professionalism."
                }
            ],
            "Medium": [
                {
                    "question_number": 1,
                    "question": "You realize that a Python dependency your team is using has a newly discovered security vulnerability, but upgrading it might break existing features. What should you do?",
                    "type": "mcq",
                    "options": [
                        "A) Ignore the vulnerability since it probably won't affect your specific use case.",
                        "B) Upgrade immediately in production without testing to save time.",
                        "C) Assess the risk, create a branch to test the upgrade, run automated test suites, and discuss the migration plan with the team.",
                        "D) Delete the dependency and write your own implementation of the library."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 2,
                    "question": "When explaining complex technical concepts or Python architectural decisions to non-technical stakeholders, it is crucial to avoid technical jargon and focus on business _______.",
                    "type": "fib",
                    "correct_answer": "value"
                },
                {
                    "question_number": 3,
                    "question": "During a code review, you strongly disagree with a peer's approach to implementing a Python feature, believing it will cause performance issues later. How do you address this?",
                    "type": "mcq",
                    "options": [
                        "A) Approve the PR anyway to avoid conflict.",
                        "B) Leave a rude comment criticizing their programming skills.",
                        "C) Comment constructively with data, pointing out potential performance bottlenecks and suggesting a benchmarked alternative.",
                        "D) Complain to the manager without talking to your peer first."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 4,
                    "question": "The practice of reviewing other developers' Python code to catch bugs and share knowledge is known as peer code _______.",
                    "type": "fib",
                    "correct_answer": "review"
                },
                {
                    "question_number": 5,
                    "question": "Describe a time when a Python application or script you built suffered from unexpected performance degradation in production. How did you diagnose and resolve the bottleneck?",
                    "type": "descriptive",
                    "correct_answer": "Look for systematic troubleshooting, profiling tools usage (like cProfile or memory_profiler), root-cause analysis, and implementation of optimizations."
                },
                {
                    "question_number": 6,
                    "question": "You are tasked with refactoring a legacy Python monolith into microservices, but business stakeholders keep pushing for new feature delivery simultaneously. How do you handle this tension?",
                    "type": "mcq",
                    "options": [
                        "A) Stop working on features entirely and refactor in secret.",
                        "B) Give up on refactoring and keep adding features to the monolith.",
                        "C) Collaborate with product owners to balance tech debt reduction with feature delivery, proposing incremental refactoring.",
                        "D) Tell management that their business priorities are wrong."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 7,
                    "question": "The method of breaking down large Python development projects into manageable iterations is known as _______ project management.",
                    "type": "fib",
                    "correct_answer": "agile"
                },
                {
                    "question_number": 8,
                    "question": "A junior developer on your team is struggling to write unit tests for their Python asynchronous code. How do you approach mentoring them?",
                    "type": "mcq",
                    "options": [
                        "A) Tell them to figure it out themselves because testing is their job.",
                        "B) Write the tests for them without explaining anything.",
                        "C) Schedule a pair-programming session to walk through pytest-asyncio and explain the concepts patiently.",
                        "D) Tell your manager they are not qualified for the role."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 9,
                    "question": "When multiple team members have conflicting ideas on which Python framework (e.g., FastAPI vs. Django) to use, reaching a consensus requires open _______ and compromise.",
                    "type": "fib",
                    "correct_answer": "discussion"
                },
                {
                    "question_number": 10,
                    "question": "Describe a time when you had to manage conflicting priorities between delivering a feature quickly versus writing clean, maintainable Python code. How did you make your decision?",
                    "type": "descriptive",
                    "correct_answer": "Look for pragmatic balance, technical debt awareness, communication with stakeholders, and writing adequate tests."
                },
                {
                    "question_number": 11,
                    "question": "You inherit a critical Python service with zero test coverage, and management wants a new feature added immediately. What is your strategy?",
                    "type": "mcq",
                    "options": [
                        "A) Add the new feature directly without tests, accepting high risk.",
                        "B) Refuse to work on the project until 100% test coverage is achieved.",
                        "C) Write tests for the critical paths you plan to touch before implementing the new feature safely.",
                        "D) Rewrite the entire service in another language."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 12,
                    "question": "Proactively identifying potential risks in a Python software architecture before deployment is part of proactive risk _______.",
                    "type": "fib",
                    "correct_answer": "management"
                },
                {
                    "question_number": 13,
                    "question": "You notice that your team's CI/CD pipeline for Python builds is taking 45 minutes to run, causing severe friction in deployments. What is the best way to handle this?",
                    "type": "mcq",
                    "options": [
                        "A) Accept it as normal and deploy less frequently.",
                        "B) Disable tests in the pipeline to make it run faster.",
                        "C) Investigate bottlenecks, cache dependencies, run tests in parallel, and propose pipeline optimizations to the team.",
                        "D) Complain to HR about the DevOps engineer."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 14,
                    "question": "The quality of writing code that is clean, readable, and easily understood by other team members is referred to as code _______.",
                    "type": "fib",
                    "correct_answer": "maintainability"
                },
                {
                    "question_number": 15,
                    "question": "Tell me about a time when a critical production bug occurred due to an error in your Python code. How did you handle the incident and subsequent post-mortem?",
                    "type": "descriptive",
                    "correct_answer": "Look for accountability, calm incident response, root cause analysis, and implementing preventative measures (like tests)."
                },
                {
                    "question_number": 16,
                    "question": "A product manager requests a feature change late in the sprint that requires rewriting a core data processing pipeline in Python. How do you respond?",
                    "type": "mcq",
                    "options": [
                        "A) Say yes immediately and work 80 hours to get it done.",
                        "B) Say flatly 'No' and refuse to speak to them.",
                        "C) Evaluate the technical impact, explain the risks and timeline adjustments to the product manager, and negotiate scope.",
                        "D) Implement the change secretly without testing."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 17,
                    "question": "When working with distributed cross-functional teams, maintaining alignment requires clear documentation and asynchronous _______.",
                    "type": "fib",
                    "correct_answer": "communication"
                },
                {
                    "question_number": 18,
                    "question": "You are asked to evaluate a third-party Python package to replace an in-house module. What criteria should guide your evaluation?",
                    "type": "mcq",
                    "options": [
                        "A) Choose the one with the coolest logo.",
                        "B) Community support, maintenance activity, security history, licensing, and performance benchmarks.",
                        "C) Whatever package your friend recommended on Twitter.",
                        "D) The package with the longest name."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "The practice of sharing knowledge across the engineering team through tech talks or documentation is known as knowledge _______.",
                    "type": "fib",
                    "correct_answer": "sharing"
                },
                {
                    "question_number": 20,
                    "question": "Describe a project where you had to collaborate closely with QA engineers and Product Owners. How did you ensure everyone stayed aligned on acceptance criteria for Python features?",
                    "type": "descriptive",
                    "correct_answer": "Look for cross-functional collaboration, clear specification writing, proactive communication, and shared understanding."
                }
            ],
            "Hard": [
                {
                    "question_number": 1,
                    "question": "As a Lead Python Developer, you notice deep silos forming between your backend Python team and the frontend team, leading to integration failures. What strategic initiative do you implement?",
                    "type": "mcq",
                    "options": [
                        "A) Punish teams that fail API integrations.",
                        "B) Establish contract testing (e.g., Pact), shared API specifications (OpenAPI/Swagger), and cross-functional pairing sessions.",
                        "C) Merge both teams into one massive team with no defined roles.",
                        "D) Let them resolve it organically without intervention."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 2,
                    "question": "The strategic leadership quality of inspiring and guiding engineering teams toward a shared technical vision is known as technical _______.",
                    "type": "fib",
                    "correct_answer": "leadership"
                },
                {
                    "question_number": 3,
                    "question": "Your engineering organization is experiencing high turnover, and morale is low due to severe technical debt in a core Python monolith. As a senior leader, what is your first step?",
                    "type": "mcq",
                    "options": [
                        "A) Blame the previous engineering leadership.",
                        "B) Hire more junior developers to write new code quickly.",
                        "C) Conduct a tech debt audit, establish a dedicated refactoring allocation (e.g., 20% rule), and create a transparent roadmap with stakeholders.",
                        "D) Ignore the debt and demand faster feature delivery."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 4,
                    "question": "Strategic planning for long-term scalability and maintainability of software systems is referred to as software _______.",
                    "type": "fib",
                    "correct_answer": "architecture"
                },
                {
                    "question_number": 5,
                    "question": "Describe a time when you had to convince executive leadership to allocate significant budget and time for a major architectural overhaul (e.g., migrating a large Python codebase to asynchronous architecture or microservices). How did you frame the business case?",
                    "type": "descriptive",
                    "correct_answer": "Look for ROI focus, risk mitigation, translating tech debt into business impact, clear metrics, and stakeholder management."
                },
                {
                    "question_number": 6,
                    "question": "Two senior Python developers on your team have a toxic technical disagreement over architecture that is halting sprint progress. How do you resolve this?",
                    "type": "mcq",
                    "options": [
                        "A) Fire both developers immediately.",
                        "B) Choose one developer's side arbitrarily without listening.",
                        "C) Facilitate a structured architecture review meeting, evaluate trade-offs objectively against business goals, make a final decision as the lead, and secure alignment.",
                        "D) Tell them to fight it out in the parking lot."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 7,
                    "question": "The cultural and technical practice of bridging the gap between development and IT operations for rapid, reliable Python deployments is called _______.",
                    "type": "fib",
                    "correct_answer": "devops"
                },
                {
                    "question_number": 8,
                    "question": "You discover that a senior developer under your mentorship is consistently bypassing code reviews and merging risky Python code directly into main. How do you handle this performance and culture issue?",
                    "type": "mcq",
                    "options": [
                        "A) Revoke all their repository permissions without warning.",
                        "B) Have a private, empathetic 1-on-1 meeting to discuss the importance of governance, understand their bottlenecks, and set clear guardrails.",
                        "C) Publicly reprimand them in the team Slack channel.",
                        "D) Do nothing and let production break."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "The capability to foresee potential security vulnerabilities, scaling bottlenecks, and failure modes in complex Python distributed systems is called architectural _______.",
                    "type": "fib",
                    "correct_answer": "foresight"
                },
                {
                    "question_number": 10,
                    "question": "Describe a complex distributed system failure involving Python microservices under your watch. How did you lead the incident response, root cause analysis, and post-mortem culture?",
                    "type": "descriptive",
                    "correct_answer": "Look for blameless post-mortems, incident command structure, systemic fixes, and transparent communication with stakeholders."
                },
                {
                    "question_number": 11,
                    "question": "Your company is scaling rapidly, and the current Python monolith is hitting database connection limits. Management wants a quick band-aid, but you know it requires a complete data layer redesign. How do you navigate this?",
                    "type": "mcq",
                    "options": [
                        "A) Implement a quick connection pool hack while simultaneously negotiating a phased migration to connection pooling proxies (like PgBouncer) and caching layers.",
                        "B) Quit your job to avoid the crisis.",
                        "C) Refuse to implement any temporary fix and stall the project.",
                        "D) Rewrite the entire database engine over the weekend without testing."
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 12,
                    "question": "Establishing clear engineering standards, style guides, and review protocols across an entire department creates a strong engineering _______.",
                    "type": "fib",
                    "correct_answer": "culture"
                },
                {
                    "question_number": 13,
                    "question": "You are tasked with building a high-performance Python data ingestion pipeline, but your team has zero experience with asyncio or multiprocessing. What is your strategy?",
                    "type": "mcq",
                    "options": [
                        "A) Build it all by yourself over the weekend and never explain it.",
                        "B) Outsource the project to an external agency.",
                        "C) Design a proof-of-concept, conduct internal workshops and knowledge-sharing sessions, pair-program with team members, and scale execution iteratively.",
                        "D) Cancel the project and tell management it's impossible."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 14,
                    "question": "The continuous measurement of system performance, availability, and error rates in production Python applications is known as observability and _______.",
                    "type": "fib",
                    "correct_answer": "monitoring"
                },
                {
                    "question_number": 15,
                    "question": "Tell me about a time when you had to mentor and groom a high-potential mid-level Python developer into a senior technical leader. What was your strategy and outcome?",
                    "type": "descriptive",
                    "correct_answer": "Look for delegation of high-impact tasks, constructive feedback, coaching, and empowering them to make architectural decisions."
                },
                {
                    "question_number": 16,
                    "question": "A key client threatens to leave because of recurring intermittent bugs in a Python enterprise application. As the technical lead, what is your immediate and long-term action plan?",
                    "type": "mcq",
                    "options": [
                        "A) Tell the client they are using the software wrong.",
                        "B) Personally join customer calls with leadership, establish a dedicated war room for rapid bug fixes, conduct root-cause analysis, and communicate transparently on preventative measures.",
                        "C) Ignore the client and focus on new features.",
                        "D) Offer them a 90% discount and hope they stay quiet."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "Balancing velocity of feature delivery with rigorous security compliance in Python enterprise applications is known as DevSec_______.",
                    "type": "fib",
                    "correct_answer": "Ops"
                },
                {
                    "question_number": 18,
                    "question": "When defining the technology stack for a new greenfield enterprise product, what should be your primary guiding principle?",
                    "type": "mcq",
                    "options": [
                        "A) Using whatever trendy Python framework was released on Hacker News yesterday.",
                        "B) Aligning technology choices with long-term business goals, team expertise, scalability requirements, and ecosystem maturity.",
                        "C) Choosing the most complex stack to impress future hires.",
                        "D) Using the oldest, most outdated tools for maximum stability."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "The practice of evaluating and paying down accumulated technical debt systematically is called debt _______.",
                    "type": "fib",
                    "correct_answer": "remediation"
                },
                {
                    "question_number": 20,
                    "question": "Describe a situation where a major strategic technical decision you made (e.g., choosing a specific Python framework or database) turned out to be the wrong choice down the road. How did you own up to it and course-correct?",
                    "type": "descriptive",
                    "correct_answer": "Look for humility, accountability, objective evaluation of failure, and effective migration planning to correct course."
                }
            ]
        }
    },
    "Java Developer": {
        "Technical": {
            "Easy": [
                {
                    "question_number": 1,
                    "question": "Which keyword is used to prevent a class from being inherited in Java?",
                    "type": "mcq",
                    "options": [
                        "static",
                        "final",
                        "abstract",
                        "private"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "The default value of a boolean instance variable in Java is ______.",
                    "type": "fib",
                    "correct_answer": "false"
                },
                {
                    "question_number": 3,
                    "question": "Which of the following is not a primitive data type in Java?",
                    "type": "mcq",
                    "options": [
                        "int",
                        "boolean",
                        "String",
                        "char"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 4,
                    "question": "In Maven, the configuration file is named pom.xml, which stands for Project ______ Model.",
                    "type": "fib",
                    "correct_answer": "Object"
                },
                {
                    "question_number": 5,
                    "question": "Explain the difference between JDK, JRE, and JVM.",
                    "type": "descriptive",
                    "correct_answer": "JDK includes development tools and JRE; JRE provides runtime libraries; JVM executes the bytecode."
                },
                {
                    "question_number": 6,
                    "question": "Which annotation in Spring Boot is used to mark a class as a controller?",
                    "type": "mcq",
                    "options": [
                        "@Component",
                        "@Service",
                        "@Controller",
                        "@Repository"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 7,
                    "question": "The '==' operator in Java compares the ______ of two objects.",
                    "type": "fib",
                    "correct_answer": "reference"
                },
                {
                    "question_number": 8,
                    "question": "Which SQL command is used to retrieve data from a database?",
                    "type": "mcq",
                    "options": [
                        "GET",
                        "SELECT",
                        "PULL",
                        "FETCH"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "In Git, the command used to save changes to the local repository is git ______.",
                    "type": "fib",
                    "correct_answer": "commit"
                },
                {
                    "question_number": 10,
                    "question": "What is the purpose of an Interface in Java?",
                    "type": "descriptive",
                    "correct_answer": "To define a contract for classes, achieving abstraction and multiple inheritance of type."
                },
                {
                    "question_number": 11,
                    "question": "Which collection class is synchronized?",
                    "type": "mcq",
                    "options": [
                        "ArrayList",
                        "HashMap",
                        "Vector",
                        "HashSet"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 12,
                    "question": "The ______ access modifier makes a member accessible only within the same class.",
                    "type": "fib",
                    "correct_answer": "private"
                },
                {
                    "question_number": 13,
                    "question": "Which of these is a Spring dependency injection type?",
                    "type": "mcq",
                    "options": [
                        "Constructor",
                        "Field",
                        "Setter",
                        "All of the above"
                    ],
                    "correct_answer": "D"
                },
                {
                    "question_number": 14,
                    "question": "In JUnit, the annotation used to identify a method that runs before each test is @______.",
                    "type": "fib",
                    "correct_answer": "BeforeEach"
                },
                {
                    "question_number": 15,
                    "question": "What is the difference between Checked and Unchecked exceptions?",
                    "type": "descriptive",
                    "correct_answer": "Checked exceptions are checked at compile-time; Unchecked (Runtime) exceptions are checked at runtime."
                },
                {
                    "question_number": 16,
                    "question": "Which Docker command creates a container from an image?",
                    "type": "mcq",
                    "options": [
                        "docker run",
                        "docker start",
                        "docker create",
                        "docker build"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 17,
                    "question": "Java 8 introduced the ______ API to process sequences of elements.",
                    "type": "fib",
                    "correct_answer": "Stream"
                },
                {
                    "question_number": 18,
                    "question": "Which method is used to start a thread in Java?",
                    "type": "mcq",
                    "options": [
                        "run()",
                        "start()",
                        "init()",
                        "execute()"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "HTTP status code ______ indicates 'Not Found'.",
                    "type": "fib",
                    "correct_answer": "404"
                },
                {
                    "question_number": 20,
                    "question": "Describe the main benefit of using Dependency Injection.",
                    "type": "descriptive",
                    "correct_answer": "Loose coupling, better testability, and easier maintenance of components."
                }
            ],
            "Medium": [
                {
                    "question_number": 1,
                    "question": "Which design pattern is commonly used for Spring Beans?",
                    "type": "mcq",
                    "options": [
                        "Factory",
                        "Singleton",
                        "Prototype",
                        "Strategy"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "In Hibernate, the ______ annotation is used to map an object to a database table.",
                    "type": "fib",
                    "correct_answer": "@Entity"
                },
                {
                    "question_number": 3,
                    "question": "Which of these is not a feature of Java Generics?",
                    "type": "mcq",
                    "options": [
                        "Type safety",
                        "Code reusability",
                        "Compile-time checks",
                        "Runtime performance"
                    ],
                    "correct_answer": "D"
                },
                {
                    "question_number": 4,
                    "question": "The ______ state in JPA refers to an object that has an ID but is not currently tracked by the EntityManager.",
                    "type": "fib",
                    "correct_answer": "detached"
                },
                {
                    "question_number": 5,
                    "question": "Explain the difference between @Controller and @RestController.",
                    "type": "descriptive",
                    "correct_answer": "@RestController combines @Controller and @ResponseBody, serializing return values directly to JSON."
                },
                {
                    "question_number": 6,
                    "question": "What is the default scope of a bean in Spring?",
                    "type": "mcq",
                    "options": [
                        "prototype",
                        "request",
                        "singleton",
                        "session"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 7,
                    "question": "In Java concurrency, a ______ is a low-level synchronization construct.",
                    "type": "fib",
                    "correct_answer": "lock"
                },
                {
                    "question_number": 8,
                    "question": "Which of these is true about the String Pool?",
                    "type": "mcq",
                    "options": [
                        "It uses heap memory",
                        "It uses stack memory",
                        "It causes memory leaks",
                        "It is for primitives"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 9,
                    "question": "The ______ method in Mockito is used to define behavior for a mocked method.",
                    "type": "fib",
                    "correct_answer": "when"
                },
                {
                    "question_number": 10,
                    "question": "Describe how an Autowired annotation works in Spring.",
                    "type": "descriptive",
                    "correct_answer": "It signals the container to automatically inject dependencies by matching bean types."
                },
                {
                    "question_number": 11,
                    "question": "Which SQL isolation level prevents non-repeatable reads?",
                    "type": "mcq",
                    "options": [
                        "Read Uncommitted",
                        "Read Committed",
                        "Repeatable Read",
                        "None"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 12,
                    "question": "In Java 8, a(n) ______ interface has exactly one abstract method.",
                    "type": "fib",
                    "correct_answer": "functional"
                },
                {
                    "question_number": 13,
                    "question": "What is the purpose of the 'finally' block?",
                    "type": "mcq",
                    "options": [
                        "Execute cleanup code",
                        "Catch errors",
                        "Stop execution",
                        "Restart thread"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 14,
                    "question": "______ is a REST architectural style constraint where client/server communication is stateless.",
                    "type": "fib",
                    "correct_answer": "Statelessness"
                },
                {
                    "question_number": 15,
                    "question": "What is the difference between parallelStream and stream?",
                    "type": "descriptive",
                    "correct_answer": "parallelStream processes elements concurrently using the ForkJoinPool; stream is sequential."
                },
                {
                    "question_number": 16,
                    "question": "Which exception is thrown when a bean cannot be found?",
                    "type": "mcq",
                    "options": [
                        "NullPointerException",
                        "NoSuchBeanDefinitionException",
                        "BeanNotFoundException",
                        "InjectionException"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "Docker ______ allows you to define and run multi-container applications.",
                    "type": "fib",
                    "correct_answer": "Compose"
                },
                {
                    "question_number": 18,
                    "question": "Which interface is the root of the Collection hierarchy?",
                    "type": "mcq",
                    "options": [
                        "List",
                        "Set",
                        "Collection",
                        "Map"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 19,
                    "question": "The ______ pattern is used to decouple an object's construction from its representation.",
                    "type": "fib",
                    "correct_answer": "Builder"
                },
                {
                    "question_number": 20,
                    "question": "Explain the role of the Transactional annotation.",
                    "type": "descriptive",
                    "correct_answer": "It manages database transactions by setting boundaries (begin, commit, rollback) declaratively."
                }
            ],
            "Hard": [
                {
                    "question_number": 1,
                    "question": "Which Garbage Collector is optimized for low latency?",
                    "type": "mcq",
                    "options": [
                        "Serial",
                        "G1",
                        "ZGC",
                        "Parallel"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 2,
                    "question": "The JVM Memory Model uses the ______ to store class structures and static variables.",
                    "type": "fib",
                    "correct_answer": "Metaspace"
                },
                {
                    "question_number": 3,
                    "question": "What happens if a deadlock occurs in a multithreaded environment?",
                    "type": "mcq",
                    "options": [
                        "JVM crashes",
                        "Thread waits indefinitely",
                        "Exception is thrown",
                        "Garbage collection clears it"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "______ is a common problem in JPA where accessing lazy-loaded fields outside a session throws an error.",
                    "type": "fib",
                    "correct_answer": "LazyInitializationException"
                },
                {
                    "question_number": 5,
                    "question": "Explain how the Spring IoC container handles circular dependencies.",
                    "type": "descriptive",
                    "correct_answer": "It uses setter injection for circular dependencies or fails on constructor injection; requires @Lazy."
                },
                {
                    "question_number": 6,
                    "question": "Which ClassLoader is responsible for loading the core Java API?",
                    "type": "mcq",
                    "options": [
                        "Application",
                        "Extension",
                        "Bootstrap",
                        "System"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 7,
                    "question": "The ______ algorithm is often used in internal JVM GC cycle detection.",
                    "type": "fib",
                    "correct_answer": "Mark-Sweep"
                },
                {
                    "question_number": 8,
                    "question": "What is the benefit of using Spring Security's FilterChainProxy?",
                    "type": "mcq",
                    "options": [
                        "Faster routing",
                        "Delegated security filter management",
                        "DB connection pooling",
                        "Automatic encryption"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "In Java memory management, an ______ reference is cleared by GC when memory is low.",
                    "type": "fib",
                    "correct_answer": "Soft"
                },
                {
                    "question_number": 10,
                    "question": "Describe the difference between optimistic and pessimistic locking in Hibernate.",
                    "type": "descriptive",
                    "correct_answer": "Optimistic uses versioning to check for updates; pessimistic locks the row at the database level."
                },
                {
                    "question_number": 11,
                    "question": "Which of these is a valid way to optimize a REST API?",
                    "type": "mcq",
                    "options": [
                        "Caching",
                        "HATEOAS",
                        "Pagination",
                        "All of the above"
                    ],
                    "correct_answer": "D"
                },
                {
                    "question_number": 12,
                    "question": "The ______ pattern is used in microservices to manage service registration and discovery.",
                    "type": "fib",
                    "correct_answer": "Sidecar"
                },
                {
                    "question_number": 13,
                    "question": "How does ThreadLocal work internally?",
                    "type": "mcq",
                    "options": [
                        "Thread-specific Map",
                        "Static field",
                        "Synchronized lock",
                        "Global variable"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 14,
                    "question": "______ is a technique to optimize SQL performance by pre-compiling the query.",
                    "type": "fib",
                    "correct_answer": "Prepared Statement"
                },
                {
                    "question_number": 15,
                    "question": "Explain the concept of 'Double-Checked Locking' and why it is used.",
                    "type": "descriptive",
                    "correct_answer": "Used in Singleton pattern for thread-safe lazy initialization while avoiding synchronization overhead."
                },
                {
                    "question_number": 16,
                    "question": "What is the primary function of the JVM Just-In-Time (JIT) compiler?",
                    "type": "mcq",
                    "options": [
                        "Compiles Bytecode to Native Code",
                        "Garbage collection",
                        "Memory allocation",
                        "Class loading"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 17,
                    "question": "The ______ principle in SOLID design promotes coding to abstractions, not implementations.",
                    "type": "fib",
                    "correct_answer": "Dependency Inversion"
                },
                {
                    "question_number": 18,
                    "question": "Which memory area is not shared between threads?",
                    "type": "mcq",
                    "options": [
                        "Heap",
                        "Metaspace",
                        "Stack",
                        "Constant Pool"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 19,
                    "question": "______-oriented programming is a Spring feature that decouples cross-cutting concerns.",
                    "type": "fib",
                    "correct_answer": "Aspect"
                },
                {
                    "question_number": 20,
                    "question": "How does a Circuit Breaker pattern improve microservice resilience?",
                    "type": "descriptive",
                    "correct_answer": "It stops calls to a failing service after a threshold, preventing cascading failures."
                }
            ]
        },
        "HR": {
            "Easy": [
                {
                    "question_number": 1,
                    "question": "As an entry-level Java Developer, you find a bug in a legacy module written by a senior team member. What is the most professional approach?",
                    "type": "mcq",
                    "options": [
                        "A) Publicly point out the flaw in the team chat to warn others.",
                        "B) Quietly fix it without telling anyone and hope nobody notices.",
                        "C) Politely inform the senior developer or lead in private, explain the issue, and offer a suggested fix.",
                        "D) Ignore the bug since it was written by someone more experienced."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 2,
                    "question": "The ability to work effectively and harmoniously in a group, especially when collaborating on shared Java repositories, is known as ______.",
                    "type": "fib",
                    "correct_answer": "teamwork"
                },
                {
                    "question_number": 3,
                    "question": "You are given a complex Java task with a tight deadline, and you realize you might not finish on time. What should you do?",
                    "type": "mcq",
                    "options": [
                        "A) Wait until the deadline day to announce that the task is incomplete.",
                        "B) Communicate the bottleneck early to your manager or mentor and ask for guidance or reprioritization.",
                        "C) Stop working on it and start a different, easier task.",
                        "D) Blame the ambiguity of the requirements during the retro."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "When you actively listen to instructions, ask clarifying questions, and ensure you understand project requirements, you are demonstrating strong ______ skills.",
                    "type": "fib",
                    "correct_answer": "communication"
                },
                {
                    "question_number": 5,
                    "question": "Describe a time when you had to learn a new tool or technology quickly for a Java project. How did you approach the learning curve?",
                    "type": "descriptive",
                    "correct_answer": "Proactive learning, utilizing documentation, building small prototypes, and seeking help when blocked."
                },
                {
                    "question_number": 6,
                    "question": "During a code review for your first pull request, a senior developer leaves multiple constructive criticisms. How should you react?",
                    "type": "mcq",
                    "options": [
                        "A) Take it personally and defend your original code defensively.",
                        "B) Close the pull request and refuse to work on that module.",
                        "C) View it as a learning opportunity, thank the reviewer, and make the necessary updates.",
                        "D) Ignore the comments and merge the code anyway."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 7,
                    "question": "The capacity to accept feedback without becoming defensive and using it to improve your coding habits is known as constructive ______.",
                    "type": "fib",
                    "correct_answer": "criticism"
                },
                {
                    "question_number": 8,
                    "question": "You notice that your teammate is struggling to write unit tests for a Java service. How do you respond?",
                    "type": "mcq",
                    "options": [
                        "A) Tell them it's not your problem and focus strictly on your own Jira tickets.",
                        "B) Offer to spend 15 minutes pairing with them to show how you write JUnit tests.",
                        "C) Complain to the scrum master about their lack of testing skills.",
                        "D) Write their tests for them without explaining how you did it."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "To ensure that your code changes do not break existing functionality, it is essential to practice professional ______ by running existing test suites.",
                    "type": "fib",
                    "correct_answer": "due diligence"
                },
                {
                    "question_number": 10,
                    "question": "Describe a situation where you had a disagreement with a peer regarding a coding style or syntax convention. How did you resolve it?",
                    "type": "descriptive",
                    "correct_answer": "Focusing on project standards, referencing style guides, open discussion, and compromising professionally."
                },
                {
                    "question_number": 11,
                    "question": "Your manager asks you to take on a minor administrative task for the engineering team that takes time away from your Java coding. What is the best attitude to display?",
                    "type": "mcq",
                    "options": [
                        "A) Refuse flatly because you were hired as a developer, not an administrator.",
                        "B) Accept it with a positive attitude, recognizing that team support tasks are part of being a good team player.",
                        "C) Do it poorly so you are never asked again.",
                        "D) Complain to HR about unfair task distribution."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "The quality of being reliable, meeting deadlines, and delivering clean, working Java code consistently reflects your professional ______.",
                    "type": "fib",
                    "correct_answer": "accountability"
                },
                {
                    "question_number": 13,
                    "question": "You realize you accidentally committed sensitive database credentials into a public or shared Git repository. What is your immediate action?",
                    "type": "mcq",
                    "options": [
                        "A) Delete the file locally and hope no one clones the repo.",
                        "B) Immediately alert your tech lead/security team, invalidate the credentials, and follow repo-cleaning procedures.",
                        "C) Leave it there; it's just a development database anyway.",
                        "D) Wait until the next sprint review to mention it."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 14,
                    "question": "When you manage your daily tasks, organize your workspace, and prioritize coding tickets effectively, you exhibit strong ______ skills.",
                    "type": "fib",
                    "correct_answer": "time management"
                },
                {
                    "question_number": 15,
                    "question": "Tell me about a time when you received negative feedback from a mentor or manager. How did you process it and apply it to your work?",
                    "type": "descriptive",
                    "correct_answer": "Active listening, removing ego, actionable improvement steps, and following up on progress."
                },
                {
                    "question_number": 16,
                    "question": "During a daily stand-up, you have nothing significant to report because you were blocked all day yesterday. What should you say?",
                    "type": "mcq",
                    "options": [
                        "A) Lie and say you made great progress to look productive.",
                        "B) State clearly that you were blocked on a specific issue and ask for assistance to unblock.",
                        "C) Stay silent and skip your update.",
                        "D) Blame the IT department for your computer being slow."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "The trait of being open-ended, curious, and eager to learn new Java frameworks and updates is known as a growth ______.",
                    "type": "fib",
                    "correct_answer": "mindset"
                },
                {
                    "question_number": 18,
                    "question": "You are assigned a repetitive, manual task of generating boilerplate code. What is the most proactive approach?",
                    "type": "mcq",
                    "options": [
                        "A) Complain that it is boring and do it as slowly as possible.",
                        "B) Complete the manual task first, then research or build a small script/generator to automate it for the future.",
                        "C) Skip the task and hope nobody notices it wasn't done.",
                        "D) Refuse to do it unless you get a bonus."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "Maintaining a calm demeanor when production builds fail and working systematically to find the cause demonstrates emotional ______.",
                    "type": "fib",
                    "correct_answer": "intelligence"
                },
                {
                    "question_number": 20,
                    "question": "Describe a project where you collaborated closely with QA or testers to resolve bugs in your Java code. How did you ensure smooth collaboration?",
                    "type": "descriptive",
                    "correct_answer": "Clear reproduction steps, respectful communication, prompt bug fixes, and continuous feedback loop."
                }
            ],
            "Medium": [
                {
                    "question_number": 1,
                    "question": "As a mid-level Java Developer, you notice a junior developer repeatedly writing inefficient SQL queries within a Spring Data JPA service. How do you handle this?",
                    "type": "mcq",
                    "options": [
                        "A) Rewrite their code silently without telling them.",
                        "B) Schedule a brief 1-on-1 mentoring session to explain the performance implications and teach them how to optimize queries.",
                        "C) Reject their pull request without explanation so they learn the hard way.",
                        "D) Complain to the engineering manager about their incompetence."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "The process of guiding, supporting, and sharing technical knowledge with newer team members to elevate the team's overall skill level is called ______.",
                    "type": "fib",
                    "correct_answer": "mentorship"
                },
                {
                    "question_number": 3,
                    "question": "Product management requests an urgent new feature that requires bypassing standard code review and testing protocols to meet a marketing event. How do you respond?",
                    "type": "mcq",
                    "options": [
                        "A) Agree instantly and push untested code to production.",
                        "B) Refuse to speak to product management altogether.",
                        "C) Explain the risks of technical debt and production instability while negotiating a streamlined but safe review path.",
                        "D) Agree, but blame product management later when things break."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 4,
                    "question": "When mediating discussions between backend Java teams and frontend teams regarding API contracts, strong ______ skills are essential.",
                    "type": "fib",
                    "correct_answer": "negotiation"
                },
                {
                    "question_number": 5,
                    "question": "Describe a time when you identified a significant technical debt bottleneck in a Java application. How did you pitch the refactoring effort to stakeholders?",
                    "type": "descriptive",
                    "correct_answer": "Data-driven justification, linking tech debt to business impact (latency/bugs), proposing phased approach."
                },
                {
                    "question_number": 6,
                    "question": "You are leading a sub-task, and a critical dependency managed by another team is delayed, blocking your progress. What is your next step?",
                    "type": "mcq",
                    "options": [
                        "A) Stop working entirely until they deliver the dependency.",
                        "B) Proactively reach out to the other team's lead to understand their timeline, find a mock/stub solution in the interim, and update your manager.",
                        "C) Talk negatively about the other team in the next sprint retro.",
                        "D) Attempt to hack into their repository to finish the dependency yourself."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "The ability to adapt quickly when project requirements, tech stacks, or business priorities shift suddenly is known as professional ______.",
                    "type": "fib",
                    "correct_answer": "agility"
                },
                {
                    "question_number": 8,
                    "question": "During a code review, you find a massive architectural flaw in a pull request submitted by a peer who is sensitive to criticism. How do you phrase your feedback?",
                    "type": "mcq",
                    "options": [
                        "A) 'This code is terrible and completely violates our design patterns.'",
                        "B) 'Why did you write it this way? Didn't you read the docs?'",
                        "C) 'Great job on the functionality! Let's discuss an alternative pattern for this module to improve scalability over the long term.'",
                        "D) Approve it anyway to avoid hurting their feelings."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 9,
                    "question": "Taking ownership of a feature from conception, development, testing, to post-deployment monitoring is an example of end-to-end ______.",
                    "type": "fib",
                    "correct_answer": "ownership"
                },
                {
                    "question_number": 10,
                    "question": "Describe a situation where a critical bug was found in production late at night. How did you handle the pressure and collaborate with your team to resolve it?",
                    "type": "descriptive",
                    "correct_answer": "Calm triage, effective communication, collaborative root-cause analysis, and systematic debugging."
                },
                {
                    "question_number": 11,
                    "question": "You have too many tasks on your plate for the current sprint and realize you will miss one of your commitments. What do you do?",
                    "type": "mcq",
                    "options": [
                        "A) Hide the status and work 80 hours over the weekend without telling anyone.",
                        "B) Raise the flag during standup or to the Scrum Master early, present the workload, and help reprioritize items.",
                        "C) Randomly drop the hardest task and hope nobody notices.",
                        "D) Blame your teammates for not helping you."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "The skill of breaking down a massive enterprise Java migration project into manageable, incremental milestones is called ______ planning.",
                    "type": "fib",
                    "correct_answer": "strategic"
                },
                {
                    "question_number": 13,
                    "question": "You are tasked with choosing a new third-party library for caching in a Java Spring Boot application. Two libraries are proposed with conflicting opinions in the team. How do you decide?",
                    "type": "mcq",
                    "options": [
                        "A) Pick the one with the coolest sounding name.",
                        "B) Flip a coin to save time.",
                        "C) Conduct a small proof-of-concept (PoC) comparing performance, community support, and maintenance, then present findings for a team decision.",
                        "D) Pick your personal favorite regardless of team input."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 14,
                    "question": "When you clearly explain complex Java concurrency concepts to non-technical stakeholders using business analogies, you demonstrate effective translation of ______.",
                    "type": "fib",
                    "correct_answer": "complexity"
                },
                {
                    "question_number": 15,
                    "question": "Describe a time when you had to onboard a new developer onto your Java project. What steps did you take to make them productive quickly?",
                    "type": "descriptive",
                    "correct_answer": "Clear documentation, setting up local environment guidelines, pairing sessions, and assigning good first issues."
                },
                {
                    "question_number": 16,
                    "question": "A team member consistently misses meetings and delivers their Java microservice components late, impacting your work. How do you address this?",
                    "type": "mcq",
                    "options": [
                        "A) Complain to upper management immediately behind their back.",
                        "B) Have a direct, empathetic conversation with them to understand if they are facing personal or professional blockers, and offer support before escalating.",
                        "C) Stop talking to them and isolate them from the team.",
                        "D) Start missing your own deadlines in retaliation."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "The practice of continuously improving team processes, communication, and technical practices during regular retrospective meetings fosters a culture of ______.",
                    "type": "fib",
                    "correct_answer": "kaizen"
                },
                {
                    "question_number": 18,
                    "question": "You are asked to estimate the delivery time for a new microservice in Java, but requirements are still vague. How do you provide an estimate?",
                    "type": "mcq",
                    "options": [
                        "A) Refuse to give any estimate until every single detail is finalized.",
                        "B) Guess a random number like two weeks to keep stakeholders happy.",
                        "C) Provide a range (e.g., 3-5 weeks) based on current assumptions, explicitly stating dependencies and risks that could affect the timeline.",
                        "D) Promise it will be done tomorrow."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 19,
                    "question": "When collaborating across global time zones with remote team members, asynchronous ______ is crucial for maintaining project velocity.",
                    "type": "fib",
                    "correct_answer": "communication"
                },
                {
                    "question_number": 20,
                    "question": "Describe a situation where a project you worked hard on was canceled or drastically changed directions mid-stream. How did you maintain your motivation and pivot?",
                    "type": "descriptive",
                    "correct_answer": "Resilience, understanding the business rationale, refocusing energy on the new direction, and reusing valuable learnings."
                }
            ],
            "Hard": [
                {
                    "question_number": 1,
                    "question": "As a Senior Java Architect/Lead, you inherit a legacy monolithic system with massive tech debt that the business wants to rewrite entirely in microservices. However, a full rewrite carries massive risk. What is your strategic leadership approach?",
                    "type": "mcq",
                    "options": [
                        "A) Stop all feature development and force a risky 12-month rewrite.",
                        "B) Propose the Strangler Fig pattern, gradually migrating high-value modules to microservices while keeping the monolith running.",
                        "C) Tell the business it is impossible and refuse to touch the system.",
                        "D) Add more layers of abstraction inside the monolith without fixing the core structure."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "The strategic foresight to anticipate future scale, security vulnerabilities, and maintenance burdens in enterprise Java system design is known as architectural ______.",
                    "type": "fib",
                    "correct_answer": "vision"
                },
                {
                    "question_number": 3,
                    "question": "Two senior engineers on your team are locked in a toxic dispute over whether to use Spring WebFlux or traditional Spring MVC for a new high-throughput platform, stalling progress. How do you resolve this?",
                    "type": "mcq",
                    "options": [
                        "A) Tell them to figure it out themselves while you watch.",
                        "B) Fire both engineers immediately.",
                        "C) Facilitate an objective evaluation based on project requirements, team expertise, and maintenance cost, make a final architectural decision, and align the team.",
                        "D) Let whichever engineer shouts louder win the argument."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 4,
                    "question": "When balancing rapid feature delivery with robust enterprise security and compliance standards, leadership must maintain a strict risk ______ framework.",
                    "type": "fib",
                    "correct_answer": "management"
                },
                {
                    "question_number": 5,
                    "question": "Describe a time when a critical enterprise Java application suffered a catastrophic outage under your leadership. Walk through your incident response, stakeholder management, and post-mortem culture.",
                    "type": "descriptive",
                    "correct_answer": "Clear incident command, transparent stakeholder updates, blameless post-mortem, and actionable preventive engineering."
                },
                {
                    "question_number": 6,
                    "question": "Your executive leadership demands a hard release date for a complex multi-tenant Java cloud platform, but your engineering assessment shows it will take 30% longer to ensure stability. How do you handle this negotiation?",
                    "type": "mcq",
                    "options": [
                        "A) Agree to the executive deadline and force your team into mandatory 80-hour workweeks.",
                        "B) Present a trade-off analysis: show what scope can be delivered by their deadline versus the full scope with the required timeline, letting them make an informed business choice.",
                        "C) Tell them engineering timelines cannot be discussed.",
                        "D) Quit on the spot."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "The practice of fostering psychological safety so team members can admit failures and highlight production risks without fear of retribution is called a ______ culture.",
                    "type": "fib",
                    "correct_answer": "blameless"
                },
                {
                    "question_number": 8,
                    "question": "A top-performing senior Java developer on your team is exhibiting toxic behavior, alienating junior staff and lowering overall morale. How do you manage this delicate situation?",
                    "type": "mcq",
                    "options": [
                        "A) Ignore the behavior because their individual code output is high.",
                        "B) Publicly reprimand them in front of the entire team.",
                        "C) Have a private, direct conversation highlighting how their behavior impacts team dynamics, set clear behavioral expectations, and establish a timeline for improvement.",
                        "D) Immediately terminate them without warning."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 9,
                    "question": "Aligning technical roadmap initiatives with the overarching financial and strategic goals of the enterprise is referred to as business-technology ______.",
                    "type": "fib",
                    "correct_answer": "alignment"
                },
                {
                    "question_number": 10,
                    "question": "Describe a situation where you had to scale an engineering team rapidly while maintaining high code quality standards and onboarding velocity in a Java ecosystem.",
                    "type": "descriptive",
                    "correct_answer": "Establishing automated CI/CD guardrails, standardized code reviews, comprehensive architecture documentation, and scalable mentoring structures."
                },
                {
                    "question_number": 11,
                    "question": "You discover that a major architectural decision made by a former lead architect is fundamentally flawed and causing systemic memory leaks in your distributed Java services. How do you approach rectifying this?",
                    "type": "mcq",
                    "options": [
                        "A) Blame the former architect during all hands meetings.",
                        "B) Keep it secret and patch symptoms as they occur.",
                        "C) Conduct a formal root-cause analysis, document the technical and financial impact, and propose a prioritized refactoring roadmap to leadership.",
                        "D) Rewrite the entire system over a weekend without approval."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 12,
                    "question": "The strategic allocation of engineering resources between new feature development and technical debt reduction is known as capacity ______.",
                    "type": "fib",
                    "correct_answer": "allocation"
                },
                {
                    "question_number": 13,
                    "question": "Your company is acquiring a startup, and you are tasked with evaluating their Java codebase. You find it is poorly documented, uses outdated dependencies, and lacks tests. What is your leadership strategy for integration?",
                    "type": "mcq",
                    "options": [
                        "A) Recommend scrapping the acquisition entirely based on the code.",
                        "B) Force the startup engineers to rewrite everything in your company's stack within two weeks.",
                        "C) Perform a risk assessment, categorize vulnerabilities and technical debt, and create a phased integration and modernization plan that minimizes business disruption.",
                        "D) Absorb their code directly into your production repository without review."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 14,
                    "question": "When leading cross-functional transformation initiatives across multiple departments, driving consensus and shared ownership is a core test of executive ______.",
                    "type": "fib",
                    "correct_answer": "leadership"
                },
                {
                    "question_number": 15,
                    "question": "Describe a time when you had to mentor and develop high-potential mid-level Java engineers into autonomous senior leaders. What was your strategy?",
                    "type": "descriptive",
                    "correct_answer": "Delegating complex architectural ownership, providing constructive feedback, sponsoring high-visibility projects, and encouraging leadership autonomy."
                },
                {
                    "question_number": 16,
                    "question": "A key stakeholder insists on implementing a fragile, unscalable feature into your core Java enterprise application due to short-term commercial pressure. How do you manage this conflict?",
                    "type": "mcq",
                    "options": [
                        "A) Implement the fragile feature immediately without comment.",
                        "B) Tell the stakeholder they do not understand software engineering.",
                        "C) Educate the stakeholder on long-term maintenance costs and security risks, and propose an alternative scalable design that meets their underlying business need.",
                        "D) Ignore their request and build something completely different."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 17,
                    "question": "The deliberate and structured process of evaluating emerging technologies for enterprise Java adoption through proofs-of-concept is known as technology ______.",
                    "type": "fib",
                    "correct_answer": "evaluation"
                },
                {
                    "question_number": 18,
                    "question": "Your engineering organization is suffering from severe burnout due to frequent emergency releases and unstable staging environments. As a senior leader, what is your first intervention?",
                    "type": "mcq",
                    "options": [
                        "A) Tell the team to work harder and push through the burnout.",
                        "B) Pause non-essential feature development to invest in automated testing, CI/CD pipeline reliability, and debt reduction.",
                        "C) Hire external consultants and ignore the existing team's feedback.",
                        "D) Do nothing and wait for people to resign."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "Maintaining long-term architectural integrity while empowering decentralized teams to make local decisions requires robust governance and clear ______.",
                    "type": "fib",
                    "correct_answer": "guardrails"
                },
                {
                    "question_number": 20,
                    "question": "Describe a strategic decision where you had to sunset a popular Java service or product version used by clients. How did you manage customer communication and migration?",
                    "type": "descriptive",
                    "correct_answer": "Clear sunset roadmap, proactive client communication, providing migration guides and tooling, and extended support windows."
                }
            ]
        },
        "Behavioral": {
            "Easy": [
                {
                    "question_number": 1,
                    "question": "You have been working on fixing a bug in a Java service for two hours without progress. What is the most appropriate next step?",
                    "type": "mcq",
                    "options": [
                        "A) Continue trying solutions on your own for the rest of the day to show self-reliance.",
                        "B) Document what you have tried so far and ask a senior developer for guidance.",
                        "C) Rewrite the entire class from scratch without telling anyone.",
                        "D) Mark the bug ticket as unresolvable and move on to another task."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "When receiving constructive criticism during a Java pull request review, showing open-mindedness and a willingness to improve demonstrates standard professional ___.",
                    "type": "fib",
                    "correct_answer": "receptivity to feedback"
                },
                {
                    "question_number": 3,
                    "question": "A senior developer leaves multiple comments on your pull request regarding Java naming conventions and standard design patterns. How should you respond?",
                    "type": "mcq",
                    "options": [
                        "A) Ignore the comments and merge the code since it passes all existing tests.",
                        "B) Politely ask for clarification on points you don't understand and apply the suggested fixes.",
                        "C) Argue that code style is purely subjective and reject all changes.",
                        "D) Delete the pull request and re-submit it hoping someone else reviews it."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "Proactively informing your team lead about a potential delay in delivering your assigned Java task as soon as a blocker arises demonstrates personal ___.",
                    "type": "fib",
                    "correct_answer": "accountability"
                },
                {
                    "question_number": 5,
                    "question": "Describe a time when you struggled to navigate an unfamiliar legacy Java codebase. How did you handle it, and what did you learn?",
                    "type": "descriptive",
                    "correct_answer": "Look for answers emphasizing curiosity, methodically tracing code/writing unit tests to understand flow, seeking appropriate help, and documenting findings for future teammates."
                },
                {
                    "question_number": 6,
                    "question": "You realize a unit test you wrote for a Java service is flaky (passes intermittently). Sprint deadline is in two hours. What should you do?",
                    "type": "mcq",
                    "options": [
                        "A) Delete the unit test so the build pipeline turns green.",
                        "B) Add `@Ignore` / `@Disabled` without telling anyone and push to main.",
                        "C) Inform your lead, investigate the root cause, or temporarily disable it while logging a follow-up ticket with team consent.",
                        "D) Keep re-running the CI build until it passes once, then deploy immediately."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 7,
                    "question": "When working in a shared Java repository, avoiding pushing broken code to the shared branch is an act of consideration and team ___.",
                    "type": "fib",
                    "correct_answer": "collaboration"
                },
                {
                    "question_number": 8,
                    "question": "You accidentally discover an unhandled `NullPointerException` in your module right before a sprint demo. How do you handle this?",
                    "type": "mcq",
                    "options": [
                        "A) Cover up the scenario during the demo so no one notices.",
                        "B) Transparently notify your team, assess if a quick fix is safe, or exclude that specific path from the demo.",
                        "C) Blame the quality assurance engineer for not catching it earlier.",
                        "D) Cancel the entire feature demo without explanation."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "Demonstrating the drive to learn new Java features like Lambdas, Streams, or modern JDK syntax outside of basic sprint assignments shows a mindset of continuous ___.",
                    "type": "fib",
                    "correct_answer": "learning"
                },
                {
                    "question_number": 10,
                    "question": "Describe a situation where you made a mistake in a Java implementation (e.g., incorrect logic or broken test). How did you communicate and rectify the issue?",
                    "type": "descriptive",
                    "correct_answer": "Look for honesty, taking responsibility without blaming others, prompt communication to impacted team members, and taking steps to prevent recurrence."
                },
                {
                    "question_number": 11,
                    "question": "You have a minor disagreement with a peer about whether to use a `for` loop or Java Streams for a simple data filter. What is the best action?",
                    "type": "mcq",
                    "options": [
                        "A) Argue until the peer agrees to your preference.",
                        "B) Escalate to the engineering director immediately.",
                        "C) Discuss readability, team standards, and performance, then reach a quick consensus.",
                        "D) Intentionally delay your work until the other developer backs down."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 12,
                    "question": "Asking for clear acceptance criteria when assigned a vague user story demonstrates proactive ___.",
                    "type": "fib",
                    "correct_answer": "clarification"
                },
                {
                    "question_number": 13,
                    "question": "You are assigned three small Java bug tickets and one research task simultaneously. How do you decide which to work on first?",
                    "type": "mcq",
                    "options": [
                        "A) Pick the easiest bug ticket first regardless of priority.",
                        "B) Ask the Tech Lead/Scrum Master about ticket business priorities and dependencies.",
                        "C) Flip a coin to choose the order.",
                        "D) Work on all four simultaneously by switching tasks every 15 minutes."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "When a senior team member explains a complex Java Spring context concept to you, taking notes so you do not need the same lesson repeated reflects respect for their ___.",
                    "type": "fib",
                    "correct_answer": "time"
                },
                {
                    "question_number": 15,
                    "question": "Tell me about a time you had to adapt quickly to a change in project requirements while working on a Java module.",
                    "type": "descriptive",
                    "correct_answer": "Look for adaptability, calm demeanor under changing priorities, effective re-estimation of tasks, and clear communication regarding scope changes."
                },
                {
                    "question_number": 16,
                    "question": "You notice that internal setup documentation for the Java development environment is outdated and missing steps. What should you do?",
                    "type": "mcq",
                    "options": [
                        "A) Complain to your manager during your 1-on-1.",
                        "B) Follow the old steps and complain online about broken docs.",
                        "C) Update the documentation with the correct steps once you figure them out.",
                        "D) Ignore it because you have already configured your machine."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 17,
                    "question": "Helping a fellow junior developer debug a tricky Java exception promotes a supportive team ___.",
                    "type": "fib",
                    "correct_answer": "culture"
                },
                {
                    "question_number": 18,
                    "question": "During a daily standup, what is the best way to report your status as an entry-level Java developer?",
                    "type": "mcq",
                    "options": [
                        "A) Give a 15-minute detailed line-by-line explanation of your code changes.",
                        "B) State clearly what you completed yesterday, your plan for today, and any blockers you have.",
                        "C) Say 'everything is fine' even if you are stuck.",
                        "D) Remain silent until spoken to directly by the Scrum Master."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "Maintaining consistent code formatting according to agreed Java style guides reflects attention to ___.",
                    "type": "fib",
                    "correct_answer": "detail"
                },
                {
                    "question_number": 20,
                    "question": "Give an example of a time when you took the initiative to learn a new tool, library, or Java framework feature to solve a problem.",
                    "type": "descriptive",
                    "correct_answer": "Look for self-driven motivation, practical application of new knowledge, evaluation of options, and sharing key learnings with peers."
                }
            ],
            "Medium": [
                {
                    "question_number": 1,
                    "question": "A Product Owner demands adding a feature directly to production, skipping the standard automated Java integration testing suite to meet a marketing event. How do you respond?",
                    "type": "mcq",
                    "options": [
                        "A) Comply immediately without raising concerns to avoid conflict.",
                        "B) Refuse outright and publicly criticize the Product Owner in Slack.",
                        "C) Explain the operational risks, propose a minimal test scope or feature flag solution, and escalate risks to the Tech Lead.",
                        "D) Silently push the code and blame the CI tool if production breaks."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 2,
                    "question": "Balancing the delivery of functional features with the reduction of Java technical debt requires effective business ___.",
                    "type": "fib",
                    "correct_answer": "negotiation"
                },
                {
                    "question_number": 3,
                    "question": "While refactoring a core Java business service, you notice legacy code with no unit tests. What is the most responsible action before modifying logic?",
                    "type": "mcq",
                    "options": [
                        "A) Write characterization tests to lock down current behavior before making changes.",
                        "B) Refactor the code quickly and rely on manual QA to catch issues.",
                        "C) Delete the legacy code and write brand-new logic without consulting business rules.",
                        "D) Postpone the refactoring task permanently."
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 4,
                    "question": "Conducting thorough code reviews that point out potential Java memory leaks or thread-safety issues helps foster technical ___.",
                    "type": "fib",
                    "correct_answer": "excellence"
                },
                {
                    "question_number": 5,
                    "question": "Describe a scenario where you had to negotiate an API contract change between your Java microservice and a front-end or third-party team.",
                    "type": "descriptive",
                    "correct_answer": "Look for proactive communication, backward compatibility considerations, contract-first design alignment, clear documentation (e.g., OpenAPI), and empathy for client developers."
                },
                {
                    "question_number": 6,
                    "question": "You strongly disagree with a senior architect's decision to use a heavy framework when a lightweight Java library would suffice. How do you proceed?",
                    "type": "mcq",
                    "options": [
                        "A) Maliciously comply by implementing it poorly so it fails later.",
                        "B) Prepare a data-backed trade-off analysis (pros, cons, benchmarks) and discuss it respectfully in a technical sync.",
                        "C) Gossip with team members to build a coalition against the architect.",
                        "D) Ignore the architect's decision and build your preferred option anyway."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "When production incidents occur in Java services, focusing on systems improvement rather than personal blame creates a culture of ___.",
                    "type": "fib",
                    "correct_answer": "psychological safety"
                },
                {
                    "question_number": 8,
                    "question": "During a peak traffic event, a critical Java Spring service experiences high CPU usage and OutOfMemory errors. What is your immediate behavioral priority?",
                    "type": "mcq",
                    "options": [
                        "A) Panic and start restarting all servers continuously.",
                        "B) Focus on restoring service stability (e.g., failover, traffic shedding) while capturing heap dumps/logs for post-incident analysis.",
                        "C) Blame the infrastructure team for not provisioning enough RAM.",
                        "D) Lock yourself in a room until the issue resolves naturally."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "Guiding a junior developer through a complex Java concurrency debugging session without taking over the keyboard exhibits effective ___.",
                    "type": "fib",
                    "correct_answer": "mentorship"
                },
                {
                    "question_number": 10,
                    "question": "Tell me about a time you had to deal with technical debt in a Java project that was severely impacting team velocity.",
                    "type": "descriptive",
                    "correct_answer": "Look for ability to quantify tech debt, communicating impact to non-technical stakeholders, creating incremental refactoring plans, and successfully executing fixes alongside feature delivery."
                },
                {
                    "question_number": 11,
                    "question": "A junior developer repeatedly submits PRs with poor test coverage and non-standard Java patterns. How do you handle code reviews for this engineer?",
                    "type": "mcq",
                    "options": [
                        "A) Reject every PR with generic harsh comments like 'Fix this'.",
                        "B) Pair-program with the developer on a PR, explaining the 'why' behind testing standards and coding guidelines.",
                        "C) Approve the code to avoid hurting their feelings, then silently fix it yourself.",
                        "D) Ask management to remove the junior developer from your team."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "Adhering to agreed-upon team standards for Java code structure, even when you personally prefer a different style, demonstrates professional ___.",
                    "type": "fib",
                    "correct_answer": "alignment"
                },
                {
                    "question_number": 13,
                    "question": "You notice that two sub-teams are building separate Java services that duplicate significant core domain logic. What is the best step to take?",
                    "type": "mcq",
                    "options": [
                        "A) Do nothing; let each team maintain their duplicate code.",
                        "B) Initiate a joint technical alignment meeting to discuss extracting common functionality into a shared library or common service.",
                        "C) Write a blog post mocking the redundancy.",
                        "D) Delete one team's code without telling them."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "Taking ownership of a complex Java module failure in production and leading the remediation process displays strong professional ___.",
                    "type": "fib",
                    "correct_answer": "responsibility"
                },
                {
                    "question_number": 15,
                    "question": "Describe a scenario where you had to optimize the performance of a slow Java application under tight time constraints.",
                    "type": "descriptive",
                    "correct_answer": "Look for data-driven approach (using profilers like JProfiler/VisualVM, measuring before/after), identifying bottlenecks (DB queries, algorithm complexity, object allocation), and pragmatic trade-off management."
                },
                {
                    "question_number": 16,
                    "question": "Midway through a sprint, a key requirement for your Java microservice changes dramatically. What is your approach?",
                    "type": "mcq",
                    "options": [
                        "A) Continue building the old requirement to finish your assigned sprint commitment.",
                        "B) Immediately pause, evaluate the impact with the team/PO, re-estimate tasks, and adjust sprint backlog accordingly.",
                        "C) Complain publicly in the sprint retrospective about management's incompetence.",
                        "D) Rush to build both versions just in case."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "Translating complex Java system architecture concepts into clear business impact terms for Product Managers requires strong technical ___.",
                    "type": "fib",
                    "correct_answer": "communication"
                },
                {
                    "question_number": 18,
                    "question": "You discover a critical security vulnerability in a third-party Java dependency (e.g., Log4j-style issue) used across multiple services. What is your initial action?",
                    "type": "mcq",
                    "options": [
                        "A) Wait for the next scheduled quarterly release to patch it.",
                        "B) Flag the severity to engineering leadership, help audit impacted services, and coordinate emergency patch deployments.",
                        "C) Send an email to all developers telling them to stop writing Java.",
                        "D) Keep quiet so hackers don't notice it."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "Consistently documenting architectural decisions using Lightweight Architecture Decision Records (ADRs) ensures organizational ___.",
                    "type": "fib",
                    "correct_answer": "transparency"
                },
                {
                    "question_number": 20,
                    "question": "Share an experience where you had to balance trade-offs between clean code architecture and rapid time-to-market for a Java service.",
                    "type": "descriptive",
                    "correct_answer": "Look for pragmatic engineering judgment, conscious creation of managed technical debt, clear documentation of trade-offs, and follow-up plans to pay down debt."
                }
            ],
            "Hard": [
                {
                    "question_number": 1,
                    "question": "As a Senior/Lead Java Engineer, you are leading a migration from Java 8 to Java 21 across 50+ microservices. Several team leads resist, claiming it interrupts feature delivery. How do you lead this initiative?",
                    "type": "mcq",
                    "options": [
                        "A) Mandate the upgrade immediately via executive order, penalizing non-compliant teams.",
                        "B) Build a business and technical case showing performance/cost benefits, create automated migration tools, run a pilot, and partner with leads to phase the rollout.",
                        "C) Abandon the migration project to keep all engineering teams happy.",
                        "D) Perform the migration for all 50 services by yourself over the weekend."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "Establishing clear Java technical visions while rallying resistant engineering teams requires strategic ___.",
                    "type": "fib",
                    "correct_answer": "leadership"
                },
                {
                    "question_number": 3,
                    "question": "During a high-severity production outage caused by a deadlock in a newly deployed Java service, executive management demands immediate hourly updates while engineers are debugging. How do you manage this crisis?",
                    "type": "mcq",
                    "options": [
                        "A) Force the engineers to join the executive call and answer questions live.",
                        "B) Appoint yourself or a dedicated liaison as Incident Commander to communicate with executives while shielding developers to focus on resolution.",
                        "C) Ignore executive messages until the system is fully restored.",
                        "D) Revert all cloud infrastructure and resign from the position."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "Shielding your engineering team from external organizational friction during high-stress deployments protects team ___.",
                    "type": "fib",
                    "correct_answer": "focus"
                },
                {
                    "question_number": 5,
                    "question": "Describe a scenario where two Principal Java Architects held opposing, firm views on system architecture (e.g., Event-Driven Microservices vs. Modular Monolith). How did you mediate and resolve the conflict?",
                    "type": "descriptive",
                    "correct_answer": "Look for objective evaluation framework creation, focusing on business requirements and constraints over dogma, facilitating consensus-building, and establishing clear decision ownership."
                },
                {
                    "question_number": 6,
                    "question": "A senior Java developer on your team is technically brilliant but exhibits toxic behavior in PR reviews, discouraging junior engineers. How do you address this?",
                    "type": "mcq",
                    "options": [
                        "A) Ignore the behavior because their technical output is irreplaceable.",
                        "B) Conduct a private 1-on-1 using radical candor, detailing specific behavioral instances, establishing expectations, and monitoring progress.",
                        "C) Publicly call out the senior developer in a team retrospective meeting.",
                        "D) Reassign all junior developers away so they don't interact with the senior engineer."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "Nurturing psychological safety while maintaining high standards of code quality in Java engineering teams requires balanced ___.",
                    "type": "fib",
                    "correct_answer": "emotional intelligence"
                },
                {
                    "question_number": 8,
                    "question": "Your company decides to transition from self-hosted Java applications to cloud-native Kubernetes deployments. Half the team lacks DevOps experience. What strategy do you implement?",
                    "type": "mcq",
                    "options": [
                        "A) Replace non-cloud engineers with external cloud consultants.",
                        "B) Design a comprehensive upskilling program, establish golden-path CI/CD templates, and pair experienced engineers with learners.",
                        "C) Expect engineers to learn everything in their personal time.",
                        "D) Cancel the cloud migration initiative to avoid friction."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "Empowering team members to make autonomous architectural decisions within safe guardrails fosters organizational ___.",
                    "type": "fib",
                    "correct_answer": "scalability"
                },
                {
                    "question_number": 10,
                    "question": "Walk through how you conducted a blameless post-mortem following a major Java application crash caused by improper garbage collection configuration.",
                    "type": "descriptive",
                    "correct_answer": "Look for focus on systemic root causes rather than individual error, actionable preventive measures (monitoring, tuning, load testing), open communication, and sharing learnings organization-wide."
                },
                {
                    "question_number": 11,
                    "question": "Executive leadership mandates a 30% reduction in cloud infrastructure costs for your Java microservice ecosystem without degrading SLAs. How do you lead this effort?",
                    "type": "mcq",
                    "options": [
                        "A) Arbitrarily shut down 30% of application pods across all environments.",
                        "B) Refuse the mandate, stating that infrastructure cannot be optimized further.",
                        "C) Analyze system metrics, conduct profiling (JVM memory tuning, right-sizing containers, GraalVM/Native images examination), and execute a prioritized optimization plan.",
                        "D) Tell developers to work overtime to rewrite all Java services in C++."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 12,
                    "question": "Sustaining team morale during prolonged high-pressure delivery cycles requires active empathetic ___.",
                    "type": "fib",
                    "correct_answer": "advocacy"
                },
                {
                    "question_number": 13,
                    "question": "You discover that an vendor-supplied Java library critical to core business operations is being deprecated and has unpatched security vulnerabilities. How do you manage this strategic risk?",
                    "type": "mcq",
                    "options": [
                        "A) Continue using the library and hope security audits do not catch it.",
                        "B) Conduct a risk assessment, propose build-vs-replace options with cost/timeline estimates, present to leadership, and initiate a phased migration.",
                        "C) Fork the library secretly and attempt to maintain it alone indefinitely.",
                        "D) Blame the vendor publicly and freeze all deployment pipelines."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "Fostering an engineering culture where developers actively share Java best practices across business units requires cross-team ___.",
                    "type": "fib",
                    "correct_answer": "collaboration"
                },
                {
                    "question_number": 15,
                    "question": "Describe a time when you had to make an unpopular technical decision regarding Java technology stack choices (e.g., framework, JDK version, build tool). How did you gain buy-in?",
                    "type": "descriptive",
                    "correct_answer": "Look for objective rationale, active listening to team concerns, transparent decision-making frameworks, clear communication of long-term vision, and helping the team transition smoothly."
                },
                {
                    "question_number": 16,
                    "question": "Your engineering organization is scaling rapidly from 15 to 80 Java developers. Development standards are becoming fragmented across teams. What leadership action do you take?",
                    "type": "mcq",
                    "options": [
                        "A) Personally review every pull request across all teams.",
                        "B) Establish a Java Community of Practice, define shared architecture principles, implement automated linter/governance tools in CI pipelines, and empower tech leads.",
                        "C) Mandate that all teams merge back into a single monolithic codebase.",
                        "D) Allow every team to adopt whatever standards they want without coordination."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "Aligning technical roadmap goals for Java infrastructure with long-term business objectives demonstrates strategic ___.",
                    "type": "fib",
                    "correct_answer": "vision"
                },
                {
                    "question_number": 18,
                    "question": "A key client requires a custom non-standard Java feature integration that violates your team's microservice architecture standards. How do you handle this executive pressure?",
                    "type": "mcq",
                    "options": [
                        "A) Build a messy workaround inside the core service to satisfy the client immediately.",
                        "B) Reject the client request abruptly without offering alternatives.",
                        "C) Work with Product Leadership to offer an extensible plugin/adapter pattern architecture that satisfies the requirement without compromising core integrity.",
                        "D) Resign from the project in protest."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 19,
                    "question": "Creating clear career progression pathways for senior Java engineers into technical leadership roles enhances talent ___.",
                    "type": "fib",
                    "correct_answer": "retention"
                },
                {
                    "question_number": 20,
                    "question": "Describe a situation where you had to manage an underperforming senior Java developer. What steps did you take to help them recover, or how did you handle performance management?",
                    "type": "descriptive",
                    "correct_answer": "Look for early clear feedback, identifying root causes (skill gap, personal issue, burnout), creating structured measurable improvement plans (PIP), providing support, and acting decisively if expectations are not met."
                }
            ]
        }
    },
    "Data Analyst": {
        "Technical": {
            "Easy": [
                {
                    "question_number": 1,
                    "question": "Which SQL clause is used to filter rows based on a specified condition?",
                    "type": "mcq",
                    "options": [
                        "A) GROUP BY",
                        "B) WHERE",
                        "C) ORDER BY",
                        "D) HAVING"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "In Excel, the formula to find the average of a range of cells from A1 to A10 is =AVERAGE(_____).",
                    "type": "fib",
                    "correct_answer": "A1:A10"
                },
                {
                    "question_number": 3,
                    "question": "Which Python library is primarily used for data manipulation and analysis using DataFrames?",
                    "type": "mcq",
                    "options": [
                        "A) Matplotlib",
                        "B) Pandas",
                        "C) Requests",
                        "D) Flask"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "In a relational database, a column or set of columns that uniquely identifies each row in a table is called a primary _____.",
                    "type": "fib",
                    "correct_answer": "key"
                },
                {
                    "question_number": 5,
                    "question": "Explain the difference between a bar chart and a histogram.",
                    "type": "descriptive",
                    "correct_answer": "Bar charts display categorical data with spaces between bars, whereas histograms display continuous numerical data grouped into bins with no spaces between bars."
                },
                {
                    "question_number": 6,
                    "question": "What type of join returns all records when there is a match in either the left or the right table?",
                    "type": "mcq",
                    "options": [
                        "A) INNER JOIN",
                        "B) LEFT JOIN",
                        "C) FULL OUTER JOIN",
                        "D) CROSS JOIN"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 7,
                    "question": "To count the number of rows in a Pandas DataFrame nameddf, you can use the attribute df._____.",
                    "type": "fib",
                    "correct_answer": "shape"
                },
                {
                    "question_number": 8,
                    "question": "Which measure of central tendency is most sensitive to extreme outliers?",
                    "type": "mcq",
                    "options": [
                        "A) Median",
                        "B) Mode",
                        "C) Mean",
                        "D) Interquartile Range"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 9,
                    "question": "In Power BI or Tableau, a field that can be aggregated or used to slice data into categories is commonly referred to as a _____.",
                    "type": "fib",
                    "correct_answer": "dimension"
                },
                {
                    "question_number": 10,
                    "question": "Describe how you would handle missing values in a small dataset where removing rows would result in losing critical information.",
                    "type": "descriptive",
                    "correct_answer": "Imputation methods should be used, such as filling missing values with the mean, median, mode, or using predictive modeling based on other variables."
                },
                {
                    "question_number": 11,
                    "question": "Which Excel function is commonly used to perform a vertical lookup for a value in the leftmost column of a table?",
                    "type": "mcq",
                    "options": [
                        "A) HLOOKUP",
                        "B) VLOOKUP",
                        "C) XMATCH",
                        "D) INDEX"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "In SQL, to remove duplicate rows from a query result set, you use the _____ keyword.",
                    "type": "fib",
                    "correct_answer": "DISTINCT"
                },
                {
                    "question_number": 13,
                    "question": "Which Seaborn function is best suited for visualizing the distribution of a single continuous numerical variable?",
                    "type": "mcq",
                    "options": [
                        "A) sns.scatterplot()",
                        "B) sns.barplot()",
                        "C) sns.histplot()",
                        "D) sns.heatmap()"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 14,
                    "question": "The probability of an event occurring given that another event has already occurred is known as _____ probability.",
                    "type": "fib",
                    "correct_answer": "conditional"
                },
                {
                    "question_number": 15,
                    "question": "What is data cleansing and why is it an essential first step in data analysis?",
                    "type": "descriptive",
                    "correct_answer": "Data cleansing involves detecting and correcting corrupt, inaccurate, or duplicate records from a dataset. It is essential because dirty data leads to flawed insights and incorrect decision-making."
                },
                {
                    "question_number": 16,
                    "question": "In a data warehouse, what type of schema is characterized by a central fact table surrounded by denormalized dimension tables?",
                    "type": "mcq",
                    "options": [
                        "A) Snowflake schema",
                        "B) Star schema",
                        "C) Galaxy schema",
                        "D) Network schema"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "To convert a string column containing dates into actual datetime objects in Pandas, you use pd.to______().",
                    "type": "fib",
                    "correct_answer": "datetime"
                },
                {
                    "question_number": 18,
                    "question": "What does ETL stand for in data engineering and data warehousing?",
                    "type": "mcq",
                    "options": [
                        "A) Extract, Transform, Load",
                        "B) Evaluate, Test, Launch",
                        "C) Encrypt, Transport, Log",
                        "D) Edit, Trace, Link"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 19,
                    "question": "In statistics, the difference between the 75th percentile and the 25th percentile is called the Interquartile _____.",
                    "type": "fib",
                    "correct_answer": "Range"
                },
                {
                    "question_number": 20,
                    "question": "Explain the concept of correlation vs. causation using a brief example.",
                    "type": "descriptive",
                    "correct_answer": "Correlation means two variables move together, while causation means one variable causes the other. Example: Ice cream sales and shark attacks are correlated due to warm weather, but ice cream does not cause shark attacks."
                }
            ],
            "Medium": [
                {
                    "question_number": 1,
                    "question": "Which SQL window function assigns a unique sequential integer to rows within a partition of a result set, starting at 1 for the first row in each partition?",
                    "type": "mcq",
                    "options": [
                        "A) RANK()",
                        "B) DENSE_RANK()",
                        "C) ROW_NUMBER()",
                        "D) NTILE()"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 2,
                    "question": "In Pandas, to combine two DataFrames based on a common column index or key, you use the pd._____() function.",
                    "type": "fib",
                    "correct_answer": "merge"
                },
                {
                    "question_number": 3,
                    "question": "What is the primary purpose of a Common Table Expression (CTE) in SQL?",
                    "type": "mcq",
                    "options": [
                        "A) To permanently store data in a new table",
                        "B) To improve query readability and allow recursive queries",
                        "C) To index large columns automatically",
                        "D) To replace all JOIN operations"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "In hypothesis testing, the threshold probability used to reject the null hypothesis is commonly denoted by the Greek letter alpha (_____).",
                    "type": "fib",
                    "correct_answer": "\u03b1"
                },
                {
                    "question_number": 5,
                    "question": "Explain how an A/B test is structured and how statistical significance helps determine the winning variant.",
                    "type": "descriptive",
                    "correct_answer": "An A/B test splits users randomly into a control (A) and variant (B) group to compare performance metrics. Statistical significance (p-value < 0.05) ensures the observed difference is due to the change rather than random chance."
                },
                {
                    "question_number": 6,
                    "question": "Which of the following is true about a LEFT JOIN when the right table has multiple matching rows for a single row in the left table?",
                    "type": "mcq",
                    "options": [
                        "A) The row is duplicated for each match in the right table",
                        "B) Only the first matching row is returned",
                        "C) An error is thrown",
                        "D) The query returns NULL for all columns"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 7,
                    "question": "In Excel, to perform a flexible lookup that can search in any direction (both left and right), you should use the _____ function instead of VLOOKUP.",
                    "type": "fib",
                    "correct_answer": "XLOOKUP"
                },
                {
                    "question_number": 8,
                    "question": "What statistical test is best used to determine if there is a significant association between two categorical variables?",
                    "type": "mcq",
                    "options": [
                        "A) Student's t-test",
                        "B) ANOVA",
                        "C) Chi-Square Test of Independence",
                        "D) Pearson Correlation"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 9,
                    "question": "In data warehousing, a table that stores measurable, quantitative data for analysis (such as sales amount or quantity sold) is called a _____ table.",
                    "type": "fib",
                    "correct_answer": "fact"
                },
                {
                    "question_number": 10,
                    "question": "Describe the difference between inner join and outer join in SQL, and provide a scenario where you would use a full outer join.",
                    "type": "descriptive",
                    "correct_answer": "Inner join returns only matching records from both tables. Outer join returns matching records plus unmatched records from one or both tables. Full outer join is used when you need to see all records from both datasets and identify matches and mismatches on both sides (e.g., reconciling two separate system logs)."
                },
                {
                    "question_number": 11,
                    "question": "In Pandas, what method is used to reshape a DataFrame by pivoting columns into rows?",
                    "type": "mcq",
                    "options": [
                        "A) pivot()",
                        "B) melt()",
                        "C) stack()",
                        "D) explode()"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "In Tableau, calculations that are computed on the aggregated data in the view rather than at the row level are known as _____ calculations.",
                    "type": "fib",
                    "correct_answer": "aggregate"
                },
                {
                    "question_number": 13,
                    "question": "What is a Type I error in hypothesis testing?",
                    "type": "mcq",
                    "options": [
                        "A) Rejecting a true null hypothesis (False Positive)",
                        "B) Failing to reject a false null hypothesis (False Negative)",
                        "C) Accepting a false alternative hypothesis",
                        "D) Choosing the wrong sample size"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 14,
                    "question": "In Python, to group a Pandas DataFrame by a column and calculate the mean of another column, you use df.groupby('col1')['col2']._____().",
                    "type": "fib",
                    "correct_answer": "mean"
                },
                {
                    "question_number": 15,
                    "question": "How do you handle skewed data when preparing it for statistical modeling or visualization?",
                    "type": "descriptive",
                    "correct_answer": "Skewed data can be handled using transformations such as log transformation, square root transformation, or Box-Cox transformation to make the distribution more normal and reduce the impact of outliers."
                },
                {
                    "question_number": 16,
                    "question": "Which SQL clause is executed after the grouping of data, specifically to filter aggregated results?",
                    "type": "mcq",
                    "options": [
                        "A) WHERE",
                        "B) HAVING",
                        "C) FILTER",
                        "D) QUALIFY"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "To compute the rolling or moving average of a time-series column in Pandas, you use the _____ function.",
                    "type": "fib",
                    "correct_answer": "rolling"
                },
                {
                    "question_number": 18,
                    "question": "What is the primary difference between a Star Schema and a Snowflake Schema?",
                    "type": "mcq",
                    "options": [
                        "A) Snowflake schemas normalize dimension tables, whereas star schemas denormalize them",
                        "B) Star schemas do not use fact tables",
                        "C) Snowflake schemas are faster for all queries",
                        "D) Star schemas require more storage space"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 19,
                    "question": "In Power BI, the formula language used to create calculated columns and measures is called _____.",
                    "type": "fib",
                    "correct_answer": "DAX"
                },
                {
                    "question_number": 20,
                    "question": "Explain the concept of multicollinearity in regression analysis and why it is problematic for data analysts.",
                    "type": "descriptive",
                    "correct_answer": "Multicollinearity occurs when independent variables in a regression model are highly correlated. It is problematic because it destabilizes coefficient estimates, makes models sensitive to small changes in data, and makes it difficult to determine the individual effect of each predictor."
                }
            ],
            "Hard": [
                {
                    "question_number": 1,
                    "question": "When writing an advanced SQL query to calculate running totals across a partition, which window frame specification ensures the sum includes all rows from the start of the partition up to the current row?",
                    "type": "mcq",
                    "options": [
                        "A) ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING",
                        "B) ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW",
                        "C) RANGE BETWEEN 1 PRECEDING AND 1 FOLLOWING",
                        "D) ROWS BETWEEN 1 PRECEDING AND CURRENT ROW"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "In Pandas, to apply a custom scalar function element-wise across a DataFrame column efficiently without using a slow Python for-loop, you can use the ._____() method.",
                    "type": "fib",
                    "correct_answer": "map"
                },
                {
                    "question_number": 3,
                    "question": "How does a Self-Join differ from standard joins, and what is its primary use case?",
                    "type": "mcq",
                    "options": [
                        "A) It joins a table to itself, useful for hierarchical or sequential data like employee-manager relationships",
                        "B) It creates an automatic backup of the table",
                        "C) It joins two identical databases on different servers",
                        "D) It only works with temporary tables"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 4,
                    "question": "In A/B testing, when sample sizes are small or data violates normality assumptions, analysts often use non-parametric tests such as the Mann-Whitney _____ test.",
                    "type": "fib",
                    "correct_answer": "U"
                },
                {
                    "question_number": 5,
                    "question": "Design an ETL pipeline architecture for a real-time streaming e-commerce application processing millions of clickstream events daily. Outline the ingestion, processing, and storage components.",
                    "type": "descriptive",
                    "correct_answer": "Ingestion via Apache Kafka or AWS Kinesis for real-time event streaming; processing using Apache Flink or Spark Streaming for transformation and aggregation; storage in a data lake (S3/GCS) for raw data and a cloud data warehouse (Snowflake/BigQuery) or NoSQL store for structured querying and analytics."
                },
                {
                    "question_number": 6,
                    "question": "Which of the following scenarios describes the Simpson's Paradox?",
                    "type": "mcq",
                    "options": [
                        "A) A trend appearing in different groups of data disappears or reverses when these groups are combined",
                        "B) Two variables show high correlation without any logical causation",
                        "C) A statistical test fails due to multicollinearity",
                        "D) Missing data completely invalidates the mean calculation"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 7,
                    "question": "In advanced SQL performance tuning, creating an index on a table can speed up SELECT queries, but it typically slows down _____ operations like INSERT, UPDATE, and DELETE.",
                    "type": "fib",
                    "correct_answer": "DML"
                },
                {
                    "question_number": 8,
                    "question": "What is the purpose of using a stratified sampling technique in survey design or machine learning data splitting?",
                    "type": "mcq",
                    "options": [
                        "A) To ensure the proportion of samples in each subgroup matches the population distribution",
                        "B) To randomly select every nth record from a sorted file",
                        "C) To maximize the variance of the sample dataset",
                        "D) To eliminate all missing values automatically"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 9,
                    "question": "In Pandas, to handle complex multi-conditional filtering and aggregation across hierarchical index levels, you can use the ._____ accessor.",
                    "type": "fib",
                    "correct_answer": "xs"
                },
                {
                    "question_number": 10,
                    "question": "Explain how you would diagnose and resolve a severe performance bottleneck in a complex SQL query that joins five large tables and times out.",
                    "type": "descriptive",
                    "correct_answer": "Use EXPLAIN or EXPLAIN PLAN to analyze the query execution plan. Look for full table scans, high-cost nested loops, and missing indexes on join and filter columns. Optimize by adding appropriate indexes, rewriting subqueries as JOINs or CTEs, filtering data early before joining, and updating table statistics."
                },
                {
                    "question_number": 11,
                    "question": "Which time series decomposition method assumes that the seasonal component is constant in magnitude throughout the series?",
                    "type": "mcq",
                    "options": [
                        "A) Multiplicative decomposition",
                        "B) Additive decomposition",
                        "C) Exponential smoothing",
                        "D) ARIMA modeling"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "When dealing with high-dimensional datasets in analytics, dimensionality reduction techniques like Principal Component Analysis (PCA) project data onto orthogonal axes that maximize _____.",
                    "type": "fib",
                    "correct_answer": "variance"
                },
                {
                    "question_number": 13,
                    "question": "What is the primary risk of performing multiple pairwise t-tests across multiple treatment groups in an experiment?",
                    "type": "mcq",
                    "options": [
                        "A) Increased probability of a Type I error (Family-wise Error Rate inflation)",
                        "B) Decreased statistical power",
                        "C) Guaranteed multicollinearity",
                        "D) Automatic normalization failure"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 14,
                    "question": "In database architecture, the process of structuring a relational database to reduce data redundancy and improve data integrity is called _____.",
                    "type": "fib",
                    "correct_answer": "normalization"
                },
                {
                    "question_number": 15,
                    "question": "Walk through the statistical and methodological steps you would take to design an A/B test for a new checkout button, ensuring no leakage and calculating required sample size.",
                    "type": "descriptive",
                    "correct_answer": "Define the primary metric (conversion rate) and secondary metrics. Determine baseline conversion rate and Minimum Detectable Effect (MDE). Calculate sample size using statistical power (typically 80%) and alpha (0.05). Ensure proper randomization (cookie or user ID hashing) to prevent sample ratio mismatch (SRM) and data leakage."
                },
                {
                    "question_number": 16,
                    "question": "Which analytical technique is most appropriate for identifying distinct customer segments based on purchasing behavior without predefined labels?",
                    "type": "mcq",
                    "options": [
                        "A) Linear Regression",
                        "B) K-Means Clustering",
                        "C) Logistic Regression",
                        "D) Decision Tree Classification"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "In SQL, to evaluate a list of conditions and return one of multiple possible result expressions, you use the _____ expression.",
                    "type": "fib",
                    "correct_answer": "CASE"
                },
                {
                    "question_number": 18,
                    "question": "What does a p-value less than 0.05 signify in the context of hypothesis testing?",
                    "type": "mcq",
                    "options": [
                        "A) There is less than a 5% probability that the observed results occurred purely by random chance under the null hypothesis",
                        "B) The null hypothesis is definitely true",
                        "C) The sample size was 5% too small",
                        "D) The probability of a Type II error is 5%"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 19,
                    "question": "In Python, to execute high-performance vectorized numerical operations across multi-dimensional arrays, data analysts rely heavily on the _____ library.",
                    "type": "fib",
                    "correct_answer": "NumPy"
                },
                {
                    "question_number": 20,
                    "question": "Describe how you would approach anomaly detection in a time-series dataset representing server CPU utilization. What methods would you consider?",
                    "type": "descriptive",
                    "correct_answer": "Approach includes checking for seasonality and trend, cleaning missing timestamps, and establishing a baseline. Methods considered include rolling z-score / moving average thresholds, Seasonal Hybrid ESD (Statsmodels/Twitter anomaly detection), Isolation Forests, or LSTM autoencoders for complex multivariate patterns."
                }
            ]
        },
        "HR": {
            "Easy": [
                {
                    "question_number": 1,
                    "question": "A stakeholder asks for a report by EOD, but you are behind schedule. What do you do?",
                    "type": "mcq",
                    "options": [
                        "A) Ignore the request",
                        "B) Communicate the delay and provide an updated ETA",
                        "C) Send incomplete data",
                        "D) Work through the weekend without telling anyone"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "In a team environment, being ________ means you actively listen to teammates and build upon their ideas.",
                    "type": "fib",
                    "correct_answer": "collaborative"
                },
                {
                    "question_number": 3,
                    "question": "You find an error in your previous data submission. How should you handle it?",
                    "type": "mcq",
                    "options": [
                        "A) Hope nobody notices",
                        "B) Delete the file",
                        "C) Notify your manager immediately and offer a correction",
                        "D) Blame the data source software"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 4,
                    "question": "When explaining data to non-technical staff, you should use ________ language to ensure clarity.",
                    "type": "fib",
                    "correct_answer": "accessible"
                },
                {
                    "question_number": 5,
                    "question": "Describe a time you had to learn a new software tool quickly to finish a project.",
                    "type": "descriptive",
                    "correct_answer": "Demonstrates adaptability, self-directed learning, and resourcefulness."
                },
                {
                    "question_number": 6,
                    "question": "What is the best way to handle conflicting requirements from two different managers?",
                    "type": "mcq",
                    "options": [
                        "A) Prioritize the one who asked first",
                        "B) Prioritize the most senior manager",
                        "C) Set up a meeting with both to clarify business priorities",
                        "D) Do both poorly"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 7,
                    "question": "Maintaining ________ is critical when handling sensitive company or user information.",
                    "type": "fib",
                    "correct_answer": "data integrity"
                },
                {
                    "question_number": 8,
                    "question": "If you are unsure about the definition of a specific KPI, what is your first step?",
                    "type": "mcq",
                    "options": [
                        "A) Guess based on context",
                        "B) Ask a colleague or manager for documentation",
                        "C) Skip the KPI entirely",
                        "D) Use a generic industry standard"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "Being ________ involves checking your own work multiple times before sharing it with stakeholders.",
                    "type": "fib",
                    "correct_answer": "detail-oriented"
                },
                {
                    "question_number": 10,
                    "question": "Describe a situation where you had to manage your time effectively to meet a strict deadline.",
                    "type": "descriptive",
                    "correct_answer": "Demonstrates prioritization skills, time-boxing, and stress management."
                },
                {
                    "question_number": 11,
                    "question": "How do you respond to constructive feedback on a report you submitted?",
                    "type": "mcq",
                    "options": [
                        "A) Defend your work",
                        "B) Accept it and ask for specific ways to improve the next iteration",
                        "C) Ignore the feedback",
                        "D) Take it personally and quit"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "A key soft skill for data analysts is ________, which helps in translating data into business actions.",
                    "type": "fib",
                    "correct_answer": "communication"
                },
                {
                    "question_number": 13,
                    "question": "If you notice a trend in the data that contradicts current company strategy, what do you do?",
                    "type": "mcq",
                    "options": [
                        "A) Suppress the finding",
                        "B) Prepare a report showing the evidence neutrally",
                        "C) Change the data to fit the strategy",
                        "D) Tell your colleagues only"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "Constructive ________ with teammates leads to more accurate data interpretations.",
                    "type": "fib",
                    "correct_answer": "peer review"
                },
                {
                    "question_number": 15,
                    "question": "Describe a time you had to clarify a vague request from a stakeholder.",
                    "type": "descriptive",
                    "correct_answer": "Demonstrates questioning skills, active listening, and business acumen."
                },
                {
                    "question_number": 16,
                    "question": "What is the best way to handle a data project where you lack necessary access rights?",
                    "type": "mcq",
                    "options": [
                        "A) Find a workaround",
                        "B) Report the issue to IT/Manager with a request for specific access",
                        "C) Stop working indefinitely",
                        "D) Try to hack the password"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "Having a ________ mindset means you are constantly looking for ways to improve your data processes.",
                    "type": "fib",
                    "correct_answer": "growth"
                },
                {
                    "question_number": 18,
                    "question": "Which quality is most important when presenting data to a non-technical audience?",
                    "type": "mcq",
                    "options": [
                        "A) Mathematical complexity",
                        "B) Simplicity and storytelling",
                        "C) Using as many charts as possible",
                        "D) Using technical jargon"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "Your ________ of the data should be clearly documented for others to follow your steps.",
                    "type": "fib",
                    "correct_answer": "methodology"
                },
                {
                    "question_number": 20,
                    "question": "Describe a situation where you had to work with a teammate whose working style was very different from yours.",
                    "type": "descriptive",
                    "correct_answer": "Demonstrates empathy, adaptability, and conflict resolution."
                }
            ],
            "Medium": [
                {
                    "question_number": 1,
                    "question": "A stakeholder disagrees with your findings. What is your approach?",
                    "type": "mcq",
                    "options": [
                        "A) Stick to your guns blindly",
                        "B) Validate your methodology, present your logic, and listen to their objections",
                        "C) Give in to their opinion",
                        "D) Tell them the data doesn't lie"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "Stakeholder ________ is essential when projects involve multiple departments with different goals.",
                    "type": "fib",
                    "correct_answer": "alignment"
                },
                {
                    "question_number": 3,
                    "question": "You discover a systemic data quality issue impacting multiple dashboards. What is your priority?",
                    "type": "mcq",
                    "options": [
                        "A) Fix it silently",
                        "B) Communicate the impact to stakeholders immediately and provide a timeline for a fix",
                        "C) Wait for someone to complain",
                        "D) Blame the database engineer"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "Good data storytelling turns raw numbers into ________ information.",
                    "type": "fib",
                    "correct_answer": "actionable"
                },
                {
                    "question_number": 5,
                    "question": "Describe a time you identified a business opportunity using data that wasn't explicitly requested.",
                    "type": "descriptive",
                    "correct_answer": "Demonstrates proactivity, business value identification, and analytical depth."
                },
                {
                    "question_number": 6,
                    "question": "How do you manage 'scope creep' during a long-term analytical project?",
                    "type": "mcq",
                    "options": [
                        "A) Agree to every change",
                        "B) Politely explain the timeline impact of new requests to the stakeholder",
                        "C) Do the extra work without saying anything",
                        "D) Refuse all changes"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "Providing ________ metrics helps leadership understand the impact of their strategic decisions.",
                    "type": "fib",
                    "correct_answer": "contextual"
                },
                {
                    "question_number": 8,
                    "question": "You realize a project will miss its deadline. What is the most professional way to handle this?",
                    "type": "mcq",
                    "options": [
                        "A) Keep working and hope for the best",
                        "B) Proactively inform stakeholders early, explaining reasons and mitigation plans",
                        "C) Send an email at the deadline",
                        "D) Ask for help on the day of the deadline"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "Managing expectations is a key part of ________ management in data roles.",
                    "type": "fib",
                    "correct_answer": "project"
                },
                {
                    "question_number": 10,
                    "question": "Describe a time you had to justify a complex analytical decision to someone without a technical background.",
                    "type": "descriptive",
                    "correct_answer": "Demonstrates communication skills, simplification of complex topics, and patience."
                },
                {
                    "question_number": 11,
                    "question": "How do you handle a situation where data is missing or incomplete for a crucial analysis?",
                    "type": "mcq",
                    "options": [
                        "A) Make up numbers",
                        "B) Clearly state the limitations and assumptions in your report",
                        "C) Cancel the project",
                        "D) Ignore the missing data"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "Establishing clear ________ for data projects prevents confusion later on.",
                    "type": "fib",
                    "correct_answer": "KPIs"
                },
                {
                    "question_number": 13,
                    "question": "Which approach is most effective for long-term knowledge sharing within a data team?",
                    "type": "mcq",
                    "options": [
                        "A) Keeping your code secret",
                        "B) Writing detailed documentation and conducting team walk-throughs",
                        "C) Writing code only you can understand",
                        "D) Relying on verbal instruction only"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "Data ________ is critical when presenting information to prevent misleading visual cues.",
                    "type": "fib",
                    "correct_answer": "governance"
                },
                {
                    "question_number": 15,
                    "question": "Describe a time you had to pivot your approach mid-analysis due to a change in business goals.",
                    "type": "descriptive",
                    "correct_answer": "Demonstrates flexibility, quick thinking, and organizational awareness."
                },
                {
                    "question_number": 16,
                    "question": "If you are asked to perform an analysis that you know is ethically questionable, what do you do?",
                    "type": "mcq",
                    "options": [
                        "A) Comply immediately",
                        "B) Raise your concerns with your manager and discuss the implications",
                        "C) Report them to the police",
                        "D) Quit immediately"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "A strong ________ review process minimizes errors in final dashboard delivery.",
                    "type": "fib",
                    "correct_answer": "quality assurance"
                },
                {
                    "question_number": 18,
                    "question": "What is the best way to handle a peer who refuses to follow standard coding practices?",
                    "type": "mcq",
                    "options": [
                        "A) Publicly call them out",
                        "B) Have a one-on-one conversation explaining the benefits of consistency",
                        "C) Ignore them",
                        "D) Report them to HR"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "Developing a ________ for how data flows helps debug errors faster.",
                    "type": "fib",
                    "correct_answer": "data map"
                },
                {
                    "question_number": 20,
                    "question": "Describe a time you took the lead on a team project to ensure it met organizational standards.",
                    "type": "descriptive",
                    "correct_answer": "Demonstrates leadership, accountability, and commitment to quality."
                }
            ],
            "Hard": [
                {
                    "question_number": 1,
                    "question": "Your department head requests an analysis that you know will be misused. How do you lead through this?",
                    "type": "mcq",
                    "options": [
                        "A) Perform it as requested",
                        "B) Facilitate a meeting to clarify the intent and address the ethical risk/misuse concerns",
                        "C) Perform it but warn others",
                        "D) Refuse the task without explanation"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "Effective leaders foster a culture of ________ where team members feel safe identifying flaws.",
                    "type": "fib",
                    "correct_answer": "psychological safety"
                },
                {
                    "question_number": 3,
                    "question": "A high-visibility project is failing. As the lead, what is your primary move?",
                    "type": "mcq",
                    "options": [
                        "A) Find someone to blame",
                        "B) Take responsibility, assess the root cause, and present a recovery roadmap to stakeholders",
                        "C) Work 24/7 until it is done",
                        "D) Ask for more budget"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "Building ________ with cross-functional leaders is key to moving data-driven initiatives forward.",
                    "type": "fib",
                    "correct_answer": "consensus"
                },
                {
                    "question_number": 5,
                    "question": "Describe a time you had to influence a senior leader's decision using data insights against their prior intuition.",
                    "type": "descriptive",
                    "correct_answer": "Demonstrates persuasiveness, diplomatic communication, and evidence-based decision-making."
                },
                {
                    "question_number": 6,
                    "question": "How do you manage a team member who is technically brilliant but disruptive to team culture?",
                    "type": "mcq",
                    "options": [
                        "A) Let them work alone",
                        "B) Provide direct, behavioral feedback and set clear expectations for cultural conduct",
                        "C) Fire them immediately",
                        "D) Pretend it isn't happening"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "Establishing a data ________ can bridge the gap between technical and business teams.",
                    "type": "fib",
                    "correct_answer": "strategy"
                },
                {
                    "question_number": 8,
                    "question": "Your team is burned out from a heavy workload. What is your leadership response?",
                    "type": "mcq",
                    "options": [
                        "A) Push them harder to finish",
                        "B) Prioritize tasks and negotiate deadlines with stakeholders to alleviate pressure",
                        "C) Offer bonuses",
                        "D) Ignore it"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "Promoting ________ in data collection ensures bias is removed from AI/ML models.",
                    "type": "fib",
                    "correct_answer": "diversity"
                },
                {
                    "question_number": 10,
                    "question": "Describe a time you set up a new data governance process or framework for your team.",
                    "type": "descriptive",
                    "correct_answer": "Demonstrates structural thinking, change management, and long-term vision."
                },
                {
                    "question_number": 11,
                    "question": "How do you handle budget cuts while maintaining the quality of your analytics department?",
                    "type": "mcq",
                    "options": [
                        "A) Cut everyone's salary",
                        "B) Audit project value to deprioritize low-impact tasks and focus on automation",
                        "C) Do less work",
                        "D) Ask for more money"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "Mentoring team members is key to developing ________ within the organization.",
                    "type": "fib",
                    "correct_answer": "internal talent"
                },
                {
                    "question_number": 13,
                    "question": "When presenting to a board, your data suggests a negative outlook. How do you lead the conversation?",
                    "type": "mcq",
                    "options": [
                        "A) Sugarcoat the results",
                        "B) Present the reality clearly and offer evidence-based recommendations for potential pivot points",
                        "C) Present only the positive data",
                        "D) Blame the previous strategy"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "A ________ of success is vital for measuring the health of a data-driven organization.",
                    "type": "fib",
                    "correct_answer": "framework"
                },
                {
                    "question_number": 15,
                    "question": "Describe a time you navigated an organizational restructure while keeping your team focused on data deliverables.",
                    "type": "descriptive",
                    "correct_answer": "Demonstrates stability, emotional intelligence, and change management."
                },
                {
                    "question_number": 16,
                    "question": "What is the best way to handle a massive, company-wide error in a report published by your team?",
                    "type": "mcq",
                    "options": [
                        "A) Delete it",
                        "B) Accept full accountability, communicate the error transparently, and publish a correction immediately",
                        "C) Blame the IT department",
                        "D) Pretend it was intentional"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "Promoting a culture of ________ ensures that every data point can be traced back to its origin.",
                    "type": "fib",
                    "correct_answer": "accountability"
                },
                {
                    "question_number": 18,
                    "question": "When two departments disagree on data definitions, what is your approach as a leader?",
                    "type": "mcq",
                    "options": [
                        "A) Choose the department that pays more",
                        "B) Moderate a meeting to define a single 'source of truth' acceptable to all stakeholders",
                        "C) Let them choose their own",
                        "D) Pick one at random"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "Aligning your data roadmap with the company's ________ is essential for getting leadership buy-in.",
                    "type": "fib",
                    "correct_answer": "strategic goals"
                },
                {
                    "question_number": 20,
                    "question": "Describe a time you had to let go of a legacy reporting system to build something more scalable.",
                    "type": "descriptive",
                    "correct_answer": "Demonstrates technical vision, risk assessment, and long-term planning."
                }
            ]
        },
        "Behavioral": {
            "Easy": [
                {
                    "question_number": 1,
                    "question": "When you receive a dataset with multiple missing values during a routine task, what is the best first step?",
                    "type": "mcq",
                    "options": [
                        "A) Delete all rows with missing values immediately.",
                        "B) Document the missing values and consult documentation or the data provider to understand why they are missing.",
                        "C) Replace all missing values with zeros without checking context.",
                        "D) Ignore the missing values and proceed with the analysis."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "The ability to understand and share the feelings of others, crucial when gathering requirements from non-technical stakeholders, is known as ________.",
                    "type": "fib",
                    "correct_answer": "empathy"
                },
                {
                    "question_number": 3,
                    "question": "A stakeholder asks you to add twenty new metrics to an existing dashboard overnight. How should you respond?",
                    "type": "mcq",
                    "options": [
                        "A) Refuse the request outright because it is too much work.",
                        "B) Add all twenty metrics immediately without formatting them properly.",
                        "C) Acknowledge the request, explain the timeline needed for quality assurance, and discuss which metrics are most critical to prioritize first.",
                        "D) Promise to finish it by morning even if the data is inaccurate."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 4,
                    "question": "The process of verifying that data meets quality standards and business rules before using it in analysis is called data ________.",
                    "type": "fib",
                    "correct_answer": "validation"
                },
                {
                    "question_number": 5,
                    "question": "Describe a time when you had to learn a new tool or programming language quickly to complete a data task. How did you approach the learning curve?",
                    "type": "descriptive",
                    "correct_answer": "Proactive learning, resource utilization, hands-on practice, timely delivery."
                },
                {
                    "question_number": 6,
                    "question": "You notice a discrepancy between a weekly report you generated and a previous report run by a colleague. What is the most professional action?",
                    "type": "mcq",
                    "options": [
                        "A) Assume your report is correct and ignore the colleague's version.",
                        "B) Quietly delete your report to avoid confrontation.",
                        "C) Investigate the methodology and SQL queries used in both reports, then discuss the difference with your colleague constructively.",
                        "D) Blame the colleague publicly in a team meeting."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 7,
                    "question": "When presenting data insights to non-technical audiences, avoiding jargon and focusing on clear takeaways demonstrates effective communication ________.",
                    "type": "fib",
                    "correct_answer": "clarity"
                },
                {
                    "question_number": 8,
                    "question": "If your direct supervisor gives you conflicting instructions on two different data projects with the same deadline, what should you do?",
                    "type": "mcq",
                    "options": [
                        "A) Guess which one is more important and only do that one.",
                        "B) Bring the conflict to your supervisor's attention, present your current workload, and ask for clarification on priority.",
                        "C) Work twice as fast to complete both, sacrificing accuracy.",
                        "D) Stop working entirely until someone else notices."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "Working effectively with team members from different departments to achieve a common analytical goal requires strong ________ skills.",
                    "type": "fib",
                    "correct_answer": "collaboration"
                },
                {
                    "question_number": 10,
                    "question": "Tell me about a time when you received constructive feedback on a data report or visualization. How did you react and what did you change?",
                    "type": "descriptive",
                    "correct_answer": "Openness to feedback, lack of defensiveness, willingness to iterate, improved output."
                },
                {
                    "question_number": 11,
                    "question": "You realize you made a calculation error in a report sent to management yesterday. What is your immediate course of action?",
                    "type": "mcq",
                    "options": [
                        "A) Hope no one notices the error.",
                        "B) Wait until the next regular reporting cycle to fix it.",
                        "C) Promptly notify stakeholders, provide the corrected figures, and briefly explain what caused the error.",
                        "D) Blame the source data for the mistake."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 12,
                    "question": "The trait that allows a data analyst to bounce back from failed queries, messy data, or rejected proposals is known as ________.",
                    "type": "fib",
                    "correct_answer": "resilience"
                },
                {
                    "question_number": 13,
                    "question": "How should you handle sensitive customer PII (Personally Identifiable Information) when running exploratory data analysis?",
                    "type": "mcq",
                    "options": [
                        "A) Share it freely on internal chat channels for easier collaboration.",
                        "B) Mask, anonymize, or securely handle the data in compliance with company privacy policies.",
                        "C) Leave it unencrypted on your local desktop.",
                        "D) Copy it to personal external storage for backup."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "The ability to manage your time and prioritize tasks when faced with multiple ad-hoc data requests is called ________ management.",
                    "type": "fib",
                    "correct_answer": "time"
                },
                {
                    "question_number": 15,
                    "question": "Describe a situation where you had to manage your time effectively to meet a tight deadline for a recurring data report. How did you prioritize your tasks?",
                    "type": "descriptive",
                    "correct_answer": "Prioritization framework, structured approach, time management, meeting deadlines."
                },
                {
                    "question_number": 16,
                    "question": "If a stakeholder asks you to present data in a way that exaggerates a positive trend while hiding negative metrics, what should you do?",
                    "type": "mcq",
                    "options": [
                        "A) Comply fully to keep the stakeholder happy.",
                        "B) Refuse to show any data at all.",
                        "C) Advocate for objective reporting by presenting the balanced picture and explaining why transparent context is vital.",
                        "D) Falsify the underlying database to match their request."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 17,
                    "question": "Remaining open-ended and curious when exploring a new dataset without jumping to premature conclusions is an example of intellectual ________.",
                    "type": "fib",
                    "correct_answer": "curiosity"
                },
                {
                    "question_number": 18,
                    "question": "When documenting your SQL queries and data transformation steps for team handovers, what is the best practice?",
                    "type": "mcq",
                    "options": [
                        "A) Write no comments because the code should be self-explanatory.",
                        "B) Include clear comments, business logic explanations, and version history so others can easily replicate your work.",
                        "C) Use obscure variable names to protect your proprietary workflow.",
                        "D) Only save the final output file without the code."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "The quality of being dependable, honest, and ethical in handling confidential company data is known as ________.",
                    "type": "fib",
                    "correct_answer": "integrity"
                },
                {
                    "question_number": 20,
                    "question": "Describe a project where you collaborated with a non-technical team member to solve a business problem using data. How did you ensure mutual understanding?",
                    "type": "descriptive",
                    "correct_answer": "Cross-functional teamwork, translation of technical terms, active listening, shared success."
                }
            ],
            "Medium": [
                {
                    "question_number": 1,
                    "question": "A product manager insists that a new feature is a success based on one week of high usage data, but you notice seasonality effects and a high churn rate after day 7. How do you handle this disagreement?",
                    "type": "mcq",
                    "options": [
                        "A) Agree with the product manager to avoid conflict.",
                        "B) Dismiss their observation and present your metrics aggressively in a public forum.",
                        "C) Schedule a 1-on-1 walkthrough to present a holistic view of the retention data, explaining the impact of seasonality and churn.",
                        "D) Cancel the feature launch without telling anyone."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 2,
                    "question": "The practice of aligning analytical goals with broader business objectives to ensure maximum impact is known as strategic ________.",
                    "type": "fib",
                    "correct_answer": "alignment"
                },
                {
                    "question_number": 3,
                    "question": "You are halfway through a complex cohort analysis when a senior executive requests an urgent, unrelated ad-hoc analysis that will take two days. What is your best course of action?",
                    "type": "mcq",
                    "options": [
                        "A) Drop the cohort analysis permanently and switch tasks.",
                        "B) Work 24 hours straight without sleeping to finish both.",
                        "C) Communicate transparently with your manager about the trade-off, present the impact on the current timeline, and ask for priority guidance.",
                        "D) Ignore the executive's request completely."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 4,
                    "question": "The skill of guiding discussions with stakeholders to uncover their true underlying business questions rather than just taking their initial data requests at face value is called requirement ________.",
                    "type": "fib",
                    "correct_answer": "elicitation"
                },
                {
                    "question_number": 5,
                    "question": "Describe a time when your preliminary data analysis disproved a long-held assumption by key stakeholders. How did you present these unexpected findings?",
                    "type": "descriptive",
                    "correct_answer": "Tactful communication, evidence-based storytelling, handling pushback, data integrity."
                },
                {
                    "question_number": 6,
                    "question": "During a cross-functional meeting, a marketing lead claims your attribution model is flawed because it undervalues their campaign channel. How do you respond professionally?",
                    "type": "mcq",
                    "options": [
                        "A) Defend the model defensively and state that marketing doesn't understand analytics.",
                        "B) Acknowledge their perspective, invite them to review the underlying logic and assumptions together, and explore potential adjustments if justified.",
                        "C) Immediately rewrite the model to favor their channel to keep the peace.",
                        "D) Escalate the disagreement to the CEO immediately."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "When data pipelines fail unexpectedly and upstream errors corrupt downstream reporting tables, managing the communication and resolution process efficiently requires strong incident ________.",
                    "type": "fib",
                    "correct_answer": "management"
                },
                {
                    "question_number": 8,
                    "question": "You discover that a widely used company dashboard contains a formula error that has been inflating conversion rates for months. What steps should you take?",
                    "type": "mcq",
                    "options": [
                        "A) Quietly fix the formula and hope no one notices the historical drop in numbers.",
                        "B) Fix the formula, perform an audit to determine how long the error existed, notify affected stakeholders transparently, and publish a corrected trend analysis.",
                        "C) Blame the data engineer who built the initial data source.",
                        "D) Delete the dashboard to remove evidence of the error."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "The ability to look beyond surface-level numbers to investigate root causes of anomalies and operational bottlenecks is known as analytical ________.",
                    "type": "fib",
                    "correct_answer": "depth"
                },
                {
                    "question_number": 10,
                    "question": "Tell me about a time when you had to balance speed and accuracy for a high-stakes business decision. How did you determine what 'good enough' data looked like?",
                    "type": "descriptive",
                    "correct_answer": "Risk assessment, pragmatic approach, clear communication of limitations, timely delivery."
                },
                {
                    "question_number": 11,
                    "question": "Two departments request the same customer metric, but each defines it slightly differently, leading to political friction. How do you resolve this?",
                    "type": "mcq",
                    "options": [
                        "A) Provide different numbers to each department to keep them both happy.",
                        "B) Refuse to provide the metric to either team.",
                        "C) Facilitate a workshop to establish a single, standardized corporate definition and document it in the data dictionary.",
                        "D) Choose your favorite department's definition and ignore the other."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 12,
                    "question": "The process of guiding stakeholders away from vanity metrics and toward actionable, value-driven KPIs is called metric ________.",
                    "type": "fib",
                    "correct_answer": "governance"
                },
                {
                    "question_number": 13,
                    "question": "You are tasked with building a predictive model, but the historical data available is biased and sparse. What is your ethical and professional approach?",
                    "type": "mcq",
                    "options": [
                        "A) Build the model anyway and hide the biases in the documentation.",
                        "B) Fabricate synthetic data to make the dataset look robust.",
                        "C) Document the data limitations and biases clearly, evaluate alternative methodologies, and advise stakeholders on the risks of using the model in its current state.",
                        "D) Blame the data collection team and quit the project."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 14,
                    "question": "When managing multiple stakeholders with competing priorities for your analytical queue, establishing a transparent prioritization ________ is essential.",
                    "type": "fib",
                    "correct_answer": "framework"
                },
                {
                    "question_number": 15,
                    "question": "Describe a scenario where you identified an operational inefficiency or data bottleneck independently and proposed a solution that saved the team time.",
                    "type": "descriptive",
                    "correct_answer": "Proactiveness, problem identification, solution implementation, measurable impact."
                },
                {
                    "question_number": 16,
                    "question": "A stakeholder wants to run an A/B test but refuses to wait for the required sample size because they need a decision by tomorrow. How do you handle this?",
                    "type": "mcq",
                    "options": [
                        "A) Run the test for one day and present the statistically underpowered results as definitive truth.",
                        "B) Explain the statistical risks of false positives and sample size requirements, and propose alternative qualitative or historical analyses for quick guidance.",
                        "C) Falsify the sample size in the report to satisfy their demand.",
                        "D) Cancel all A/B testing protocols permanently."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "The structured process of reviewing past projects to identify what went well and what could be improved is called a post- ________.",
                    "type": "fib",
                    "correct_answer": "mortem"
                },
                {
                    "question_number": 18,
                    "question": "When presenting complex statistical findings to executive leadership who have limited time, what is the best strategy?",
                    "type": "mcq",
                    "options": [
                        "A) Walk through every line of your Python script and SQL query in detail.",
                        "B) Lead with the bottom-line business impact, provide high-level visual summaries, and keep technical methodology in the appendix.",
                        "C) Present only raw data tables without any context or summary.",
                        "D) Keep the presentation overly vague to avoid hard questions."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "The ongoing maintenance of data definitions, lineage, and documentation across an organization is known as data ________.",
                    "type": "fib",
                    "correct_answer": "cataloging"
                },
                {
                    "question_number": 20,
                    "question": "Tell me about a time when you had to mediate a disagreement between two teams regarding which metrics to track for a new product launch. What was your role?",
                    "type": "descriptive",
                    "correct_answer": "Mediation, objective facilitation, balancing perspectives, alignment on KPIs."
                }
            ],
            "Hard": [
                {
                    "question_number": 1,
                    "question": "As a lead data analyst, you discover that a core corporate metric used for executive bonuses was calculated incorrectly for the past two quarters due to a legacy pipeline bug. What is your leadership response?",
                    "type": "mcq",
                    "options": [
                        "A) Keep it confidential to protect team morale and fix it quietly going forward.",
                        "B) Immediately escalate to executive leadership and audit the full impact, presenting a transparent account of the error, its root cause, and corrected figures.",
                        "C) Blame the junior analyst who last touched the pipeline.",
                        "D) Resign immediately to avoid association with the error."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "The strategic leadership ability to drive organizational change and decision-making using data insights is often referred to as data ________.",
                    "type": "fib",
                    "correct_answer": "evangelism"
                },
                {
                    "question_number": 3,
                    "question": "Your department is facing severe budget cuts, and executive leadership asks you to justify the ROI of the analytics team using quantitative metrics. How do you approach this challenge?",
                    "type": "mcq",
                    "options": [
                        "A) Refuse to provide metrics and argue that analytics cannot be measured.",
                        "B) Compile a comprehensive impact portfolio highlighting revenue generation, cost savings, and risk mitigation delivered by recent data projects.",
                        "C) Inflate the numbers arbitrarily to look indispensable.",
                        "D) Blame the finance team for not understanding your value."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "The overarching framework an organization uses to manage data availability, usability, integrity, and security is enterprise data ________.",
                    "type": "fib",
                    "correct_answer": "governance"
                },
                {
                    "question_number": 5,
                    "question": "Describe a high-stakes scenario where you had to influence executive leadership to pivot a product or business strategy based entirely on your predictive analysis.",
                    "type": "descriptive",
                    "correct_answer": "Executive influence, robust methodology, strategic storytelling, measurable business pivot."
                },
                {
                    "question_number": 6,
                    "question": "A powerful executive wants to implement a company-wide initiative based on an intuitive hunch, but your thorough exploratory analysis indicates the initiative will likely fail and waste capital. How do you navigate this political minefield?",
                    "type": "mcq",
                    "options": [
                        "A) Stay silent and let the company waste the money.",
                        "B) Publicly humiliate the executive in a board meeting using your charts.",
                        "C) Schedule a strategic briefing to frame your findings constructively, highlighting risks while proposing a low-cost, phased pilot test to validate the hypothesis safely.",
                        "D) Falsify your analysis to support their hunch."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 7,
                    "question": "When scaling an analytics function from a siloed team to a centralized center of excellence, establishing standardized workflows and code reviews is part of analytics ________.",
                    "type": "fib",
                    "correct_answer": "maturity"
                },
                {
                    "question_number": 8,
                    "question": "You are leading a cross-functional data migration project. Halfway through, key data engineers leave the company, threatening the timeline and system integrity. What is your leadership strategy?",
                    "type": "mcq",
                    "options": [
                        "A) Panic and inform the CEO that the project is completely dead.",
                        "B) Assess remaining resources, re-prioritize critical migration milestones, document existing tribal knowledge, and negotiate timeline adjustments with stakeholders.",
                        "C) Work 100 hours a week yourself until burnout occurs.",
                        "D) Blame the departing engineers for sabotaging the company."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "The practice of embedding ethical considerations, fairness, and bias detection into automated analytics pipelines is known as responsible ________.",
                    "type": "fib",
                    "correct_answer": "AI"
                },
                {
                    "question_number": 10,
                    "question": "Tell me about a time when you designed and implemented a company-wide data democratization strategy. How did you balance accessibility with data security?",
                    "type": "descriptive",
                    "correct_answer": "Data democratization, security protocols, role-based access, enablement and training."
                },
                {
                    "question_number": 11,
                    "question": "A newly hired executive demands full, unrestricted database access to raw customer data, bypassing standard compliance protocols and data masking. As the senior data leader, how do you handle this?",
                    "type": "mcq",
                    "options": [
                        "A) Give them total access immediately because they are an executive.",
                        "B) Refuse rudely without offering alternatives.",
                        "C) Uphold security standards by explaining compliance policies, offering role-based access to anonymized views, and facilitating expedited training for compliant access.",
                        "D) Tell them to download the database onto a personal laptop."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 12,
                    "question": "The strategic alignment where data insights directly shape corporate vision and long-term planning is called data-driven ________.",
                    "type": "fib",
                    "correct_answer": "strategy"
                },
                {
                    "question_number": 13,
                    "question": "Your team builds a complex machine learning attribution model, but stakeholders refuse to use it because they 'don't understand the black box.' How do you address adoption?",
                    "type": "mcq",
                    "options": [
                        "A) Force them to use it by locking down access to older models.",
                        "B) Abandon advanced modeling and go back to simple spreadsheets.",
                        "C) Invest in explainable AI techniques (like SHAP/LIME), conduct workshops, and translate model outputs into intuitive business narratives.",
                        "D) Complain that the business stakeholders are not sophisticated enough."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 14,
                    "question": "Building a culture where continuous learning, peer code reviews, and mentorship thrive within an analytics team fosters high technical ________.",
                    "type": "fib",
                    "correct_answer": "excellence"
                },
                {
                    "question_number": 15,
                    "question": "Describe a major crisis where data infrastructure suffered a catastrophic failure during a critical business period (e.g., Black Friday). How did you lead the triage and recovery?",
                    "type": "descriptive",
                    "correct_answer": "Crisis management, decisive leadership, stakeholder communication, root-cause recovery."
                },
                {
                    "question_number": 16,
                    "question": "An external auditor finds compliance vulnerabilities in how your team stores and processes consumer analytics data. What is your immediate executive response?",
                    "type": "mcq",
                    "options": [
                        "A) Dismiss the auditor's findings as overly bureaucratic.",
                        "B) Take immediate ownership, partner with legal and engineering to remediate vulnerabilities, and institute robust compliance checks moving forward.",
                        "C) Hide the audit report from upper management.",
                        "D) Blame the third-party cloud vendor."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "The ability to anticipate future analytical needs of an organization before stakeholders articulate them is a hallmark of proactive ________.",
                    "type": "fib",
                    "correct_answer": "foresight"
                },
                {
                    "question_number": 18,
                    "question": "When mentoring junior analysts, you notice one team member struggling significantly with stakeholder communication and project delivery. How do you mentor them?",
                    "type": "mcq",
                    "options": [
                        "A) Fire them immediately without support.",
                        "B) Take over all their work so they never have to communicate.",
                        "C) Provide constructive feedback, role-play stakeholder meetings, pair up on projects, and create a structured development plan.",
                        "D) Tell them analytics is simply not for them."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 19,
                    "question": "The metric used to measure the financial return generated relative to the resources invested in data infrastructure and team operations is known as ROI or return on ________.",
                    "type": "fib",
                    "correct_answer": "investment"
                },
                {
                    "question_number": 20,
                    "question": "Tell me about a time when you successfully pitched and secured budget for a major enterprise data tooling upgrade. How did you build the business case?",
                    "type": "descriptive",
                    "correct_answer": "Business case formulation, cost-benefit analysis, executive persuasion, strategic investment."
                }
            ]
        }
    },
    "Data Scientist": {
        "Technical": {
            "Easy": [
                {
                    "question_number": 1,
                    "question": "Which Pandas function is used to remove missing values from a DataFrame?",
                    "type": "mcq",
                    "options": [
                        "A) dropna()",
                        "B) remove_null()",
                        "C) fillna()",
                        "D) isna()"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 2,
                    "question": "In SQL, the statement used to combine rows that have equal values in specified columns into summary rows is _____.",
                    "type": "fib",
                    "correct_answer": "GROUP BY"
                },
                {
                    "question_number": 3,
                    "question": "Which metric of central tendency is most sensitive to extreme outliers in a skewed distribution?",
                    "type": "mcq",
                    "options": [
                        "A) Median",
                        "B) Mean",
                        "C) Mode",
                        "D) Interquartile Range"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "The harmonic mean of precision and recall is known as the _____ score.",
                    "type": "fib",
                    "correct_answer": "F1"
                },
                {
                    "question_number": 5,
                    "question": "How would you explain the concept of model overfitting to a non-technical business executive?",
                    "type": "descriptive",
                    "correct_answer": "Key concepts: Overfitting occurs when a model learns training data (including noise/random fluctuations) too closely, memorizing details rather than learning general patterns. As a result, it performs exceptionally well on past data but fails to generalize accurately to new, unseen business data."
                },
                {
                    "question_number": 6,
                    "question": "Which of the following algorithms is supervised and primarily used for classification tasks?",
                    "type": "mcq",
                    "options": [
                        "A) Logistic Regression",
                        "B) K-Means",
                        "C) Principal Component Analysis",
                        "D) DBSCAN"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 7,
                    "question": "Standard scaling (Z-score normalization) transforms a feature such that it has a mean of 0 and a variance of _____.",
                    "type": "fib",
                    "correct_answer": "1"
                },
                {
                    "question_number": 8,
                    "question": "Which Git command is used to create a new local branch and switch to it immediately?",
                    "type": "mcq",
                    "options": [
                        "A) git branch create <name>",
                        "B) git merge <name>",
                        "C) git checkout -b <name>",
                        "D) git commit -b <name>"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 9,
                    "question": "In NumPy, the attribute used to check the dimensions and size along each axis of an array is `._____`.",
                    "type": "fib",
                    "correct_answer": "shape"
                },
                {
                    "question_number": 10,
                    "question": "Describe the basic steps for setting up a standard A/B test for an online user feature.",
                    "type": "descriptive",
                    "correct_answer": "Key concepts: Define hypothesis and metric (KPI), calculate required sample size based on statistical power and significance level, randomly split users into control and treatment groups, run experiment without bias, and conduct hypothesis testing (e.g., t-test or chi-square) to check statistical significance."
                },
                {
                    "question_number": 11,
                    "question": "K-Means clustering belongs to which category of machine learning?",
                    "type": "mcq",
                    "options": [
                        "A) Supervised Learning",
                        "B) Unsupervised Learning",
                        "C) Reinforcement Learning",
                        "D) Semi-supervised Learning"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "The proportion of variance in the dependent variable predictable from the independent variables in linear regression is denoted by _____.",
                    "type": "fib",
                    "correct_answer": "R-squared"
                },
                {
                    "question_number": 13,
                    "question": "Principal Component Analysis (PCA) is primarily used for which of the following operations?",
                    "type": "mcq",
                    "options": [
                        "A) Feature Generation",
                        "B) Missing Value Imputation",
                        "C) Target Encoding",
                        "D) Dimensionality Reduction"
                    ],
                    "correct_answer": "D"
                },
                {
                    "question_number": 14,
                    "question": "In Pandas, the function used to combine two DataFrames along a common key column is `pd._____`.",
                    "type": "fib",
                    "correct_answer": "merge"
                },
                {
                    "question_number": 15,
                    "question": "What are the key trade-offs when filling missing values in a numerical column using mean imputation?",
                    "type": "descriptive",
                    "correct_answer": "Key concepts: Mean imputation is simple and preserves sample size, but it reduces overall variance, underestimates standard errors, distorts feature correlations, and assumes data is Missing Completely at Random (MCAR)."
                },
                {
                    "question_number": 16,
                    "question": "Which SQL clause is used to filter aggregated group results obtained from a `GROUP BY` clause?",
                    "type": "mcq",
                    "options": [
                        "A) WHERE",
                        "B) ORDER BY",
                        "C) HAVING",
                        "D) FILTER"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 17,
                    "question": "In Bayesian statistics, the updated probability distribution of a parameter after observing sample data is called the _____ distribution.",
                    "type": "fib",
                    "correct_answer": "posterior"
                },
                {
                    "question_number": 18,
                    "question": "An ROC curve evaluates a classification model by plotting True Positive Rate against which metric?",
                    "type": "mcq",
                    "options": [
                        "A) False Positive Rate",
                        "B) False Negative Rate",
                        "C) Precision",
                        "D) Accuracy"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 19,
                    "question": "A standard method for outlier detection that measures how many standard deviations a data point lies away from the mean is the _____.",
                    "type": "fib",
                    "correct_answer": "Z-score"
                },
                {
                    "question_number": 20,
                    "question": "How should a data scientist effectively communicate complex machine learning predictions to non-technical stakeholders?",
                    "type": "descriptive",
                    "correct_answer": "Key concepts: Focus on business outcomes and actionability rather than technical formulas, use intuitive visualizations (e.g., feature importance charts), map model predictions directly to financial or operational KPIs, and clearly highlight risks or confidence bounds."
                }
            ],
            "Medium": [
                {
                    "question_number": 1,
                    "question": "In Pandas, which method avoids creating a SettingWithCopyWarning when assigning values to a filtered subset of a DataFrame?",
                    "type": "mcq",
                    "options": [
                        "A) df.filter()",
                        "B) df.loc[]",
                        "C) df.where()",
                        "D) df.iloc[].copy_values()"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "In SQL, the window function used to assign a unique sequential integer to each row within a partition is _____.",
                    "type": "fib",
                    "correct_answer": "ROW_NUMBER()"
                },
                {
                    "question_number": 3,
                    "question": "When interpreting a p-value from a hypothesis test, what does a p-value of 0.03 indicate at a significance level of 0.05?",
                    "type": "mcq",
                    "options": [
                        "A) 3% chance that the alternative hypothesis is true",
                        "B) Fail to reject the null hypothesis",
                        "C) Reject the null hypothesis as the result is statistically significant",
                        "D) The effect size is exactly 0.03"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 4,
                    "question": "For highly imbalanced binary classification datasets, evaluating the area under the _____ curve is often preferred over ROC-AUC.",
                    "type": "fib",
                    "correct_answer": "Precision-Recall"
                },
                {
                    "question_number": 5,
                    "question": "Explain the bias-variance tradeoff and how L1 (Lasso) and L2 (Ridge) regularizations influence this tradeoff.",
                    "type": "descriptive",
                    "correct_answer": "Key concepts: Bias measures error from overly simplistic assumptions; variance measures sensitivity to training noise. Overfitting occurs with high variance, underfitting with high bias. Regularization adds penalty terms to loss functions to reduce model complexity (variance), slightly increasing bias to improve overall generalization. L1 produces sparse models (feature selection), while L2 shrinks coefficients uniformly."
                },
                {
                    "question_number": 6,
                    "question": "What core mechanism makes Random Forest resistant to overfitting compared to an individual Decision Tree?",
                    "type": "mcq",
                    "options": [
                        "A) Bootstrap aggregating (bagging) and random feature subset selection",
                        "B) Iterative error correction via gradient optimization",
                        "C) Distance metric minimization in vector space",
                        "D) Linear boundary optimization in high dimensions"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 7,
                    "question": "MinMax Scaling transforms numerical data so that all values lie strictly in the range between _____ and 1.",
                    "type": "fib",
                    "correct_answer": "0"
                },
                {
                    "question_number": 8,
                    "question": "Which Git operation rewrites commit history by taking commits from one branch and replaying them onto another branch?",
                    "type": "mcq",
                    "options": [
                        "A) git merge",
                        "B) git pull",
                        "C) git fetch",
                        "D) git rebase"
                    ],
                    "correct_answer": "D"
                },
                {
                    "question_number": 9,
                    "question": "In NumPy, matrix multiplication of two 2D arrays `A` and `B` can be computed using `np._____` or the `@` operator.",
                    "type": "fib",
                    "correct_answer": "matmul"
                },
                {
                    "question_number": 10,
                    "question": "How do you detect and mitigate Sample Ratio Mismatch (SRM) during an A/B test?",
                    "type": "descriptive",
                    "correct_answer": "Key concepts: SRM occurs when observed sample counts between control and variant deviate significantly from expected proportions. Detected using a Chi-Square goodness-of-fit test on sample allocations. Mitigation involves auditing randomization triggers, fixing assignment pipelines, ensuring equal tracking latency, and discarding compromised test data."
                },
                {
                    "question_number": 11,
                    "question": "Which clustering algorithm identifies clusters based on density and is capable of discovering arbitrary shapes and noise points?",
                    "type": "mcq",
                    "options": [
                        "A) Hierarchical Agglomerative Clustering",
                        "B) DBSCAN",
                        "C) K-Means",
                        "D) Gaussian Mixture Models"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "In multiple linear regression, severe correlation between independent variables is measured using the _____ factor.",
                    "type": "fib",
                    "correct_answer": "Variance Inflation"
                },
                {
                    "question_number": 13,
                    "question": "What is a primary distinction between PCA and t-SNE?",
                    "type": "mcq",
                    "options": [
                        "A) PCA is non-linear, while t-SNE is linear",
                        "B) t-SNE preserves global covariance structure better than PCA",
                        "C) PCA focuses on linear global variance; t-SNE focuses on non-linear local neighborhood preservation",
                        "D) t-SNE is faster and scales better to large datasets than PCA"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 14,
                    "question": "In Pandas, to map a scalar transformation function to every individual element in a DataFrame, you use the `._____()` method.",
                    "type": "fib",
                    "correct_answer": "applymap"
                },
                {
                    "question_number": 15,
                    "question": "Compare Gradient Boosting Trees (e.g., XGBoost) and Random Forests regarding training behavior, hyperparameter sensitivity, and risk of overfitting.",
                    "type": "descriptive",
                    "correct_answer": "Key concepts: Random Forest trains trees in parallel (independent) reducing variance; Gradient Boosting builds sequential trees correcting previous residual errors. XGBoost often yields higher predictive power but requires careful tuning (learning rate, depth) to prevent overfitting. Random Forests are generally robust to hyperparameter tuning and harder to overfit."
                },
                {
                    "question_number": 16,
                    "question": "Which SQL join returns all records when there is a match in either left or right table records, filling missing pairs with NULLs?",
                    "type": "mcq",
                    "options": [
                        "A) FULL OUTER JOIN",
                        "B) INNER JOIN",
                        "C) CROSS JOIN",
                        "D) LEFT JOIN"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 17,
                    "question": "In Bayes' Theorem, the formula computes Posterior = (Likelihood * Prior) / _____.",
                    "type": "fib",
                    "correct_answer": "Evidence"
                },
                {
                    "question_number": 18,
                    "question": "Which loss function is minimized during the training of standard binary Logistic Regression models?",
                    "type": "mcq",
                    "options": [
                        "A) Mean Squared Error",
                        "B) Mean Absolute Error",
                        "C) Hinge Loss",
                        "D) Binary Cross-Entropy (Log-Loss)"
                    ],
                    "correct_answer": "D"
                },
                {
                    "question_number": 19,
                    "question": "The Interquartile Range (IQR) used for robust outlier detection is calculated as the 75th percentile (Q3) minus the 25th percentile (_____).",
                    "type": "fib",
                    "correct_answer": "Q1"
                },
                {
                    "question_number": 20,
                    "question": "Describe how SHAP (SHapley Additive exPlanations) values can be used to explain machine learning predictions to non-technical business partners.",
                    "type": "descriptive",
                    "correct_answer": "Key concepts: SHAP allocates feature contributions to specific model outcomes based on game theory. Explain feature values relative to a baseline prediction, showing how individual inputs drive the final output up or down. Use summary plots to communicate feature importance across the dataset and waterfall plots for specific case predictions."
                }
            ],
            "Hard": [
                {
                    "question_number": 1,
                    "question": "When managing memory constraints with massive datasets in Pandas, which practice provides the most effective memory reduction without losing structural rows?",
                    "type": "mcq",
                    "options": [
                        "A) Using `df.dropna()` on non-essential columns",
                        "B) Storing all integer features as 64-bit floats",
                        "C) Downcasting numeric types and converting low-cardinality string columns to `category` dtype",
                        "D) Applying `df.replace()` to replace zeroes with null values"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 2,
                    "question": "In modern analytical SQL engines (such as Snowflake or BigQuery), the SQL clause used specifically to filter the results of window functions is _____.",
                    "type": "fib",
                    "correct_answer": "QUALIFY"
                },
                {
                    "question_number": 3,
                    "question": "Which statistical hypothesis test should be used to evaluate whether two independent normally distributed samples have significantly different variances?",
                    "type": "mcq",
                    "options": [
                        "A) Student's t-test",
                        "B) F-test of Equality of Variances",
                        "C) Mann-Whitney U test",
                        "D) Chi-Square test of independence"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "In search and recommendation systems, the evaluation metric that measures the quality of ranked lists by discounting relevance exponentially at lower positions is abbreviated as _____.",
                    "type": "fib",
                    "correct_answer": "NDCG"
                },
                {
                    "question_number": 5,
                    "question": "How would you design a machine learning solution for severe target imbalance (e.g., 1:10,000 fraud ratio) without relying solely on simple oversampling (SMOTE) or undersampling?",
                    "type": "descriptive",
                    "correct_answer": "Key concepts: Cost-sensitive learning (modifying loss functions with class weights), threshold tuning based on business cost matrix, evaluating with Precision-Recall AUC/F-beta rather than ROC-AUC, anomaly detection paradigms (e.g., Isolation Forest, Autoencoders), focal loss, and ensembling sub-sampled majority datasets with minority samples."
                },
                {
                    "question_number": 6,
                    "question": "What is the objective function optimized by a Support Vector Machine (SVM) in its standard soft-margin formulation?",
                    "type": "mcq",
                    "options": [
                        "A) Minimizing Hinge Loss plus an L2 regularization penalty on model weights",
                        "B) Maximizing cross-entropy loss with slack variables",
                        "C) Minimizing Mean Squared Error across support vector hyperplanes",
                        "D) Maximizing total variance of project data points onto high-dimensional space"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 7,
                    "question": "To prevent data leakage when applying Target Encoding to high-cardinality categorical variables, practitioners implement out-of-fold target encoding and add additive _____.",
                    "type": "fib",
                    "correct_answer": "smoothing"
                },
                {
                    "question_number": 8,
                    "question": "In Git, if you want to apply a single specific commit from a feature branch onto your production main branch, which command should you run?",
                    "type": "mcq",
                    "options": [
                        "A) git merge --single",
                        "B) git rebase --onto main",
                        "C) git pull --commit",
                        "D) git cherry-pick <commit-hash>"
                    ],
                    "correct_answer": "D"
                },
                {
                    "question_number": 9,
                    "question": "According to NumPy broadcasting rules, two dimensions are compatible if they are equal or if one of the dimensions equals _____.",
                    "type": "fib",
                    "correct_answer": "1"
                },
                {
                    "question_number": 10,
                    "question": "How would you handle network effects and spillover/interference between treatment and control units when running an A/B test in a two-sided marketplace (e.g., Uber or Airbnb)?",
                    "type": "descriptive",
                    "correct_answer": "Key concepts: Network spillover violates SUTVA (Stable Unit Treatment Value Assumption). Mitigation strategies include cluster-based randomization (geographical/community clusters), synthetic control groups, staggered rollout (time-based randomization like switchback experiments), and bipartite graph isolation."
                },
                {
                    "question_number": 11,
                    "question": "Compared to t-SNE, what theoretical advantage does UMAP (Uniform Manifold Approximation and Projection) provide?",
                    "type": "mcq",
                    "options": [
                        "A) UMAP is strictly a linear reduction method",
                        "B) UMAP guarantees global optimum convergence without initialization",
                        "C) UMAP better preserves both local structure and global continuum connectivity with superior computational scalability",
                        "D) UMAP does not use hyperparameter tuning"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 12,
                    "question": "When OLS linear regression assumptions are violated by heteroskedasticity in residual errors, coefficient standard errors should be recalculated using _____ standard errors.",
                    "type": "fib",
                    "correct_answer": "robust"
                },
                {
                    "question_number": 13,
                    "question": "How does Kernel PCA differ fundamentally from standard Linear PCA?",
                    "type": "mcq",
                    "options": [
                        "A) Kernel PCA maps input space into a high-dimensional feature space using the kernel trick to extract non-linear principal components",
                        "B) Kernel PCA operates without using eigenvalues or eigenvectors",
                        "C) Linear PCA handles non-linear relationships, whereas Kernel PCA can only model straight lines",
                        "D) Kernel PCA performs supervised dimensionality reduction using target labels"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 14,
                    "question": "In Pandas, while `pd.melt()` transforms data from wide format to long format, the inverse function to transform long to wide is `pd._____()`.",
                    "type": "fib",
                    "correct_answer": "pivot"
                },
                {
                    "question_number": 15,
                    "question": "Design an end-to-end framework to detect, monitor, and remediate Data Drift and Concept Drift for a live production recommendation engine.",
                    "type": "descriptive",
                    "correct_answer": "Key concepts: Monitoring input distribution shifts (covariate shift) using metrics like Kolmogorov-Smirnov test, Population Stability Index (PSI), or Wasserstein distance. Monitoring output/target shift (concept drift) by tracking error metrics over time. Remediation strategies include automated retraining triggers, sliding-window models, online learning algorithms, fallback rule engines, and updating ground-truth feedback loops."
                },
                {
                    "question_number": 16,
                    "question": "When optimizing a SQL query joining multi-billion row tables in a distributed data warehouse, which technique prevents data skew and excessive network shuffling?",
                    "type": "mcq",
                    "options": [
                        "A) Adding `ORDER BY` clauses on non-indexed text attributes",
                        "B) Partitioning and clustering tables on common join keys",
                        "C) Replacing `INNER JOIN` with subqueries containing `LIKE` wildcards",
                        "D) Disabling index scans across all compute nodes"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "In Bayesian computation, the Markov Chain Monte Carlo (MCMC) algorithm that uses a proposal distribution and an acceptance probability ratio to sample intractable posteriors is Metropolis-_____.",
                    "type": "fib",
                    "correct_answer": "Hastings"
                },
                {
                    "question_number": 18,
                    "question": "If a modern gradient-boosted classification model outputs predicted probabilities that are uncalibrated (e.g., overconfident near 0 and 1), which technique calibrates these probabilities non-parametrically?",
                    "type": "mcq",
                    "options": [
                        "A) Min-Max Scaling",
                        "B) Box-Cox Transformation",
                        "C) L1 Regularization",
                        "D) Isotonic Regression"
                    ],
                    "correct_answer": "D"
                },
                {
                    "question_number": 19,
                    "question": "An Isolation Forest isolates anomalies by randomly selecting a feature and split value; anomalous points are identified because they have a significantly shorter average _____ length in the trees.",
                    "type": "fib",
                    "correct_answer": "path"
                },
                {
                    "question_number": 20,
                    "question": "A business leadership team demands absolute interpretability before deploying a complex model for credit risk evaluation. How do you navigate the trade-off between complex model predictive power and strict interpretability constraints?",
                    "type": "descriptive",
                    "correct_answer": "Key concepts: Evaluate regulatory constraints (e.g., FCRA requirement for reason codes). Propose a hybrid approach: train interpretable baseline models (Scorecards, GAMs, EBMs) alongside complex black-box models (XGBoost/Neural Nets) to quantify performance delta. If complex models yield significant gains, employ global and local model-agnostic interpretability post-hoc techniques (SHAP, LIME, PDPs) to satisfy regulatory and business requirements."
                }
            ]
        },
        "HR": {
            "Easy": [
                {
                    "question_number": 1,
                    "question": "When presenting a basic data visualization to a non-technical stakeholder who is confused by the metrics, what is the best initial approach?",
                    "type": "mcq",
                    "options": [
                        "A) Send them a link to the raw SQL queries and documentation.",
                        "B) Explain the underlying mathematical formula in detail.",
                        "C) Simplify the chart and focus on the core business takeaway rather than statistical jargon.",
                        "D) Tell them that data science requires technical literacy and they should review the slides alone."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 2,
                    "question": "Effective communication between a data scientist and business teams requires strong ________ skills to translate complex numbers into actionable insights.",
                    "type": "fib",
                    "correct_answer": "interpersonal"
                },
                {
                    "question_number": 3,
                    "question": "You realize you made a small calculation error in a report you presented to your manager yesterday. What should you do?",
                    "type": "mcq",
                    "options": [
                        "A) Wait until someone else points it out before fixing it.",
                        "B) Immediately notify your manager, explain the correction, and provide the updated report.",
                        "C) Delete the original report and hope no one saved a copy.",
                        "D) Blame the data engineering team for pulling incorrect data."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "When working in a new team, establishing mutual trust and understanding different working styles is an essential part of team ________.",
                    "type": "fib",
                    "correct_answer": "integration"
                },
                {
                    "question_number": 5,
                    "question": "Describe a time when you had to learn a new tool or programming language quickly for a project. How did you approach it?",
                    "type": "descriptive",
                    "correct_answer": "Proactive learning, utilizing online resources, building small proof-of-concept projects, seeking mentorship, and applying knowledge directly to business tasks."
                },
                {
                    "question_number": 6,
                    "question": "If a stakeholder asks you to rush an analysis without verifying data quality, how should you respond?",
                    "type": "mcq",
                    "options": [
                        "A) Run the analysis immediately and ignore potential errors.",
                        "B) Refuse to do the work entirely.",
                        "C) Politely explain the risks of unverified data and propose a swift yet reliable validation step.",
                        "D) Alter the data to fit their preconceived expectations."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 7,
                    "question": "The ability to accept constructive criticism on your code or analytical approach without taking it personally is known as receiving ________.",
                    "type": "fib",
                    "correct_answer": "feedback"
                },
                {
                    "question_number": 8,
                    "question": "Why is documentation considered an important responsibility for an entry-level data scientist?",
                    "type": "mcq",
                    "options": [
                        "A) It is only required to pass compliance audits.",
                        "B) It ensures reproducibility, helps teammates understand your work, and saves time later.",
                        "C) It replaces the need to ever talk to your team members.",
                        "D) It guarantees that your model will never encounter errors."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "Managing your daily tasks effectively and prioritizing assignments based on urgency and impact demonstrates strong ________ management.",
                    "type": "fib",
                    "correct_answer": "time"
                },
                {
                    "question_number": 10,
                    "question": "Tell me about a time when you received constructive feedback on a project. How did you handle it and what did you change?",
                    "type": "descriptive",
                    "correct_answer": "Openness to critique, active listening, implementing suggested changes, and demonstrating professional growth."
                },
                {
                    "question_number": 11,
                    "question": "How should you handle conflicting priorities between two different senior managers requesting your time?",
                    "type": "mcq",
                    "options": [
                        "A) Ignore both managers and work on whatever you prefer.",
                        "B) Bring the managers together or consult your direct supervisor to align on business priorities.",
                        "C) Promise both managers you will finish their tasks by tomorrow.",
                        "D) Work 80 hours a week to satisfy both without saying anything."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "Remaining calm and constructive when facing unexpected data discrepancies or deadlines is a sign of emotional ________.",
                    "type": "fib",
                    "correct_answer": "intelligence"
                },
                {
                    "question_number": 13,
                    "question": "What is the primary benefit of actively participating in daily stand-up meetings within an agile data team?",
                    "type": "mcq",
                    "options": [
                        "A) To complain about workload and slow down operations.",
                        "B) To keep the team aligned, share blockers, and track daily progress transparently.",
                        "C) To avoid writing weekly status reports altogether.",
                        "D) To prove to management that you work harder than everyone else."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "The process of working jointly with others on a shared data model or analysis report is called ________.",
                    "type": "fib",
                    "correct_answer": "collaboration"
                },
                {
                    "question_number": 15,
                    "question": "Describe a situation where you had to work with a teammate who had a very different working style than yours. How did you succeed?",
                    "type": "descriptive",
                    "correct_answer": "Adaptability, mutual respect, open communication, finding common ground, and leveraging individual strengths."
                },
                {
                    "question_number": 16,
                    "question": "When you are stuck on a difficult coding bug for several hours, what is the best professional step to take?",
                    "type": "mcq",
                    "options": [
                        "A) Give up and delete the entire repository.",
                        "B) Keep trying blindly for another three days.",
                        "C) Timebox your independent troubleshooting, research documentation, and then ask a senior peer for guidance.",
                        "D) Blame the programming language's compiler."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 17,
                    "question": "Ensuring your data models and recommendations adhere to ethical guidelines and data privacy laws is an aspect of professional ________.",
                    "type": "fib",
                    "correct_answer": "ethics"
                },
                {
                    "question_number": 18,
                    "question": "Why is intellectual curiosity considered a vital trait for a data scientist?",
                    "type": "mcq",
                    "options": [
                        "A) It helps you ask deeper questions beyond the initial prompt to uncover hidden insights.",
                        "B) It allows you to distract the team with irrelevant trivia.",
                        "C) It guarantees you will spend less time writing production code.",
                        "D) It replaces the need for formal statistical training."
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 19,
                    "question": "The willingness to admit when you do not know something and seek guidance is a sign of professional ________.",
                    "type": "fib",
                    "correct_answer": "humility"
                },
                {
                    "question_number": 20,
                    "question": "Describe a project where things did not go according to plan. What was your role, and how did you adapt to the changes?",
                    "type": "descriptive",
                    "correct_answer": "Resilience, problem-solving, flexibility, clear communication of roadblocks, and focusing on alternative solutions."
                }
            ],
            "Medium": [
                {
                    "question_number": 1,
                    "question": "A product manager wants to push a model into production immediately, but you know it suffers from demographic bias. What is your best course of action?",
                    "type": "mcq",
                    "options": [
                        "A) Deploy it anyway to meet product deadlines.",
                        "B) Clearly communicate the fairness risks, present evidence of the bias, and collaborate on mitigation steps before launch.",
                        "C) Cancel the project entirely without consulting the product manager.",
                        "D) Hide the bias metrics in a footnote of a hidden document."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "Aligning data science deliverables directly with core company key performance indicators ensures business ________.",
                    "type": "fib",
                    "correct_answer": "impact"
                },
                {
                    "question_number": 3,
                    "question": "How should you manage a situation where a stakeholder repeatedly changes project requirements mid-way through your model development?",
                    "type": "mcq",
                    "options": [
                        "A) Complain to HR about the stakeholder's behavior.",
                        "B) Silently rewrite the code every time without discussing timelines.",
                        "C) Have a structured conversation outlining the impact of scope creep on delivery timelines and negotiate a revised plan.",
                        "D) Ignore the new requirements and deliver the original model."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 4,
                    "question": "The practice of mentoring junior team members and sharing technical knowledge helps foster a culture of continuous ________.",
                    "type": "fib",
                    "correct_answer": "learning"
                },
                {
                    "question_number": 5,
                    "question": "Tell me about a time when you had to persuade a skeptical cross-functional team to adopt a data-driven recommendation. How did you do it?",
                    "type": "descriptive",
                    "correct_answer": "Stakeholder empathy, clear storytelling, addressing concerns directly, using data to build trust, and framing insights around their business goals."
                },
                {
                    "question_number": 6,
                    "question": "You discover that a key metric your team has been tracking for months was defined incorrectly. How do you handle this disclosure?",
                    "type": "mcq",
                    "options": [
                        "A) Keep quiet so nobody notices past mistakes.",
                        "B) Inform leadership transparently, explain the impact, provide the corrected definition, and offer a retroactive adjustment plan.",
                        "C) Blame the person who originally set up the metric.",
                        "D) Delete the historical dashboards."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "Taking ownership of a project from conception through to production deployment and monitoring demonstrates strong professional ________.",
                    "type": "fib",
                    "correct_answer": "accountability"
                },
                {
                    "question_number": 8,
                    "question": "What is the most effective way to handle disagreement with a peer data scientist over model architecture choices?",
                    "type": "mcq",
                    "options": [
                        "A) Escalate immediately to the VP without discussion.",
                        "B) Insist your approach is superior because of seniority.",
                        "C) Run an A/B test or comparative benchmark to let empirical evidence guide the decision.",
                        "D) Randomly pick one method without testing."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 9,
                    "question": "Breaking down a massive ambiguous business problem into well-defined, testable analytical milestones is a key sign of strong ________ thinking.",
                    "type": "fib",
                    "correct_answer": "structured"
                },
                {
                    "question_number": 10,
                    "question": "Describe a time when a machine learning model you built failed or underperformed in production. How did you diagnose and resolve the issue?",
                    "type": "descriptive",
                    "correct_answer": "Root-cause analysis, post-mortem culture, collaboration with engineering, data drift identification, and iterative improvement."
                },
                {
                    "question_number": 11,
                    "question": "If a junior analyst on your team is struggling to meet deadlines due to technical hurdles, what is the best leadership response?",
                    "type": "mcq",
                    "options": [
                        "A) Reassign all their work to yourself and say nothing.",
                        "B) Report them for poor performance immediately.",
                        "C) Offer constructive guidance, pair-programme to unblock them, and help them improve their skills.",
                        "D) Tell them to figure it out on their own."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 12,
                    "question": "Balancing technical perfection with business speed and pragmatism is essential for delivering timely ________.",
                    "type": "fib",
                    "correct_answer": "value"
                },
                {
                    "question_number": 13,
                    "question": "How do you approach prioritizing multiple feature requests for a predictive model when resources are severely limited?",
                    "type": "mcq",
                    "options": [
                        "A) Build whichever feature sounds the most fun to code.",
                        "B) Evaluate features based on business impact versus implementation effort and consult stakeholders.",
                        "C) Try to build all features simultaneously, leading to burnout.",
                        "D) Refuse to prioritize and let features ship randomly."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "Building strong working relationships with software engineers and product managers ensures seamless cross-functional ________.",
                    "type": "fib",
                    "correct_answer": "alignment"
                },
                {
                    "question_number": 15,
                    "question": "Describe a project where requirements were vague and ambiguous. How did you scope the project and drive it to a successful outcome?",
                    "type": "descriptive",
                    "correct_answer": "Stakeholder interviews, defining success metrics, prototyping, iterative feedback loops, and managing scope."
                },
                {
                    "question_number": 16,
                    "question": "A stakeholder wants to use a complex deep learning model for a simple tabular dataset where logistic regression performs equally well. How do you respond?",
                    "type": "mcq",
                    "options": [
                        "A) Build the deep learning model to impress them.",
                        "B) Explain the trade-offs of interpretability, maintenance cost, and complexity, advocating for the simpler model.",
                        "C) Refuse to build anything at all.",
                        "D) Secretly build the logistic regression model and lie about it."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "Anticipating potential data pipeline failures or concept drift before they impact business operations is an example of ________ planning.",
                    "type": "fib",
                    "correct_answer": "proactive"
                },
                {
                    "question_number": 18,
                    "question": "What is the best approach when you realize your data analysis contradicts the executive team's intuition?",
                    "type": "mcq",
                    "options": [
                        "A) Alter your analysis to match what they want to hear.",
                        "B) Present your methodology and findings objectively, welcoming scrutiny while standing by your empirical data.",
                        "C) Send the report anonymously.",
                        "D) Tell them they are completely wrong and inexperienced."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "The ability to remain objective and separate personal ego from analytical findings is known as intellectual ________.",
                    "type": "fib",
                    "correct_answer": "honesty"
                },
                {
                    "question_number": 20,
                    "question": "Tell me about a time when you successfully mentored or upskilled a colleague in a technical domain. What approach did you take?",
                    "type": "descriptive",
                    "correct_answer": "Tailored guidance, patience, practical exercises, setting clear milestones, and encouraging independent problem-solving."
                }
            ],
            "Hard": [
                {
                    "question_number": 1,
                    "question": "As a lead data scientist, you discover that a high-revenue machine learning feature relies on data collected in a legally gray area regarding user privacy. Executive leadership pushes to keep it. What do you do?",
                    "type": "mcq",
                    "options": [
                        "A) Keep quiet since revenue is high.",
                        "B) Escalate the compliance and ethical risks clearly to leadership and legal counsel, advocating for immediate remediation or feature suspension.",
                        "C) Delete the data yourself without telling anyone.",
                        "D) Blame the engineering team for collecting the data."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "Building a resilient data culture across an entire enterprise requires strategic vision and strong organizational ________.",
                    "type": "fib",
                    "correct_answer": "leadership"
                },
                {
                    "question_number": 3,
                    "question": "Your data science team is experiencing severe burnout due to constant ad-hoc requests from various business units. As a senior leader, how do you resolve this?",
                    "type": "mcq",
                    "options": [
                        "A) Tell the team to work faster and longer hours.",
                        "B) Implement a formal intake and triage process, establish service-level agreements, and push back on low-impact ad-hoc work.",
                        "C) Hire fifty contractors overnight without budget approval.",
                        "D) Stop answering requests from all business units permanently."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "Aligning data science roadmap initiatives with long-term corporate strategy is essential for maximizing return on ________.",
                    "type": "fib",
                    "correct_answer": "investment"
                },
                {
                    "question_number": 5,
                    "question": "Describe a time when you had to lead a major strategic pivot for a data science initiative after initial results showed the core hypothesis was invalid. How did you manage stakeholders?",
                    "type": "descriptive",
                    "correct_answer": "Transparency, pivoting strategy based on empirical evidence, managing stakeholder expectations, and refocusing the team on new opportunities."
                },
                {
                    "question_number": 6,
                    "question": "Two senior executives have opposing strategic visions for how a predictive analytics platform should be monetized, and both demand your team's exclusive support. How do you navigate this political challenge?",
                    "type": "mcq",
                    "options": [
                        "A) Choose one executive at random and ignore the other.",
                        "B) Facilitate a joint alignment session to present data-driven trade-offs and help leadership reach a consensus.",
                        "C) Tell both executives their ideas are unviable and walk away.",
                        "D) Build two competing products without informing either executive."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "Creating a safe psychological environment where team members feel comfortable admitting failure is crucial for high-performing data ________.",
                    "type": "fib",
                    "correct_answer": "organizations"
                },
                {
                    "question_number": 8,
                    "question": "You are leading a high-stakes AI project where key milestones are being missed due to technical complexity and talent gaps. What is your leadership strategy?",
                    "type": "mcq",
                    "options": [
                        "A) Panic and micromanage every single line of code.",
                        "B) Reassess scope, de-risk critical components, reallocate internal talent, and communicate transparently with stakeholders about revised timelines.",
                        "C) Blame the junior developers for lack of capability.",
                        "D) Cancel the project and pretend it never started."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "Balancing innovation and experimentation with production stability and robust MLOps is a hallmark of mature engineering ________.",
                    "type": "fib",
                    "correct_answer": "governance"
                },
                {
                    "question_number": 10,
                    "question": "Tell me about a time when you had to manage significant organizational resistance to an automated, AI-driven decision-making system. How did you drive adoption?",
                    "type": "descriptive",
                    "correct_answer": "Change management, addressing human-in-the-loop concerns, building explainable AI, establishing trust, and training programs."
                },
                {
                    "question_number": 11,
                    "question": "A key senior data scientist on your team wants to leave because they disagree with the company's technical direction. As their manager, how do you handle this?",
                    "type": "mcq",
                    "options": [
                        "A) Let them leave immediately without a conversation.",
                        "B) Have an open dialogue to understand their concerns, explore potential growth opportunities or scope adjustments, and ensure a smooth transition if departure is inevitable.",
                        "C) Threaten legal action to keep them on the team.",
                        "D) Insult their technical skills in front of the team."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "Fostering a culture where reproducibility, rigorous testing, and peer review are non-negotiable standards represents technical ________.",
                    "type": "fib",
                    "correct_answer": "excellence"
                },
                {
                    "question_number": 13,
                    "question": "How do you evaluate and decide whether to build a custom machine learning solution in-house versus purchasing an enterprise SaaS platform?",
                    "type": "mcq",
                    "options": [
                        "A) Always build in-house because building is more fun.",
                        "B) Always buy SaaS to avoid writing code.",
                        "C) Perform a comprehensive cost-benefit analysis considering core competitive advantage, maintenance burden, data security, and long-term TCO.",
                        "D) Flip a coin to decide."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 14,
                    "question": "Ensuring that AI models do not perpetuate historical biases or discriminate against protected groups requires continuous algorithmic ________.",
                    "type": "fib",
                    "correct_answer": "auditing"
                },
                {
                    "question_number": 15,
                    "question": "Describe a time when you had to secure executive sponsorship and budget for a long-term R&D data science initiative with uncertain short-term ROI. How did you pitch it?",
                    "type": "descriptive",
                    "correct_answer": "Strategic framing, milestone-based funding, risk mitigation, connecting R&D to long-term competitive advantage, and clear communication."
                },
                {
                    "question_number": 16,
                    "question": "You discover that a widely publicized company report featured flawed data science methodologies, potentially harming the company's reputation. What is your immediate executive action?",
                    "type": "mcq",
                    "options": [
                        "A) Hope the public doesn't notice.",
                        "B) Alert leadership immediately, lead an internal investigation, issue a correction, and implement stricter review protocols.",
                        "C) Blame the marketing team for publishing the report.",
                        "D) Resign immediately without telling anyone."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "Developing talent and building a strong internal promotion pipeline are key responsibilities of effective team ________.",
                    "type": "fib",
                    "correct_answer": "sponsorship"
                },
                {
                    "question_number": 18,
                    "question": "How do you approach establishing a new data-driven culture in a traditional, legacy-bound organization that is skeptical of algorithms?",
                    "type": "mcq",
                    "options": [
                        "A) Force everyone to use complex neural networks on day one.",
                        "B) Start with quick-win projects that solve immediate pain points, demonstrate tangible value, and build trust gradually through education.",
                        "C) Complain to management about their lack of modernity.",
                        "D) Work in total isolation and ignore the rest of the company."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "The ability to inspire a cross-functional team of engineers, analysts, and product managers toward a unified AI vision is called strategic ________.",
                    "type": "fib",
                    "correct_answer": "vision"
                },
                {
                    "question_number": 20,
                    "question": "Tell me about a time when you had to manage a toxic team dynamic or underperforming senior contributor during a critical product launch. How did you handle it?",
                    "type": "descriptive",
                    "correct_answer": "Decisive leadership, private feedback sessions, protecting team morale, establishing clear performance expectations, and taking necessary personnel actions."
                }
            ]
        },
        "Behavioral": {
            "Easy": [
                {
                    "question_number": 1,
                    "question": "If you find a discrepancy in your data during analysis, what is the best first step?",
                    "type": "mcq",
                    "options": [
                        "Ignore it and move on",
                        "Immediately notify your manager and document the finding",
                        "Delete the outliers",
                        "Change the code to hide it"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "The ability to translate complex technical findings into understandable insights for non-technical stakeholders is known as data ____________.",
                    "type": "fib",
                    "correct_answer": "storytelling"
                },
                {
                    "question_number": 3,
                    "question": "When faced with a tight deadline, how should you prioritize your data cleaning tasks?",
                    "type": "mcq",
                    "options": [
                        "Do everything perfectly",
                        "Focus on the data most critical to the core business question",
                        "Randomly sample the data",
                        "Skip cleaning"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "Working effectively with team members from different departments is a key component of ____________ collaboration.",
                    "type": "fib",
                    "correct_answer": "cross-functional"
                },
                {
                    "question_number": 5,
                    "question": "Describe a time you had to learn a new tool or library quickly to finish a project.",
                    "type": "descriptive",
                    "correct_answer": "Demonstrate proactivity, resourcefulness, structured learning approach, and successful application."
                },
                {
                    "question_number": 6,
                    "question": "If a stakeholder requests a feature that is not feasible given the data, what do you do?",
                    "type": "mcq",
                    "options": [
                        "Agree to do it anyway",
                        "Explain the data limitations and suggest an alternative solution",
                        "Simply say 'no'",
                        "Blame the engineering team"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "A commitment to using data in a way that respects user privacy and complies with regulations is called ____________ responsibility.",
                    "type": "fib",
                    "correct_answer": "data ethics"
                },
                {
                    "question_number": 8,
                    "question": "How do you handle receiving critical feedback on your model code from a peer review?",
                    "type": "mcq",
                    "options": [
                        "Take it personally",
                        "Ignore the suggestions",
                        "View it as an opportunity to learn and improve code quality",
                        "Argue back"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 9,
                    "question": "The process of verifying that a model performs consistently on new data is known as model ____________.",
                    "type": "fib",
                    "correct_answer": "validation"
                },
                {
                    "question_number": 10,
                    "question": "Describe a situation where you had to ask for help on a technical roadblock.",
                    "type": "descriptive",
                    "correct_answer": "Show humility, ability to articulate the problem clearly, and willingness to learn from others."
                },
                {
                    "question_number": 11,
                    "question": "Which quality is most important for a junior data scientist?",
                    "type": "mcq",
                    "options": [
                        "Knowing every algorithm",
                        "Curiosity and a willingness to learn",
                        "Perfect presentation skills",
                        "Expertise in management"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "To ensure others can replicate your analysis, you should keep your code ____________.",
                    "type": "fib",
                    "correct_answer": "documented"
                },
                {
                    "question_number": 13,
                    "question": "If you find that your model results are unexpected, what is the best practice?",
                    "type": "mcq",
                    "options": [
                        "Submit them anyway",
                        "Double-check your assumptions and data preprocessing steps",
                        "Blame the dataset quality",
                        "Find someone else to blame"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "When your analysis does not yield the results the stakeholder hoped for, you should remain ____________.",
                    "type": "fib",
                    "correct_answer": "objective"
                },
                {
                    "question_number": 15,
                    "question": "Describe a time you managed your time effectively to handle multiple minor tasks.",
                    "type": "descriptive",
                    "correct_answer": "Show organization, prioritization skills, and meeting deadlines without compromising quality."
                },
                {
                    "question_number": 16,
                    "question": "What is the best way to handle a data request that lacks clear requirements?",
                    "type": "mcq",
                    "options": [
                        "Start working immediately",
                        "Ask clarifying questions to understand the business goal",
                        "Send a generic report",
                        "Ignore the request"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "A shared repository for version controlling your code is known as ____________.",
                    "type": "fib",
                    "correct_answer": "Git"
                },
                {
                    "question_number": 18,
                    "question": "When working in a team, what is your primary responsibility?",
                    "type": "mcq",
                    "options": [
                        "Being the loudest voice",
                        "Contributing to shared goals and supporting colleagues",
                        "Working in a silo",
                        "Focusing only on your tasks"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "Being open to change and new methods in a fast-paced environment is called ____________.",
                    "type": "fib",
                    "correct_answer": "adaptability"
                },
                {
                    "question_number": 20,
                    "question": "Describe a project where you were proud of the quality of your output.",
                    "type": "descriptive",
                    "correct_answer": "Highlight attention to detail, thorough testing, and positive impact on the business goal."
                }
            ],
            "Medium": [
                {
                    "question_number": 1,
                    "question": "How do you handle a scenario where your model's performance drops after deployment?",
                    "type": "mcq",
                    "options": [
                        "Roll back immediately",
                        "Monitor for data drift and investigate feature changes",
                        "Retrain with more data",
                        "Ignore minor drops"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "Effective project management in data science requires balancing model complexity with ____________.",
                    "type": "fib",
                    "correct_answer": "business value"
                },
                {
                    "question_number": 3,
                    "question": "When explaining an 'opaque' model to a stakeholder, how do you handle interpretability?",
                    "type": "mcq",
                    "options": [
                        "Use complex math",
                        "Use SHAP or LIME to explain feature importance",
                        "Dismiss their concerns",
                        "Show only the accuracy score"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "Aligning your technical roadmap with organizational goals is essential for ____________.",
                    "type": "fib",
                    "correct_answer": "strategic alignment"
                },
                {
                    "question_number": 5,
                    "question": "Describe a time you navigated a conflict with a stakeholder over project scope or results.",
                    "type": "descriptive",
                    "correct_answer": "Focus on negotiation, empathy, data-driven reasoning, and finding a compromise."
                },
                {
                    "question_number": 6,
                    "question": "How do you decide when a model is 'good enough' for production?",
                    "type": "mcq",
                    "options": [
                        "Highest possible accuracy",
                        "It meets pre-defined business metrics and latency requirements",
                        "It's the newest architecture",
                        "My manager said so"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "To avoid bias, it is crucial to audit your training data for ____________.",
                    "type": "fib",
                    "correct_answer": "representativeness"
                },
                {
                    "question_number": 8,
                    "question": "How do you mentor a junior team member who is struggling with technical tasks?",
                    "type": "mcq",
                    "options": [
                        "Do the work for them",
                        "Provide clear guidance and resources to help them learn",
                        "Assign them even more work",
                        "Critique them publicly"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "A culture where team members feel safe to share mistakes and learn is called ____________.",
                    "type": "fib",
                    "correct_answer": "psychological safety"
                },
                {
                    "question_number": 10,
                    "question": "Describe a situation where you had to pivot your technical approach halfway through a project.",
                    "type": "descriptive",
                    "correct_answer": "Highlight flexibility, reasoning behind the pivot, and effective communication to stakeholders."
                },
                {
                    "question_number": 11,
                    "question": "How do you manage 'technical debt' in your production pipelines?",
                    "type": "mcq",
                    "options": [
                        "Ignore it",
                        "Allocate dedicated time for refactoring and maintenance",
                        "Build everything from scratch",
                        "Keep adding patches"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "Ensuring that multiple team members can maintain your code requires good ____________.",
                    "type": "fib",
                    "correct_answer": "collaboration practices"
                },
                {
                    "question_number": 13,
                    "question": "When presenting a failed experiment to leadership, how do you handle it?",
                    "type": "mcq",
                    "options": [
                        "Hide the results",
                        "Present what was learned and pivot to the next strategy",
                        "Blame the data",
                        "Quit"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "To maintain a scalable data infrastructure, you must prioritize ____________.",
                    "type": "fib",
                    "correct_answer": "automation"
                },
                {
                    "question_number": 15,
                    "question": "Describe a time you influenced a decision by using data-backed evidence.",
                    "type": "descriptive",
                    "correct_answer": "Highlight persuasion skills, clarity of presentation, and linking data to business outcomes."
                },
                {
                    "question_number": 16,
                    "question": "What is the best way to handle a peer review process?",
                    "type": "mcq",
                    "options": [
                        "Be defensive",
                        "Ensure rigorous testing and constructive feedback",
                        "Skip the review",
                        "Only review your friends"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "Regular performance checks on models in production are essential for detecting ____________.",
                    "type": "fib",
                    "correct_answer": "model decay"
                },
                {
                    "question_number": 18,
                    "question": "How do you ensure you stay updated on rapid developments in Data Science?",
                    "type": "mcq",
                    "options": [
                        "Read only what is required",
                        "Dedicate time to continuous learning and community engagement",
                        "Never update",
                        "Depend entirely on company training"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "When data needs are complex, you must work to clarify the ____________.",
                    "type": "fib",
                    "correct_answer": "business objective"
                },
                {
                    "question_number": 20,
                    "question": "Describe a time you identified a business opportunity through data analysis that wasn't previously obvious.",
                    "type": "descriptive",
                    "correct_answer": "Show initiative, analytical depth, and ability to bridge the gap between data and strategy."
                }
            ],
            "Hard": [
                {
                    "question_number": 1,
                    "question": "As a lead, how do you balance long-term research initiatives with immediate business requests?",
                    "type": "mcq",
                    "options": [
                        "Focus only on research",
                        "Maintain a portfolio approach with a clear prioritization framework",
                        "Focus only on immediate requests",
                        "Let team members choose randomly"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "A leader in data science fosters a culture of ____________.",
                    "type": "fib",
                    "correct_answer": "data-driven decision making"
                },
                {
                    "question_number": 3,
                    "question": "How do you resolve a fundamental disagreement between two high-performing senior data scientists?",
                    "type": "mcq",
                    "options": [
                        "Choose your favorite",
                        "Use objective criteria and a structured debate/pilot phase to resolve",
                        "Let them fight it out",
                        "Ignore them"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "Scaling a data team effectively requires clear ____________.",
                    "type": "fib",
                    "correct_answer": "governance and processes"
                },
                {
                    "question_number": 5,
                    "question": "Describe a time you had to deliver bad news to executive leadership about a project.",
                    "type": "descriptive",
                    "correct_answer": "Show transparency, ownership, proposed solutions, and professional poise."
                },
                {
                    "question_number": 6,
                    "question": "How do you ensure data ethics and bias mitigation are embedded in your team's lifecycle?",
                    "type": "mcq",
                    "options": [
                        "Wait for a complaint",
                        "Integrate automated checks and mandatory ethics reviews into the workflow",
                        "Leave it to Legal",
                        "Assume the data is unbiased"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "Strong leadership in AI requires a focus on ____________.",
                    "type": "fib",
                    "correct_answer": "responsible innovation"
                },
                {
                    "question_number": 8,
                    "question": "When your department is being asked to cut budget, how do you prioritize?",
                    "type": "mcq",
                    "options": [
                        "Cut everything equally",
                        "Focus on the highest ROI projects and clear business value drivers",
                        "Cut the most expensive projects",
                        "Let the CEO decide"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "Aligning data strategy with the company's long-term vision requires ____________.",
                    "type": "fib",
                    "correct_answer": "cross-departmental advocacy"
                },
                {
                    "question_number": 10,
                    "question": "Highlight investment in others, delegation skills, and seeing growth.",
                    "type": "descriptive"
                },
                {
                    "question_number": 11,
                    "question": "How do you handle a project that is failing despite the team's effort?",
                    "type": "mcq",
                    "options": [
                        "Keep pushing",
                        "Conduct a 'post-mortem', learn, and shut it down if it no longer provides value",
                        "Blame the tools",
                        "Add more staff"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "A key challenge for senior data leaders is managing ____________.",
                    "type": "fib",
                    "correct_answer": "stakeholder expectations"
                },
                {
                    "question_number": 13,
                    "question": "How do you cultivate innovation within a team that is bogged down by maintenance?",
                    "type": "mcq",
                    "options": [
                        "Mandate innovation",
                        "Allocate 'innovation time' and reward experimentation",
                        "Ignore maintenance",
                        "Hire consultants"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "The most effective way to measure team success is by ____________.",
                    "type": "fib",
                    "correct_answer": "business outcomes"
                },
                {
                    "question_number": 15,
                    "question": "Describe a time you navigated an organizational change while leading a data team.",
                    "type": "descriptive",
                    "correct_answer": "Show leadership, clear communication, and keeping the team motivated."
                },
                {
                    "question_number": 16,
                    "question": "What is the best way to present a complex AI initiative to a non-technical board?",
                    "type": "mcq",
                    "options": [
                        "Explain the neural network architecture",
                        "Focus on ROI, strategic impact, and risk mitigation",
                        "Show lines of code",
                        "Talk about research papers"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "Building a diverse team is critical for avoiding ____________.",
                    "type": "fib",
                    "correct_answer": "groupthink"
                },
                {
                    "question_number": 18,
                    "question": "When a model is deemed unethical, what is your primary action?",
                    "type": "mcq",
                    "options": [
                        "Continue with caution",
                        "Stop deployment and rectify before moving forward",
                        "Apologize later",
                        "Ask for a different opinion"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "A truly mature data organization treats data as a ____________.",
                    "type": "fib",
                    "correct_answer": "product"
                },
                {
                    "question_number": 20,
                    "question": "Describe a time you set a long-term strategic vision for a data-driven product.",
                    "type": "descriptive",
                    "correct_answer": "Highlight vision, roadmap planning, consensus building, and successful execution."
                }
            ]
        }
    },
    "Machine Learning Engineer": {
        "Technical": {
            "Easy": [
                {
                    "question_number": 1,
                    "question": "Which of the following activation functions is most commonly used in the hidden layers of modern deep neural networks to mitigate the vanishing gradient problem?",
                    "type": "mcq",
                    "options": [
                        "Sigmoid",
                        "Tanh",
                        "ReLU",
                        "Softmax"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 2,
                    "question": "In Git, the command used to combine changes from one branch into another is known as _______.",
                    "type": "fib",
                    "correct_answer": "merge"
                },
                {
                    "question_number": 3,
                    "question": "What is the primary purpose of containerization tools like Docker in a Machine Learning workflow?",
                    "type": "mcq",
                    "options": [
                        "To speed up model training using GPUs",
                        "To ensure reproducibility and consistency across different environments",
                        "To automatically tune hyperparameters",
                        "To replace Git for version control"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "When building a REST API in Python for model inference, _______ is a modern, fast web framework that automatically generates interactive API documentation.",
                    "type": "fib",
                    "correct_answer": "FastAPI"
                },
                {
                    "question_number": 5,
                    "question": "Explain the difference between L1 (Lasso) and L2 (Ridge) regularization in machine learning models.",
                    "type": "descriptive",
                    "correct_answer": "L1 adds a penalty proportional to the absolute values of coefficients, often driving some coefficients to zero for feature selection. L2 adds a penalty proportional to the squared values of coefficients, shrinking them towards zero without eliminating them."
                },
                {
                    "question_number": 6,
                    "question": "Which tool is commonly used for experiment tracking, model registry, and artifact management in MLOps?",
                    "type": "mcq",
                    "options": [
                        "Kubernetes",
                        "MLflow",
                        "Docker",
                        "FastAPI"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "The process of converting a trained floating-point model (e.g., FP32) to lower precision (e.g., INT8) to reduce memory footprint and latency is called _______.",
                    "type": "fib",
                    "correct_answer": "quantization"
                },
                {
                    "question_number": 8,
                    "question": "In a decision tree, which metric is commonly used to measure the impurity of a split?",
                    "type": "mcq",
                    "options": [
                        "Mean Squared Error",
                        "Gini Impurity",
                        "F1 Score",
                        "Learning Rate"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "To track large datasets and model weights alongside your source code in Git, you would typically use _______ Data Version Control.",
                    "type": "fib",
                    "correct_answer": "DVC"
                },
                {
                    "question_number": 10,
                    "question": "What is the role of an orchestrator like Airflow or Prefect in an ML pipeline?",
                    "type": "descriptive",
                    "correct_answer": "They are used to programmatically author, schedule, and monitor data and machine learning workflows as Directed Acyclic Graphs (DAGs), ensuring tasks run in the correct order with proper retry logic."
                },
                {
                    "question_number": 11,
                    "question": "Which format is widely used for exporting and interoperating deep learning models across different runtimes and frameworks?",
                    "type": "mcq",
                    "options": [
                        "CSV",
                        "ONNX",
                        "PNG",
                        "JSON"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "In supervised learning, the data split used to evaluate the final performance of a tuned model after training and validation is called the _______ set.",
                    "type": "fib",
                    "correct_answer": "test"
                },
                {
                    "question_number": 13,
                    "question": "Which of the following is an ensemble learning method that builds trees sequentially by fitting each new tree to the residuals of the previous ones?",
                    "type": "mcq",
                    "options": [
                        "Random Forest",
                        "Bagging",
                        "Gradient Boosting",
                        "Standard Decision Tree"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 14,
                    "question": "In PyTorch, the base class for all neural network modules is `torch.nn._______`.",
                    "type": "fib",
                    "correct_answer": "Module"
                },
                {
                    "question_number": 15,
                    "question": "Why is data leakage dangerous in machine learning, and how can it be avoided?",
                    "type": "descriptive",
                    "correct_answer": "Data leakage occurs when information from outside the training dataset is used to create the model, leading to overly optimistic performance during evaluation. It is avoided by properly isolating training and validation/test splits before performing feature engineering or scaling."
                },
                {
                    "question_number": 16,
                    "question": "What is the primary function of Kubernetes in MLOps?",
                    "type": "mcq",
                    "options": [
                        "Writing clean Python code",
                        "Container orchestration and scaling production deployments",
                        "Version controlling large datasets",
                        "Performing hyperparameter optimization"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "When testing a machine learning pipeline or components, writing automated checks to verify code behavior without running the entire training script is known as writing _______ tests.",
                    "type": "fib",
                    "correct_answer": "unit"
                },
                {
                    "question_number": 18,
                    "question": "Which metric is generally preferred for evaluating a binary classification model when the dataset is severely imbalanced?",
                    "type": "mcq",
                    "options": [
                        "Accuracy",
                        "F1-Score / ROC-AUC",
                        "Mean Absolute Error",
                        "R-squared"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "In TensorFlow, the high-level API used for building and training models by stacking layers sequentially is `tf.keras.models._______`.",
                    "type": "fib",
                    "correct_answer": "Sequential"
                },
                {
                    "question_number": 20,
                    "question": "Describe the core responsibilities of a Machine Learning Engineer versus a Data Scientist.",
                    "type": "descriptive",
                    "correct_answer": "Data scientists focus on exploratory data analysis, statistical modeling, feature engineering, and finding insights. ML engineers focus on taking those models to production, building robust pipelines, scaling infrastructure, optimizing inference, and monitoring model performance."
                }
            ],
            "Medium": [
                {
                    "question_number": 1,
                    "question": "When using the Adam optimizer in deep learning, what do the first and second moment estimators correspond to?",
                    "type": "mcq",
                    "options": [
                        "Mean and Variance",
                        "Gradient and Hessian",
                        "Mean of gradients (momentum) and uncentered variance of gradients (RMSprop)",
                        "Learning rate and weight decay"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 2,
                    "question": "In gradient boosting frameworks like XGBoost or LightGBM, the technique of randomly sampling a fraction of training data for each tree is called _______.",
                    "type": "fib",
                    "correct_answer": "subsampling"
                },
                {
                    "question_number": 3,
                    "question": "Which of the following techniques helps stabilize the training of deep neural networks by normalizing the inputs of each layer for each training mini-batch?",
                    "type": "mcq",
                    "options": [
                        "Dropout",
                        "Batch Normalization",
                        "Data Augmentation",
                        "Early Stopping"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "The process of a model's predictive performance degrading over time due to changes in the statistical properties of the input features is known as data _______.",
                    "type": "fib",
                    "correct_answer": "drift"
                },
                {
                    "question_number": 5,
                    "question": "Explain how Support Vector Machines (SVMs) use the kernel trick to handle non-linearly separable data.",
                    "type": "descriptive",
                    "correct_answer": "The kernel trick computes the inner products of data in a higher-dimensional feature space without explicitly transforming the data into that space, allowing linear hyperplanes to separate complex non-linear boundaries efficiently."
                },
                {
                    "question_number": 6,
                    "question": "What is the primary benefit of using model serving frameworks like Triton Inference Server or BentoML over a basic Flask/FastAPI script?",
                    "type": "mcq",
                    "options": [
                        "Automatic feature engineering",
                        "Dynamic batching, concurrent model execution, and hardware acceleration out of the box",
                        "Automatic dataset versioning",
                        "Simplified Git integration"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "In PyTorch, to prevent gradient accumulation from previous iterations during training loops, you must explicitly call `optimizer._______()` before the backward pass.",
                    "type": "fib",
                    "correct_answer": "zero_grad"
                },
                {
                    "question_number": 8,
                    "question": "Which CI/CD practice is most critical for ensuring that an automated ML training pipeline functions correctly when code or data changes?",
                    "type": "mcq",
                    "options": [
                        "Manual code reviews only",
                        "Automated pipeline testing with integration and unit tests on CI runners",
                        "Deploying directly to production",
                        "Disabling unit tests to speed up builds"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "In the context of transformer architectures, the mechanism that allows the model to weigh the importance of different tokens in a sequence is called _______ attention.",
                    "type": "fib",
                    "correct_answer": "self"
                },
                {
                    "question_number": 10,
                    "question": "Discuss the trade-offs between online (real-time) inference and batch inference.",
                    "type": "descriptive",
                    "correct_answer": "Online inference provides low-latency responses for individual requests but requires high availability and complex infrastructure. Batch inference processes large volumes of data efficiently at scheduled intervals with lower infrastructure complexity, but cannot handle real-time or instantaneous requests."
                },
                {
                    "question_number": 11,
                    "question": "What is the main advantage of using a tree-based model like LightGBM over standard Gradient Boosting (GBM)?",
                    "type": "mcq",
                    "options": [
                        "It uses gradient-based one-side sampling (GOSS) and exclusive feature bundling (EFB) to train significantly faster on large datasets",
                        "It only works for linear regression",
                        "It eliminates the need for any data preprocessing",
                        "It prevents overfitting completely without hyperparameter tuning"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 12,
                    "question": "In Kubernetes, a scalable set of identical pods managed by a controller to handle high inference traffic is typically deployed as a _______.",
                    "type": "fib",
                    "correct_answer": "Deployment"
                },
                {
                    "question_number": 13,
                    "question": "Which of the following is a common technique used in recommendation systems to handle sparse user-item interaction matrices?",
                    "type": "mcq",
                    "options": [
                        "Principal Component Analysis (PCA)",
                        "Matrix Factorization (e.g., SVD)",
                        "K-Means Clustering",
                        "Decision Trees"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "When structuring a Python project for clean code and maintainability, configuration management is often handled using libraries like Hydra or _______.",
                    "type": "fib",
                    "correct_answer": "OmegaConf"
                },
                {
                    "question_number": 15,
                    "question": "Explain the concept of shadow deployment in ML model deployment strategies.",
                    "type": "descriptive",
                    "correct_answer": "A shadow deployment routes live production traffic to both the current model and the new model simultaneously. The new model processes the requests in the background, but its predictions are logged rather than returned to the user, allowing safe evaluation of performance and latency in production."
                },
                {
                    "question_number": 16,
                    "question": "What is the purpose of pruning in neural networks or tree models?",
                    "type": "mcq",
                    "options": [
                        "To increase the model size",
                        "To remove redundant parameters/branches, reducing model size and latency while maintaining accuracy",
                        "To add more training data",
                        "To increase learning rate"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "In MLOps, monitoring the model outputs against known ground truth labels that arrive later is used to detect concept _______.",
                    "type": "fib",
                    "correct_answer": "drift"
                },
                {
                    "question_number": 18,
                    "question": "Which loss function is typically used for multi-class classification problems where each sample belongs to exactly one class?",
                    "type": "mcq",
                    "options": [
                        "Mean Squared Error",
                        "Categorical Cross-Entropy",
                        "Binary Cross-Entropy",
                        "Hinge Loss"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "To profile Python code and identify performance bottlenecks or slow functions during training, developers often use the cProfile module or _______-py.",
                    "type": "fib",
                    "correct_answer": "py-spy"
                },
                {
                    "question_number": 20,
                    "question": "Describe how you would design an automated CI/CD pipeline for an ML model using Git and Docker.",
                    "type": "descriptive",
                    "correct_answer": "Upon pushing code to Git, CI triggers unit tests and code linters. If tests pass, the pipeline builds a Docker image containing the code, dependencies, and model artifacts (or downloads them from an artifact store), pushes the image to a container registry, and triggers a deployment rollout to a staging or production Kubernetes cluster."
                }
            ],
            "Hard": [
                {
                    "question_number": 1,
                    "question": "When implementing distributed training across multiple nodes using PyTorch's DistributedDataParallel (DDP), how are gradients synchronized across processes?",
                    "type": "mcq",
                    "options": [
                        "Through a centralized parameter server that updates weights sequentially",
                        "Using an All-Reduce algorithm via a backend like NCCL during the backward pass",
                        "By averaging all model weights after every epoch",
                        "Using asynchronous parameter locking via shared memory"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "In distributed model parallelism, when a single model is too large to fit into the memory of one GPU, layers are partitioned across devices, introducing pipeline bubbles known as _______ time.",
                    "type": "fib",
                    "correct_answer": "idle"
                },
                {
                    "question_number": 3,
                    "question": "What is the primary mechanism behind Post-Training Quantization (PTQ) calibration using algorithms like Entropy Calibration (TensorRT)?",
                    "type": "mcq",
                    "options": [
                        "Retraining the model from scratch with quantized weights",
                        "Minimizing the Kullback-Leibler (KL) divergence between the floating-point and quantized activation distributions",
                        "Using random noise injection to smooth gradients",
                        "Maximizing the weight decay coefficient"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "In advanced MLOps architectures, feature stores (like Feast or Tecton) decouple feature engineering from model training and serving, solving the problem of training-serving _______.",
                    "type": "fib",
                    "correct_answer": "skew"
                },
                {
                    "question_number": 5,
                    "question": "Design an end-to-end real-time fraud detection system handling 50,000 requests per second with sub-50ms latency constraints.",
                    "type": "descriptive",
                    "correct_answer": "Architecture involves an ingestion layer (Kafka), a low-latency feature store for real-time feature retrieval, a highly optimized inference service running on Triton/ONNX deployed on Kubernetes with GPU acceleration, async logging for monitoring drift, and autoscaling based on traffic spikes."
                },
                {
                    "question_number": 6,
                    "question": "How does FlashAttention optimize Transformer memory bottlenecks during training?",
                    "type": "mcq",
                    "options": [
                        "By increasing the hidden dimension size",
                        "By tiling attention computation to avoid materializing the massive $N \\times N$ attention matrix in High Bandwidth Memory (HBM)",
                        "By replacing self-attention with standard convolutions",
                        "By pruning 90% of attention heads randomly"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "In high-throughput serving environments, grouping multiple incoming inference requests into a single tensor batch dynamically on the fly is referred to as dynamic _______.",
                    "type": "fib",
                    "correct_answer": "batching"
                },
                {
                    "question_number": 8,
                    "question": "What is a major limitation of using standard SHAP (SHapley Additive exPlanations) for real-time model explainability in production?",
                    "type": "mcq",
                    "options": [
                        "It only works for linear models",
                        "It is computationally expensive and slow to compute exact values for large, complex models in real-time",
                        "It violates data privacy regulations",
                        "It requires GPU clusters for inference"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "When training LLMs or large models, activation checkpointing (or gradient _______) trades extra compute during the backward pass to save significant GPU memory.",
                    "type": "fib",
                    "correct_answer": "checkpointing"
                },
                {
                    "question_number": 10,
                    "question": "Explain how LoRA (Low-Rank Adaptation) works for fine-tuning large language models and why it is memory-efficient.",
                    "type": "descriptive",
                    "correct_answer": "LoRA freezes the pre-trained model weights and injects trainable rank decomposition matrices into each layer of the Transformer. Instead of computing gradients for all billions of parameters, it only trains a tiny fraction of parameters within these low-rank matrices, drastically reducing VRAM and optimizer state storage requirements."
                },
                {
                    "question_number": 11,
                    "question": "In the context of Kubernetes-based ML platforms (like Kubeflow or KFServing/KServe), what is the purpose of a Custom Resource Definition (CRD)?",
                    "type": "mcq",
                    "options": [
                        "To define custom Python functions inside Jupyter notebooks",
                        "To extend Kubernetes capabilities by defining custom API objects tailored for ML workflows (e.g., InferenceService)",
                        "To replace Docker container registries",
                        "To manage system-level GPU drivers"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "In streaming data pipelines for ML feature extraction, windowing operations that handle late-arriving data using watermarks are commonly implemented in frameworks like Apache _______.",
                    "type": "fib",
                    "correct_answer": "Beam"
                },
                {
                    "question_number": 13,
                    "question": "What is the primary architectural difference between Parameter Server training paradigms and All-Reduce ring-based topologies?",
                    "type": "mcq",
                    "options": [
                        "Parameter servers rely on centralized nodes to aggregate gradients, whereas ring-based All-Reduce distributes gradient communication evenly across all peer nodes in a ring structure",
                        "Ring-based topologies require no network communication",
                        "Parameter servers cannot be used with GPUs",
                        "All-Reduce only works for decision trees"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 14,
                    "question": "To ensure determinism and reproducibility in deep learning training runs across different hardware and CUDA versions, setting random seeds is insufficient; you must also configure PyTorch benchmark flags and use deterministic _______.",
                    "type": "fib",
                    "correct_answer": "algorithms"
                },
                {
                    "question_number": 15,
                    "question": "Detail the challenges and mitigation strategies when deploying large foundation models on edge devices with strict power and memory constraints.",
                    "type": "descriptive",
                    "correct_answer": "Challenges include limited RAM, thermal throttling, and battery constraints. Mitigations involve model compression (quantization to INT4/INT8, pruning, distillation), hardware-specific runtimes (TensorRT-Lite, CoreML, TFLite), and offloading heavy tasks to the cloud while keeping sensitive or latency-critical inference on-device."
                },
                {
                    "question_number": 16,
                    "question": "Which of the following describes Quantization-Aware Training (QAT)?",
                    "type": "mcq",
                    "options": [
                        "Quantizing a model after full convergence without any fine-tuning",
                        "Simulating quantization effects in the forward and backward passes during training using fake-quantization nodes",
                        "Only quantizing the bias terms of neural networks",
                        "Using higher precision integers for training"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "In advanced recommendation systems, two-tower neural network architectures separate user features and item features into independent sub-networks whose embeddings are joined at the final layer using cosine _______.",
                    "type": "fib",
                    "correct_answer": "similarity"
                },
                {
                    "question_number": 18,
                    "question": "When debugging a sudden spike in NaN (Not a Number) loss values during deep learning training, which of the following is the most robust diagnostic and corrective approach?",
                    "type": "mcq",
                    "options": [
                        "Ignoring the NaN values and continuing training",
                        "Adding gradient clipping, inspecting learning rates, checking for division by zero in loss formulations, and monitoring activation magnitudes",
                        "Switching from GPU to CPU training permanently",
                        "Doubling the batch size"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "In distributed training of massive models, ZeRO (Zero Redundancy Optimizer) eliminates memory redundancy across data-parallel processes by partitioning optimizer states, gradients, and model _______.",
                    "type": "fib",
                    "correct_answer": "parameters"
                },
                {
                    "question_number": 20,
                    "question": "Outline a comprehensive strategy for monitoring and detecting silent failures (e.g., software bugs, upstream data schema changes) in a production ML system.",
                    "type": "descriptive",
                    "correct_answer": "Implement automated data validation checks (using Great Expectations) on incoming payloads before inference, monitor prediction distribution shifts (Population Stability Index / KS-test), track system health metrics (latency, error rates, resource utilization), and maintain canary/shadow pipelines to catch anomalies early."
                }
            ]
        },
        "HR": {
            "Easy": [
                {
                    "question_number": 1,
                    "question": "When receiving critical feedback on your model training code during a peer review, what is the most professional response?",
                    "type": "mcq",
                    "options": [
                        "Defend your code immediately to show your technical expertise.",
                        "Listen openly, ask clarifying questions, and evaluate how the feedback can improve performance.",
                        "Ignore the feedback and merge the pull request anyway.",
                        "Escalate the matter to the engineering manager to bypass code review."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "When joining an ML team, demonstrating ___ helps junior engineers integrate feedback effectively and absorb domain knowledge quickly.",
                    "type": "fib",
                    "correct_answer": "coachability"
                },
                {
                    "question_number": 3,
                    "question": "You notice that the data annotations provided by an external vendor have several inconsistencies. What should you do first as an entry-level ML engineer?",
                    "type": "mcq",
                    "options": [
                        "Train the model anyway and hope it learns past the noisy data.",
                        "Document specific examples of inconsistencies and discuss them with your lead before proceeding.",
                        "Manually re-label all thousands of samples yourself without telling anyone.",
                        "Reject the entire dataset and halt all work silently."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "Proactively asking for assistance when stuck on an ML pipeline bug for hours is a key indicator of good ___.",
                    "type": "fib",
                    "correct_answer": "time management"
                },
                {
                    "question_number": 5,
                    "question": "Describe a time when your baseline machine learning model did not meet the expected accuracy metrics. How did you communicate this to your team lead and what steps did you take next?",
                    "type": "descriptive",
                    "correct_answer": "Candidate should demonstrate transparency, analytical problem-solving, structured error analysis, clear communication without being defensive, and initiative in proposing next iteration steps (e.g., feature engineering, data collection)."
                },
                {
                    "question_number": 6,
                    "question": "How should a junior ML engineer balance spending time reading latest ML research papers versus completing assigned sprint tasks?",
                    "type": "mcq",
                    "options": [
                        "Spend 80% of work hours reading papers to stay cutting-edge.",
                        "Prioritize sprint tasks first, and allocate dedicated structured time or permission from the team lead for research.",
                        "Never read research papers during work hours under any circumstances.",
                        "Only work on research and delegate sprint tasks to senior engineers."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "Documenting data cleaning steps and model hyperparameters clearly demonstrates a commitment to technical ___.",
                    "type": "fib",
                    "correct_answer": "reproducibility"
                },
                {
                    "question_number": 8,
                    "question": "You are assigned to work on an existing codebase with minimal documentation. What is the best initial approach?",
                    "type": "mcq",
                    "options": [
                        "Rewrite the entire codebase from scratch in a framework you prefer.",
                        "Complain to management about poor engineering standards.",
                        "Spend time reading the code, run existing tests, and document your understanding while seeking guidance on unclear parts.",
                        "Skip understanding the legacy code and build a parallel independent system."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 9,
                    "question": "Maintaining strong ___ allows junior engineers to collaborate smoothly with data annotators, data engineers, and software developers.",
                    "type": "fib",
                    "correct_answer": "interpersonal skills"
                },
                {
                    "question_number": 10,
                    "question": "Describe a situation where you had to quickly learn a new machine learning framework or tool to complete a project. How did you approach the learning process?",
                    "type": "descriptive",
                    "correct_answer": "Candidate should highlight adaptability, self-directed learning, practical application through small prototypes, resourcefulness, and effective time utilization under deadline pressure."
                },
                {
                    "question_number": 11,
                    "question": "A product owner asks for an ML feature implementation by the end of the day, but you know proper validation requires more time. What should you do?",
                    "type": "mcq",
                    "options": [
                        "Rush the model into production without validation to meet the deadline.",
                        "Explain the risks of skipping validation clearly to the product owner and discuss a realistic timeline.",
                        "Say yes and then turn off your communication channels when the deadline passes.",
                        "Deliver a dummy script and claim the ML model is fully functional."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "Taking full responsibility when a data preprocessing script introduces a bug shows professional ___.",
                    "type": "fib",
                    "correct_answer": "accountability"
                },
                {
                    "question_number": 13,
                    "question": "Your model training job is taking up shared GPU resources unexpectedly, slowing down a teammate's urgent experiment. What is the best course of action?",
                    "type": "mcq",
                    "options": [
                        "Let your job finish and ignore your teammate's messages.",
                        "Cancel their job so yours can complete faster.",
                        "Communicate immediately with your teammate to coordinate schedule or optimize resource allocation.",
                        "Hide your process so they cannot see who is using the GPU."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 14,
                    "question": "Demonstrating high ___ helps early-career engineers stay persistent when model training fails repeatedly during experimentation.",
                    "type": "fib",
                    "correct_answer": "resilience"
                },
                {
                    "question_number": 15,
                    "question": "Tell me about a time you made a mistake in data split logic (e.g., data leakage between train and test sets). How did you catch it, and what did you learn?",
                    "type": "descriptive",
                    "correct_answer": "Candidate should demonstrate honesty, attention to detail, post-incident analysis, proactive error detection, and implementation of preventative measures like automated testing or validation checks."
                },
                {
                    "question_number": 16,
                    "question": "Two senior engineers give you conflicting advice on which model architecture to choose for your project. How do you handle this?",
                    "type": "mcq",
                    "options": [
                        "Pick the advice of the senior engineer you like personally.",
                        "Gather benchmark data on both architectures, present the empirical results to both, and decide together.",
                        "Ignore both and use a third architecture without consulting them.",
                        "Flip a coin to decide which recommendation to implement."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "Showing active ___ during technical discussions ensures you understand data requirements correctly before starting model development.",
                    "type": "fib",
                    "correct_answer": "listening"
                },
                {
                    "question_number": 18,
                    "question": "You notice that the dataset you were handed contains potentially sensitive personal identifiers. What should you do?",
                    "type": "mcq",
                    "options": [
                        "Proceed with model training without saying anything since you were assigned the data.",
                        "Flag the data privacy concern immediately to your manager or security lead.",
                        "Delete the dataset permanently without informing anyone.",
                        "Post the sample data on an open technical forum to ask how to clean it."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "A key trait of a reliable junior engineer is ___, taking the step to update project trackers and docs without needing constant reminders.",
                    "type": "fib",
                    "correct_answer": "proactivity"
                },
                {
                    "question_number": 20,
                    "question": "How do you keep yourself motivated and focused when working on repetitive, mundane tasks like data cleaning or manual feature verification?",
                    "type": "descriptive",
                    "correct_answer": "Candidate should display a strong work ethic, understanding of the foundational importance of data quality in ML, and automation mindset (finding ways to script repetitive work while remaining diligent)."
                }
            ],
            "Medium": [
                {
                    "question_number": 1,
                    "question": "A product manager wants to launch an ML model next week, but your evaluation shows unexpected performance drops on minority demographic groups. How do you handle this?",
                    "type": "mcq",
                    "options": [
                        "Approve the launch to meet business deadlines and fix it in a future patch.",
                        "Clearly communicate the ethical and business risks to the PM, recommend delaying release until biased performance is mitigated, and propose a mitigation plan.",
                        "Secretly alter evaluation metrics so the model appears ready for launch.",
                        "Blame the data collection team publicly in a company-wide email."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "Effective ___ skills are required when translating complex machine learning metrics like F1-score or AUC-ROC into business ROI for non-technical stakeholders.",
                    "type": "fib",
                    "correct_answer": "communication"
                },
                {
                    "question_number": 3,
                    "question": "Your team is debating between a complex Deep Learning model with high accuracy but high latency, versus a simple XGBoost model with low latency and lower accuracy. How do you resolve this technical trade-off?",
                    "type": "mcq",
                    "options": [
                        "Always choose Deep Learning because it uses newer technology.",
                        "Always choose XGBoost because latency is the only metric that matters.",
                        "Analyze product SLA constraints and business requirements first, then run cost-benefit benchmarks to guide the decision.",
                        "Refuse to make a choice and let the software developers handle it."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 4,
                    "question": "Balancing rapid model experimentation with production-grade software architecture requires strong technical ___.",
                    "type": "fib",
                    "correct_answer": "pragmatism"
                },
                {
                    "question_number": 5,
                    "question": "Describe a scenario where a deployed machine learning model suffered from severe performance decay due to concept drift in production. How did you identify, troubleshoot, and resolve the issue?",
                    "type": "descriptive",
                    "correct_answer": "Candidate should explain monitoring strategies (data/concept drift detectors), root-cause analysis, cross-functional coordination with backend engineering/data engineering, and long-term resolution (automated retraining pipelines, shadow deployments)."
                },
                {
                    "question_number": 6,
                    "question": "The Data Engineering team refuses to modify a pipeline schema that is causing downstream ML feature extraction failures, citing tight deadlines. How do you navigate this conflict?",
                    "type": "mcq",
                    "options": [
                        "Hack a workaround in your code without addressing the root cause.",
                        "Schedule a collaborative meeting to explain the business impact, understand their constraints, and agree on a mutually feasible timeline or compromise.",
                        "Escalate directly to the CTO to force them to change the schema immediately.",
                        "Stop working until the Data Engineering team gives in to your request."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "Navigating technical disagreements between ML researchers and software platform teams requires strong ___.",
                    "type": "fib",
                    "correct_answer": "negotiation"
                },
                {
                    "question_number": 8,
                    "question": "Business stakeholders are urging you to deploy a recommendation model built with unvalidated user data to boost holiday sales. What is your response?",
                    "type": "mcq",
                    "options": [
                        "Comply immediately because revenue is the ultimate priority.",
                        "Highlight compliance, privacy, and performance risks, and propose an expedited validation check before deployment.",
                        "Deploy the model secretly under a different name.",
                        "Refuse to talk to the business stakeholders."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "Ensuring models do not violate data governance policies or ethical guidelines requires strong professional ___.",
                    "type": "fib",
                    "correct_answer": "integrity"
                },
                {
                    "question_number": 10,
                    "question": "Describe a time when you had to mentor a junior ML engineer on MLOps best practices (such as CI/CD for ML, feature stores, or model versioning). How did you structure your mentorship?",
                    "type": "descriptive",
                    "correct_answer": "Candidate should demonstrate patience, structured knowledge transfer, empowering others, setting clear engineering standards, and balancing guidance with allowing autonomy."
                },
                {
                    "question_number": 11,
                    "question": "Your project suffers from technical debt because previous models were deployed as monolithic scripts without modular testing. How do you address this while maintaining feature velocity?",
                    "type": "mcq",
                    "options": [
                        "Stop all new feature delivery for six months to refactor everything.",
                        "Ignore the technical debt and continue adding features on top of legacy scripts.",
                        "Propose an incremental refactoring strategy integrated into regular sprint planning.",
                        "Quit the project and join a team with cleaner code."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 12,
                    "question": "When working in an agile environment, mid-level engineers must exhibit strong ___ to adjust priorities as data availability changes.",
                    "type": "fib",
                    "correct_answer": "flexibility"
                },
                {
                    "question_number": 13,
                    "question": "You realize that a model training run you launched on a multi-node GPU cluster had an error and wasted $5,000 in cloud compute. What do you do?",
                    "type": "mcq",
                    "options": [
                        "Delete the logs and hope finance does not notice.",
                        "Blame the cloud provider for infrastructure instability.",
                        "Inform your manager immediately, explain what happened, and implement cost alerting and checks to prevent future occurrences.",
                        "Attempt to hide the costs by spreading them across other department budgets."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 14,
                    "question": "Building trust with cross-functional software teams requires ML engineers to practice consistent ___ in code quality and model documentation.",
                    "type": "fib",
                    "correct_answer": "transparency"
                },
                {
                    "question_number": 15,
                    "question": "Tell me about a time you pushed back against a business request because the proposed machine learning solution was inappropriate or over-engineered for the problem.",
                    "type": "descriptive",
                    "correct_answer": "Candidate should demonstrate pragmatic decision-making, cost/complexity consciousness, ability to recommend simpler rule-based or statistical alternatives, and effective stakeholder communication."
                },
                {
                    "question_number": 16,
                    "question": "A production service goes down because an ML model inference endpoint ran out of memory under peak traffic. During the post-mortem, what is your approach?",
                    "type": "mcq",
                    "options": [
                        "Blame the DevOps engineer for not setting up auto-scaling rules.",
                        "Focus on blameless root-cause analysis, identifying memory leaks or payload edge cases, and establishing fallback mechanisms.",
                        "Insist that model memory usage is outside your responsibility.",
                        "Refuse to participate in the post-mortem discussion."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "Conducting a constructive, blameless post-mortem fosters psychological ___ across engineering teams.",
                    "type": "fib",
                    "correct_answer": "safety"
                },
                {
                    "question_number": 18,
                    "question": "You are managing multiple projects: one high-visibility executive initiative and two critical infrastructure maintenance tasks. How do you prioritize?",
                    "type": "mcq",
                    "options": [
                        "Only work on the executive initiative because it offers higher career visibility.",
                        "Focus solely on maintenance tasks and ignore executive requests.",
                        "Evaluate business impact, technical dependencies, and deadlines; align priorities with your lead and communicate trade-offs clearly.",
                        "Work on whichever task is easiest first."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 19,
                    "question": "Mid-level ML engineers demonstrate technical leadership by taking personal ___ for model performance end-to-end, from training to production monitoring.",
                    "type": "fib",
                    "correct_answer": "ownership"
                },
                {
                    "question_number": 20,
                    "question": "Walk me through a complex ML project that failed to reach production. What were the root causes (technical vs organizational), and what lessons did you apply to subsequent projects?",
                    "type": "descriptive",
                    "correct_answer": "Candidate should display self-reflection, objective analysis of technical failure vs alignment failure, resilience, and actionable organizational or engineering takeaways implemented in later work."
                }
            ],
            "Hard": [
                {
                    "question_number": 1,
                    "question": "Executive leadership wants to mandate Generative AI adoption across all product lines within two quarters. However, your team lacks infrastructure and data readiness. As a Senior/Lead ML Engineer, how do you respond?",
                    "type": "mcq",
                    "options": [
                        "Agree blindly to executive demands and force your team into mandatory 80-hour workweeks.",
                        "Publicly criticize executive leadership during an all-hands meeting for lack of understanding.",
                        "Present a realistic roadmap detailing current gaps, mitigation strategies, proof-of-concept timelines, and resource requirements to reach the goal responsibly.",
                        "Refuse to implement any Generative AI capabilities under any circumstances."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 2,
                    "question": "A key responsibility of an ML Leader is aligning AI strategies with broad organizational goals through long-term technical ___.",
                    "type": "fib",
                    "correct_answer": "vision"
                },
                {
                    "question_number": 3,
                    "question": "A senior research scientist on your team insists on spending months prototyping novel algorithms rather than adopting existing open-source models that meet business SLAs. How do you manage this situation?",
                    "type": "mcq",
                    "options": [
                        "Allow them infinite time to research, ignoring product deadlines.",
                        "Fire the research scientist immediately to set an example.",
                        "Align on product impact metrics and time-to-market constraints, framing pure research within innovation spikes while keeping main deliverables on track.",
                        "Reassign all software tasks to the researcher so they stop doing research."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 4,
                    "question": "Leading large-scale MLOps transformations requires effective change management and diplomatic ___ across executive and engineering tiers.",
                    "type": "fib",
                    "correct_answer": "influence"
                },
                {
                    "question_number": 5,
                    "question": "How do you establish and enforce an Ethical AI and Governance framework across multiple ML engineering sub-teams with competing velocity deadlines?",
                    "type": "descriptive",
                    "correct_answer": "Candidate should detail strategic framework creation, integrating compliance and fairness gates into standard CI/CD pipelines, securing leadership buy-in, training engineers, and balancing governance rigor with development speed."
                },
                {
                    "question_number": 6,
                    "question": "Your company is facing severe cloud cost overruns due to expanding LLM training and fine-tuning workloads. How do you lead an initiative to optimize compute spending without halting innovation?",
                    "type": "mcq",
                    "options": [
                        "Shut down all GPU clusters immediately and stop model development.",
                        "Conduct an audit of training workloads, establish resource quotas, champion efficiency techniques (e.g., quantization, pruning, spot instances), and implement cost tracking dashboards.",
                        "Ask accounting to double the department budget without providing justification.",
                        "Delegate the entire issue to junior engineers without oversight."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "Making high-stakes decisions on whether to build in-house ML platform tooling versus buying vendor solutions requires strong executive ___.",
                    "type": "fib",
                    "correct_answer": "decisiveness"
                },
                {
                    "question_number": 8,
                    "question": "A core business ML algorithm is accused by an external investigative report of displaying bias in customer loan approvals. As the ML Lead, what is your immediate course of action?",
                    "type": "mcq",
                    "options": [
                        "Deny all claims publicly before investigating.",
                        "Lead a thorough audit of model decisions, cooperate transparently with legal/PR/compliance teams, halt or fallback biased endpoints if necessary, and publish remediation plans.",
                        "Blame third-party software vendors and refuse internal responsibility.",
                        "Delete historical model predictions to prevent further scrutiny."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "Navigating high-pressure public controversies or regulatory challenges around AI models requires exceptional leadership ___.",
                    "type": "fib",
                    "correct_answer": "composure"
                },
                {
                    "question_number": 10,
                    "question": "Describe how you maintain team morale and retention during prolonged periods of experimental failure or when high-profile ML initiatives are canceled due to changing market conditions.",
                    "type": "descriptive",
                    "correct_answer": "Candidate should emphasize empathetic leadership, reframing failure as learning, celebrating milestone achievements, transparent communication, realigning team focus to new impactful challenges, and psychological support."
                },
                {
                    "question_number": 11,
                    "question": "Competitors are actively trying to poach top ML talent from your team with significantly higher compensation offers. How do you work to retain your key engineers?",
                    "type": "mcq",
                    "options": [
                        "Threaten engineers with legal action if they speak to recruiters.",
                        "Focus on career growth pathways, technical autonomy, compelling project impact, and advocate with HR/Leadership for competitive compensation adjustments.",
                        "Ignore the situation and assume engineers will stay out of loyalty.",
                        "Tell the team that anyone considering leaving will be terminated early."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "Developing future technical leaders on your ML team depends on effective delegation and proactive ___.",
                    "type": "fib",
                    "correct_answer": "mentorship"
                },
                {
                    "question_number": 13,
                    "question": "You realize a legacy ML product line brings in modest revenue but consumes 60% of your team's maintenance bandwidth. How do you approach executive stakeholders to sunset it?",
                    "type": "mcq",
                    "options": [
                        "Decommission the system without telling executives or customers.",
                        "Present data showing maintenance opportunity costs, propose a migration/sunset strategy, and demonstrate how reallocated bandwidth will drive higher ROI projects.",
                        "Continue supporting the system indefinitely without raising concerns.",
                        "Deliberately break the system so customers cancel their subscriptions."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "Making tough decisions to shut down unpromising multi-million dollar ML research efforts requires strong financial stewardship and professional ___.",
                    "type": "fib",
                    "correct_answer": "courage"
                },
                {
                    "question_number": 15,
                    "question": "Detail a scenario where you structured the organizational collaboration model between centralized Data Science Research teams and embedded ML Systems Engineering teams to eliminate friction.",
                    "type": "descriptive",
                    "correct_answer": "Candidate should discuss organizational design, clear handoff interfaces, shared goals, standard tooling adoption, cross-functional integration, and eliminating 'throw code over the wall' mentalities."
                },
                {
                    "question_number": 16,
                    "question": "A brilliant Lead Principal ML Architect on your team is consistently condescending toward junior team members, eroding team morale. How do you address this?",
                    "type": "mcq",
                    "options": [
                        "Tolerate the toxic behavior because their technical output is irreplaceable.",
                        "Have a direct 1-on-1 performance meeting setting clear behavioral expectations, providing specific feedback, and establishing consequences if toxic behavior continues.",
                        "Complain about the architect to junior team members behind their back.",
                        "Isolate the architect completely so they never interact with anyone."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "Fostering an inclusive culture where every engineer feels respected is essential for team ___.",
                    "type": "fib",
                    "correct_answer": "cohesion"
                },
                {
                    "question_number": 18,
                    "question": "Your company is planning an acquisition of an AI startup. What role do you play in conducting technical and team due diligence?",
                    "type": "mcq",
                    "options": [
                        "Focus only on financial figures and leave technical evaluation to accountants.",
                        "Assess their model architectures, IP integrity, data pipeline scalability, code quality, infrastructure costs, and team culture fit.",
                        "Recommend acquiring the company based solely on marketing claims.",
                        "Refuse to participate in M&A activities."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "Senior leadership must balance long-term strategic research investments with short-term delivery commitments through effective operational ___.",
                    "type": "fib",
                    "correct_answer": "prioritization"
                },
                {
                    "question_number": 20,
                    "question": "How do you reorient your organization's machine learning strategy when rapid technological disruptions (such as Foundation Models/LLMs) make your current proprietary model stack obsolete?",
                    "type": "descriptive",
                    "correct_answer": "Candidate should explain technology horizon scanning, strategic pivot management, retraining/upskilling workforce, reevaluating build vs buy dynamics, minimizing technical debt during pivots, and maintaining stakeholder confidence."
                }
            ]
        },
        "Behavioral": {
            "Easy": [
                {
                    "question_number": 1,
                    "question": "When you encounter a bug in your machine learning data pipeline that you cannot immediately solve, what is the best first step?",
                    "type": "mcq",
                    "options": [
                        "A) Delete the pipeline and rewrite it from scratch.",
                        "B) Isolate the failure point by logging intermediate outputs and checking data schemas.",
                        "C) Ignore the bug if the model still trains without throwing an error.",
                        "D) Immediately escalate the issue to the VP of Engineering."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "The practice of actively listening to stakeholders to understand their business requirements before building an ML model is known as requirement ________.",
                    "type": "fib",
                    "correct_answer": "gathering"
                },
                {
                    "question_number": 3,
                    "question": "How should you handle constructive feedback from a senior engineer during a code review of your Python feature engineering script?",
                    "type": "mcq",
                    "options": [
                        "A) Argue that your code works and refuse to change it.",
                        "B) Quietly ignore the comments and push the code anyway.",
                        "C) Thank them, review the feedback objectively, and apply the suggested best practices.",
                        "D) Report them to HR for being overly critical."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 4,
                    "question": "When working in a cross-functional team, sharing project updates clearly and consistently helps maintain team ________.",
                    "type": "fib",
                    "correct_answer": "alignment"
                },
                {
                    "question_number": 5,
                    "question": "Describe a time when you had to learn a new tool, library, or framework quickly to complete a machine learning task. How did you approach the learning curve?",
                    "type": "descriptive",
                    "correct_answer": "Proactive learning, utilizing documentation, building a small proof-of-concept, and seeking mentorship."
                },
                {
                    "question_number": 6,
                    "question": "If you realize you will miss a minor deadline for submitting your model evaluation report due to unexpected data cleaning issues, what should you do?",
                    "type": "mcq",
                    "options": [
                        "A) Wait until the deadline passes and hope nobody notices.",
                        "B) Submit incomplete and untested results to meet the deadline.",
                        "C) Inform your manager proactively, explain the roadblock, and provide a realistic revised timeline.",
                        "D) Blame the data engineering team for the delay."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 7,
                    "question": "Adhering to coding standards and writing clean, readable scripts demonstrates professional ________.",
                    "type": "fib",
                    "correct_answer": "accountability"
                },
                {
                    "question_number": 8,
                    "question": "You notice that a dataset provided for an entry-level classification task contains missing values. What is the most appropriate collaborative approach?",
                    "type": "mcq",
                    "options": [
                        "A) Drop all rows with missing values without checking the impact on data distribution.",
                        "B) Discuss the missing data patterns with the data provider or team to understand the root cause before imputing.",
                        "C) Make up random values to fill the gaps so the script runs.",
                        "D) Complain that the data is unusable and stop working."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "Working effectively with teammates from diverse technical backgrounds requires strong interpersonal ________.",
                    "type": "fib",
                    "correct_answer": "communication"
                },
                {
                    "question_number": 10,
                    "question": "Describe a situation where you had a disagreement with a peer regarding how to handle outliers in a dataset. How did you resolve it?",
                    "type": "descriptive",
                    "correct_answer": "Data-driven discussion, testing both approaches, open-mindedness, and reaching a consensus."
                },
                {
                    "question_number": 11,
                    "question": "When documenting your exploratory data analysis (EDA) notebook for team members, what is the most important practice?",
                    "type": "mcq",
                    "options": [
                        "A) Writing zero comments to keep the notebook mysterious.",
                        "B) Including clear markdown cells explaining your assumptions, methodology, and key takeaways.",
                        "C) Only including raw, unformatted code blocks.",
                        "D) Pasting screenshots of code instead of actual text."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "The ability to bounce back and maintain productivity after encountering a model training failure or poor evaluation metric is known as ________.",
                    "type": "fib",
                    "correct_answer": "resilience"
                },
                {
                    "question_number": 13,
                    "question": "If a team member asks for help debugging their model script while you are in the middle of an important task, how should you handle it?",
                    "type": "mcq",
                    "options": [
                        "A) Tell them to go away and never bother you.",
                        "B) Immediately drop your current task and spend the entire day on their problem.",
                        "C) Acknowledge their request, finish or safely pause your immediate priority, and set a specific time to help them.",
                        "D) Ignore their message completely."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 14,
                    "question": "Taking ownership of your mistakes when a model experiment fails rather than shifting blame shows strong personal ________.",
                    "type": "fib",
                    "correct_answer": "responsibility"
                },
                {
                    "question_number": 15,
                    "question": "Describe a time when you received negative feedback on your presentation or code. How did you process it and what did you change?",
                    "type": "descriptive",
                    "correct_answer": "Receptivity, lack of defensiveness, implementing changes, and continuous self-improvement."
                },
                {
                    "question_number": 16,
                    "question": "How should you approach a recurring status meeting where you have no major updates on your machine learning experiment?",
                    "type": "mcq",
                    "options": [
                        "A) Skip the meeting without telling anyone.",
                        "B) Invent false progress to sound busy.",
                        "C) Share minor learnings, ongoing challenges, and small milestones honestly.",
                        "D) Spend the meeting complaining about the compute cluster."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 17,
                    "question": "Being open to new ideas and changing your approach when presented with better evidence is a sign of mental ________.",
                    "type": "fib",
                    "correct_answer": "flexibility"
                },
                {
                    "question_number": 18,
                    "question": "What is the best way to manage your daily tasks when working on multiple small ML feature tickets?",
                    "type": "mcq",
                    "options": [
                        "A) Work on whatever looks most fun at the moment.",
                        "B) Prioritize tasks based on project impact and dependencies using a task tracker.",
                        "C) Do all tasks simultaneously in random order.",
                        "D) Wait for your manager to assign every single hourly task."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "Safeguarding sensitive user data during model training and preprocessing complies with privacy ________.",
                    "type": "fib",
                    "correct_answer": "regulations"
                },
                {
                    "question_number": 20,
                    "question": "Describe an instance where you successfully collaborated with a non-technical stakeholder to explain an ML metric like accuracy or precision. How did you make it understandable?",
                    "type": "descriptive",
                    "correct_answer": "Using analogies, avoiding technical jargon, focusing on business impact, and checking for understanding."
                }
            ],
            "Medium": [
                {
                    "question_number": 1,
                    "question": "You discover that a deployed model is showing signs of concept drift, but the product team wants to delay retraining to launch a new UI feature. How do you handle this?",
                    "type": "mcq",
                    "options": [
                        "A) Silently deploy a retrained model without telling anyone and risk breaking the UI integration.",
                        "B) Refuse to work until the UI feature is canceled.",
                        "C) Present data on the performance degradation to product managers and negotiate a balanced timeline that accommodates both retraining and the UI release.",
                        "D) Blame the product team in front of leadership for poor planning."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 2,
                    "question": "The process of translating complex machine learning outputs into actionable business value for stakeholders is called value ________.",
                    "type": "fib",
                    "correct_answer": "translation"
                },
                {
                    "question_number": 3,
                    "question": "A mid-level engineer on your team is consistently missing code review deadlines, impacting your model integration timeline. What is your best course of action?",
                    "type": "mcq",
                    "options": [
                        "A) Complain to the engineering manager immediately without talking to the peer.",
                        "B) Have an empathetic 1-on-1 discussion to understand their bottlenecks and offer support or workload rebalancing.",
                        "C) Rewrite their code yourself without letting them know.",
                        "D) Publicly call them out in the next team sync."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "Anticipating potential bottlenecks in an ML pipeline before they impact production stability demonstrates strategic ________.",
                    "type": "fib",
                    "correct_answer": "foresight"
                },
                {
                    "question_number": 5,
                    "question": "Describe a situation where a machine learning project you were leading scope-crept significantly due to changing stakeholder requests. How did you manage expectations and project scope?",
                    "type": "descriptive",
                    "correct_answer": "Managing scope, stakeholder negotiation, impact analysis, documenting changes, and setting clear boundaries."
                },
                {
                    "question_number": 6,
                    "question": "You built a complex deep learning model, but the stakeholders prefer a simpler, interpretable logistic regression model due to latency and compliance needs. How do you respond?",
                    "type": "mcq",
                    "options": [
                        "A) Argue that deep learning is always superior and refuse to use logistic regression.",
                        "B) Accept their requirements gracefully, evaluate the simpler model, and explain trade-offs transparently.",
                        "C) Deploy the deep learning model anyway under a hidden endpoint.",
                        "D) Resign from the project."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "Balancing technical debt reduction with the delivery of new machine learning features requires careful task ________.",
                    "type": "fib",
                    "correct_answer": "prioritization"
                },
                {
                    "question_number": 8,
                    "question": "During a cross-functional sprint review, a data engineer blames your model for causing pipeline memory overflows. How do you address this professionally?",
                    "type": "mcq",
                    "options": [
                        "A) Immediately argue that their data pipeline is badly engineered.",
                        "B) Stay calm, propose a joint debugging session to profile memory usage, and fix the root cause collaboratively.",
                        "C) Stay silent and ignore the accusation.",
                        "D) Escalate to the CEO immediately."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "Encouraging open discussion of failed model experiments in team retrospectives builds a culture of psychological ________.",
                    "type": "fib",
                    "correct_answer": "safety"
                },
                {
                    "question_number": 10,
                    "question": "Describe a time when you had to mentor or onboard a junior team member onto an ML project. How did you balance giving them autonomy with ensuring project quality?",
                    "type": "descriptive",
                    "correct_answer": "Delegation, scaffolding tasks, providing constructive feedback, patience, and setting clear milestones."
                },
                {
                    "question_number": 11,
                    "question": "You notice that your team has been relying on an outdated model evaluation metric that encourages false positives. How do you introduce a better metric?",
                    "type": "mcq",
                    "options": [
                        "A) Change the metric overnight without telling anyone.",
                        "B) Prepare a brief comparative analysis showing the business risks of the old metric and pitch the new metric in a team meeting.",
                        "C) Complain to management that the team is incompetent.",
                        "D) Do nothing and let the business suffer the consequences."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "Facilitating constructive compromise between conflicting technical opinions from different team members requires strong ________ skills.",
                    "type": "fib",
                    "correct_answer": "mediation"
                },
                {
                    "question_number": 13,
                    "question": "Your model shows high offline accuracy in experiments, but performs poorly after being deployed to production due to a feature representation mismatch. How do you handle this?",
                    "type": "mcq",
                    "options": [
                        "A) Blame the inference API developers for messing up your features.",
                        "B) Conduct a thorough audit of training vs. inference pipelines, identify the discrepancy, and establish automated parity checks.",
                        "C) Hide the performance drop and hope users don't notice.",
                        "D) Delete the inference service."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "Ensuring that different teams across the organization understand the limitations and ethical boundaries of deployed AI models promotes AI ________.",
                    "type": "fib",
                    "correct_answer": "governance"
                },
                {
                    "question_number": 15,
                    "question": "Describe a situation where you had to deliver bad news to leadership\u2014such as a key ML model failing to meet accuracy thresholds right before launch. How did you communicate it and what was your recovery plan?",
                    "type": "descriptive",
                    "correct_answer": "Transparency, timely communication, presenting a clear mitigation plan, and data-backed reasoning."
                },
                {
                    "question_number": 16,
                    "question": "You are assigned to lead a multi-week ML project with engineers who have conflicting working styles. What is your strategy for team cohesion?",
                    "type": "mcq",
                    "options": [
                        "A) Force everyone to adopt your exact working style immediately.",
                        "B) Establish team working agreements early, respect individual strengths, and maintain transparent communication channels.",
                        "C) Let chaos ensue and assume everything will work out.",
                        "D) Work in complete isolation and refuse to collaborate."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "The ability to look at a complex machine learning system holistically from data ingestion to user inference is known as systems ________.",
                    "type": "fib",
                    "correct_answer": "thinking"
                },
                {
                    "question_number": 18,
                    "question": "A stakeholder demands that you build a predictive model for a use case where historical data is severely biased and incomplete. How do you respond?",
                    "type": "mcq",
                    "options": [
                        "A) Build the model anyway and let the bias propagate to users.",
                        "B) Educate the stakeholder on data limitations, ethical risks, and propose alternative data collection or scoping strategies.",
                        "C) Tell them they are foolish and walk away.",
                        "D) Fake the data to make the model look good."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "Continuously evaluating your own assumptions and biases when designing machine learning algorithms requires intellectual ________.",
                    "type": "fib",
                    "correct_answer": "humility"
                },
                {
                    "question_number": 20,
                    "question": "Describe a time when you had to refactor a messy, legacy machine learning codebase while under tight deadlines. How did you prioritize what to fix?",
                    "type": "descriptive",
                    "correct_answer": "Risk assessment, incremental refactoring, writing unit tests, balancing speed with code quality."
                }
            ],
            "Hard": [
                {
                    "question_number": 1,
                    "question": "As a lead ML engineer, you discover that a high-profile production recommendation model is amplifying discriminatory bias against a protected demographic group. The business impact of shutting it down immediately is millions in revenue. What is your executive recommendation?",
                    "type": "mcq",
                    "options": [
                        "A) Keep the model running to protect quarterly revenue; ethics can wait.",
                        "B) Immediately halt the affected model traffic or apply emergency fallback rules, transparently brief executive leadership, and initiate a rapid bias mitigation sprint.",
                        "C) Silently tweak the training data overnight without informing legal or compliance.",
                        "D) Blame the product team for approving the feature set."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "Guiding an entire organization through a paradigm shift in how they view data quality and AI ethics requires visionary leadership and change ________.",
                    "type": "fib",
                    "correct_answer": "management"
                },
                {
                    "question_number": 3,
                    "question": "Two senior teams (Platform Infrastructure and Product Data Science) are deadlocked over whether to adopt a cloud-agnostic MLOps framework or a vendor-lock-in proprietary solution, stalling company-wide AI initiatives. As a Principal ML Leader, how do you resolve this?",
                    "type": "mcq",
                    "options": [
                        "A) Side with your friends on the platform team without evaluating technical merits.",
                        "B) Conduct a comprehensive total cost of ownership (TCO) and risk analysis, host a joint architectural review, and make a principled, data-backed decision aligned with long-term company strategy.",
                        "C) Tell them both to figure it out while you take PTO.",
                        "D) Cancel all AI initiatives."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "Aligning complex machine learning research roadmaps with overarching corporate business goals requires strong strategic ________.",
                    "type": "fib",
                    "correct_answer": "vision"
                },
                {
                    "question_number": 5,
                    "question": "Describe a situation where you had to convince executive leadership to kill a pet AI project that was technically fascinating but lacked viable ROI or ethical sustainability. How did you frame the conversation?",
                    "type": "descriptive",
                    "correct_answer": "Executive communication, ROI analysis, risk mitigation, objective data presentation, pivoting resources to high-value areas."
                },
                {
                    "question_number": 6,
                    "question": "An external audit reveals that your enterprise generative AI system is susceptible to sophisticated prompt injection attacks that could leak proprietary corporate data. Fixing it requires delaying your company's flagship product launch by a month. What is your leadership stance?",
                    "type": "mcq",
                    "options": [
                        "A) Launch on time and deal with security breaches as they happen.",
                        "B) Prioritize security and data integrity by halting the launch, rallying the engineering leads to patch the vulnerability, and communicating transparently with stakeholders.",
                        "C) Hide the audit report from the board of directors.",
                        "D) Fire the security auditors."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "Fostering a culture of rigorous scientific peer review and model validation across multiple engineering squads establishes organizational ________.",
                    "type": "fib",
                    "correct_answer": "rigor"
                },
                {
                    "question_number": 8,
                    "question": "You are leading a large organization of machine learning engineers, and morale is plummeting due to repeated project cancellations caused by shifting executive priorities. How do you restore team trust and engagement?",
                    "type": "mcq",
                    "options": [
                        "A) Tell the engineers to stop complaining and work harder.",
                        "B) Advocate upward for team protection, create transparent feedback loops, decouple internal research spikes from volatile product shifts, and celebrate small engineering wins.",
                        "C) Resign immediately without warning.",
                        "D) Pretend nothing is wrong and continue assigning doomed projects."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "Empowering senior engineers to make autonomous architectural decisions while maintaining overarching system guardrails is a hallmark of empowering ________.",
                    "type": "fib",
                    "correct_answer": "leadership"
                },
                {
                    "question_number": 10,
                    "question": "Describe a high-stakes crisis where a core production machine learning model suffered catastrophic failure during peak traffic (e.g., Black Friday). How did you manage the incident response and lead your team through the post-mortem?",
                    "type": "descriptive",
                    "correct_answer": "Incident command, rapid triage, blameless post-mortem, systemic remediation, stakeholder communication."
                },
                {
                    "question_number": 11,
                    "question": "A brilliant but toxic senior ML researcher consistently demeans junior engineers during code reviews and design sessions. Their research output is top-tier. How do you handle this leadership dilemma?",
                    "type": "mcq",
                    "options": [
                        "A) Ignore the toxicity because their research brings in grant money or prestige.",
                        "B) Fire the junior engineers to appease the senior researcher.",
                        "C) Address the behavior directly with clear performance boundaries; if uncorrected, prioritize team psychological safety and culture over individual output by offboarding them.",
                        "D) Publicly humiliate the senior researcher in retaliation."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 12,
                    "question": "Balancing cutting-edge AI research exploration with stable, production-ready MLOps infrastructure requires meticulous portfolio ________.",
                    "type": "fib",
                    "correct_answer": "management"
                },
                {
                    "question_number": 13,
                    "question": "Your company is considering acquiring a smaller startup primarily for its proprietary ML models and talent. You are tasked with technical due diligence. You discover their models are unscalable and poorly documented. How do you report this?",
                    "type": "mcq",
                    "options": [
                        "A) Give a glowing review because you want the acquisition to happen.",
                        "B) Provide an objective, unvarnished risk assessment detailing the technical debt, required refactoring costs, and realistic integration timeline to executive leadership.",
                        "C) Delete your findings so nobody knows.",
                        "D) Buy the startup with your own money."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "Ensuring AI systems comply with emerging global regulatory frameworks like the EU AI Act requires cross-functional collaboration with legal and ________ teams.",
                    "type": "fib",
                    "correct_answer": "compliance"
                },
                {
                    "question_number": 15,
                    "question": "Describe a scenario where you had to restructure an underperforming ML department or squad. How did you assess talent, realign roles, and maintain team motivation during the transition?",
                    "type": "descriptive",
                    "correct_answer": "Talent assessment, empathetic restructuring, transparent communication, role alignment, rebuilding trust."
                },
                {
                    "question_number": 16,
                    "question": "As Head of AI, you are asked by the CEO to build a facial recognition surveillance feature for enterprise clients that raises severe civil liberties and privacy concerns. What is your leadership approach?",
                    "type": "mcq",
                    "options": [
                        "A) Build it immediately without question to please the CEO.",
                        "B) Prepare a comprehensive ethical risk memo, consult legal counsel, present alternative privacy-preserving approaches, and respectfully decline if ethical red lines are crossed.",
                        "C) Leak company internal emails to the press.",
                        "D) Outsource the unethical work to a third party."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "Building long-term technological resilience against rapidly evolving AI threats and adversarial attacks requires continuous innovation and threat ________.",
                    "type": "fib",
                    "correct_answer": "modeling"
                },
                {
                    "question_number": 18,
                    "question": "You are tasked with allocating a multi-million dollar cloud GPU budget across five competing machine learning initiatives. How do you ensure optimal ROI and fairness?",
                    "type": "mcq",
                    "options": [
                        "A) Give all the budget to your favorite project.",
                        "B) Distribute the budget equally without checking if projects are viable.",
                        "C) Establish a governance committee, evaluate projects based on projected business value, technical feasibility, and resource efficiency, and tie funding to quarterly milestones.",
                        "D) Spend it all on personal crypto mining."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 19,
                    "question": "Transforming an ad-hoc machine learning experimentation culture into a standardized, industrialized enterprise MLOps powerhouse requires operational ________.",
                    "type": "fib",
                    "correct_answer": "maturity"
                },
                {
                    "question_number": 20,
                    "question": "Describe a time when you drove a major company-wide technical transformation (e.g., migrating from on-prem clusters to a cloud-native MLOps platform). How did you overcome organizational resistance and ensure adoption?",
                    "type": "descriptive",
                    "correct_answer": "Change management, stakeholder buy-in, training programs, clear migration roadmap, addressing friction points."
                }
            ]
        }
    },
    "AI Engineer": {
        "Technical": {
            "Easy": [
                {
                    "question_number": 1,
                    "question": "What does RAG stand for in the context of LLMs?",
                    "type": "mcq",
                    "options": [
                        "Retrieval Augmented Generation",
                        "Random Access Generation",
                        "Recursive Algorithmic Generation",
                        "Rapid Artificial Grouping"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 2,
                    "question": "The process of providing a few examples within a prompt to guide model output is known as _______ prompting.",
                    "type": "fib",
                    "correct_answer": "few-shot"
                },
                {
                    "question_number": 3,
                    "question": "Which of these is a common vector database?",
                    "type": "mcq",
                    "options": [
                        "Pinecone",
                        "MongoDB",
                        "Redis",
                        "Apache Kafka"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 4,
                    "question": "The architecture that powers modern LLMs like GPT is called the _______.",
                    "type": "fib",
                    "correct_answer": "Transformer"
                },
                {
                    "question_number": 5,
                    "question": "What is a 'hallucination' in an LLM?",
                    "type": "descriptive",
                    "correct_answer": "Generating factually incorrect or nonsensical information confidently."
                },
                {
                    "question_number": 6,
                    "question": "Which Python framework is commonly used to create APIs for AI models?",
                    "type": "mcq",
                    "options": [
                        "Flask",
                        "FastAPI",
                        "Django",
                        "Pyramid"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "A vector represents text as an array of _______ numbers.",
                    "type": "fib",
                    "correct_answer": "floating-point"
                },
                {
                    "question_number": 8,
                    "question": "What is the primary function of an embedding model?",
                    "type": "mcq",
                    "options": [
                        "Summarizing text",
                        "Translating languages",
                        "Converting text to numerical vectors",
                        "Generating images"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 9,
                    "question": "The 'temperature' parameter in LLMs controls the _______ of the generated output.",
                    "type": "fib",
                    "correct_answer": "randomness"
                },
                {
                    "question_number": 10,
                    "question": "What is prompt engineering?",
                    "type": "descriptive",
                    "correct_answer": "The practice of crafting input text to guide an LLM toward producing a specific desired output."
                },
                {
                    "question_number": 11,
                    "question": "Which component is essential for storing document chunks for semantic search?",
                    "type": "mcq",
                    "options": [
                        "SQL Table",
                        "Vector Database",
                        "Cache",
                        "CSV File"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "LangChain is a framework designed to facilitate the development of LLM _______.",
                    "type": "fib",
                    "correct_answer": "applications"
                },
                {
                    "question_number": 13,
                    "question": "What does a 'token' represent in LLM processing?",
                    "type": "mcq",
                    "options": [
                        "A full sentence",
                        "A single word",
                        "A chunk of text (word or sub-word)",
                        "A paragraph"
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 14,
                    "question": "In a RAG pipeline, the _______ retrieves relevant information from the database.",
                    "type": "fib",
                    "correct_answer": "retriever"
                },
                {
                    "question_number": 15,
                    "question": "What is the purpose of a stop sequence in model inference?",
                    "type": "descriptive",
                    "correct_answer": "To prevent the model from generating text beyond a specific point or character."
                },
                {
                    "question_number": 16,
                    "question": "What does the 'self-attention' mechanism allow a transformer to do?",
                    "type": "mcq",
                    "options": [
                        "Run faster",
                        "Weight the importance of different words in a sequence",
                        "Use less RAM",
                        "Access the internet"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "The output of an embedding model is often called a _______.",
                    "type": "fib",
                    "correct_answer": "vector"
                },
                {
                    "question_number": 18,
                    "question": "Which of these is a popular open-source library for Transformers?",
                    "type": "mcq",
                    "options": [
                        "Hugging Face",
                        "Pandas",
                        "NumPy",
                        "Matplotlib"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 19,
                    "question": "Semantic search differs from keyword search by matching based on _______.",
                    "type": "fib",
                    "correct_answer": "meaning"
                },
                {
                    "question_number": 20,
                    "question": "What is a system prompt?",
                    "type": "descriptive",
                    "correct_answer": "A high-level instruction given to an LLM to define its persona, behavior, or constraints."
                }
            ],
            "Medium": [
                {
                    "question_number": 1,
                    "question": "What is LoRA primarily used for?",
                    "type": "mcq",
                    "options": [
                        "Pre-training",
                        "Parameter-efficient fine-tuning",
                        "Data augmentation",
                        "Vector indexing"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "In RAG, the step of splitting a document into smaller segments is called _______.",
                    "type": "fib",
                    "correct_answer": "chunking"
                },
                {
                    "question_number": 3,
                    "question": "Which metric is commonly used to measure the similarity between two embedding vectors?",
                    "type": "mcq",
                    "options": [
                        "Euclidean distance",
                        "Cosine similarity",
                        "Manhattan distance",
                        "All of the above"
                    ],
                    "correct_answer": "D"
                },
                {
                    "question_number": 4,
                    "question": "To ensure an LLM returns a specific JSON schema, one should use _______ output.",
                    "type": "fib",
                    "correct_answer": "structured"
                },
                {
                    "question_number": 5,
                    "question": "Explain the difference between zero-shot and few-shot prompting.",
                    "type": "descriptive",
                    "correct_answer": "Zero-shot relies on the model's inherent knowledge; few-shot provides explicit examples in the context."
                },
                {
                    "question_number": 6,
                    "question": "Which of these is a disadvantage of naive RAG?",
                    "type": "mcq",
                    "options": [
                        "Context overflow",
                        "Irrelevant retrieval",
                        "High latency",
                        "All of the above"
                    ],
                    "correct_answer": "D"
                },
                {
                    "question_number": 7,
                    "question": "A model's ability to 'reason' over multi-step tasks is often improved via _______.",
                    "type": "fib",
                    "correct_answer": "Chain-of-Thought"
                },
                {
                    "question_number": 8,
                    "question": "What is the primary benefit of using a semantic cache?",
                    "type": "mcq",
                    "options": [
                        "Reduced latency and costs",
                        "Better accuracy",
                        "Improved grammar",
                        "Increased memory"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 9,
                    "question": "Fine-tuning a model involves updating its _______ weights.",
                    "type": "fib",
                    "correct_answer": "internal"
                },
                {
                    "question_number": 10,
                    "question": "Describe the function of a Retriever in a LlamaIndex-based system.",
                    "type": "descriptive",
                    "correct_answer": "It fetches relevant context from a knowledge base based on the query, typically using vector similarity."
                },
                {
                    "question_number": 11,
                    "question": "Which of the following is an orchestration framework for agents?",
                    "type": "mcq",
                    "options": [
                        "PyTorch",
                        "LangGraph",
                        "Scikit-learn",
                        "Requests"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "In diffusion models, the process of removing noise from an image is called _______.",
                    "type": "fib",
                    "correct_answer": "denoising"
                },
                {
                    "question_number": 13,
                    "question": "What is 'context window' in an LLM?",
                    "type": "mcq",
                    "options": [
                        "The screen size",
                        "The total tokens a model can process at once",
                        "The model's file size",
                        "The RAM usage"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "To allow an LLM to call external tools, we typically define a set of _______.",
                    "type": "fib",
                    "correct_answer": "functions"
                },
                {
                    "question_number": 15,
                    "question": "What is the role of the 'Attention Mask' in transformers?",
                    "type": "descriptive",
                    "correct_answer": "To ignore padding tokens or specific sections of input during self-attention computation."
                },
                {
                    "question_number": 16,
                    "question": "Which technique helps mitigate the problem of context window limitations?",
                    "type": "mcq",
                    "options": [
                        "Summarization",
                        "Vector search",
                        "Recursive retrieval",
                        "All of the above"
                    ],
                    "correct_answer": "D"
                },
                {
                    "question_number": 17,
                    "question": "The Ragas framework is used specifically for evaluating _______ pipelines.",
                    "type": "fib",
                    "correct_answer": "RAG"
                },
                {
                    "question_number": 18,
                    "question": "What is a 'Model Router'?",
                    "type": "mcq",
                    "options": [
                        "A hardware component",
                        "A mechanism to select the best model for a task",
                        "A database connector",
                        "An embedding model"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "The process of re-ranking retrieved documents to improve relevance is called _______.",
                    "type": "fib",
                    "correct_answer": "re-ranking"
                },
                {
                    "question_number": 20,
                    "question": "Explain the concept of 'Temperature' in LLM generation.",
                    "type": "descriptive",
                    "correct_answer": "A hyperparameter that adjusts the probability distribution of tokens, where higher values lead to more diversity."
                }
            ],
            "Hard": [
                {
                    "question_number": 1,
                    "question": "Which architecture is most commonly associated with modern diffusion models?",
                    "type": "mcq",
                    "options": [
                        "U-Net",
                        "ResNet",
                        "GAN",
                        "RNN"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 2,
                    "question": "The technique of using multiple agents to collaborate on a task is known as a _______ architecture.",
                    "type": "fib",
                    "correct_answer": "multi-agent"
                },
                {
                    "question_number": 3,
                    "question": "Which of these is a method to prevent model drift in production?",
                    "type": "mcq",
                    "options": [
                        "Continuous monitoring",
                        "Active learning",
                        "Regular retraining",
                        "All of the above"
                    ],
                    "correct_answer": "D"
                },
                {
                    "question_number": 4,
                    "question": "To perform gradient descent on only a subset of parameters, we often use _______-rank adaptation.",
                    "type": "fib",
                    "correct_answer": "low"
                },
                {
                    "question_number": 5,
                    "question": "Describe the difference between 'Self-RAG' and standard RAG.",
                    "type": "descriptive",
                    "correct_answer": "Self-RAG allows the model to critique its own retrieved documents and output, deciding whether to use them or generate based on internal knowledge."
                },
                {
                    "question_number": 6,
                    "question": "What is a 'KV Cache' used for in LLM inference?",
                    "type": "mcq",
                    "options": [
                        "Caching prompts",
                        "Storing previous attention states to speed up generation",
                        "Caching user data",
                        "Indexing vectors"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "Quantization reduces the memory footprint of an LLM by reducing the _______ of weights.",
                    "type": "fib",
                    "correct_answer": "precision"
                },
                {
                    "question_number": 8,
                    "question": "In multi-agent systems, how is 'circular dependency' typically avoided?",
                    "type": "mcq",
                    "options": [
                        "Using a central supervisor",
                        "Dynamic task allocation",
                        "Asynchronous communication",
                        "All of the above"
                    ],
                    "correct_answer": "D"
                },
                {
                    "question_number": 9,
                    "question": "The 'Flash Attention' algorithm optimizes the _______ complexity of self-attention.",
                    "type": "fib",
                    "correct_answer": "memory"
                },
                {
                    "question_number": 10,
                    "question": "How do you evaluate RAG systems that lack ground truth?",
                    "type": "descriptive",
                    "correct_answer": "Using LLM-as-a-judge approaches like Ragas or TruLens, evaluating faithfulness and answer relevance via synthetic benchmarks."
                },
                {
                    "question_number": 11,
                    "question": "Which technique is most effective for long-document retrieval?",
                    "type": "mcq",
                    "options": [
                        "Parent Document Retrieval",
                        "Simple windowing",
                        "Character splitting",
                        "Keyword mapping"
                    ],
                    "correct_answer": "A"
                },
                {
                    "question_number": 12,
                    "question": "The _______ protocol is the industry standard for LLM function calling via APIs.",
                    "type": "fib",
                    "correct_answer": "OpenAI function calling"
                },
                {
                    "question_number": 13,
                    "question": "What does 'Speculative Decoding' achieve?",
                    "type": "mcq",
                    "options": [
                        "Higher model accuracy",
                        "Faster inference by using a smaller draft model",
                        "Lower vector storage costs",
                        "Better prompt alignment"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "To measure the 'faithfulness' of a generated answer to the retrieved context, we look for _______.",
                    "type": "fib",
                    "correct_answer": "hallucinations"
                },
                {
                    "question_number": 15,
                    "question": "Explain the trade-offs of using 4-bit vs 8-bit quantization.",
                    "type": "descriptive",
                    "correct_answer": "4-bit significantly reduces memory requirements but may degrade model accuracy and perplexity compared to 8-bit."
                },
                {
                    "question_number": 16,
                    "question": "Which of these is a core challenge in deploying LLMs at scale?",
                    "type": "mcq",
                    "options": [
                        "Latency",
                        "Throughput/Concurrency",
                        "Cost management",
                        "All of the above"
                    ],
                    "correct_answer": "D"
                },
                {
                    "question_number": 17,
                    "question": "The process of iteratively improving a model's response through tool use is called _______ reasoning.",
                    "type": "fib",
                    "correct_answer": "agentic"
                },
                {
                    "question_number": 18,
                    "question": "What does 'Mixture of Experts' (MoE) represent?",
                    "type": "mcq",
                    "options": [
                        "Multiple models running in parallel",
                        "A sparse model architecture using specialized sub-networks",
                        "A training method using many datasets",
                        "A hardware cluster approach"
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "To handle large vector collections, _______ indexes are used to speed up search.",
                    "type": "fib",
                    "correct_answer": "ANN"
                },
                {
                    "question_number": 20,
                    "question": "Explain how you would optimize a RAG pipeline's retrieval precision.",
                    "type": "descriptive",
                    "correct_answer": "Implement hybrid search (vector + keyword), add a re-ranking model, and optimize chunking strategies or metadata filtering."
                }
            ]
        },
        "HR": {
            "Easy": [
                {
                    "question_number": 1,
                    "question": "When working on your first collaborative AI coding project, a senior engineer points out a flaw in your data preprocessing script. How should you respond?",
                    "type": "mcq",
                    "options": [
                        "Defend your script because it runs without crashing.",
                        "Listen to the feedback, ask clarifying questions, and implement the suggested improvements.",
                        "Ignore the feedback and continue with your original approach.",
                        "Ask to be reassigned to a different task to avoid criticism."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "The ability to work effectively with others toward a common goal, especially when combining software engineering and data science disciplines, is known as ______.",
                    "type": "fib",
                    "correct_answer": "teamwork"
                },
                {
                    "question_number": 3,
                    "question": "You notice that your teammate is struggling to meet a deadline for gathering training data. What is the most appropriate course of action?",
                    "type": "mcq",
                    "options": [
                        "Report them to the manager immediately.",
                        "Wait until the deadline passes to see if they fail.",
                        "Offer to help them streamline the data collection process if your own tasks allow.",
                        "Take over their entire project without telling them."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 4,
                    "question": "The practice of openly sharing progress, blockers, and AI model metrics with your manager and team is referred to as ______.",
                    "type": "fib",
                    "correct_answer": "transparency"
                },
                {
                    "question_number": 5,
                    "question": "Describe a time when you had to learn a new machine learning framework or tool quickly. How did you approach it and what was the outcome?",
                    "type": "descriptive",
                    "correct_answer": "Proactive learning, resource utilization, hands-on practice, successful project application."
                },
                {
                    "question_number": 6,
                    "question": "During a sprint planning meeting, you realize the timeline given for training and tuning a neural network is too short. What should you do?",
                    "type": "mcq",
                    "options": [
                        "Agree to the timeline and silently plan to miss the deadline.",
                        "Politely raise your concerns, explain the technical reasons, and propose a realistic adjusted timeline.",
                        "Refuse to work on the project entirely.",
                        "Complain to other team members behind the scenes."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "Maintaining a positive attitude and remaining productive when your AI model underperforms on initial tests requires personal ______.",
                    "type": "fib",
                    "correct_answer": "resilience"
                },
                {
                    "question_number": 8,
                    "question": "You receive conflicting instructions from a product manager and a technical lead regarding feature extraction priorities. What is your best next step?",
                    "type": "mcq",
                    "options": [
                        "Ignore both and do whatever you think is easiest.",
                        "Follow the product manager's instructions without talking to the technical lead.",
                        "Facilitate a brief sync between the product manager and technical lead to align on priorities.",
                        "Stop working until someone else resolves it."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 9,
                    "question": "The willingness to accept constructive criticism on your code or model architecture without taking it personally is an example of emotional ______.",
                    "type": "fib",
                    "correct_answer": "maturity"
                },
                {
                    "question_number": 10,
                    "question": "Tell me about a situation where you had to explain a complex AI concept to a non-technical stakeholder. How did you ensure they understood?",
                    "type": "descriptive",
                    "correct_answer": "Clear communication, avoiding jargon, using analogies, checking for understanding."
                },
                {
                    "question_number": 11,
                    "question": "You accidentally push a script containing hardcoded database credentials to a shared repository. What is the immediate priority?",
                    "type": "mcq",
                    "options": [
                        "Wait for someone else to notice it.",
                        "Revoke the credentials immediately, notify security/team lead, and remove the commit.",
                        "Delete your local repository and pretend nothing happened.",
                        "Write a note in the README telling people not to look at it."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "Prioritizing your daily coding and experimentation tasks based on urgency and business impact is known as time ______.",
                    "type": "fib",
                    "correct_answer": "management"
                },
                {
                    "question_number": 13,
                    "question": "You notice that a dataset provided for training contains obvious demographic biases. How should you address this?",
                    "type": "mcq",
                    "options": [
                        "Proceed with training; it is not an engineer's job to worry about bias.",
                        "Quietly delete the biased records without documenting the change.",
                        "Document the bias, raise the concern to your lead or product owner, and suggest mitigation steps.",
                        "Complain on social media about the company's data practices."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 14,
                    "question": "Adhering to coding standards, documentation norms, and ethical guidelines in AI development demonstrates professional ______.",
                    "type": "fib",
                    "correct_answer": "accountability"
                },
                {
                    "question_number": 15,
                    "question": "Describe a project where you worked as part of a team to build an application or model. What was your specific contribution and how did you collaborate?",
                    "type": "descriptive",
                    "correct_answer": "Clear role definition, active collaboration, shared goals, successful delivery."
                },
                {
                    "question_number": 16,
                    "question": "A user tests your deployed AI model and reports that it gives erratic outputs. How do you handle the user report?",
                    "type": "mcq",
                    "options": [
                        "Tell the user they are using the model incorrectly and close the ticket.",
                        "Thank the user, gather input logs and reproduction steps, and investigate the anomaly.",
                        "Ignore the report because it worked fine on your local machine.",
                        "Blame the infrastructure team for network issues."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "The ability to put yourself in the shoes of end-users who rely on your AI system for critical tasks is called ______.",
                    "type": "fib",
                    "correct_answer": "empathy"
                },
                {
                    "question_number": 18,
                    "question": "You are assigned a repetitive data cleaning task that you believe can be automated with a script. What should you do?",
                    "type": "mcq",
                    "options": [
                        "Do it manually every time to ensure no mistakes happen.",
                        "Spend weeks writing a complex automated pipeline without telling anyone.",
                        "Check with your lead, propose a quick automation script, and estimate the time savings.",
                        "Refuse to do the task because it is boring."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 19,
                    "question": "When your code fails a unit test or your model fails validation, maintaining a systematic and calm approach to fixing it demonstrates patience and ______.",
                    "type": "fib",
                    "correct_answer": "perseverance"
                },
                {
                    "question_number": 20,
                    "question": "Share an experience where you received negative feedback on a piece of code or an experiment design. How did you react and what did you change?",
                    "type": "descriptive",
                    "correct_answer": "Openness to feedback, lack of defensiveness, action-oriented improvement, reflection."
                }
            ],
            "Medium": [
                {
                    "question_number": 1,
                    "question": "As a mid-level AI Engineer, you notice a junior team member repeatedly writing inefficient data pipelines that slow down training. How do you approach them?",
                    "type": "mcq",
                    "options": [
                        "Rewrite their code without telling them to save time.",
                        "Publicly call them out in the next team meeting.",
                        "Schedule a 1-on-1 session to patiently review their code, explain the bottleneck, and mentor them on optimization.",
                        "Complain to the engineering manager about their lack of skills."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 2,
                    "question": "The continuous process of refining communication channels between data scientists, AI engineers, and DevOps teams is known as cross-functional ______.",
                    "type": "fib",
                    "correct_answer": "alignment"
                },
                {
                    "question_number": 3,
                    "question": "An urgent production bug in your recommendation model occurs outside of normal working hours. As the owner of the service, what is your best approach?",
                    "type": "mcq",
                    "options": [
                        "Wait until Monday morning to look at it.",
                        "Acknowledge the alert, assess severity, follow incident response protocols, and coordinate a fix.",
                        "Turn off the monitoring system so the alerts stop.",
                        "Send an email and go on vacation."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "Balancing technical debt reduction with the delivery of new AI model features requires strategic ______ management.",
                    "type": "fib",
                    "correct_answer": "backlog"
                },
                {
                    "question_number": 5,
                    "question": "Describe a situation where a machine learning project you worked on faced scope creep or changing business requirements mid-development. How did you manage stakeholder expectations?",
                    "type": "descriptive",
                    "correct_answer": "Stakeholder communication, impact analysis, negotiation, reprioritization."
                },
                {
                    "question_number": 6,
                    "question": "You have built a model with high accuracy, but the product team wants to pivot to a different use case that requires low latency instead. How do you respond?",
                    "type": "mcq",
                    "options": [
                        "Refuse to change because you already finished your assigned model.",
                        "Analyze the latency constraints, evaluate existing model trade-offs, and collaborate on a path forward (e.g., distillation or quantization).",
                        "Deploy the high-accuracy model anyway and let users deal with slow response times.",
                        "Quit the project immediately."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "Ensuring that AI models adhere to privacy laws and ethical standards is a key part of maintaining corporate ______.",
                    "type": "fib",
                    "correct_answer": "governance"
                },
                {
                    "question_number": 8,
                    "question": "During a code review, you find that a peer has committed code that lacks proper logging and monitoring for model drift. How do you handle this?",
                    "type": "mcq",
                    "options": [
                        "Approve the code anyway to avoid delaying the sprint.",
                        "Reject the PR with clear, constructive comments explaining the necessity of monitoring drift in production.",
                        "Insult the peer's coding standards in the review comments.",
                        "Fix it yourself without leaving any review comments."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "When multiple teams depend on your shared feature store or model API, clear versioning and documentation foster trust and ______.",
                    "type": "fib",
                    "correct_answer": "reliability"
                },
                {
                    "question_number": 10,
                    "question": "Tell me about a time when a machine learning experiment failed repeatedly despite your best efforts. How did you maintain your motivation and pivot your strategy?",
                    "type": "descriptive",
                    "correct_answer": "Scientific method, root cause analysis, perseverance, strategic pivoting."
                },
                {
                    "question_number": 11,
                    "question": "A stakeholder demands that your team deploy an AI model immediately, even though automated bias testing is incomplete. What is the most professional response?",
                    "type": "mcq",
                    "options": [
                        "Deploy it immediately to keep the stakeholder happy.",
                        "Refuse aggressively and threaten to escalate to HR.",
                        "Explain the risks of deploying without bias checks, present data on potential fallout, and propose a fast-tracked safety review.",
                        "Hide the model files so no one can access them."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 12,
                    "question": "The ability to mediate disagreements between data scientists and software engineers regarding model deployment architectures is a form of conflict ______.",
                    "type": "fib",
                    "correct_answer": "resolution"
                },
                {
                    "question_number": 13,
                    "question": "You discover that a dataset your team purchased contains potential copyright issues. What should you do?",
                    "type": "mcq",
                    "options": [
                        "Keep it secret and train the model anyway.",
                        "Immediately notify legal/compliance and your manager, pausing training until cleared.",
                        "Share the dataset publicly so others can check it.",
                        "Delete all your code and pretend you never saw the dataset."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "Anticipating potential failure modes of an AI system before it goes live is an example of proactive risk ______.",
                    "type": "fib",
                    "correct_answer": "assessment"
                },
                {
                    "question_number": 15,
                    "question": "Describe a project where you successfully collaborated with DevOps or MLOps engineers to streamline a CI/CD pipeline for machine learning. What was your role?",
                    "type": "descriptive",
                    "correct_answer": "Cross-functional collaboration, understanding MLOps principles, automation, iterative improvement."
                },
                {
                    "question_number": 16,
                    "question": "A key team member leaves unexpectedly in the middle of an important model migration project. How do you help the team adapt?",
                    "type": "mcq",
                    "options": [
                        "Panic and assume the project will fail.",
                        "Review the departing member's documentation, map out unfinished tasks, and volunteer to take on a key piece of the migration.",
                        "Blame management for not retaining staff.",
                        "Stop working until a replacement is hired."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "Taking ownership of an incident caused by your deployed model without deflecting blame shows true professional ______.",
                    "type": "fib",
                    "correct_answer": "accountability"
                },
                {
                    "question_number": 18,
                    "question": "You are asked to mentor a new hire joining your AI team. How do you structure your approach during their first week?",
                    "type": "mcq",
                    "options": [
                        "Give them a complex model architecture to build alone with no instructions.",
                        "Ignore them and focus entirely on your own deliverables.",
                        "Provide onboarding resources, set up regular check-ins, explain system architecture, and pair program on initial tasks.",
                        "Tell them to figure everything out via Google search."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 19,
                    "question": "Effectively managing competing demands for GPU compute resources across multiple engineering projects requires careful ______ allocation.",
                    "type": "fib",
                    "correct_answer": "resource"
                },
                {
                    "question_number": 20,
                    "question": "Describe a time when you identified a systemic inefficiency in your team's AI development workflow. How did you propose and implement a solution?",
                    "type": "descriptive",
                    "correct_answer": "Process optimization, data-driven proposal, stakeholder buy-in, measurable improvement."
                }
            ],
            "Hard": [
                {
                    "question_number": 1,
                    "question": "As a Lead AI Engineer, you discover that a high-stakes proprietary model your team launched has been exhibiting subtle discriminatory outputs affecting a minority user group. Executives want to downplay it to protect the product launch. What do you do?",
                    "type": "mcq",
                    "options": [
                        "Comply with executives and sweep the issue under the rug.",
                        "Leak the internal reports to the press immediately.",
                        "Present a transparent risk assessment detailing the ethical, legal, and reputational damages, and strongly advocate for pausing deployment to remediate the bias.",
                        "Blame the junior engineers who coded the data pipeline."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 2,
                    "question": "Guiding an organization through a major technological shift from legacy systems to advanced generative AI infrastructure requires visionary ______.",
                    "type": "fib",
                    "correct_answer": "leadership"
                },
                {
                    "question_number": 3,
                    "question": "Your star AI researcher wants to use an unvetted, cutting-edge external library that lacks security audits and enterprise support, citing breakthrough performance. How do you evaluate this leadership dilemma?",
                    "type": "mcq",
                    "options": [
                        "Approve it instantly to stay ahead of competitors regardless of security risks.",
                        "Reject it completely with no discussion because it is new.",
                        "Conduct a thorough security and compliance review, weigh innovation against risk, and explore sandboxed or internal implementations.",
                        "Fire the researcher for suggesting unvetted tools."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 4,
                    "question": "Aligning long-term artificial intelligence research goals with immediate commercial product roadmaps requires strategic ______.",
                    "type": "fib",
                    "correct_answer": "planning"
                },
                {
                    "question_number": 5,
                    "question": "Describe a critical production outage or catastrophic model failure you led the response for. How did you manage incident triage, technical recovery, and stakeholder communication under pressure?",
                    "type": "descriptive",
                    "correct_answer": "Crisis management, root cause analysis, clear communication, post-mortem culture, preventive measures."
                },
                {
                    "question_number": 6,
                    "question": "Two senior teams within your engineering organization are locked in a turf war over ownership of the core LLM orchestration platform, stalling company-wide AI initiatives. As a leader, how do you resolve this?",
                    "type": "mcq",
                    "options": [
                        "Pick a team arbitrarily and tell the other to give up.",
                        "Facilitate a strategic alignment workshop to define clear boundaries, shared ownership models, and unified architectural goals based on business value.",
                        "Escalate the dispute to legal and let them sue each other.",
                        "Ignore the conflict and build a competing third platform yourself."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "Building a culture of psychological safety where engineers feel comfortable reporting model failures or ethical risks without fear of retribution fosters true ______.",
                    "type": "fib",
                    "correct_answer": "innovation"
                },
                {
                    "question_number": 8,
                    "question": "A major enterprise client threatens to cancel their contract unless your company customizes your foundational AI model to include unverified data sources that violate your company's strict data privacy pledge. What is your leadership stance?",
                    "type": "mcq",
                    "options": [
                        "Accept the client's data immediately to save the contract.",
                        "Decline the request firmly, explaining that data privacy commitments are non-negotiable, while offering privacy-preserving alternatives (e.g., federated learning).",
                        "Fabricate compliance reports to trick the client.",
                        "Blame the sales team for making promises."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "The capability to foresee long-term technological trends and position an AI engineering department for future industry disruption is strategic ______.",
                    "type": "fib",
                    "correct_answer": "foresight"
                },
                {
                    "question_number": 10,
                    "question": "Tell me about a time when you had to restructure an underperforming AI engineering team or pivot a failing R&D division. How did you manage morale and turn performance around?",
                    "type": "descriptive",
                    "correct_answer": "Change management, empathy, restructuring, restoring team morale, clear milestones."
                },
                {
                    "question_number": 11,
                    "question": "An ambitious AI initiative you championed fails to deliver the expected ROI after heavy investment. The board is questioning the value of the AI division. How do you handle this executive review?",
                    "type": "mcq",
                    "options": [
                        "Hide the financial metrics and pretend everything is fine.",
                        "Blame the engineers and data scientists who executed the project.",
                        "Own the outcome transparently, present a detailed post-mortem analysis of why the ROI fell short, and outline a pragmatic pivot backed by validated learnings.",
                        "Resign immediately to avoid difficult questions."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 12,
                    "question": "Successfully negotiating AI budget allocations with CFOs and board members by translating complex technical metrics into business value is executive ______.",
                    "type": "fib",
                    "correct_answer": "influence"
                },
                {
                    "question_number": 13,
                    "question": "You find out that a top-performing senior AI engineer on your team has been systematically taking credit for the work of junior peers. How do you handle this personnel issue?",
                    "type": "mcq",
                    "options": [
                        "Ignore it because their individual performance metrics are high.",
                        "Publicly humiliate the senior engineer in front of the team.",
                        "Investigate the claims privately, gather facts, address the behavior directly with the senior engineer, and ensure recognition is properly restored to the junior peers.",
                        "Fire all the junior engineers to eliminate the dispute."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 14,
                    "question": "Establishing robust AI governance frameworks to ensure compliance with emerging global regulations (like the EU AI Act) requires organizational ______.",
                    "type": "fib",
                    "correct_answer": "compliance"
                },
                {
                    "question_number": 15,
                    "question": "Describe a scenario where you had to lead a multi-disciplinary initiative involving software engineering, legal, product, and data science teams to deploy a high-risk AI system. How did you drive consensus?",
                    "type": "descriptive",
                    "correct_answer": "Cross-functional leadership, consensus building, risk management, holistic alignment."
                },
                {
                    "question_number": 16,
                    "question": "A key strategic partner suddenly revokes access to a primary API that powers your core AI product, threatening your company's revenue stream. As a senior leader, what is your immediate and secondary response?",
                    "type": "mcq",
                    "options": [
                        "Panic and shut down the company.",
                        "Activate the business continuity fallback plan, pivot to backup models/APIs, and concurrently lead executive negotiations for contract restoration.",
                        "Sue the partner without attempting to negotiate.",
                        "Wait for the partner to change their mind."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "Empowering senior engineers to make autonomous architectural decisions while maintaining overarching technical coherence is effective ______ leadership.",
                    "type": "fib",
                    "correct_answer": "delegation"
                },
                {
                    "question_number": 18,
                    "question": "You are tasked with hiring a Head of AI Ethics for your organization. What primary trait should you prioritize during the selection process?",
                    "type": "mcq",
                    "options": [
                        "Someone who always agrees with product managers to speed up launches.",
                        "Someone with deep technical AI understanding combined with the moral courage to challenge leadership when ethical boundaries are tested.",
                        "Someone whose sole background is corporate PR and marketing.",
                        "Someone who has never worked with machine learning models before."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "Cultivating an environment of continuous learning and experimentation in a rapidly evolving AI landscape requires fostering a culture of ______.",
                    "type": "fib",
                    "correct_answer": "curiosity"
                },
                {
                    "question_number": 20,
                    "question": "Reflecting on your career as an AI engineering leader, describe a time when you had to make an ethically difficult decision that cost your company short-term financial gain but preserved its long-term integrity.",
                    "type": "descriptive",
                    "correct_answer": "Ethical fortitude, long-term vision, principled leadership, corporate integrity."
                }
            ]
        },
        "Behavioral": {
            "Easy": [
                {
                    "question_number": 1,
                    "question": "You discover a bug in your data preprocessing script that slightly corrupted training data for a model you submitted for review. What is the most appropriate action to take?",
                    "type": "mcq",
                    "options": [
                        "A) Ignore it since the impact seems minor and hope nobody notices during testing.",
                        "B) Immediately inform your lead, fix the script, and re-run the training pipeline.",
                        "C) Patch the production data directly without updating the script to save time.",
                        "D) Blame the data team for providing inconsistent input data formats."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "When presenting initial AI model metrics to non-technical team members, it is crucial to practice ______ by translating metrics like precision and recall into business outcomes.",
                    "type": "fib",
                    "correct_answer": "simplification"
                },
                {
                    "question_number": 3,
                    "question": "You are assigned a task involving a deep learning framework you have never used before. How do you approach this challenge?",
                    "type": "mcq",
                    "options": [
                        "A) Ask a senior engineer to write the code for you while you watch.",
                        "B) Inform your manager that you cannot complete the task due to lack of experience.",
                        "C) Review official documentation, complete sample tutorials, and consult peers when stuck.",
                        "D) Refactor the project to use a framework you already know without asking the team."
                    ],
                    "correct_answer": "C"
                },
                {
                    "question_number": 4,
                    "question": "Demonstrating ______ involves reaching out to senior team members for guidance after independently trying to debug a failing model pipeline for a reasonable amount of time.",
                    "type": "fib",
                    "correct_answer": "resourcefulness"
                },
                {
                    "question_number": 5,
                    "question": "Describe a time when an AI model you trained did not meet performance expectations during initial evaluation. How did you troubleshoot and address the issue?",
                    "type": "descriptive",
                    "correct_answer": "Key traits: Methodical problem-solving, structured error analysis (data inspection vs hyperparameter tuning), resilience, and willingness to seek guidance when needed."
                },
                {
                    "question_number": 6,
                    "question": "During a code review, a senior engineer points out that your PyTorch data loader is inefficient and causing GPU starvation. How should you respond?",
                    "type": "mcq",
                    "options": [
                        "A) Defend your code and argue that execution speed is not important at this stage.",
                        "B) Ask for advice on optimization best practices and update the code accordingly.",
                        "C) Ignore the comment and merge the pull request anyway.",
                        "D) Pass the task to another junior engineer to fix."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "Accepting constructive feedback on your code and model design without getting defensive demonstrates professional ______.",
                    "type": "fib",
                    "correct_answer": "humility"
                },
                {
                    "question_number": 8,
                    "question": "Your model evaluation deadline is in 2 hours, and accuracy is slightly below target. What is the best immediate response?",
                    "type": "mcq",
                    "options": [
                        "A) Artificially modify evaluation metrics to meet the required threshold.",
                        "B) Communicate the current status to your manager, share the bottleneck, and ask for a short extension.",
                        "C) Skip evaluation and release the unverified model code.",
                        "D) Stop working and log off early out of frustration."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "When working with sensitive user datasets for AI model training, maintaining strict user data ______ is required to uphold ethical standards.",
                    "type": "fib",
                    "correct_answer": "privacy"
                },
                {
                    "question_number": 10,
                    "question": "Describe a situation where you had to collaborate with a backend software engineer to integrate your AI model into a production API.",
                    "type": "descriptive",
                    "correct_answer": "Key traits: Effective teamwork, clear communication on API schemas/data formats, understanding software engineering requirements, and collaborative testing."
                },
                {
                    "question_number": 11,
                    "question": "You notice significant data labeling errors in a dataset provided by an external vendor. What should you do?",
                    "type": "mcq",
                    "options": [
                        "A) Manually fix a small subset, ignore the rest, and train the model.",
                        "B) Document sample errors and report them to your team lead to coordinate vendor re-labeling.",
                        "C) Train the model anyway because data quality does not affect deep learning performance.",
                        "D) Delete the entire dataset without telling anyone."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "Proactively informing your team about potential delays in model training runs exhibits strong ______.",
                    "type": "fib",
                    "correct_answer": "accountability"
                },
                {
                    "question_number": 13,
                    "question": "You are given two high-priority data cleanup tasks due at the same time. How do you manage your workload?",
                    "type": "mcq",
                    "options": [
                        "A) Work on whichever task is easier and ignore the second task.",
                        "B) Clarify task priorities with your project manager and adjust your schedule accordingly.",
                        "C) Rush through both tasks quickly without checking for errors.",
                        "D) Delegate one task to another junior engineer without manager approval."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "Adapting quickly when a project pivots from fine-tuning an open-source model to prompt engineering requires high operational ______.",
                    "type": "fib",
                    "correct_answer": "flexibility"
                },
                {
                    "question_number": 15,
                    "question": "Tell me about a time when you had to learn a new machine learning tool or library quickly to deliver a feature.",
                    "type": "descriptive",
                    "correct_answer": "Key traits: Self-directed learning, agility, practical application, efficient time management, and curiosity."
                },
                {
                    "question_number": 16,
                    "question": "A peer suggests using a simple rule-based system instead of your complex neural network for a basic text filtering task. How do you evaluate this recommendation?",
                    "type": "mcq",
                    "options": [
                        "A) Insist on using the neural network because it sounds more modern.",
                        "B) Compare both approaches based on implementation effort, latency, and accuracy needs.",
                        "C) Reject the suggestion immediately as rule-based systems are obsolete.",
                        "D) Abandon your project entirely and let the peer handle it."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "Thoroughly logging hyperparameter settings, dataset versions, and evaluation metrics demonstrates strong attention to ______.",
                    "type": "fib",
                    "correct_answer": "detail"
                },
                {
                    "question_number": 18,
                    "question": "Your training job repeatedly crashes due to Out-Of-Memory (OOM) errors on the shared GPU server. What is your first step?",
                    "type": "mcq",
                    "options": [
                        "A) Kill other team members' training jobs to free up GPU memory.",
                        "B) Reduce batch size or use gradient accumulation while checking memory usage.",
                        "C) Request an immediate upgrade to a multi-node cluster without profiling.",
                        "D) Give up on the project and notify management that the task is impossible."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "Showing ______ during code discussions helps build trust when technical approaches differ.",
                    "type": "fib",
                    "correct_answer": "respect"
                },
                {
                    "question_number": 20,
                    "question": "Describe a scenario where you had to perform repetitive data annotation or data cleaning tasks. How did you stay engaged and maintain accuracy?",
                    "type": "descriptive",
                    "correct_answer": "Key traits: Diligence, process automation mindset, quality orientation, and understanding the impact of clean data on model success."
                }
            ],
            "Medium": [
                {
                    "question_number": 1,
                    "question": "A Product Manager insists on adding a heavy LLM feature to a real-time mobile app, but latency tests show it violates SLA thresholds. How do you resolve this conflict?",
                    "type": "mcq",
                    "options": [
                        "A) Deploy the feature as requested and let users complain about slow responses.",
                        "B) Present benchmark trade-offs between model size, latency, and costs, offering optimized alternatives like quantized models or caching.",
                        "C) Refuse to work on the project until the PM drops the request.",
                        "D) Build a simple dummy function without informing the product team."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "Balancing technical model trade-offs with business deadlines requires strong ______ thinking.",
                    "type": "fib",
                    "correct_answer": "strategic"
                },
                {
                    "question_number": 3,
                    "question": "You and a senior teammate disagree on whether to use Retrieval-Augmented Generation (RAG) or Fine-Tuning for a domain-specific QA system. How do you proceed?",
                    "type": "mcq",
                    "options": [
                        "A) Implement your preferred method secretly and present it as the only solution.",
                        "B) Propose a quick proof-of-concept (PoC) comparison based on accuracy, cost, maintainability, and data updating needs.",
                        "C) Escalate immediately to executive management to make the decision.",
                        "D) Yield blindly to avoid any debate."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "Resolving architectural disagreements constructively within an engineering team relies on effective ______ skills.",
                    "type": "fib",
                    "correct_answer": "negotiation"
                },
                {
                    "question_number": 5,
                    "question": "Describe a project where an AI model deployed to production began experiencing performance degradation due to data drift. How did you identify and remediate the issue?",
                    "type": "descriptive",
                    "correct_answer": "Key traits: Monitoring/observability focus, root-cause diagnosis, automated retraining strategies, and proactive cross-team communication."
                },
                {
                    "question_number": 6,
                    "question": "Your team's monthly cloud LLM API bill unexpectedly exceeds the budget by 300% due to inefficient prompt design and excessive token limits. What is your response?",
                    "type": "mcq",
                    "options": [
                        "A) Request budget doubling without modifying the underlying prompt architecture.",
                        "B) Conduct prompt optimization, implement semantic caching, and enforce strict token input/output constraints.",
                        "C) Shut down the production service permanently.",
                        "D) Blame the Cloud provider for high pricing model."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "Taking full responsibility for an AI feature from data collection to production monitoring demonstrates end-to-end ______.",
                    "type": "fib",
                    "correct_answer": "ownership"
                },
                {
                    "question_number": 8,
                    "question": "Stakeholders want to deploy a facial recognition model, but internal testing shows skewed false-positive rates for demographic minorities. How do you handle this?",
                    "type": "mcq",
                    "options": [
                        "A) Deploy the model as-is since demographic skew is common in AI.",
                        "B) Halt deployment, present the bias metrics clearly to stakeholders, and propose targeted dataset balancing and mitigation steps.",
                        "C) Adjust threshold parameters selectively to obscure the evaluation findings.",
                        "D) Resign from the team immediately without explaining."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "Communicating model uncertainty and potential hallucination risks to non-technical business partners requires setting proper ______.",
                    "type": "fib",
                    "correct_answer": "expectations"
                },
                {
                    "question_number": 10,
                    "question": "Tell me about a time you had to make a tough trade-off between model accuracy and system cost/latency requirements.",
                    "type": "descriptive",
                    "correct_answer": "Key traits: Pragmatism, business alignment, quantitative decision-making, stakeholder alignment, and technical trade-off evaluation."
                },
                {
                    "question_number": 11,
                    "question": "A pipeline feeding data into your AI feature silent-fails on weekends, causing stale predictions on Mondays. How do you address this recurring issue?",
                    "type": "mcq",
                    "options": [
                        "A) Manually rerun the script every Monday morning.",
                        "B) Implement automated data validation, alerting systems, and retry logic for the ingestion pipeline.",
                        "C) Ignore it until customer churn increases significantly.",
                        "D) Ask the product team to disable the feature over weekends."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "Effective collaboration between AI engineers and DevOps/MLOps teams depends heavily on cross-functional ______.",
                    "type": "fib",
                    "correct_answer": "alignment"
                },
                {
                    "question_number": 13,
                    "question": "A key client reports that your enterprise search assistant provides incorrect information in 5% of niche queries. How do you manage this bug priority?",
                    "type": "mcq",
                    "options": [
                        "A) Dismiss the bug because 95% accuracy is acceptable for AI systems.",
                        "B) Analyze edge cases, create regression benchmark test suites, and implement targeted guardrails or fallback mechanisms.",
                        "C) Blame the underlying third-party LLM provider.",
                        "D) Turn off search for all enterprise customers."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "Mentoring junior engineers on debugging ML models requires patience and an emphasis on fostering psychological ______.",
                    "type": "fib",
                    "correct_answer": "safety"
                },
                {
                    "question_number": 15,
                    "question": "Describe a scenario where you successfully advocated for simplifying an AI solution over a overly complex, trendy architecture proposed by the team.",
                    "type": "descriptive",
                    "correct_answer": "Key traits: Objectivity, advocacy for maintainability/simplicity, focus on ROI and business value, and persuasive communication."
                },
                {
                    "question_number": 16,
                    "question": "Business stakeholders provide vague requirements for a customer churn prediction model. What is your immediate next step?",
                    "type": "mcq",
                    "options": [
                        "A) Build a model based on your assumptions without further consultation.",
                        "B) Schedule discovery workshops to define success metrics, key inputs, and actionable prediction thresholds.",
                        "C) Wait indefinitely for stakeholders to provide complete specs.",
                        "D) Refuse to start the project until formal documentation is finalized."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "Maintaining consistent delivery quality during unplanned model retraining demands personal and operational ______.",
                    "type": "fib",
                    "correct_answer": "resilience"
                },
                {
                    "question_number": 18,
                    "question": "Cloud budget cuts force you to reduce your GPU cluster allocation by 50%. How do you maintain training throughput?",
                    "type": "mcq",
                    "options": [
                        "A) Stop all model experimentation until the budget is restored.",
                        "B) Explore mixed-precision training, parameter-efficient fine-tuning (PEFT), and dataset pruning techniques.",
                        "C) Run training jobs locally on personal laptops.",
                        "D) Complain to management that AI cannot function with budget cuts."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "Creating clear technical documentation for model architectures and training pipelines promotes long-term team ______.",
                    "type": "fib",
                    "correct_answer": "sustainability"
                },
                {
                    "question_number": 20,
                    "question": "Describe a situation where you had to manage technical debt in your machine learning codebase while delivering urgent client features.",
                    "type": "descriptive",
                    "correct_answer": "Key traits: Prioritization, technical debt refactoring strategy, stakeholder transparent communication, and pragmatic balance."
                }
            ],
            "Hard": [
                {
                    "question_number": 1,
                    "question": "Executive leadership wants to launch an unvetted Generative AI customer service bot in two weeks to beat a competitor. You know guardrails against toxic output are incomplete. What is your strategy?",
                    "type": "mcq",
                    "options": [
                        "A) Agree to launch immediately to satisfy executive pressure, ignoring safety risks.",
                        "B) Present a clear risk assessment on brand damage, propose a phased rollout (internal beta first), and mandate baseline safety guardrails.",
                        "C) Leaks confidential code to external media to force project cancellation.",
                        "D) Quietly sabotage the deployment scripts to delay the release date."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 2,
                    "question": "Establishing enterprise-wide standards for ethical AI deployment and risk governance requires strategic ______.",
                    "type": "fib",
                    "correct_answer": "leadership"
                },
                {
                    "question_number": 3,
                    "question": "Two senior AI architects in your organization are locked in a persistent disagreement over migrating to a proprietary AI framework vs an open-source stack, stalling team progress. How do you resolve this?",
                    "type": "mcq",
                    "options": [
                        "A) Arbitrarily pick one platform to break the tie without technical review.",
                        "B) Establish a objective evaluation matrix based on TCO, vendor lock-in, security, and developer speed, and lead a structured trade-off decision workshop.",
                        "C) Allow both teams to build separate parallel systems indefinitely.",
                        "D) Reassign both architects to unrelated legacy projects."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 4,
                    "question": "Aligning cross-functional leadership across legal, compliance, and engineering around an AI innovation roadmap demands strong stakeholder ______.",
                    "type": "fib",
                    "correct_answer": "management"
                },
                {
                    "question_number": 5,
                    "question": "Describe a scenario where a high-visibility AI initiative you led was failing to deliver expected business results. How did you manage leadership expectations, maintain team morale, and pivot the strategy?",
                    "type": "descriptive",
                    "correct_answer": "Key traits: Executive communication, psychological safety, decisive strategic pivoting, root-cause analysis, and leadership composure under pressure."
                },
                {
                    "question_number": 6,
                    "question": "An unexpected infrastructure surge causes monthly LLM hosting costs to skyrocket by $200k. The CFO demands immediate cost reductions. How do you lead your team's response?",
                    "type": "mcq",
                    "options": [
                        "A) Terminate all generative AI projects effective immediately.",
                        "B) Audit model resource utilization, implement model distillation, self-hosting optimizations, and establish automated cost-capping governance.",
                        "C) Tell the CFO that high cost is an unavoidable tax for using modern AI.",
                        "D) Pass responsibility entirely to the Cloud Infrastructure team."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 7,
                    "question": "Navigating complex global AI compliance mandates (e.g., EU AI Act) while preserving development momentum demands high organizational ______.",
                    "type": "fib",
                    "correct_answer": "agility"
                },
                {
                    "question_number": 8,
                    "question": "Your Lead AI Scientist resigns in the middle of a multi-million-dollar foundation model training effort. How do you ensure project continuity?",
                    "type": "mcq",
                    "options": [
                        "A) Cancel the model training and discard all research progress.",
                        "B) Conduct immediate knowledge transfer, review checkpointing mechanisms, delegate technical leads, and audit pipeline documentation.",
                        "C) Pause all team activities until a senior replacement is hired externally.",
                        "D) Assume the scientist's duties alone while neglecting your own leadership responsibilities."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 9,
                    "question": "Fostering an R&D culture that balances cutting-edge research exploration with reliable product delivery requires ______ leadership.",
                    "type": "fib",
                    "correct_answer": "transformational"
                },
                {
                    "question_number": 10,
                    "question": "Tell me about a time when you had to balance strict ethical/safety considerations with a major commercial partner's aggressive deadline.",
                    "type": "descriptive",
                    "correct_answer": "Key traits: Uncompromised integrity, negotiation capability, executive stakeholder management, and creative technical mitigation."
                },
                {
                    "question_number": 11,
                    "question": "A production LLM system suffers an adversarial prompt injection attack that leaks proprietary system prompts and user context. What is your immediate executive action plan?",
                    "type": "mcq",
                    "options": [
                        "A) Issue a public statement denying that any vulnerability exists.",
                        "B) Initiate incident response, isolate affected endpoints, deploy input sanitization/guardrail updates, and communicate transparently with impacted stakeholders.",
                        "C) Permanently pull all AI products from the market.",
                        "D) Blame the end user for maliciously crafting input strings."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 12,
                    "question": "Instilling a security-first culture for AI data pipelines across multiple engineering teams requires proactive risk ______.",
                    "type": "fib",
                    "correct_answer": "governance"
                },
                {
                    "question_number": 13,
                    "question": "Your engineering organization suffers from severe burnout due to relentless on-call incidents caused by unstable ML pipelines and rapid AI launch schedules. How do you intervene?",
                    "type": "mcq",
                    "options": [
                        "A) Tell the engineers that long hours are standard in high-growth AI tech.",
                        "B) Halt non-critical releases, conduct post-mortems, invest in infrastructure stability, and redistribute on-call burden fairly.",
                        "C) Replace burnt-out engineers with new recruits immediately.",
                        "D) Reduce engineering salary to compensate for reduced velocity."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 14,
                    "question": "Driving organizational transition from legacy deterministic software architectures to non-deterministic AI paradigms requires effective change ______.",
                    "type": "fib",
                    "correct_answer": "management"
                },
                {
                    "question_number": 15,
                    "question": "Describe how you led an engineering organization through a major technology migration (e.g., transitioning from traditional ML models to Large Language Models) without interrupting existing revenue streams.",
                    "type": "descriptive",
                    "correct_answer": "Key traits: Strategic vision, risk mitigation, upskilling team talent, parallel pipeline management, and clear roadmap execution."
                },
                {
                    "question_number": 16,
                    "question": "The board of directors demands a clear ROI metric on AI investments within 30 days, or they threaten budget cuts. How do you respond?",
                    "type": "mcq",
                    "options": [
                        "A) Make up inflated revenue metrics to satisfy the board temporarily.",
                        "B) Present tangible short-term ROI wins (cost savings/efficiency gains) while mapping clear long-term value metrics linked to core business KPIs.",
                        "C) Inform the board that AI investment returns cannot be measured.",
                        "D) Challenge the board's competence publicly."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 17,
                    "question": "Maintaining engineering focus and high morale during high-stakes corporate restructures requires transparent ______.",
                    "type": "fib",
                    "correct_answer": "communication"
                },
                {
                    "question_number": 18,
                    "question": "The Information Security team completely blocks the launch of your team's flagship AI product 24 hours before launch due to third-party data processing concerns. What do you do?",
                    "type": "mcq",
                    "options": [
                        "A) Override the InfoSec team and launch without security sign-off.",
                        "B) Engage InfoSec leadership immediately, review specific blocking compliance criteria, and negotiate localized data masking or temporary containment controls.",
                        "C) Publicly blame InfoSec for destroying product delivery timelines.",
                        "D) Cancel the product permanently."
                    ],
                    "correct_answer": "B"
                },
                {
                    "question_number": 19,
                    "question": "Empowering team leaders to experiment with novel AI techniques requires fostering an environment of controlled ______.",
                    "type": "fib",
                    "correct_answer": "innovation"
                },
                {
                    "question_number": 20,
                    "question": "Describe how you designed and implemented an enterprise AI governance framework that ensures compliance and safety without stifling technical innovation.",
                    "type": "descriptive",
                    "correct_answer": "Key traits: Balanced oversight, process integration, enablement over restriction, cross-functional consensus, and scalable standards."
                }
            ]
        }
    }
}

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
    return {
        "question_number": question_number,
        "question": f"Fallback question {question_number} for {job_role} {interview_type} {difficulty}.",
        "type": q_type,
        "options": ["A", "B", "C", "D"] if q_type == "mcq" else [],
        "correct_answer": "A" if q_type == "mcq" else "term"
    }

def seed_questions(db_instance):
    questions_collection = db_instance["questions"]
    
    # Drop existing collections to replace
    questions_collection.delete_many({})
    
    print("Seeding predefined questions database collection...")
    all_questions = []
    
    roles = ['Python Developer', 'Java Developer', 'Data Analyst', 'Data Scientist', 'Machine Learning Engineer', 'AI Engineer']
    types = ['Technical', 'HR', 'Behavioral']
    difficulties = ['Easy', 'Medium', 'Hard']
    
    for role in roles:
        for itype in types:
            for diff in difficulties:
                for qnum in range(1, 21):
                    base_q_obj = get_predefined_question_base(role, itype, diff, qnum)
                    
                    all_questions.append({
                        "job_role": role,
                        "interview_type": itype,
                        "difficulty": diff,
                        "question_number": qnum,
                        "question": base_q_obj.get("question", f"Fallback question {qnum}."),
                        "type": base_q_obj.get("type", "mcq"),
                        "options": base_q_obj.get("options") or base_q_obj.get("choices") or [],
                        "correct_answer": base_q_obj.get("correct_answer") or base_q_obj.get("correctAnswer") or base_q_obj.get("answer") or "A"
                    })
                    
    questions_collection.insert_many(all_questions)
    print(f"Successfully seeded {len(all_questions)} questions into the 'questions' collection.")
