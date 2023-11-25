# Repo structure

This document explains the organisation of directories and files in the `diopticon` repository and its rationale.

## Repository structure

~~~ directory structure
diopticon/
│
├── app/              
│   ├── __init__.py       
│   ├── main.py    
│   └── ...
│
├── auth/ 
│   ├── __init__.py       
│   └── ...
│
├── docs/           
│   ├── environment.md
│   ├── repo_structure.md     
│   └── ...
│
├── db
|   ├── __init__.py
│   ├── models.py 
│   └── ...
|
├── utils/         
│   ├── __init__.py
│   └── ...
│
├── tests/                
│   └── ...
│
├── Dockerfile            
├── requirements.txt 
└── .github/           
    └── workflows/
        └── ci-cd.yml     

- `app/`: This is the main directory for the Streamlit application. Within it, `main.py` is the file invoked by the Streamlit engine.
- `auth/`: This directory includes everything related to authentication. Separating this functionality should help with maintenance and scalability.
- `db/`: This is where we shall implement database interaction, such as models and ORM (Object-Relational Mapping) related code.
- `docs/`: The place where you find this wonderful artefact, and in future many others
- `utils/`: A directory for general utilities and helper functions that can be used in various parts of the application.
- `tests/`: A separate directory for test cases. Crucial for maintaining code quality, especially in growing projects.
- `Dockerfile` and `requirements.txt`: These remain in the root directory for easy access and build processes.
- `.github/`: For CI/CD configurations and other GitHub related matters. Within `workflows` a basic config is given for testing while trying to push to employment.

## Rationale

- **Quality**: Let's do it the right way and build good quality code that anyone can read. Why not? Spaghetti is a delicious dish, but it is better not vomited onto one's console.
- **Modularity**: Each part of the application has its own space. Small bits work together smoothly. Or so they say. Did anybody say microservices?
- **Scalability**: It becomes easier to add new features or modify existing ones without disrupting the entire application, my AI assistent tells me.
- **Testability**: Having a separate test directory makes it easier to write and execute unit tests and integration tests. Nice to start with testing before actually coding, isn't that what we should do these days?
- **Maintainability**: This structure helps keep the codebase organized, which is rumoured to be crucial for long-term maintenance. And short-term maintenance. And by somebody or *something* else than me, preferably.
