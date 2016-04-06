def shrink_text(text):

    text_size = len(text)

    if text_size <= 15:
        return text
    else:
        return text[0:15]
