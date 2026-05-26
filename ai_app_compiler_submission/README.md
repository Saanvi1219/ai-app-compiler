# Compiler Studio

AI-powered compiler-style application generation system.

Instead of directly generating output from prompts, the system follows a structured pipeline:

Prompt
↓
Intent Extraction
↓
System Design
↓
Schema Generation
↓
Validation
↓
Repair
↓
Runtime Simulation
↓
Final Architecture Output

---

## Features

- Intent extraction from natural language
- Automatic system design generation
- Database schema generation
- API route generation
- UI page generation
- Validation engine
- Self-repair mechanism
- Runtime simulation
- Confidence and chaos scoring
- Evaluation framework

---

## Folder Structure

```text
backend/
│
├── pipeline/
│   ├── compiler.py
│   ├── intent_extraction.py
│   ├── system_design.py
│   ├── schema_generation.py
│   ├── validation.py
│   ├── repair.py
│   └── runtime.py
│
├── evaluation/
│   ├── evaluator.py
│   └── prompts.json
│
└── main.py

frontend/
│
├── index.html
├── style.css
└── app.js
```

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run project:

```bash
uvicorn backend.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

Evaluation:

```text
http://127.0.0.1:8000/evaluate
```

---

## Example Prompt

```text
Build child rescue platform with NGO workflows and facial recognition
```

Example generated output:

- Pages created: 7
- API routes: 18
- Database tables: 9
- Roles: 4
- Runtime executable: True

---

## Tech Stack

- FastAPI
- Python
- HTML/CSS/JavaScript
- JSON