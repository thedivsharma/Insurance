#  Insurance Eligibility AI Agent

A production-grade LLM-driven inference pipeline architected for real-time multi-modal ingestion-to-decision workflows, functioning as an autonomous full-stack underwriting agent leveraging hybrid AI-ML paradigms for insurance validation automation.

###  System Architecture

Client-side asynchronous multipart/form-data upload of heterogeneous medical document images → On-device transformer-based LLM (Gemma-3) semantic parser with token-level contextual embeddings → Downstream Pydantic-based schema validation enforcing strict domain-specific JSON constraints → Custom probabilistic underwriting engine combining rule-based heuristics with Bayesian inference layers to simulate expert agent decision boundaries → Final eligibility verdict rendered with stateful session management and persisted via normalized relational schema.

### Technical Stack & Innovations

- **Ollama + Gemma-3**: Edge-native, containerized transformer inference runtime with possible,scalable and pluggable OpenAI API fallback for failover and throughput scaling.
- **Pydantic**: Declarative type-enforced data integrity layer implementing JSON Schema v7 with dynamic model coercion and runtime validation.
- **Dynamic Module Loading**: `insurance_claim` namespace injected into `sys.path` at runtime for seamless decoupling and hot-swappable model logic.
- **Structured Output Enforcement**: Leveraging LLM output parsers with strict schema post-processing, eliminating brittle regex and heuristic extraction patterns.
- **MySQL RDBMS**: multi-relational capturing of patient metadata, extracted fields, and possible inference provenance.
- **UUID-Driven Ephemeral Storage**: Stateless image lifecycle management leveraging GUID-based namespaces to mitigate data leakage and optimize ephemeral compute workloads.
- **Django 4.2**: Synchronous and asynchronous routing orchestration layer handling multi-step request lifecycles with templated UI feedback loops and session state control.
