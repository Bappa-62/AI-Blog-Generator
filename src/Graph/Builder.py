from langgraph.graph import StateGraph,START,END
# pyrefly: ignore [missing-import]
from src.State.state import BlogState
# pyrefly: ignore [missing-import]
from src.LLMs.GroqLLM import GroqLLM
# pyrefly: ignore [missing-import]
from src.Nodes.Node import BlogNode

class GraphBuilder:
    def __init__(self,llm):
        self.llm = llm
        self.graph = StateGraph(BlogState)
    

    def build_graph(self):
        """
          Build a graph to generate blogs based on the topic.
        """
        self.blog_node = BlogNode(self.llm)
        ## Nodes
        self.graph.add_node("Title_creation",self.blog_node.Title_creation)
        self.graph.add_node("Content_generation",self.blog_node.Content_generation)
        ## Edge
        self.graph.add_edge(START,"Title_creation")
        self.graph.add_edge("Title_creation","Content_generation")
        self.graph.add_edge("Content_generation",END)
        return self.graph

    def build_language_specific_graph(self):
        """
          Build a graph for blog generation for specific language.
        """
        self.blog_node = BlogNode(self.llm)
       
        ## Nodes
        self.graph.add_node("Title_creation",self.blog_node.Title_creation)
        self.graph.add_node("Content_generation",self.blog_node.Content_generation)
        self.graph.add_node("Language_specific_translation",self.blog_node.Language_specific_translation)
        self.graph.add_node("Tone",self.blog_node.Tone_setting)
        self.graph.add_node("Word_count",self.blog_node.Count_setting) 
        self.graph.add_node("Linkedin_content",self.blog_node.Linkedin_content)
        self.graph.add_node("X_content",self.blog_node.X_content)
        self.graph.add_node("Instagram_content",self.blog_node.Instagram_content)
        self.graph.add_node("Social_Media_Router", self.blog_node.Social_Media_Router)
        ##self.graph.add_node("Language_specific_translation",lambda state:self.blog_node.Language_specific_translation({**state,"language":"hindi"}))
       
        ## Edge
        self.graph.add_edge(START,"Title_creation")
        self.graph.add_edge("Title_creation","Content_generation")
        self.graph.add_edge("Content_generation","Language_specific_translation")
        self.graph.add_edge("Language_specific_translation","Tone")
        self.graph.add_edge("Tone","Word_count")
        self.graph.add_edge("Word_count","Social_Media_Router")
        self.graph.add_conditional_edges(
                  "Social_Media_Router",
                   self.blog_node.social_media_router,
                   {
                     "Linkedin_content":"Linkedin_content",
                     "X_content":"X_content",
                     "Instagram_content":"Instagram_content"
                   }
                )
        self.graph.add_edge("Linkedin_content",END)
        self.graph.add_edge("X_content",END)
        self.graph.add_edge("Instagram_content",END)
        return self.graph
 
    def setup_graph(self,usecase):
        if usecase == 'topic':
            return self.build_graph().compile()
        if usecase == 'language':
            return self.build_language_specific_graph().compile()

## For Langsmith langgraph studio
llm = GroqLLM().get_llm()
Compiled_graph = GraphBuilder(llm).build_graph().compile()




