# Svastha-AI Technical Documentation

## Project Overview

Svastha-AI is an AI-powered healthcare application designed to provide users with intelligent health-related assistance. The system combines a web frontend with a Python backend and several AI-powered capabilities.

The application is organized into frontend and backend components. The frontend provides the user interface, while the backend exposes APIs and handles application logic.

The backend is implemented using Python and FastAPI. It communicates with AI services and manages application data.

## Authentication and User Management

The application provides user authentication so that users can access their personal healthcare information securely.

Authentication is responsible for:

- User registration
- User login
- Session management
- User-specific information
- Protected API access

The backend validates user credentials before allowing access to protected resources.

User-specific information should not be exposed to other users. API endpoints that return personal information should verify that the requesting user has permission to access the data.

## AI Health Assistant

The application includes an AI health assistant that allows users to ask health-related questions using natural language.

A typical interaction works as follows:

1. The user enters a question.
2. The frontend sends the question to the backend.
3. The backend processes the request.
4. The question is sent to the configured language model.
5. The generated response is returned to the frontend.
6. The frontend displays the response to the user.

The assistant should provide explanations in simple language and should avoid presenting unsupported medical claims as facts.

The AI assistant is intended to provide informational assistance and should not replace professional medical diagnosis.

## Medical Document Processing

The system can process medical documents such as reports and prescriptions.

A document-processing workflow may contain the following stages:

1. Upload the document.
2. Extract text from the document.
3. Clean and normalize the extracted text.
4. Split large text into smaller sections.
5. Store the processed information.
6. Retrieve relevant information when the user asks a question.
7. Generate an answer using the retrieved information.

The system should preserve the relationship between the extracted information and its original document so that responses can be traced back to the source.

## Retrieval-Augmented Generation

The application can use Retrieval-Augmented Generation (RAG) to answer questions using information retrieved from documents.

The RAG workflow consists of:

1. Document ingestion
2. Text extraction
3. Text chunking
4. Embedding generation
5. Vector storage
6. Similarity search
7. Context retrieval
8. LLM response generation

When a user asks a question, the system first searches the available knowledge base for relevant information. The retrieved information is then supplied to the language model as context.

This approach helps the application generate responses based on project-specific or document-specific information rather than relying only on the model's general knowledge.

## Vector Database

Document chunks can be converted into numerical embeddings.

An embedding represents the semantic meaning of a piece of text as a vector.

For example, the following sentences may have similar embeddings:

- "The patient has elevated blood pressure."
- "The patient's blood pressure is higher than normal."

A vector database can store these embeddings and perform similarity searches.

When a user asks a question, the question is also converted into an embedding. The system searches for document chunks with similar embeddings and retrieves the most relevant information.

## LangChain Integration

LangChain can be used to organize the LLM and RAG workflow.

The application can use LangChain components for:

- Prompt management
- LLM invocation
- Document loading
- Text splitting
- Embedding generation
- Vector retrieval
- Retrieval chains
- Tool integration

A typical RAG chain can be represented as:

User Question
→ Retriever
→ Relevant Documents
→ Prompt
→ Language Model
→ Final Answer

Each component should have a clearly defined responsibility so that the system remains easy to maintain.

## FastAPI Backend

FastAPI provides the HTTP API layer for the application.

The backend can expose endpoints for:

- Authentication
- User information
- AI assistant requests
- Document upload
- Document processing
- RAG queries
- Health information

A simplified request flow is:

Client
→ HTTP Request
→ FastAPI Endpoint
→ Application Logic
→ AI or Database Service
→ HTTP Response

FastAPI also provides automatic API documentation that can be used by developers to inspect available endpoints.

## Database Layer

The backend uses a database layer to store application information.

SQLAlchemy can be used as the database access layer.

The database layer is responsible for:

- Creating database connections
- Defining models
- Reading records
- Creating records
- Updating records
- Deleting records
- Managing database transactions

Keeping database operations separate from API routes makes the application easier to maintain and test.

## Frontend Architecture

The frontend is responsible for presenting the application to users.

A frontend application can contain:

- Authentication screens
- Dashboard
- AI assistant interface
- Document upload interface
- Health information pages
- Visualization components
- Navigation components

The frontend communicates with the backend through HTTP API requests.

A typical interaction is:

User
→ Frontend UI
→ API Request
→ Backend
→ Response
→ Frontend UI

The frontend should handle loading states, errors, and successful responses so that users receive clear feedback.

## Health Data Visualization

Health information can be presented using charts and visualizations.

Possible visualization types include:

- Line charts
- Bar charts
- Progress indicators
- Historical trend charts
- Summary cards

For example, a historical measurement can be displayed as a time-series chart where:

- The X-axis represents time.
- The Y-axis represents the measured value.
- Each point represents a recorded measurement.

Visualizations should clearly communicate what is being measured and when the measurement was recorded.

## AI Model Management

The application may use different AI models for different tasks.

For example:

- A language model can generate natural-language responses.
- An embedding model can convert text into vectors.
- A vision model can process images.
- An OCR system can extract text from scanned documents.

Each model should have a clearly defined responsibility.

The system should avoid using a large generative model for tasks that can be solved more reliably using deterministic logic or specialized processing.

## Prompt Engineering

Prompts define how the language model should process user requests.

A good prompt can contain:

- System instructions
- User question
- Retrieved context
- Output requirements
- Safety instructions

For a document-based question, the prompt can instruct the model to answer using only the retrieved information.

Example:

```text
You are a technical documentation assistant.

Answer the user's question using only the supplied context.

If the answer is not present in the context, clearly state that
the information is not available.

Do not invent technical details.
