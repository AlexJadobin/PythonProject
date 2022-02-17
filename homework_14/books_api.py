from falcon import App
from timing_middleware import TimingMiddleware
from books_views import BooksListResours, BookDetailsResource

middlewares = [
    TimingMiddleware(),
]

books_list = BooksListResours()
book_details = BookDetailsResource()


app = App(middleware = middlewares)
app.add_route("/books", books_list)
app.add_route("/books/{book_id}", book_details)
