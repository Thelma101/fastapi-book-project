# from typing import OrderedDict
# from collections import OrderedDict
# from typing import List

# from fastapi import APIRouter, status, HTTPException
# from fastapi.responses import JSONResponse

# from api.db.schemas import Book, Genre, InMemoryDB

# router = APIRouter()

# db = InMemoryDB()
# db.books = {
#     1: Book(
#         id=1,
#         title="The Hobbit",
#         author="J.R.R. Tolkien",
#         publication_year=1937,
#         genre=Genre.SCI_FI,
#     ),
#     2: Book(
#         id=2,
#         title="The Lord of the Rings",
#         author="J.R.R. Tolkien",
#         publication_year=1954,
#         genre=Genre.FANTASY,
#     ),
#     3: Book(
#         id=3,
#         title="The Return of the King",
#         author="J.R.R. Tolkien",
#         publication_year=1955,
#         genre=Genre.FANTASY,
#     ),
# }

# # Add the get_book method to the InMemoryDB class
# class InMemoryDB:
#     def __init__(self):
#         self.books = {}

#     def add_book(self, book: Book):
#         self.books[book.id] = book

#     def get_book(self, book_id: int) -> Book | None:
#         return self.books.get(book_id)

#     def get_books(self) -> OrderedDict[int, Book]:
#         return OrderedDict(sorted(self.books.items()))

#     def update_book(self, book_id: int, book: Book) -> Book:
#         if book_id in self.books:
#             self.books[book_id] = book
#             return book
#         else:
#             raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 detail="Book not found"
#             )

#     def delete_book(self, book_id: int) -> None:
#         if book_id in self.books:
#             del self.books[book_id]
#         else:
#             raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 detail="Book not found"
#             )

# @router.post("/", status_code=status.HTTP_201_CREATED)
# async def create_book(book: Book):
#     db.add_book(book)
#     return JSONResponse(
#         status_code=status.HTTP_201_CREATED, content=book.model_dump()
#     )

# @router.get(
#     "/", response_model=OrderedDict[int, Book], status_code=status.HTTP_200_OK
# )
# async def get_books() -> OrderedDict[int, Book]:
#     return db.get_books()

# @router.get("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
# async def get_book(book_id: int) -> Book:
#     book = db.get_book(book_id)
#     if book:
#         return book
#     else:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Book not found"
#         )

# @router.put("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
# async def update_book(book_id: int, book: Book) -> Book:
#     return JSONResponse(
#         status_code=status.HTTP_200_OK,
#         content=db.update_book(book_id, book).model_dump(),
#     )

# @router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_book(book_id: int) -> None:
#     db.delete_book(book_id)
#     return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=None)

# # from typing import OrderedDict

# # from fastapi import APIRouter, status
# # from fastapi.responses import JSONResponse

# # from api.db.schemas import Book, Genre, InMemoryDB

# # router = APIRouter()

# # db = InMemoryDB()
# # db.books = {
# #     1: Book(
# #         id=1,
# #         title="The Hobbit",
# #         author="J.R.R. Tolkien",
# #         publication_year=1937,
# #         genre=Genre.SCI_FI,
# #     ),
# #     2: Book(
# #         id=2,
# #         title="The Lord of the Rings",
# #         author="J.R.R. Tolkien",
# #         publication_year=1954,
# #         genre=Genre.FANTASY,
# #     ),
# #     3: Book(
# #         id=3,
# #         title="The Return of the King",
# #         author="J.R.R. Tolkien",
# #         publication_year=1955,
# #         genre=Genre.FANTASY,
# #     ),
# # }


# # @router.post("/", status_code=status.HTTP_201_CREATED)
# # async def create_book(book: Book):
# #     db.add_book(book)
# #     return JSONResponse(
# #         status_code=status.HTTP_201_CREATED, content=book.model_dump()
# #     )


# # # @router.get(
# # #     "/", response_model=OrderedDict[int, Book], status_code=status.HTTP_200_OK
# # # )
# # # async def get_books() -> OrderedDict[int, Book]:
# # #     return db.get_books()

# # @router.get("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
# # async def get_book(book_id: int):
# #     book = db.books.get(book_id)
# #     if not book:
# #         raise HTTPException(status_code=404, detail="Book not found")
# #     return book.dict()

# # @router.put("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
# # async def update_book(book_id: int, book: Book) -> Book:
# #     return JSONResponse(
# #         status_code=status.HTTP_200_OK,
# #         content=db.update_book(book_id, book).model_dump(),
# #     )


# # @router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
# # async def delete_book(book_id: int) -> None:
# #     db.delete_book(book_id)
# #     return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=None)



from collections import OrderedDict
from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse

from api.db.schemas import Book, Genre

router = APIRouter()

class InMemoryDB:
    def __init__(self):
        self.books = {}

    def add_book(self, book: Book):
        self.books[book.id] = book

    def get_book(self, book_id: int):
        return self.books.get(book_id)

    def get_books(self):
        return OrderedDict(sorted(self.books.items()))  # Fixed missing parenthesis

    def update_book(self, book_id: int, book: Book):
        if book_id in self.books:
            self.books[book_id] = book
            return book
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )

    def delete_book(self, book_id: int):
        if book_id in self.books:
            del self.books[book_id]
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found"
            )

db = InMemoryDB()
db.books = {
    1: Book(
        id=1,
        title="The Hobbit",
        author="J.R.R. Tolkien",
        publication_year=1937,
        genre=Genre.SCI_FI,
    ),
    2: Book(
        id=2,
        title="The Lord of the Rings",
        author="J.R.R. Tolkien",
        publication_year=1954,
        genre=Genre.FANTASY,
    ),
    3: Book(
        id=3,
        title="The Return of the King",
        author="J.R.R. Tolkien",
        publication_year=1955,
        genre=Genre.FANTASY,
    ),
}

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    db.add_book(book)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED, content=book.model_dump()
    )

@router.get("/", response_model=dict[int, Book], status_code=status.HTTP_200_OK)
async def get_books():
    return db.get_books()

@router.get("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
async def get_book(book_id: int):
    book = db.get_book(book_id)
    if book:
        return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )

@router.put("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
async def update_book(book_id: int, book: Book):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=db.update_book(book_id, book).model_dump(),
    )

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    db.delete_book(book_id)
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=None)
