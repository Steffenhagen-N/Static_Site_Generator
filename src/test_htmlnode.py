import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        html_node = HTMLNode("h1", "This is an HTMLNode", [], {"href": "https://www.google.com", "target": "_blank"})
        print(html_node)
        print(html_node.props_to_html())

if __name__ == "__main__":
    unittest.main()