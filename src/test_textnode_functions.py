import unittest

from textnode import TextNode, TextType, extract_markdown_images, extract_markdown_links, split_text_TextNode_by_image_or_link

class TestExtractMDImage(unittest.TestCase):

    def test_all_image(self):
        text = "![a picture of your mom](link.fat.org/abcde.png)"
        my_images = extract_markdown_images(text)

        print("")
        print("Extracting image from string:")
        print(text)
        print("")
        print("Image(s):")
        print(my_images)
        print("")

    def test_noimage(self):
        text = "There is no image in this string"
        my_images = extract_markdown_images(text)

        print("")
        print("Extracting image from string:")
        print(text)
        print("")
        print("Image(s):")
        print(my_images)
        print("")

    def test_no_exclamation(self):
        text = "This image is formatted wrong [oopsie daisies!](link.none/qrstu.png)"
        my_images = extract_markdown_images(text)

        print("")
        print("Extracting image from string:")
        print(text)
        print("")
        print("Image(s):")
        print(my_images)
        print("")

    def test_empty_url(self):
        text = "I forgot the URL for this one :( ![no link]()"
        my_images = extract_markdown_images(text)

        print("")
        print("Extracting image from string:")
        print(text)
        print("")
        print("Image(s):")
        print(my_images)
        print("")

    def test_empty_alt_text(self):
        text = "This image has no alt text ![](butts.org/bigone.png)"
        my_images = extract_markdown_images(text)

        print("")
        print("Extracting image from string:")
        print(text)
        print("")
        print("Image(s):")
        print(my_images)
        print("")

    def test_has_image(self):
        text = "This should be captured correctly ![beautiful person](you.selfie/secret-folder.png) so don't worry"
        my_images = extract_markdown_images(text)

        print("")
        print("Extracting image from string:")
        print(text)
        print("")
        print("Image(s):")
        print(my_images)
        print("")

    def test_two_image(self):
        text = "This has two images in it! The first is ![a bunny](bonny.butt/wiki-for-bunnies.png) and the second is ![a turtle!](turtle.shell/reptiles.png) they're so cute"
        my_images = extract_markdown_images(text)

        print("")
        print("Extracting image from string:")
        print(text)
        print("")
        print("Image(s):")
        print(my_images)
        print("")

    def test_extra_text(self):
        text = "This is how to not format an image ![bad boy] you can't have extra text in the middle before the (url.link/your-mom.png)"
        my_images = extract_markdown_images(text)

        print("")
        print("Extracting image from string:")
        print(text)
        print("")
        print("Image(s):")
        print(my_images)
        print("")

    def test_nested_brackets(self):
        text = "This image is a little complicated... ![because there are ![brackets] inside the alt code](image.link/farts.png)"
        my_images = extract_markdown_images(text)

        print("")
        print("Extracting image from string:")
        print(text)
        print("")
        print("Image(s):")
        print(my_images)
        print("")

    def test_nested_image(self):
        text = "This image has an image in the alt text... ![Look at this cool ![image](my.image.png) that I found!](image.link/c.drive.png)"
        my_images = extract_markdown_images(text)

        print("")
        print("Extracting image from string:")
        print(text)
        print("")
        print("Image(s):")
        print(my_images)
        print("")
    
