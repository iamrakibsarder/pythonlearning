def getTag (text, tag):
    """
    About Dynamic HTML TAG
    :param text: Enter text you want to show
    :param tag: Enter your tag
    :return: HTML value
    """
    html = f'<{tag}>{text}</{tag}>'
    return html

print(getTag("Hey this is me, Your Rakib", 'p'))
print(getTag("Is the OMI?", 'h2'))
print(getTag.__doc__)
