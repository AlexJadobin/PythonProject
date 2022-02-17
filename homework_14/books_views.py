import json
import falcon
from waitress import serve
#from gunicorn import serve
from falcon import App, Request, Response, HTTP_201, HTTP_400, HTTP_404

BOOKS = {
    1: "Маугли",
    2: "Детство",
    3: "Каштанка",
    4: "Алые паруса",
}

class BooksListResours:
    def on_get(self, req: Request, res: Response):
        books_as_list = [
            {"id": book_id, "name": name}
            for book_id, name in BOOKS.items()
        ]
        res.text = json.dumps(books_as_list)

    def on_post(self, req: Request, res: Response):
        media: dict = req.get_media()
        data: dict = json.loads(media["data"])
        try:
            book_id = int(data["id"])
            book_name = data["name"]
        except (ValueError, KeyError):
            res.status = falcon.HTTP_400
            result = {"message": "bad request: recuired fields 'id' (int) and 'name' (str)"}
        else:
            if book_id in BOOKS:
                res.status = falcon.HTTP_400
                result = {"message": f"book with #{book_id} such id already exists"}
            else:
                BOOKS[book_id] = book_name
                res.status = falcon.HTTP_201
                result = {"id": book_id, "name": book_name}
                #res.text = json.dumps(result)
        res.media = result

class BookDetailsResource:
    def on_get(self, req: Request, res: Response, book_id: str):
        try:
            book_id = int(book_id)
            book_name = BOOKS[book_id]
        except (ValueError):
            res.status = falcon.HTTP_404
            result = {"message": f"not valid id {book_id!r}"}
        except (KeyError):
            res.status = falcon.HTTP_404
            result = {"message": f"book #{book_id!r} not found"}
        else:
            result = {"id": book_id, "name": book_name}
        res.text = json.dumps(result)

#books_list = BooksListResours()
#book_details = BookDetailsResource()

#app = App()
#app.add_route("/books", books_list)
#app.add_route("/books/{book_id}", book_details)

#serve(app, host='127.0.0.1', port=8000)

# http http://127.0.0.1:8000/books/1                    запуск запроса в терминале книги с id=1  - ОК!
# http http://127.0.0.1:8000/books/2                    запуск запроса в терминале книги с id=2  - ОК!
# http http://127.0.0.1:8000/books/3                    запуск запроса в терминале книги с id=3  - ОК!
# http http://127.0.0.1:8000/books/4

# для возможности активации виртуального окружения в среде PowerShell (запустить от Администратора) выполнить команду:
#     Set-ExecutionPolicy RemoteSigned
#     на запрос о потверждении ввести большую английскую букву "A"
#     после этого в терминале перед  путем к текущей рабочей папке выйдет в скобках слово venv  -   (venv)

# для выполнения ДЗ №9   в Терминале PyCharm установил
#    pip install falcon
#    pip install gunicorn   - но он у меня не заработал, так как предназначен для Unix
#    pip install waitress   - заработал, так как предназначен для Windows
#    pip install httpie		- для распознаваний команды  "http" в терминале PyCharm


#  перейти в папку урока №9:                            cd homework_09
#  выполнить команду активации виртуального окружения:  activate.ps1


#  Обеспечение запуска нашего app-приложения  в Терминале PyCharm
#  pip freeze > requirements.txt    заморозить версии ПО окружения
#  gunicorn books:app               в Unix
#  waitress-serve books:app         в Windows