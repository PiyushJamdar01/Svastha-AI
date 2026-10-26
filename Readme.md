# 🏥 SvasthaAI - Advanced AI-Powered Healthcare Ecosystem

SvasthaAI is a cutting-edge, professional-grade healthcare platform designed to provide intelligent health monitoring, AI-driven diagnostics, and personalized wellness guidance. Developed with a "Senior Developer" mindset, the project emphasizes modular architecture, high-fidelity UI/UX, and robust AI integration to bridge the gap between users and actionable medical insights.

## 🚀 Vision & Objective
Our mission is to democratize high-quality health monitoring using advanced machine learning. SvasthaAI isn't just a dashboard; it's a proactive health companion that analyzes vitals, predicts potential risks, and provides a gamified environment for wellness improvement.

## 🛠️ Advanced Technology Stack

### Core Languages & Frameworks
- **Languages**: Python (Backend/AI), TypeScript (Frontend), SQL (Database), Shell (DevOps).
- **Frontend**: Built with **React 18** and **Vite** for optimized performance.
- **Backend**: **FastAPI** leveraging asynchronous I/O for high-throughput API handling.

### Artificial Intelligence & Machine Learning (The Core)
- **Deep Learning**: Specialized models built on **TensorFlow** and **Keras** for organ-specific health analysis.
- **Predictive Modeling**: **Scikit-learn** implementations for multi-condition risk assessment (Diabetes, Anemia, Hypertension).
- **Computer Vision**: **OpenCV** and **DeepFace** for advanced facial biometric analysis and emotion-driven wellness tracking.
- **RAG (Retrieval-Augmented Generation)**: Enhanced medical chatbots using **Groq API** (Llama-3/Mixtral) for lightning-fast, context-aware responses.
- **OCR & Document Parsing**: Automated analysis of medical prescriptions and lab reports.

### UI/UX & Design
- **Premium Aesthetics**: Glassmorphism, dark mode first, and curated HSL color palettes.
- **Styling**: **TailwindCSS** for responsive design and **Shadcn UI** for high-quality accessible components.
- **Animations**: **Framer Motion** and **GSAP** for micro-animations that make the interface feel alive.

### Infrastructure & DevOps
- **Containerization**: Full **Docker** orchestration for consistent local and production environments.
- **Reverse Proxy**: **Nginx** configuration for production-ready security and performance.
- **CI/CD Ready**: Structured for automated testing and deployment pipelines.

## 📁 Systematic Project Structure

```text
Svastha-AI/
├── backend/            # Python FastAPI backend core
│   ├── ai/            # ML models and AI logic
│   ├── app/           # API routes, schemas, and database logic
│   └── storage/       # SQLite DB and user-uploaded media
├── frontend/           # React frontend source
│   ├── src/           # Components, pages, and hooks
│   └── public/        # Static assets
├── data/               # Curated datasets for ML training (CSV/JSON)
├── docs/               # Technical documentation and architecture reports
├── infra/              # Docker, Nginx, and deployment configs
├── scripts/            # Management tools (DB migration, model training)
└── README.md           # Main project entry
```

## 🧠 Key Techniques & Implementation
- **Hybrid RAG Pipeline**: Combines local medical knowledge bases with LLMs for verified medical information.
- **Multi-Organ Training**: Parallel training architectures for specialized health metrics.
- **Asynchronous Task Processing**: Ensuring UI responsiveness while heavy ML models load in the background.
- **Security-First Design**: Redacted PII, secure JWT auth, and environment-based configuration.

## ⚠️ Challenges of Deployment (The Reality)
While SvasthaAI is a robust platform, deploying it to cloud environments like **AWS** or **GCP** presents significant challenges:

1. **Heavyweight AI Libraries**: The inclusion of **TensorFlow** and **DeepFace** creates a container image that is several gigabytes in size. Building these on standard CI/CD runners often hits storage and timeout limits.
2. **Compute Intensity**: Standard cloud free-tiers (like AWS `t2.micro`) are **incapable** of running this stack. Loading the DeepFace models alone consumes ~2GB of RAM, leading to OOM (Out-of-Memory) kills on anything less than a `t3.medium` (4GB+ RAM).
3. **Hardware Acceleration**: For real-time inference, the application ideally requires GPU support (CUDA), which significantly increases deployment costs on AWS.
4. **Complex OS Dependencies**: DeepFace and OpenCV require specific system-level libraries (`libGL`, `libsm6`) that must be meticulously managed within the Docker environment to avoid runtime crashes.

---
*Disclaimer: SvasthaAI is an AI-powered tool for informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a physician for health concerns.*


## 📚 LLM-Wiki Integration

SvasthaAI documentation can be processed by an LLM-Wiki system to make project knowledge easier to search and understand.

### How It Works

- **Documentation Ingestion:** Markdown files (`.md`) are collected from the project repository and stored in AWS S3.
- **Change Detection:** A manifest containing SHA-256 hashes tracks source documents and helps identify changes.
- **Wiki Generation:** When source documentation changes, the updater can use an LLM to generate or refresh related wiki pages.
- **Cloud Storage:** Generated wiki pages, the wiki index, and the manifest are stored separately from the original source documents or Paper.
- **Knowledge Retrieval:** The generated wiki can serve as a knowledge source for answering questions about SvasthaAI.

