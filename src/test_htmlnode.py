import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        html_node = HTMLNode("h1", "This is an HTMLNode", [], {"href": "https://www.google.com", "target": "_blank"})
        print("")
        print("Testing HTMLNode props_to_HTML")
        print(html_node)
        print(html_node.props_to_html())
        print("")

    def test_LeafNode_no_value(self):
        leaf = LeafNode("a", None, {"target": "_blank"})
        print("")
        print("Testing no_value LeafNode")
        print(leaf.to_html())
        print("")

    def test_LeafNode_tag_value_props(self):
        leaf = LeafNode("a", "This will successfully transform to HTML", {"href": "https://www.boot.dev", "maxlength": "50%"})
        print("")
        print("Testing full LeafNode to_HTML")
        print(leaf.to_html())
        print("")

    def test_LeafNode_value_props(self):
        leaf = LeafNode(None, "This will successfully transform to HTML", {"href": "https://www.boot.dev"})
        print("")
        print("Testing value, props LeafNode to_HTML")
        print(leaf.to_html())
        print("")

    def test_LeafNode_tag_value(self):
        leaf = LeafNode("a", "This will successfully transform to HTML", None)
        print("")
        print("Testing tag, value LeafNode to_HTML")
        print(leaf.to_html())
        print("")

    def test_repr_LeafNode(self):
        leaf = LeafNode("a", "This will successfully transform to HTML", {"href": "https://www.boot.dev"})
        print("")
        print("Testing repr LeafNode")
        print(leaf)
        print("")

class TestParentNode(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()