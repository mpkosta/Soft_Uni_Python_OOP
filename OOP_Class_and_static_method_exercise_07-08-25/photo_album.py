from math import ceil

class PhotoAlbum:
    PAGE_PHOTO_LIMIT = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: list[list[str]] = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PAGE_PHOTO_LIMIT))

    def add_photo(self, label: str):
        for i, page in enumerate(self.photos):
            if len(page) < self.PAGE_PHOTO_LIMIT:
                page.append(label)
                

