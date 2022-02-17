import logging
# from waitress import serve
from books_api import app
logging.basicConfig(level=logging.INFO)

def main():
    from waitress import serve
    logging.info("Starting server")
    serve(app, host='127.0.0.1', port=8080)

if __name__ == '__main__':
    main()


#http http://127.0.0.1:8080/books
#http http://127.0.0.1:8080/books/1
