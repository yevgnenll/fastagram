from posts.models import Post


def find_tags(content):

    splited_content = [
        context.replace('#', '')
        for context
        in content.split(' ')
        if context.startswith('#')
    ]
    return splited_content
