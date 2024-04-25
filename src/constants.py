from enum import StrEnum, unique

@unique
class TextType(StrEnum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

if "text" in TextType:
    print("true")