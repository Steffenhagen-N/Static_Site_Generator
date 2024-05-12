import unittest

from textnode import extract_markdown_images, extract_markdown_links

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

if __name__ == "__main__":
    unittest.main()