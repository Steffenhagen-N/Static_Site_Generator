from constants import TextType
from textnode import TextNode

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        html_string = ""
        for prop in self.props:
            html_string += f''' {prop}="{self.props[prop]}"'''
        return html_string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

# add functionality for self-closing elements idiot   
class LeafNode(HTMLNode):
    def __init__(self, tag:str=None, value:str=None, props:dict=None):
        if not value:
            raise ValueError('''LeafNode requires a "value"''')
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError('''LeafNode requires a "value"''')
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag:str=None, children:list=None, props:dict=None):
        if not children:
            raise ValueError('''ParentNode requires a "children"''')
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError('''ParentNode.to_html() requires a "tag"''')
        if not self.children:
            raise ValueError('''ParentNode.to_html() requires a "children"''')
        
        children_string = ""
        
        def translate_children(child_list):
            nonlocal children_string
            if len(child_list) == 0:
                return ""
            children_string += child_list[0].to_html()
            translate_children(child_list[1:])

        translate_children(self.children)

        return f"<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>"


# ------------------ THIS NEEDS TO BE TESTED --------------------------
def text_node_to_html_node(text_node:TextNode) -> LeafNode:
    if text_node.text_type not in TextType:
        raise ValueError(f"{text_node.text_type} is an illegal text_type")
    
    if text_node.text_type == TextType.TEXT:
        return LeafNode(tag=None, value=text_node.text, props=None)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text, props=None)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text, props=None)
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text, props=None)
    elif text_node.text_type == TextType.LINK:
        if not text_node.url:
            raise ValueError("Missing URL for link-type LeafNode")
        return LeafNode(tag="a", value=text_node.text, 
                        props={"href": text_node.url})
    
    # this bastard text type made me rework how 
    # the entire LeafNode class functions
    elif text_node.text_type == TextType.IMAGE:
        if not text_node.url:
            raise ValueError("Missing URL for image-type LeafNode")
        if not text_node.text:
            raise ValueError("Missing Alt. Text for image-type LeafNode")
        return LeafNode(tag="img", value="This is an image LeafNode", 
                        props={"src": text_node.url, "alt": text_node.text})
# ------------------- THIS NEEDS TO BE TESTED ------------------------
