from constants import TextType, SelfClosedTag
from textnode import TextNode

# This is a barebones node to construct more complex nodes from
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # This function's output is child-specific and can't be defined here
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    # Formats a dictionary of properties into HTML tags
    # Leading space is inserted before each property *including the first*
    def props_to_html(self):
        if self.props is None:
            return ""
        html_string = ""
        for prop in self.props:
            html_string += f''' {prop}="{self.props[prop]}"'''
        return html_string
    
    def __repr__(self):
        return (f"HTMLNode({self.tag}, {self.value}, "
                f"children: {self.children}, {self.props})")

# Endpoint node in tree-structure
# Text is required in nodes that are not self-closed
class LeafNode(HTMLNode):
    def __init__(self, tag:str=None, value:str=None, props:dict=None):
        if tag not in SelfClosedTag:
            if not value:
                raise ValueError('''LeafNode requires a "value"''')
        super().__init__(tag=tag, value=value, children=None, props=props)

    # Formats node into a fully tagged string
    # Self-closed nodes are formatted <{tag}{props} />
    # All other nodes are formatted <{tag}{props}>{value}</{tag}>
    def to_html(self):
        if self.tag in SelfClosedTag:
            return f"<{self.tag}{self.props_to_html()} />"
        if not self.value:
            raise ValueError('''LeafNode requires a "value"''')
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

# Branch node in tree-structure
# Cannot accept a value, instead requires list of child nodes
# Child nodes can be either LeafNodes or nested ParentNodes
class ParentNode(HTMLNode):
    def __init__(self, tag:str=None, children:list=None, props:dict=None):
        if not children:
            raise ValueError('''ParentNode requires a "children"''')
        super().__init__(tag=tag, value=None, children=children, props=props)

    # Formats node into single string of tags and children
    # Children.to_html are automatically called
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

# Formats TextNodes into LeafNodes
# Does not call .to_html on result, needs to be intentionally called
# When augmenting this function, make sure to update 
# TextType and SelfClosedTag in constants.py
def text_node_to_html_node(text_node:TextNode) -> LeafNode:
    if text_node.text_type not in TextType:
        raise ValueError(f"{text_node.text_type} is an illegal text_type")
    
    # Open LeafNodes
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
    
    # Self-closed LeafNodes
        # this bastard text type made me rework how 
        # the entire LeafNode class works
    elif text_node.text_type == TextType.IMAGE:
        if not text_node.url:
            raise ValueError("Missing URL for image-type LeafNode")
        if not text_node.text:
            raise ValueError("Missing Alt. Text for image-type LeafNode")
        return LeafNode(tag="img", value="This is an image LeafNode", 
                        props={"src": text_node.url, "alt": text_node.text})
