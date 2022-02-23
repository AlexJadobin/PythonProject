from falcon import App
from kombu import Connection
import config
from stat_middleware import StatMiddleware
from timing_middleware import TimingMiddleware
from books_views import BooksListResours, BookDetailsResource

connection = Connection(config.AMQP_CONNECTION_URL)
stats_middleware = StatMiddleware(
    connection=connection,
    queue_name=config.STAT_QUEUE_NAME,
)
middlewares =[
    stats_middleware,
    TimingMiddleware(),
]

books_list = BooksListResours()
book_details = BookDetailsResource()

app = App(middleware = middlewares)
app.add_route("/books", books_list)
app.add_route("/books/{book_id}", book_details)