### Objective

The goal is to maintain an up-to-date, searchable knowledge base for SvasthaAI while avoiding unnecessary LLM calls when the source documentation has not changed.

*Note: The LLM-Wiki integration is a separate documentation workflow and does not itself provide medical diagnosis or treatment recommendations.*

## LLM-Wiki Integration Test: Personalized Health Insights and Trend Analysis

### 1. Feature Overview

SvasthaAI is being extended with a Personalized Health Insights and Trend Analysis module. The purpose of this module is to help users understand changes in their health information over time instead of viewing each medical report or health measurement as an isolated record.

The module will organize historical health information, identify meaningful changes, and generate understandable summaries that explain possible trends. It will connect with the existing SvasthaAI frontend, FastAPI backend, database layer, and AI/ML services.

This feature is intended as an architectural proposal and integration test. It should not be interpreted as confirmation that every component described below has already been implemented.

### 2. Historical Health Data Collection

The system may collect structured health information from user-provided medical reports, laboratory results, manually entered measurements, and other supported health data sources. Each record should be associated with the appropriate user and include available metadata such as the measurement name, value, unit, collection date, and source.

Before analyzing historical information, the backend should validate incoming data and normalize compatible units. Records with missing dates, unsupported units, invalid values, or ambiguous measurement names should be flagged rather than silently treated as reliable observations.

The system should preserve the original source information where appropriate so that generated insights can be traced back to the records used in the analysis.

### 3. Data Storage and Historical Records

The FastAPI backend will provide an interface for storing and retrieving historical health records. The database layer should support retrieving records for a specific user, filtering by measurement type, and sorting observations by date.

A possible conceptual data model includes the following entities:

- User: identifies the account associated with the records.
- HealthRecord: stores an individual observation or laboratory result.
- HealthMetric: describes a measurement type and its expected unit.
- HealthInsight: stores a generated summary, its supporting record references, and its generation timestamp.

These entities are a proposed design, not a statement about the current database schema. Any implementation should follow the project's existing SQLAlchemy models and migration conventions.

Historical records must remain isolated between users. A request for one user's health information must never return another user's records.

### 4. Health Trend Analysis

The trend analysis service will examine chronological observations for a selected health measurement. It may calculate changes between observations, percentage changes where mathematically appropriate, moving averages when sufficient data is available, and the frequency of measurements over a selected period.

The analysis should account for the number of observations, time intervals, missing values, and measurement units. A trend should not be reported as reliable merely because two values differ. Where there is insufficient information, the system should clearly state that the available records do not support a meaningful conclusion.

The service may classify observations as increasing, decreasing, relatively stable, or insufficient for trend assessment. These labels describe patterns in the supplied data and should not automatically be interpreted as a medical diagnosis.

### 5. AI-Generated Health Explanations

The LLM component may convert the output of the trend analysis service into a readable explanation. For example, it could summarize how a measurement has changed over several recorded dates, identify which observations support the summary, and explain the limitations of the available information.

The language model should receive only the information needed for the requested analysis. It should not invent measurements, dates, laboratory results, diagnoses, or medical history that are absent from the supplied records.

Every generated insight should distinguish recorded facts from possible interpretations. The system should explain when the information is incomplete and direct users to an appropriately qualified healthcare professional when clinical interpretation is needed.

The LLM should not independently calculate or invent numerical trends when those calculations can be performed and validated by the backend.

### 6. Relationship With the Existing Medical RAG Pipeline

The Personalized Health Insights module may complement the existing Medical Retrieval-Augmented Generation (RAG) pipeline.

The trend analysis service focuses on changes in a user's historical measurements. The RAG pipeline retrieves relevant information from an approved medical knowledge base. The LLM can use these two kinds of context for different purposes: summarizing a user's recorded history and explaining general medical concepts using retrieved references.

These responsibilities should remain separate. Retrieved medical literature must not be confused with the user's personal records, and a general explanation from a knowledge base must not be presented as a personalized diagnosis.

If the existing RAG implementation is used, its retrieval, source attribution, and answer-generation behavior should be preserved. The new module should reuse existing components where appropriate rather than introduce an unnecessary second RAG implementation.

### 7. Proposed API Integration

The FastAPI backend could expose endpoints for retrieving health history, requesting a trend analysis, and retrieving previously generated insights.

Illustrative endpoint responsibilities include:

- `GET /health-records`: retrieve authorized health records using supported filters.
- `GET /health-records/{record_id}`: retrieve a single authorized record.
- `POST /health-insights/analyze`: request analysis for a selected measurement and time period.
- `GET /health-insights`: retrieve previously generated insights for the authenticated user.

These routes are examples for architectural planning and are not claims that the endpoints currently exist. Actual route names, request schemas, authentication dependencies, and error responses should follow the conventions used by the existing backend.

