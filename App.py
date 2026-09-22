import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
# pyrefly: ignore [missing-import]
from src.Graph.Builder import GraphBuilder
# pyrefly: ignore [missing-import]
from src.LLMs.GroqLLM import GroqLLM
import os
from dotenv import load_dotenv
load_dotenv()
app = FastAPI()
## CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ai-blog-generator-murex.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
os.environ["LANGSMITH_API_KEY"] = os.getenv('LANGCHAIN_API_KEY')

## Creating API's

@app.post('/generate-blogs')
async def generate_blogs(request:Request):
    data = await request.json()
    topic = data.get('topic',None)
    language = data.get('language','English')
    tone = data.get('tone',None)
    word_count = data.get('word_count',None)
    generate_x = data.get('generate_x',False)
    generate_linkedin = data.get('generate_linkedin',False)
    generate_instagram = data.get('generate_instagram',False)


    
    model = GroqLLM()
    llm = model.get_llm()

    Graph = GraphBuilder(llm)

    if topic and language:
        graph = Graph.setup_graph(usecase = 'language')
        state = graph.invoke({"topic":topic,
                              "language":language,
                              "tone":tone,
                              "word_count":word_count,
                              "generate_x":generate_x,
                              "generate_linkedin":generate_linkedin,
                              "generate_instagram":generate_instagram
                            })
    elif topic:
        graph = Graph.setup_graph(usecase = 'topic')
        state = graph.invoke({"topic":topic})
    
    return {"data":state}

if __name__ == "__main__":
    uvicorn.run("App:app",host = "0.0.0.0",port=8000,reload=True)





