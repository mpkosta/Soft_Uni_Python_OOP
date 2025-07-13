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
                page_slot = len(page)
                return f"{label} photo added successfully on page {i + 1} slot {page_slot}"
        return "No more free slots"

    def display(self):
        result = []
        for page in self.photos:
            result.append("-----------")
            if page:
                result.append(" ".join("[]" for _ in page))
            else:
                result.append("")
        result.append("-----------")
        return "\n".join(result)
                

album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
