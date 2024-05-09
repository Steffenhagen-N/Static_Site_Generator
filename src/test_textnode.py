import unittest

from textnode import TextNode, split_text_TextNode
from constants import TextType

class TestTextNode(unittest.TestCase):

    # This is correct
    def test_notext(self):
        code = TextNode(text="print('hello world')", 
                        text_type=TextType.CODE, url=None)
        italic = TextNode(text="Italic text", 
                          text_type=TextType.ITALIC, url=None)
        bold = TextNode(text="Bold text", 
                        text_type=TextType.BOLD, url=None)
        link = TextNode(text="This is a link", 
                        text_type=TextType.LINK, url="https://www.boot.dev")
        image = TextNode(text="This is an image", 
                         text_type=TextType.IMAGE, url="Image link")
        mylist = [code, italic, bold, link, image]

        print("")
        print("Testing notext splitting...")
        print("Original list:")
        print(mylist)
        print("")
        print("Splitting list...")
        print(split_text_TextNode(mylist))
        print("")

    # This is correct
    def test_nodelim(self):
        code = TextNode(text='print("hello world")', 
                        text_type=TextType.CODE, url=None)
        italic = TextNode(text="Italic text", 
                          text_type=TextType.ITALIC, url=None)
        bold = TextNode(text="Bold text", 
                        text_type=TextType.BOLD, url=None)
        text = TextNode(text="This is a text TextNode", 
                    text_type=TextType.TEXT, url=None)
        mylist = [code, italic, bold, text]

        print("")
        print("Testing nodelim splitting...")
        print("Original list:")
        print(mylist)
        print("")
        print("Splitting list...")
        print(split_text_TextNode(mylist))
        print("")

    # Splitting and assigning correctly
    # Empty text TextNodes are being added on either side of allitalictext
    #
    #
    # Empty strings are filtered() from the list of strings after being split
    # This works now
    def test_italic_delim(self):
        allitalictext = TextNode(text="*All of this text is italic*", 
                             text_type=TextType.TEXT, url=None)
        italictext = TextNode(text="This string will have one *italic* word!", 
                          text_type=TextType.TEXT, url=None)
        mylist = [allitalictext, italictext]

        print("")
        print("Testing italic splitting...")
        print("Original list:")
        print(mylist)
        print("")
        print("Splitting list...")
        print(split_text_TextNode(mylist))
        print("")

    # Returning error "Nested delimiter not allowed"
    #
    # 
    # I don't know what the fuck I did but it works now
    # Something with negative lookahead and lookback assertions and 
    # using + instead of *
    # This works now
    def test_bold_delim(self):
        allboldtext = TextNode(text="**All of this text is bold**", 
                           text_type=TextType.TEXT, url=None)
        boldtext = TextNode(text="This string will have one **bolded** word!", 
                        text_type=TextType.TEXT, url=None)
        mylist = [allboldtext, boldtext]

        print("")
        print("Testing bold splitting...")
        print("Original list:")
        print(mylist)
        print("")
        print("Splitting list...")
        print(split_text_TextNode(mylist))
        print("")

    # Splitting correctly, but text is not being applied to code TextNode
    # Nodes are listed out of order
    # Maybe has something to do with how it interprets "" inside code?
    # Try forcing string with '''string'''
    #
    #
    # Solved false ordering by adding an including () in regex
    # Now empty text TextNodes are being added on either side of 
    # full code TextNode, similar to full bold issue...
    #
    #
    # Solved by filtering out empty strings
    def test_code_delim(self):
        allcodetext = TextNode(text="`All of this text is code`", 
                           text_type=TextType.TEXT, url=None)
        codetext = TextNode(text="This string will have one `code` word!", 
                        text_type=TextType.TEXT, url=None)
        mylist = [allcodetext, codetext]

        print("")
        print("Testing code splitting...")
        print("Original list:")
        print(mylist)
        print("")
        print("Splitting list...")
        print(split_text_TextNode(mylist))
        print("")

    # This works    
    def test_bold_italic(self):
        with self.assertRaises(SyntaxError):
            bolditalic = TextNode(text="***This text is very emphasized***", 
                              text_type=TextType.TEXT, url=None)
            mylist = [bolditalic]

            print("")
            print("Testing bold and italic splitting...")
            print("Original list:")
            print(mylist)
            print("")
            print("Splitting list...")
            print(split_text_TextNode(mylist))
            print("")

    # This works, but is remaining to retest bold
    #
    #
    # Unclosed bold works now too
    # This works
    def test_unclosed_italic(self):
        with self.assertRaises(SyntaxError):
            uncloseditalic = TextNode(text="This *italic isn't closed!", 
                                  text_type=TextType.TEXT, url=None)
            italictext = TextNode(text="This string will have one *italic* word!", 
                              text_type=TextType.TEXT, url=None)
            mylist = [uncloseditalic, italictext]

            print("")
            print("Testing unclosed italic splitting...")
            print("Original list:")
            print(mylist)
            print("")
            print("Splitting list...")
            print(split_text_TextNode(mylist))
            print("")

    # This is sending the unclosed italic error message, fix the regex :(
    #
    #
    # When checking for italic delimiters, I was only checking that no *'s
    # came after an asterisk
    # This lead to the program counting all bold delimiters as having
    # an italic asterisk at the end
    # Added a negative lookback assertion to the regex (?<!\*)
    # This works now
    def test_unclosed_bold(self):
        with self.assertRaises(SyntaxError):
            unclosedbold = TextNode(text="This **bold isn't closed!", 
                                text_type=TextType.TEXT, url=None)
            boldtext = TextNode(text="This string will have one **bolded** word!", 
                            text_type=TextType.TEXT, url=None)
            mylist = [unclosedbold, boldtext]
        
            print("")
            print("Testing unclosed bold splitting...")
            print("Original list:")
            print(mylist)
            print("")
            print("Splitting list...")
            print(split_text_TextNode(mylist))
            print("")

    # This works
    def test_unclosed_code(self):
        with self.assertRaises(SyntaxError):
            unclosedcode = TextNode(text="This `code isn't closed!", 
                                text_type=TextType.TEXT, url=None)
            codetext = TextNode(text="This string will have one `code` word!", 
                            text_type=TextType.TEXT, url=None)
            mylist = [unclosedcode, codetext]

            print("")
            print("Testing unclosed code splitting...")
            print("Original list:")
            print(mylist)
            print("")
            print("Splitting list...")
            print(split_text_TextNode(mylist))
            print("")
    
    # This works
    def test_bold_in_italic(self):
        with self.assertRaises(SyntaxError):
            nestedbold = TextNode(text="This node *has some **bold** inside italic*", 
                              text_type=TextType.TEXT, url=None)
            mylist = [nestedbold]

            print("")
            print("Testing bold in italic splitting...")
            print("Original list:")
            print(mylist)
            print("")
            print("Splitting list...")
            print(split_text_TextNode(mylist))
            print("")

    # This works
    def test_bold_in_code(self):
        with self.assertRaises(SyntaxError):
            nestedbold = TextNode(text="This node `has some **bold** inside code`", 
                                  text_type=TextType.TEXT, url=None)
            mylist = [nestedbold]

            print("")
            print("Testing bold in code splitting...")
            print("Original list:")
            print(mylist)
            print("")
            print("Splitting list...")
            print(split_text_TextNode(mylist))
            print("")
    
    # Not returning an error?
    # Somehow recognizing "**" as its own empty bold TextNode???
    # Perhapse this is what's wrong with all the bold nodes...
    #
    #
    # Works now I guess
    def test_italic_in_bold(self):
        with self.assertRaises(SyntaxError):
            nesteditalic = TextNode(text="This node **has some *italic* inside bold**", 
                                text_type=TextType.TEXT, url=None)
            mylist = [nesteditalic]

            print("")
            print("Testing italic in bold splitting...")
            print("Original list:")
            print(mylist)
            print("")
            print("Splitting list...")
            print(split_text_TextNode(mylist))
            print("")

    # This works
    def test_italic_in_code(self):
        with self.assertRaises(SyntaxError):
            nesteditalic = TextNode(text="This node `has some *italic* in code`", 
                                    text_type=TextType.TEXT, url=None)
            mylist = [nesteditalic]

            print("")
            print("Testing italic in code splitting...")
            print("Original list:")
            print(mylist)
            print("")
            print("Splitting list...")
            print(split_text_TextNode(mylist))
            print("")

    # This works
    def test_code_in_italic(self):
        with self.assertRaises(SyntaxError):
            nestedcode = TextNode(text="This node *has some `code` inside italic*", 
                              text_type=TextType.TEXT, url=None)
            mylist = [nestedcode]

            print("")
            print("Testing code in italic splitting...")
            print("Original list:")
            print(mylist)
            print("")
            print("Splitting list...")
            print(split_text_TextNode(mylist))
            print("")

    # This works
    def test_code_in_bold(self):
        with self.assertRaises(SyntaxError):
            nestedcode = TextNode(text="This node **has some `code` in bold**", 
                                  text_type=TextType.TEXT, url=None)
            mylist = [nestedcode]

            print("")
            print("Testing code in bold splitting...")
            print("Original list:")
            print(mylist)
            print("")
            print("Splitting list...")
            print(split_text_TextNode(mylist))
            print("")

    # Returning nested delims not allowed error...
    # Possibly related to how bold is being mistreated
    #
    #
    # Same with bold, this works now because why not
    # God I love regex it's so intuitive and easy to use
    # This works now
    def test_all_three(self):
        alldelimiters = TextNode(text="This node has *italic* **bold** and `code` text", 
                             text_type=TextType.TEXT, url=None)
        mylist = [alldelimiters]

        print("")
        print("Testing all delimiter splitting...")
        print("Original list:")
        print(mylist)
        print("")
        print("Splitting list...")
        print(split_text_TextNode(mylist))
        print("")

if __name__ == "__main__":
    unittest.main()