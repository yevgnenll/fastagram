from tags.models import Tag


def find_tags(content):

    splited_content = [
        context.replace('#', '')
        for context
        in content.split(' ')
        if context.startswith('#')
    ]
    return splited_content


def wrrap_link_node(content):

    with_sharp = find_tags(content)
    content_split = content.split(' ')

    result_content = []

    for word in content_split:
        if word in ["#{tag_name}".format(tag_name=tag) for tag in with_sharp]:
            word = "<a href='{tag_url}'>{tag_name}</a>".format(
                tag_url=Tag.objects.get(name=word.replace('#', '')).get_absolute_url(),
                tag_name=word,
            )
        result_content.append(word)
    return " ".join(result_content)
