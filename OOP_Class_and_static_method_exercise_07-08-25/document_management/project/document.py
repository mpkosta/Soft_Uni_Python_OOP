from project.category import Category
from project.topic import Topic


class Document:
    def __init__(self, doc_id: int, category_id: int, topic_id: int, file_name: str):
        self.id = doc_id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags: list[str] = []

    @classmethod
    def from_instances(cls, document_id: int, category: Category, topic: Topic, file_name: str):
        return cls(document_id, category.id, topic.id, file_name)

    def add_tag(self, tag_content: str) -> None:
        if tag_content not in self.tags:
            self.tags.append(tag_content)

    def remove_tag(self, tag_content: str) -> None:
        if tag_content in self.tags:
            self.tags.remove(tag_content)

    def edit(self, file_name: str) -> None:
        self.file_name = file_name

    def __repr__(self):
        return (f"Document {self.id}: {self.file_name}; category {self.category_id}, "
                f"topic {self.topic_id}, tags: {', '.join(self.tags)}")
