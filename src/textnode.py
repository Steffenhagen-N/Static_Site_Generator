from constants import TextType, ClosedDelimiter

class TextNode:
    def __init__(self, text:str, text_type:TextType, url:str):
        if text_type not in TextType:
            raise ValueError(f"{self.text_type} is an illegal TextType")
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

# Function to split a list of TextNodes
# Returns a new list of TextNodes
# Text-Type TextNodes are split by symmetrical closed delimiters
# New TextNodes are created for each split with the appropriate type
# All other nodes are returned unchanged
def split_text_TextNode(old_nodes:list) -> list:
    new_list = []

    # Recursive helper function that appends each item to the new list
    # After modifying text-type TextNodes
    def split_nodes(text_nodes:list):
        nonlocal new_list
        if len(text_nodes) == 0:
            return new_list
        
        if text_nodes[0].text_type != TextType.TEXT:
            new_list.append(text_nodes[0])
            split_nodes(text_nodes[1:])
        else:
            pass
        # consider using the re module to do this section
            # Code to find index of all delimiters
                # If no ending delimiter raise error
                # If overlapping delimiters raise error
            # Split string into different strings by delimiter
            # Assign each string as a TextNode with appropriate type
            # Append all nodes to list
            # Recall function on text_nodes +1
    
    return split_nodes(old_nodes)