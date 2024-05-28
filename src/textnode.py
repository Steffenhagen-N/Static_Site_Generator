from constants import TextType
import re

# (text:string, text_type:TextType, url:str)
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
def split_text_TextNode_by_delimiter(old_nodes:list) -> list:
#   Text-Type TextNodes are split by symmetrical closed delimiters
#   New TextNodes are created for each split with the appropriate type
#   All other nodes are returned unchanged
    new_list = []

    # Recursive helper function that appends non-text TextType TextNodes
    # Calls another helper function on text TextNodes to split them
    def verify_nodes(text_nodes:list):
        nonlocal new_list
        if len(text_nodes) == 0:
            return new_list
        
        if text_nodes[0].text_type != TextType.TEXT:
            new_list.append(text_nodes[0])
            verify_nodes(text_nodes[1:])
        else:
            new_list.extend(split_node(text_nodes[0]))
            verify_nodes(text_nodes[1:])

    # Helper function that splits text TextNodes into a list
    # Of other TextNodes by style delimiters
    def split_node(text_node:TextNode) -> list:
        if text_node.text_type != TextType.TEXT:
            raise ValueError(f"Cannot split {text_node.text_type} type TextNode")
        node_text = text_node.text
        split_string = []
        nodes = []

        # Checks if there is an even number of identical delimiters
        if len(re.findall(r"(?<!\*)\*(?!\*)", node_text))%2 != 0:
            raise SyntaxError("*Italic* style requires a closing delimiter")
        if len(re.findall(r"\*\*(?!\*)", node_text))%2 != 0:
            raise SyntaxError("**Bold** style requires a closing delimiter")
        if len(re.findall(r"\`(?!\`)", node_text))%2 != 0:
            raise SyntaxError("`Code` style requires a closing delimiter")

        # Helper function that ensures no nested delimiters
        # I am restricting nested delimiters because creating a parser
        # Is beyond the scope of this project
        # Raises an error if nested delimiters are detected
        # Returns nothing if text is valid
        check_overlap(node_text)


        # Oh God Oh Fuck Regular Expressions
        # Theoretically this should split the string by all delimiters
        # I chose to use regex because it significantly reduced the 
        # number of lines needed to accomplish the same thing
        # This is further simplified by disallowing nested delimiters

        # First the single node text is split on all italic delimiters
        # and stored as a list in split_string
        split_string = re.split(r"((?<!\*)\*[^\*]+\*(?!\*))", node_text)
        # Next each split string is checked for bold delimiters, and is 
        # split again and stored in order back in split_string
        temp_list = []
        for string in split_string:
            temp_list.extend(re.split(r"(\*\*[^\*]+\*\*)", string))
        split_string = temp_list
        # Finally all of the strings are checked for code delimiters
        temp_list = []
        for string in split_string:
            temp_list.extend(re.split(r"(\`[^\`]+\`)", string))
        split_string = temp_list
        # After all of the regex hell, split_string is a list of strings
        # with the original order preserved, and original delimiters 
        # opening and closing their respective substring
        
        # The filter method is necessary to remove any empty strings
        # generated from strings that begin with delimiters
        split_string = list(filter(None, split_string))

        # Transforms the list of strings into a list of TextNodes
        nodes = to_TextNode(split_string)

        return nodes
    
    # Checks if style delimiters are nested
    # Raises an error if True
    # Else returns "All good" 
    def check_overlap(text:str):

        italic_range = []
        bold_range = []
        code_range = []

        # Checks specifically for ***bold and italic*** text delimiters
        # because they reuse the same character
        if "***" in text:
            raise SyntaxError("I swear to GOD if you're trying to use bold "
                                "and italic at the same time I will "
                                "personally find you and beat you to death "
                                "because I can't be fucked to figure out "
                                "parsers right now because I'm already "
                                "sick of regex and I miss when commands "
                                "had names that made sense like what the "
                                "FUCK does [(.*?)\]\((.*?)\) even MEAN")
        

        # First we're compiling tuples representing the index range
        # of all italic text
        # This looks scary, but it's not too bad
        # (?<!\*) is a negative lookback that checks for *
        # \* checks for a single asterisk
        # [^\*]+ looks for one or more characters that are not *
        # (\*\*[^\*]*)? means to ignore potential ** followed by 0 or more ^*
        # \* is the ending * for the end of the italic syntax
        for m in re.finditer(r"((?<!\*)\*[^\*]+(\*\*[^\*]*)?\*)", text):
            italic_range.append((m.start(), m.end()))
        
        # Then for bold...
        # (?:\*[^\*]+)* means there will be 0 or more single asterisks, 
        # and to look for characters that are not *
        # This means the regex will keep looking for * if it finds one without
        # another one directly behind it
        for m in re.finditer(r"(\*\*(?:\*?[^\*]+)*\*\*)", text):
            bold_range.append((m.start(), m.end()))

        # And finally code
        for m in re.finditer(r"(\`[^\`]+\`)", text):
            code_range.append((m.start(), m.end()))
        

        # Then we check each italic range against the other ranges
        for itc in italic_range:
            for bld in bold_range:
                if itc[0] in range(bld[0], bld[1]):
                    raise SyntaxError("Nested delimiters not allowed")
            for cde in code_range:
                if itc[0] in range(cde[0], cde[1]):
                    raise SyntaxError("Nested delimiters not allowed")
                
        # Followed by bold...
        for bld in bold_range:
            for itc in italic_range:
                if bld[0] in range(itc[0], itc[1]):
                    raise SyntaxError("Nested delimiters not allowed")
            for cde in code_range:
                if bld[0] in range(cde[0], cde[1]):
                    raise SyntaxError("Nested delimiters not allowed")
                
        # And ending with code
        for cde in code_range:
            for itc in italic_range:
                if cde[0] in range(itc[0], itc[1]):
                    raise SyntaxError("Nested delimiters not allowed")
            for bld in bold_range:
                if cde[0] in range(bld[0], bld[1]):
                    raise SyntaxError("Nested delimiters not allowed")


        # We don't do anything with this, it's just here for debugging
        return "All good!"

    # Transforms a list of strings into a list of different TextNodes
    # based on opening and closing delimiters
    def to_TextNode(lines:list) -> list:
        temp_list = []

        # Since we've already ensured that each delimiter is only ever at
        # the start or end of a string, we can avoid regex and use 
        # the native .startswith and .endswith instead
        for line in lines:
            if line.startswith("`") and line.endswith("`"):
                node_text = line.strip("`")
                temp_list.append(TextNode(text=node_text, 
                                          text_type=TextType.CODE, url=None))
            elif line.startswith("**") and line.endswith("**"):
                node_text = line.strip("*")
                temp_list.append(TextNode(text=node_text,
                                          text_type=TextType.BOLD, url=None))
            elif line.startswith("*") and line.endswith("*"):
                node_text = line.strip("*")
                temp_list.append(TextNode(text=node_text,
                                          text_type=TextType.ITALIC, url=None))
            else:
                temp_list.append(TextNode(text=line, 
                                          text_type=TextType.TEXT, url=None))

        return temp_list

    verify_nodes(old_nodes)
    return new_list

