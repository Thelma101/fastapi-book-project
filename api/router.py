# from fastapi import APIRouter, HTTPException, status
# from api.routes import books
# from api.db.schemas import Book, Genre

# api_router = APIRouter()
# api_router.include_router(books.router, prefix="/books", tags=["books"])

# @api_router.get("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
# async def get_book(book_id: int):
#     if Book :
#         return Book
#     else :
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Book not found"
#         )



from fastapi import APIRouter, HTTPException, status
from api.routes import books
from api.db.schemas import Book

api_router = APIRouter()
api_router.include_router(books.router, prefix="/books", tags=["books"])

@api_router.get("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
async def get_book(book_id: int):
    book = books.db.get_book(book_id)
    if book:
        return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )
