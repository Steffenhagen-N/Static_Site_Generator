import unittest

from textnode import TextNode
from constants import TextType
from htmlnode import HTMLNode, text_node_to_html_node, LeafNode, ParentNode

class TestTextToHTMLNode(unittest.TestCase):
    
    def test_text(self):
        texttext = TextNode("This is a text TextNode", TextType.TEXT, None)
        textHTML = text_node_to_html_node(texttext)
        print("Testing (1/6) text text_to_HTML")
        print(textHTML)
        print(textHTML.to_html())
        print("")

    def test_bold(self):
        boldtext = TextNode("This is a bold TextNode", "bold", None)
        boldHTML = text_node_to_html_node(boldtext)
        print("Testing (2/6) bold text_to_HTML")
        print(boldHTML)
        print(boldHTML.to_html())
        print("")

    def test_italic(self):
        italictext = TextNode("This is an italic TextNode", TextType.ITALIC, None)
        italicHTML = text_node_to_html_node(italictext)
        print("Testing (3/6) italic text_to_html")
        print(italicHTML)
        print(italicHTML.to_html())
        print("")

    def test_code(self):
        codetext = TextNode("This is a code TextNode", "code", None)
        codeHTML = text_node_to_html_node(codetext)
        print("Testing (4/6) code text_to_html")
        print(codeHTML)
        print(codeHTML.to_html())
        print("")

    def test_link(self):
         linktext = TextNode("This is a link TextNode", TextType.LINK, "https://www.boot.dev")
         linkHTML = text_node_to_html_node(linktext)
         print("Testing (5/6) link text_to_html")
         print(linkHTML)
         print(linkHTML.to_html())
         print("")

    def test_image(self):
        imagetext = TextNode("This is an image TextNode", "image", "imageURL")
        imageHTML = text_node_to_html_node(imagetext)
        print("Testing (6/6) image text_to_html")
        print(imageHTML)
        print(imageHTML.to_html())
        print("")

if __name__ == "__main__":
    unittest.main()