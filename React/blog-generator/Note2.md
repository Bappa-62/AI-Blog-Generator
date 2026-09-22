                 BROWSER
                    │
                    ▼
              index.html
                    │
                    ▼
          React Entry Point
          index.js/main.jsx
                    │
                    ▼
                 App.js
             (UI / Logic)
                    │
                    ▼
                 api.js
          (HTTP/API Layer)
                    │
             POST /generate-blogs
                    │
                    ▼
              FastAPI App.py
              (Backend/API)
                    │
                    ▼
             GraphBuilder
                    │
                    ▼
          LangGraph Workflow
                    │
                    ▼
              Groq / LLM
                    │
                    ▼
          Generated Blog/State
                    │
                    ▼
              FastAPI response
                    │
                    ▼
                 api.js
                    │
                    ▼
                 App.js
                    │
                    ▼
              Display Blog