import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        html_node = HTMLNode("h1", "This is an HTMLNode", [], {"href": "https://www.google.com", "target": "_blank"})
        print(html_node)
        print(html_node.props_to_html())
        print("")

    def test_LeafNode_no_value(self):
        pass

    def test_LeafNode_tag_value_props(self):
        pass

    def test_LeafNode_value_props(self):
        pass

    def test_LeafNode_tag_value(self):
        pass

    def test_repr_LeafNode(self):
        pass

if __name__ == "__main__":
    unittest.main()