class TestExtractMDLink(unittest.TestCase):

    def test_all_link(self):
        text = "[This is a link to a secret place](link.FBI-Hit-List.org)"
        my_link = extract_markdown_links(text)

        print("")
        print("Extracting link from string:")
        print(text)
        print("")
        print("Link(s):")
        print(my_link)
        print("")

    def test_nolink(self):
        text = "There is no link in this string"
        my_link = extract_markdown_links(text)

        print("")
        print("Extracting link from string:")
        print(text)
        print("")
        print("Link(s):")
        print(my_link)
        print("")

    def test_empty_url(self):
        text = "I forgot the URL for this one :( [no link]()"
        my_link= extract_markdown_links(text)

        print("")
        print("Extracting link from string:")
        print(text)
        print("")
        print("Link(s):")
        print(my_link)
        print("")

    def test_empty_anchor_text(self):
        text = "This link has no anchor text [](butts.org)"
        my_link = extract_markdown_links(text)

        print("")
        print("Extracting link from string:")
        print(text)
        print("")
        print("Link(s):")
        print(my_link)
        print("")

    def test_has_link(self):
        text = "This should be captured correctly [beautiful person](you.selfie.com) so don't worry"
        my_link = extract_markdown_links(text)

        print("")
        print("Extracting link from string:")
        print(text)
        print("")
        print("Link(s):")
        print(my_link)
        print("")

    def test_two_links(self):
        text = "This has two links in it! The first is [to the White House's private wifi](white.house) and the second is [to your mom's house](i'm-banging-ur-mom.com)."
        my_link = extract_markdown_links(text)

        print("")
        print("Extracting link from string:")
        print(text)
        print("")
        print("Link(s):")
        print(my_link)
        print("")

    def test_extra_text(self):
        text = "This is how to not format a link [you buffoon] you can't have extra text in the middle before the (url.link)"
        my_link = extract_markdown_links(text)

        print("")
        print("Extracting link from string:")
        print(text)
        print("")
        print("Link(s):")
        print(my_link)
        print("")

    def test_nested_brackets(self):
        text = "This link is a little complicated... [because there are [brackets] inside the anchor text](fancy-pants.org)"
        my_link = extract_markdown_links(text)

        print("")
        print("Extracting link from string:")
        print(text)
        print("")
        print("Links(s):")
        print(my_link)
        print("")

    def test_nested_link(self):
        text = "This link has another link in the anchor text... [Look at this cool [link](link.url) that I found!](CIA.org)"
        my_link = extract_markdown_links(text)

        print("")
        print("Extracting link from string:")
        print(text)
        print("")
        print("Link(s):")
        print(my_link)
        print("")

    def test_on_image(self):
        text = "This is an image and should not be captured ![this is an image not a link](you.selfie.com/ur-butt.png)"
        my_link = extract_markdown_links(text)

        print("")
        print("Extracting link from string:")
        print(text)
        print("")
        print("Link(s):")
        print(my_link)
        print("")

class TestSplitImageLinkTextnode(unittest.TestCase):

    def test_notext(self):
        my_image = TextNode("a bunny", TextType.IMAGE, "bunny.png")
        my_bold = TextNode("I like bunnies", TextType.BOLD, None)
        my_italic = TextNode("Especially baby ones", TextType.ITALIC, None)
        my_nodes = [my_bold, my_image, my_italic]

        print("")
        print("Testing splitting " "\033[36m" "no text" "\033[0m" "...")
        print("Original list:")
        print(my_nodes)
        print("")
        print("Splitting...")
        print(split_text_TextNode_by_image_or_link(my_nodes))

    def test_empty_text(self):
        my_text = TextNode("", TextType.TEXT, None)
        my_text2 = TextNode(None, TextType.TEXT, None)
        my_nodes = [my_text, my_text2]

        print("")
        print("Testing splitting " "\033[36m" "empty text" "\033[0m" "...")
        print("Original list:")
        print(my_nodes)
        print("")
        print("Splitting...")
        print(split_text_TextNode_by_image_or_link(my_nodes))

    def test_images(self):
        my_text = TextNode("Image 1: ![I wish I was dead](urmom.png) Image 2: ![I sure hope this works](nohope.png)", TextType.TEXT, None)
        my_text2 = TextNode("![This is a single image](urmom.com/selfie.png)", TextType.TEXT, None)
        my_nodes = [my_text, my_text2]

        print("")
        print("Testing splitting " "\033[36m" "images" "\033[0m" "...")
        print("Original list:")
        print(my_nodes)
        print("")
        print("Splitting...")
        print(split_text_TextNode_by_image_or_link(my_nodes))
        
    def test_links(self):
        my_text = TextNode("Here's a link to [my website](www.boot.dev) that I made all by myself", TextType.TEXT, None)
        my_text2 = TextNode("[This is a single link](my_link.butts)", TextType.TEXT, None)
        my_nodes = [my_text, my_text2]

        print("")
        print("Testing splitting " "\033[36m" "links" "\033[0m" "...")
        print("Original list:")
        print(my_nodes)
        print("")
        print("Splitting...")
        print(split_text_TextNode_by_image_or_link(my_nodes))

    def test_both_in_string(self):
        my_text = TextNode("first we have an ![image](image.url.png), and then a [link](my.link.com) surrounded by text!", TextType.TEXT, None)
        my_text2 = TextNode("first we have a [link](my.link.com), and then an ![image](image.url.png) surrounded by text!", TextType.TEXT, None)
        my_nodes = [my_text, my_text2]

        print("")
        print("Testing splitting " "\033[36m" "links and images at the same time" "\033[0m" "...")
        print("Original list:")
        print(my_nodes)
        print("")
        print("Splitting...")
        print(split_text_TextNode_by_image_or_link(my_nodes))

if __name__ == "__main__":
    unittest.main()