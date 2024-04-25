from constants import TextType

class TextNode:
    def __init__(self, text:str, text_type:TextType, url:str):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node2):
        return (self.text == node2.text and 
            self.text_type == node2.text_type and
            self.url == node2.url
            )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"