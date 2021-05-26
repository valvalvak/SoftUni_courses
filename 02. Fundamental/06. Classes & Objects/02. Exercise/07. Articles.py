class Article:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    # TODO changes the old content to the new one
    def edit(self, new_content):
        self.content = new_content

    # TODO changes the old author to with the new one
    def change_author(self, new_author):
        self.author = new_author

    # TODO changes the old title with the new one
    def rename(self, new_title):
        self.title = new_title

    # TODO returns the following string "{title} - {content}: {author}"
    def __repr__(self):
        return f"{self.title} - {self.content}: {self.author}"


article = Article("some title", "some content", "some author")
article.edit("new content")
article.rename("new title")
article.change_author("new author")
print(article)
