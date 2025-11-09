# Arxiv Paper Curator

## Setup
```bash
uv python install 3.12
uv init
```

## What you’ll build (Technical Breakdown)
You will build from scratch - a fully local with API integration, production-grade RAG system with:

- Data Ingestion: Auto-download PDFs daily from arXiv using Airflow
- PDF Parsing: Extract structured content via Docling
- Metadata Storage: Store authors, titles, abstracts, etc. metadata in PostgreSQL
- Search Engine: Use OpenSearch with BM25 + semantic vectors (hybrid)
- Chunking Engine: Evaluate different chunking
- RAG Pipeline: Query expansion + retrieval + prompt templating
- Local LLM: Answer questions using Ollama or API (LLaMA3, OpenAI, etc.)
- Observability: Use Langfuse for prompt versioning, tracing, quality
- Frontend: Ask questions and explore results via Streamlit or Gradio
- FastAPI Backend: Async API server for integration and extensions
- Dev Best Practices: uv, ruff, pre-commit, pydantic, pytest, logging, etc.

## Phase 1: Infrastructure foundation (APIs, databases, orchestration)
### FastAPI Backend
- Async endpoints with comprehensive swagger documentation
- Pydantic models for request/response validation
- Dependency injection for database sessions
- Error handling middleware for production reliability
- Health check endpoints for monitoring

### PostgreSQL Database
- Optimized schema for academic paper metadata
- JSONB columns for flexible document storage
- Proper indexing for fast queries
- Connection pooling for concurrent users
- Database migrations for schema evolution

### OpenSearch Cluster
- custom analyzers for scientific terminology
- Hybrid search combining BM25 + vector similarity
- Index templates optimized for document retrieval
- Cluster health monitoring and alerting
- Query performance optimization

### Apache Airflow
- DAG orchestration for automated paper ingestion
- Retry logic and failure handling
- Task dependency management
- Moitoring dashboard for pipeline health
- Scalable task execution

### Ollama Container
- Local LLM inference with no external dependencies
- Resource allocation and performance tuning
- API endpoints for question answering
- Privacy-first AI processing
- Docker Compose Orchestration
- Service dependency management
- Health check configuration
- Network isolation and security
- Volume mounting for data persistence
- Environment variable management



## Phase 2: Data ingestion pipelines

## Phase 3: Search and retrieval

## Phase 4: Chunking and evaluation

## Phase 5: Full RAG system

## Phase 6: Production optimization