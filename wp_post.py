def wp_p(text, tag):
    text_description = f"<!-- wp:paragraph --><{tag}>{text}</{tag}><!-- /wp:paragraph -->"
    return text_description


def wp_heading (text, tag):
    text = f"<!-- wp:heading --><{tag}>{text}</{tag}<!-- /wp:heading -->"
    return text