# Small function to return a list of tuples of image alt text and URL
# sliced from within a given string 
def extract_markdown_images(text:str) -> list:
# Unsolved issue with function: 
#   As of right now, this function falls apart when encountering cases
#   where the user includes an unclosed "![" before the image declaration
#   within the same string. There is currently no way for the regex to
#   discern the context in which the string is written. 
#
#   Additionally, if you nest another image format string inside the alt
#   text of the outer image, the url of the outer image will not be captured
#   and only one image tuple will be generated
#
#
# Potential solutions considered:
#   I have considered a few different potential solutions to the issue, 
#   all of which come with their own set of issues.
# 
#   1. Using regex to disallow two "[" in a row without a "]"" between them
#       Raising a syntax error in this case would allert the user to 
#       the issue their string would cause, but locks the user out of
#       legitimate cases where brackets are used inside the image alt text
#       or an unclosed bracket in the preceding text
#
#   2. Using regex alongside pythonic functions to determine the 
#   index range of all "[" "]" pairs, and use the "[" "]" only immediately 
#   before the image URL
#       This in combination with the first solution would help, but it's
#       just a workaround that doesn't actually address the underlying issue
#
#   3. Check for an equal number of "[" and "]" and raises an error if not
#       This is another case where technically it solves the core issue, 
#       but at the expense of further functionality. In this case I 
#       believe it would restrict much more functionality than the issues
#       it prevents
# 
#   4. Ignore all "![" preceeding a "]" except the last one
#       This solves the issue, but creates a whole new issue when the user
#       wants to include an unpaired "![" inside the image alt text.
#
#
# Decision rationale:
#   I have decided to move on from this issue because it seems the only way
#   to address this issue is with a complex parser to determine context
#   within the string. This is far too much effort and code for a one-line
#   function that has an edge-case issue that most users will not encounter
#
#
# Future consideration:
#   I will revisit this decision if this project ever becomes public, or if
#   in my own use this edge case becomes more significant than I anticipated.
#   If you forsee this edge case becoming an issue, manually make a new image
#   HTML TextNode with no preceding text. 
    return re.findall(r"\!\[(.*?)\]\((.*?)\)", text)

