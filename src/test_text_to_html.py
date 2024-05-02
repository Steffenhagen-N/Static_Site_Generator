import unittest

from textnode import TextNode
from constants import TextType
from htmlnode import HTMLNode, text_node_to_html_node, LeafNode, ParentNode

class TestTextToHTMLNode(unittest.TestCase):
    
    def test_text(self):
        texttext = TextNode("This is a text TextNode", TextType.TEXT, None)
        textHTML = text_node_to_html_node(texttext)
        print("Testing text text_to_HTML")
        print(textHTML)
        print(textHTML.to_html())

    def test_bold(self):
        boldtext = TextNode("This is a bold TextNode", "bold", None)
        boldHTML = text_node_to_html_node(boldtext)
        print("Testing bold text_to_HTML")
        print(boldHTML)
        print(boldHTML.to_html())

    def test_italic(self):
        italictext = TextNode("This is an italic TextNode", TextType.ITALIC, None)
        italicHTML = text_node_to_html_node(italictext)
        print("Testing italic text_to_html")
        print(italicHTML)
        print(italicHTML.to_html())

    def test_code(self):
        codetext = TextNode("This is a code TextNode", "code", None)
        codeHTML = text_node_to_html_node(codetext)
        print("Testing code text_to_html")
        print(codeHTML)
        print(codeHTML.to_html())

    def test_link(self):
         linktext = TextNode("This is a link TextNode", TextType.LINK, "https://www.boot.dev")
         linkHTML = text_node_to_html_node(linktext)
         print("Testing link text_to_html")
         print(linkHTML)
         print(linkHTML.to_html())

    def test_image(self):
        imagetext = TextNode("This is an image TextNode", "image", "imageURL")
        imageHTML = text_node_to_html_node(imagetext)
        print("Testing image text_to_html")
        print(imageHTML)
        print(imageHTML.to_html())

    def test_falselink(self):
         falselinktext = TextNode("This is an incomplete link TextNode", "link", None)
         falselinkHTML = text_node_to_html_node(falselinktext)
         print("Testing false link text_to_html")
         return falselinkHTML.to_html()

    def test_falseimage1(self):
         falseimagetext1 = TextNode("This is an incomplete image TextNode", TextType.IMAGE, None)
         falseimageHTML1 = text_node_to_html_node(falseimagetext1)
         print("Testing false image 1 text_to_html")
         return falseimageHTML1.to_html()

    def test_falseimage2(self):
        falseimagetext2 = TextNode(None, "image", "imageurl")
        falseimageHTML2 = text_node_to_html_node(falseimagetext2)
        print("Testing false image 2 text_to_html")
        return falseimageHTML2.to_html()

    def test_falsetype(self):
        falsetexttype = TextNode("This is an illegal text type TextNode", "underline", None)
        falsetexttypeHTML = text_node_to_html_node(falsetexttype)
        print("Testing illegal type text_to_html")
        return falsetexttypeHTML.to_html()

if __name__ == "__main__":
    unittest.main()