import unittest
from block_type import BlockType, BlockUtil
from textwrap import dedent

util = BlockUtil()

class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = dedent("""
            This is **bolded** paragraph

            This is another paragraph with __italic__ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
        """)
        print(repr(md))
        blocks = util.markdown_to_blocks(md)
        for block in blocks:
            print(repr(block))
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with __italic__ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ]
        )

    def test_paragraph(self):
        block = "This is a paragraph"
        self.assertEqual(util.block_to_block_type(block), BlockType.PARAGRAPH)

    def test_heading(self):
        block = "# This is a heading"
        self.assertEqual(util.block_to_block_type(block), BlockType.HEADING)

    def test_code(self):
        block = "```\nprint('hello')\n```"
        self.assertEqual(util.block_to_block_type(block), BlockType.CODE)

    def test_quote(self):
        block = "> quote line\n> another quote line"
        self.assertEqual(util.block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- item 1\n- item 2\n- item 3"
        self.assertEqual(util.block_to_block_type(block), BlockType.UO_LIST)

    def test_ordered_list(self):
        block = "1. item\n2. another item\n3. yet another item"
        self.assertEqual(util.block_to_block_type(block), BlockType.O_LIST)

    def test_paragraph(self):
        md = dedent("""
            This is **bolded** paragraph
            text in a p
            tag here

        """)

        node = util.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = dedent("""
            This is **bolded** paragraph
            text in a p
            tag here

            This is another paragraph with __italic__ text and `code` here

        """)

        node = util.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = dedent("""
            - This is a list
            - with items
            - and __more__ items

            1. This is an `ordered` list
            2. with items
            3. and more items

        """)

        node = util.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = dedent("""
            # this is an h1

            this is paragraph text

            ## this is an h2
        """)

        node = util.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = dedent("""
            > This is a
            > blockquote block

            this is paragraph text

        """)

        node = util.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_code(self):
        md = dedent("""
            ```
            This is text that __should__ remain
            the **same** even with inline stuff
            ```
        """)

        node = util.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that __should__ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

if __name__ == "__main__":
    unittest.main()

