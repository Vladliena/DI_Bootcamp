from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Book, BookReview
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def list_books(request):
    all_books = Book.objects.all()
    book_list = []

    for book in all_books:
        book_data = {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "published_date": book.published_date,
            "description": book.description,
            "page_count": book.page_count,
            "categories": book.categories,
            "thumbnail_url": book.thumbnail_url,
        }
        book_list.append(book_data)
    return JsonResponse({"books": book_list})


def book_detail(request, book_id: int):
    try:
        books = Book.objects.get(id=book_id)
        content = {"Title": books.title, "Author": books.author}
        return JsonResponse(content)
    except Book.DoesNotExist:
        return JsonResponse("No such book")


@csrf_exempt
def create_book(request):
    if request.method == "POST":
        data = request.POST
        title = data.get("title")
        author = data.get("author")
        published_date = data.get("published_date")
        description = data.get("description")
        page_count = data.get("page_count")
        categories = data.get("categories")
        thumbnail_url = data.get("thumbnail_url")

        if (
            title
            and author
            and published_date
            and description
            and page_count
            and categories
        ):
            book = Book.objects.create(
                title=title,
                author=author,
                published_date=published_date,
                description=description,
                page_count=page_count,
                categories=categories,
                thumbnail_url=thumbnail_url,
            )
            response_data = {"message": "Book created successfully", "book_id": book.id}
            return JsonResponse(response_data)
        else:
            response_data = {"error": "Incomplete data provided"}
            return JsonResponse(response_data)
    else:
        response_data = {"error": "Invalid request method"}
        return JsonResponse(response_data)
