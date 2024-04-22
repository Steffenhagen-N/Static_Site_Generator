import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):

    def test_equal(self):
        node = TextNode("This is a text node", "bold", "https://boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://boot.dev")
        self.assertEqual(node, node2)

    def test_different_text(self):
        node = TextNode("Sonic And Knuckles", "bold", "https://epicgamecubegames.com")
        node2 = TextNode("Super Mario Sunshine", "bold", "https://epicgamecubegames.com")
        self.assertEqual(node, node2)

    def test_different_styles(self):
        node = TextNode("Chungus", "bold", "https://chungus.com")
        node2 = TextNode("Chungus", "italic", "https://chungus.com")
        self.assertEqual(node, node2)

    def test_different_url(self):
        node = TextNode("My opinion on Obama", "underline", "https://alexjones.com")
        node2 = TextNode("My opinion on Obama", "underline", "https://soros.net")
        self.assertEqual(node, node2)

    def test_none_text(self):
        node = TextNode(None, "wingdings", "https://cnn.org")
        node2 = TextNode("I have information that will lead to the arrest of Hillary Clinton", "wingdings", "https://cnn.org")
        self.assertEqual(node, node2)

    def test_none_style(self):
        node = TextNode("Why Coldplay Sucks, 100 Reasons Why", None, "https://coldplayfangroup.com")
        node2 = TextNode("Why Coldplay Sucks, 100 Reasons Why", "upside down or whatever", "https://coldplayfangroup.com")
        self.assertEqual(node, node2)

    def test_none_url(self):
        node = TextNode("Pokemon 5 sucks", "bold", None)
        node2 = TextNode("Pokemon 5 sucks", "bold", "https://pokemon.com")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()