from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    @staticmethod
    def is_obj_in_list(obj_target, obj_list):
        return any([obj for obj in obj_list if obj == obj_target])

    @staticmethod
    def get_obj(obj_target, obj_list):
        obj = [obj for obj in obj_list if obj == obj_target]
        return obj[0]

    @staticmethod
    def is_id(target_id, obj_list):
        return any([_is_id for _is_id in obj_list if _is_id.id == target_id])

    @staticmethod
    def get_id(target_id, obj_list):
        _is_id = [_is_id for _is_id in obj_list if _is_id.id == target_id]
        return _is_id[0]

    def add_category(self, category: Category):
        if not self.is_obj_in_list(category, self.categories):
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if not self.is_obj_in_list(topic, self.topics):
            self.topics.append(topic)

    def add_document(self, document: Document):
        if not self.is_obj_in_list(document, self.topics):
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        if self.is_id(category_id, self.categories):
            category = self.get_id(category_id, self.categories)
            category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        if self.is_id(topic_id, self.topics):
            topic = self.get_id(topic_id, self.topics)
            topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        if self.is_id(document_id, self.documents):
            document = self.get_id(document_id, self.documents)
            document.edit(new_file_name)

    def delete_category(self, category_id):
        if self.is_id(category_id, self.categories):
            category = self.get_id(category_id, self.categories)
            self.categories.remove(category)

    def delete_topic(self, topic_id):
        if self.is_id(topic_id, self.topics):
            topic = self.get_id(topic_id, self.topics)
            self.topics.remove(topic)

    def delete_document(self, document_id):
        if self.is_id(document_id, self.documents):
            document = self.get_id(document_id, self.documents)
            self.documents.remove(document)

    def get_document(self, document_id):
        if self.is_id(document_id, self.documents):
            document = self.get_id(document_id, self.documents)
            return document

    def __repr__(self):
        res = "\n".join([f"{doc_obj}" for doc_obj in self.documents])
        return res
