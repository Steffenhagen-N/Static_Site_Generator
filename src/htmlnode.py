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
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
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
    def __init__(self, tag=None, children=None, props=None):
        if not children:
            raise ValueError('''ParentNode requires a "children"''')
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError('''ParentNode.to_html() requires a "tag"''')
        if not self.children:
            raise ValueError('''ParentNode.to_html() requires a "children"''')
        
        children_string = ""
        # make subfunction to recur over self.children
        # and add it to children string

        return f"<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>"