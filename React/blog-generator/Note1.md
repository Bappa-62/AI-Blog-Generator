                USER
                  │
                  ▼
          React Web UI
        localhost:3000
                  │
                  │
                  ▼
              App.js
                  │
                  │  User clicks
                  │ "Generate Blog"
                  ▼
              Api.js
                  │
                  │ Axios POST
                  ▼
       http://localhost:8000
                  │
                  ▼
     FastAPI /generate-blogs
                  │
                  ▼
        generate_blogs()
                  │
                  ▼
             GroqLLM()
                  │
                  ▼
          GraphBuilder(llm)
                  │
                  ▼
          setup_graph(...)
                  │
                  ▼
         LangGraph Workflow
                  │
                  ▼
             Groq LLM
                  │
                  ▼
              state
                  │
                  ▼
        {"data": state}
                  │
                  ▼
              Axios
                  │
                  ▼
              App.js
                  │
                  ▼
            React UI
                  │
                  ▼
       Generated Blog + Social
              Content



****************************************************************************************


                 FRONTEND
────────────────────────────────────

User
 │
 ▼
React UI
 │
 ▼
App.js
 │
 │  axios.post()
 ▼
Api.js
 │
 │
 │ HTTP POST
 ▼

          BACKEND
────────────────────────────────────

FastAPI
 │
 ▼
/generate-blogs
 │
 ▼
Request JSON
 │
 ▼
GroqLLM
 │
 ▼
GraphBuilder
 │
 ▼
LangGraph
 │
 ▼
LLM / Nodes
 │
 ▼
Generated State
 │
 ▼
FastAPI Response
 │
 │ JSON
 ▼

          FRONTEND
────────────────────────────────────

Axios
 │
 ▼
response.data
 │
 ▼
setResult()
 │
 ▼
React re-render
 │
 ▼
Blog + LinkedIn
+ X + Instagram