The API should validate incoming requests, enforce authorization, return consistent error responses, and avoid exposing sensitive medical information through logs or error messages.

### 8. Frontend Visualization

The React and TypeScript frontend could display historical measurements through chronological charts, summary cards, and a timeline of important observations.

A user should be able to select a measurement, choose a time period, inspect the underlying observations, and view an explanation of the detected trend. Each visualization should show measurement units and dates clearly.

The interface should distinguish measured values from calculated statistics and LLM-generated explanations. Missing observations and insufficient data should be represented clearly rather than displayed as zero values.

The frontend should also provide loading states, useful validation messages, and appropriate handling for API failures. Visualizations must not imply clinical certainty beyond what the underlying data supports.

### 9. Privacy, Security, and Reliability

Health information is sensitive. Access to historical records and generated insights must be restricted to authorized users. Authentication and authorization should be enforced by the backend rather than relying solely on frontend controls.

The system should minimize the amount of personal information sent to external LLM providers. Any external processing must follow the project's applicable privacy requirements, provider terms, and security configuration.

The implementation should avoid placing medical records, access tokens, API keys, or other secrets in source control. Secrets should be managed through suitable environment configuration or a dedicated secrets-management service.

Generated insights should be traceable to the source records used to produce them. Failures in the LLM provider, database, or retrieval pipeline should not cause incomplete results to be presented as verified conclusions.

### 10. Testing and Evaluation

The proposed module should be tested with synthetic or appropriately de-identified data before being evaluated with real health information.

Important test scenarios include:

- A user has several dated observations for the same measurement.
- A measurement contains a different unit from previous observations.
- A record has a missing or invalid collection date.
- Only one observation exists, so a trend cannot be established.
- Historical records belong to different users.
- The LLM provider is unavailable.
- The RAG pipeline returns no relevant references.
- The generated explanation includes a numerical claim that must be checked against the source records.

Tests should verify that calculated values are correct, access controls are enforced, unsupported conclusions are avoided, and failures are handled safely.

Evaluation should consider numerical accuracy, source traceability, clarity of explanations, privacy, response time, and unnecessary LLM usage.

### 11. Relationship to Existing SvasthaAI Components

This proposal connects several areas of the existing project:

- Project Overview: expands the broader vision of personalized and proactive health support.
- System Architecture: introduces a possible interaction between historical data services, FastAPI, the database, AI/ML services, and the frontend.
- AI/ML Model Catalog: describes the separation between deterministic trend calculations and LLM-generated explanations.
- Medical RAG Pipeline: establishes how retrieved medical knowledge may complement historical health analysis.
- Backend Technical Reference: identifies possible API responsibilities and conceptual database entities.
- Frontend Overview: describes potential health trend charts and insight summaries.
- Deployment Guide: identifies operational considerations for backend services, model-provider access, configuration, and monitoring.

These relationships are intentional. They provide context for deciding whether the information belongs in existing wiki pages, should be linked from several pages, or warrants a dedicated page.

### 12. LLM-Wiki Integration Test Instructions

This section is also intended to validate the automated documentation-to-wiki pipeline.

When this README changes, the GitHub Actions workflow should synchronize the updated Markdown document to the AWS S3 `source-docs/` prefix. The LLM-Wiki updater should then compare the current source-document hashes with the hashes recorded in its manifest.

If `Readme.md` has changed, the updater should identify the existing wiki pages that depend on it and determine which pages need regeneration. It should update relevant pages, preserve unrelated pages where possible, refresh the wiki index if the page plan changes, and publish the updated manifest.

The updater should not assume that every new section requires a new wiki page. It should evaluate the subject matter, existing page descriptions, source-file dependencies, and relationships between concepts.

For this test, the system should consider whether the new health trend analysis content belongs in the existing Project Overview, System Architecture, AI/ML Model Catalog, Medical RAG Pipeline, Backend Technical Reference, and Frontend Overview pages. It should also evaluate whether the feature has enough distinct information to justify a new page such as `personalized-health-insights.md`.

A new page should be created only when it provides a meaningful, distinct topic rather than duplicating an existing page. If a new page is created, the index should describe its purpose, identify its source files, and include it in the generated knowledge structure. Related pages should be updated or linked when the new information materially affects their content.

The test should verify that the generated wiki reflects the new section, that the index and manifest remain consistent, and that a subsequent run without further source changes exits without unnecessary LLM calls.

### 13. Expected Outcome

After this documentation update is synchronized and processed, the generated wiki should contain accurate information about the proposed Personalized Health Insights and Trend Analysis feature.

The resulting wiki may update existing architecture, AI/ML, RAG, backend, frontend, or project overview pages. It may also create a dedicated page if the planner determines that the new feature deserves independent documentation.

The generated pages should preserve the distinction between implemented functionality and proposed design, avoid unsupported technical claims, and maintain useful links between related topics.

The purpose of this test is to evaluate whether the LLM-Wiki system can detect a source change, understand the new content, make a reasonable page-organization decision, regenerate the appropriate pages, and publish a consistent knowledge base without regenerating unrelated documentation unnecessarily.


