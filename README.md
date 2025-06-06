# 🧠 Insurance Eligibility AI Agent

A production-grade LLM pipeline that mediates image ingestion to eligibility decision (in real time) working as a 
full-stack AI agent automating insurance validation. 

### 💡 System Overview
Upload a medical bill → LLM (Gemma-3) parses → Pydantic validates → Custom eligibility model infers → Decision rendered.

### ⚙️ Tech Stack
- **Ollama + Gemma-3**: On-device inference which in the future can be scaled to have OpenAI fallback.
- **Pydantic**: Schema-enforced data integrity for extracted fields.
- **Custom Underwriting Model**: Rule-based + probabilistic engine simulating claim eligibility logic.
- **Modular Inference**: `insurance_claim` module hot-loaded via `sys.path` patch; keeps external logic decoupled.
- **Structured Output** – Enforced JSON schemas via LLM post-processing(not your regular regexes)
- **MySQL**: Relational persistence of predictions + patient context.
- **UUID-based Image Management**: Ephemeral storage to enforce stateless LLM interactions.
- **Django 4.2**: Orchestrates upload, routing, and display.

