from enum import StrEnum, unique

# Plaintext list of supported markdown text types
# Must include all types also in sub-enumerations
@unique
class TextType(StrEnum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

# List of HTML tags that are self-closing
# Primarily used in text_node_to_html_node and LeafNode under htmlnode
# This list can be preemptively updated as it is only checked after TextType
@unique
class SelfClosedTag(StrEnum):
    IMAGE = "img"
    #BREAK = "br"
    #BASE = "base"
    #EMBED = "embed"
    #INPUT = "input"
