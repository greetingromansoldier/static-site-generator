from htmlnode import LeafNode 
from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode():
    def __init__ (self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, obj):
        if (
            self.text == obj.text 
            and self.text_type == obj.text_type 
            and self.url == obj.url
            ):
            return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