# This function is similar to the one above, except instead of images
# it extracts link tuples from a string.
def extract_markdown_links(text:str) -> list:
    # It also has the same issues as the previous function, and for similar
    # reasons they are being ignored
    #  
    # A negative lookbehind has been added to the beginnig to ensure
    # the function does not falsely capture images
    return re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)

# Splits a text TextNode by image or link formatting and 
# assigns new TextTypes to appropriate nodes
def split_text_TextNode_by_image_or_link(old_nodes:list) -> list:
    temp_list = []

    # main recursive function
    def verify_nodes(nodes:list):
        nonlocal temp_list

        # End case for recursion
        if len(nodes) == 0:
            return temp_list
        
        # If TextNode != text, appends to temp_list
        if nodes[0].text_type != TextType.TEXT:
            temp_list.append(nodes[0])
            verify_nodes(nodes=nodes[1:])

        # For all text TextNodes...
        elif nodes[0].text_type == TextType.TEXT:
            # If the text is empty, it is ignored and the function recurs
            if not nodes[0].text:
                verify_nodes(nodes=nodes[1:])
            # Else the node is split, images and links are
            # correctly formatted, and temp_list is extended
            else:
                temp_list.extend(split_text(nodes[0]))
                verify_nodes(nodes=nodes[1:])

    # helper function that splits a single text TextNode by image and link
    # and assigns correct TextType TextNodes
    def split_text(node:TextNode) -> list:
        if node.text_type != TextType.TEXT:
            raise ValueError(f"Cannot split {node.text_type} type TextNode")
        
        node_text = node.text
        split_string = []
        nodes = []

        # splits the node text by images, includes the images in the list
        res = re.split(r"(\!\[.*?\]\(.*?\))", node_text)

        # splits each string in split_string by link, includes link       
        for x in res:
            split_string.extend(re.split(r"(?<!\!)(\[.*?\]\(.*?\))", x))

        nodes = to_TextNode(split_string)

        return nodes
    
    # helper function that converts each element of a list
    # into the correct TextType TextNode
    def to_TextNode(my_list):
        new_list = []

        for x in my_list:
            if not x:
                continue

            extracted_image = extract_markdown_images(x)
            extracted_link = extract_markdown_links(x)

            if extracted_image:
                new_list.append(TextNode(text=extracted_image[0][0], 
                                         text_type=TextType.IMAGE, 
                                         url=extracted_image[0][1]))
            elif extracted_link:
                new_list.append(TextNode(text=extracted_link[0][0],
                                         text_type=TextType.LINK,
                                         url=extracted_link[0][1]))
            else:
                new_list.append(TextNode(text=x, text_type=TextType.TEXT, 
                                         url=None))

        return new_list
    
    verify_nodes(old_nodes)
    return temp_list

# Takes a markdown-formatted string and returns a list of TextNodes 
# with appropriate types
def text_to_textnodes(text:str) -> list:
    temp_textnode = TextNode(text=text, text_type=TextType.TEXT, url=None)
    temp_list = [temp_textnode]
    # both split functions only accept lists as arguments, so we need to 
    # add our temporary textnode to a temporary list in order to pass it

    first_split = [split_text_TextNode_by_delimiter(temp_list)]
    second_split = sum([split_text_TextNode_by_image_or_link(x) 
                        for x in first_split], [])
    # the sum method is the easiest way to resolve an issue with nested lists

    return second_split
