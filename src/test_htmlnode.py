import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

#class TestHTMLNode(unittest.TestCase):

#    def test_props_to_html(self):
#        html_node = HTMLNode("h1", "This is an HTMLNode", [], {"href": "https://www.google.com", "target": "_blank"})
#        print("")
#        print("Testing HTMLNode props_to_HTML")
#        print(html_node)
#        print(html_node.props_to_html())
#        print("")

#    def test_LeafNode_no_value(self):
#        leaf = LeafNode("a", None, {"target": "_blank"})
#        print("")
#        print("Testing no_value LeafNode")
#        print(leaf.to_html())
#        print("")

#    def test_LeafNode_tag_value_props(self):
#        leaf = LeafNode("a", "This will successfully transform to HTML", {"href": "https://www.boot.dev", "maxlength": "50%"})
#        print("")
#        print("Testing full LeafNode to_HTML")
#        print(leaf.to_html())
#        print("")

#    def test_LeafNode_value_props(self):
#        leaf = LeafNode(None, "This will successfully transform to HTML", {"href": "https://www.boot.dev"})
#        print("")
#        print("Testing value, props LeafNode to_HTML")
#        print(leaf.to_html())
#        print("")

#    def test_LeafNode_tag_value(self):
#        leaf = LeafNode("a", "This will successfully transform to HTML", None)
#        print("")
#        print("Testing tag, value LeafNode to_HTML")
#        print(leaf.to_html())
#        print("")

#    def test_repr_LeafNode(self):
#        leaf = LeafNode("a", "This will successfully transform to HTML", {"href": "https://www.boot.dev"})
#        print("")
#        print("Testing repr LeafNode")
#        print(leaf)
#        print("")

class TestParentNode(unittest.TestCase):
    
    def test_ParentNode_tree_to_html(self):
        leaf1 = LeafNode("a", "my site", {"href": "www.boot.dev"})
        leaf2 = LeafNode("b", "MIND GOBLIN DEEZ NUTS LMAO GOTTEM", None)
        leaf3 = LeafNode(None, "Just some normal text", None)
        leaf4 = LeafNode("title", "What's a mind goblin?", None)
        leaf5 = LeafNode(None, "I ran out of text ideas", {"key": "value"})
        parent4 = ParentNode("s", [leaf3], None)
        parent3 = ParentNode("p", [leaf4, leaf2], None)
        parent2 = ParentNode("q", [leaf5, parent3], None)
        parent1 = ParentNode("r", [leaf1, parent2, parent4], {"style": "_bold"})

        print("")
        print("Testing ParentNode to_html")
        print(parent1.to_html())
        print("")

    def test_parent2(self):
        leaf1 = LeafNode("a", "my site", {"href": "www.boot.dev"})
        leaf2 = LeafNode("b", "MIND GOBLIN DEEZ NUTS LMAO GOTTEM", None)
        leaf3 = LeafNode(None, "Just some normal text", None)
        leaf4 = LeafNode("title", "What's a mind goblin?", None)
        leaf5 = LeafNode(None, "I ran out of text ideas", {"key": "value"})
        parent = ParentNode("p", [leaf1, leaf2, leaf3, leaf4, leaf5], None)

        print("")
        print(parent.to_html())

if __name__ == "__main__":
    unittest.main()