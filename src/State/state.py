from sqlalchemy.sql.coercions import AnonymizedFromClauseImpl
from typing import TypedDict, Annotated
from pydantic import BaseModel,Field

class Blog(BaseModel):
    title : str = Field(description="title of the blog post")
    content : str = Field(description="Main content of the blog")

class SocialMediaContent(BaseModel):
    linkedin: str | None = Field(default=None,description="LinkedIn content")
    twitter: str | None = Field(default=None,description="Twitter content")
    instagram: str | None  = Field(default=None,description="Instagram caption content")

def merge_content(current: SocialMediaContent | None, update: dict) -> SocialMediaContent:
    if isinstance(current,SocialMediaContent):
        current_data = current.model_dump()
    else:
        current_data = current if current else {}
    current_data.update(update)
    return SocialMediaContent(**current_data)



class BlogState(TypedDict):
    topic : str | None
    blog : Blog | None
    language : str | None
    tone : str | None
    word_count : int | None
    generate_linkedin : bool 
    generate_x : bool 
    generate_instagram : bool 
    social_media : Annotated[
        SocialMediaContent | None,
        merge_content
    ]





