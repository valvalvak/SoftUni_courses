class Document:
    def __init__(self, id: int, category_id: int, topic_id: int, file_name: str):
        self.id = id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = list()

    def form_instance(self):
        pass

    def add_tag(self):
        pass

    def remove_tag(self):
        pass

    def edit(self):
        pass

    def __repr__(self):
        """returns a string representation of a document in the format"""
        return "Document {id}: {file_name}; category {category_id}, topic {topic_id}, tags: {tags joined by comma and space)}"
