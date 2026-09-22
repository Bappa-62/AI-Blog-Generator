# pyrefly: ignore [missing-import]
from src.State.state import BlogState,Blog
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage,SystemMessage

class BlogNode:
    """
      Defining all the Nodes.
    """
    def __init__(self,llm):
        self.llm = llm

    def Title_creation(self,state:BlogState):
        """
         Create the title of the blog.
        """
        if 'topic' in state and state['topic']:
            prompt = """
              You are an expert blog content generator. Use Markdown Format and generate a blog title 
              for the {topic}. The title should be creative,interesting and most importantly SEO friendly.
            """
            system_message = prompt.format(topic = state['topic'])
            result = self.llm.invoke(system_message)
            return {"blog":{"title":result.content}}


    def Content_generation(self,state:BlogState):
        if 'topic' in state and state['topic']:
            prompt = """
                     You are an expert blog content generator. Using markdown formatting, generate
                     a detailed blog content with detailed breakdown for the {topic} """
            system_message = prompt.format(topic = state['topic'])
            result = self.llm.invoke(system_message)
            return {"blog":{"title":state['blog']['title'],"content":result.content}}

    def Language_specific_translation(self,state:BlogState):
        if 'language' in state and state['language']:
            """
              Translate the content to the specific language.
            """
            prompt = """
                     Translate the following content into {language}.
                     - Maintain the original tone, style and formatting.
                     - Adapt cultural references and idioms to be appropriate for {language}.
                     Original Content: {blog_content}
                    """
            blog_content = state['blog']['content']
            messages = [
                HumanMessage(content=prompt.format(language = state['language'],blog_content = blog_content))
            ]

            response = self.llm.invoke(messages)
            return {
            "blog": {
                "title": state["blog"]["title"],
                "content": response.content
            }
        }

    def Tone_setting(self,state:BlogState):
        """
         Set the tone of the generated content.
        """
        prompt = """
                   Write the blog in a {tone} tone.
                   Maintain the selected tone consistently throughout the blog.
                   The tone should be appropriate for the topic, target audience, and purpose of the blog.
                   Do not change the factual meaning of the content while adapting the tone.
                   Content: {blog_content}
                """
        blog_content = state['blog']['content']
        messages = [
                HumanMessage(content=prompt.format(tone = state['tone'],blog_content = blog_content))
            ]
        response = self.llm.with_structured_output(Blog).invoke(messages)
        return {
            "blog": {
                "title": response.title,
                "content": response.content
            }
        }

    def Count_setting(self,state:BlogState):
        """
         Concise the generated content with given no of words.
        """
        prompt = """
                   Keep the blog approximately {word_count} words long.
                   Use the requested word count as a target while maintaining clarity, completeness, and natural flow.
                   Do not add unnecessary content merely to reach the target word count.
                   Content: {blog_content}
                """
        blog_content = state['blog']['content']
        messages = [
                HumanMessage(content=prompt.format(word_count = state['word_count'],blog_content = blog_content))
            ]
        response = self.llm.with_structured_output(Blog).invoke(messages)
        return {
            "blog": {
                "title": response.title,
                "content": response.content
            }
        }


    def Linkedin_content(self,state:BlogState):
        """
          Generate content for LinkedIn.
        """
        prompt = """
        Convert the following blog into a professional LinkedIn post.
        Blog Title:
        {title}
        Blog Content:
        {content}
        Requirements:
        - Create an engaging opening hook.
        - Keep the content professional and informative.
        - Highlight the key insights from the blog.
        - End with a relevant call-to-action.
        - Add 3-5 relevant hashtags.
        """
        messages = [HumanMessage(content= prompt.format(
            title=state["blog"]["title"],
            content=state["blog"]["content"]))
        ]
        result = self.llm.invoke(messages)
        return {"social_media": {"linkedin": result.content }}


    def X_content(self, state: BlogState):
        """
         Generating content for X.
        """
        prompt = """
        Convert the following blog into a concise X (Twitter) post.
        Blog Title:
        {title}
        Blog Content:
        {content}
        Requirements:
        - Create a strong hook.
        - Keep it concise and engaging.
        - Capture the most important insight.
        - Add 1-3 relevant hashtags.
        """
        messages = [HumanMessage(content= prompt.format(
            title=state["blog"]["title"],
            content=state["blog"]["content"]))
        ]
        result = self.llm.invoke(messages)
        return {"social_media": {"twitter": result.content}}


    def Instagram_content(self, state: BlogState):
        """
         Generating for Instagram Caption.
        """
        prompt = """
        Convert the following blog into an engaging Instagram caption.
        Blog Title:
        {title}
         Blog Content:
        {content}
        Requirements:
        - Start with an attention-grabbing line.
        - Use short, easy-to-read paragraphs.
        - Use emojis appropriately.
        - End with a call-to-action.
        - Add relevant hashtags.
        """
        messages = [HumanMessage(content= prompt.format(
            title=state["blog"]["title"],
            content=state["blog"]["content"]))
        ]
        result = self.llm.invoke(messages)
        return {"social_media": {"instagram": result.content }}

    def Social_Media_Router(self,state:BlogState):
        pass

    def social_media_router(self,state: BlogState):
        routes = []

        if state.get("generate_linkedin"):
            routes.append("Linkedin_content")
        if state.get("generate_x"):
            routes.append("X_content")
        if state.get("generate_instagram"):
            routes.append("Instagram_content")
        return routes

            

