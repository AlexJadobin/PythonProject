# установка mariadb

docker run -d \
-p 3306:3306 \
--name some-mariadb \
--env MARIADB_DATABASE=blog_app \
--env MARIADB_USER=example-user \
--env MARIADB_PASSWORD=my_cool_secret \
--env MARIADB_ROOT_PASSWORD=my-secret-pw \
mariadb:latest


# mariadb никак не устанавливался. После долгих мучений он установился только при вводе команды в одной строке без переноса, а не так как написано в методичке

docker run -d -p 3306:3306 --name some-mariadb --env MARIADB_DATABASE=blog_app --env MARIADB_USER=example-user --env MARIADB_PASSWORD=my_cool_secret --env MARIADB_ROOT_PASSWORD=my-secret-pw mariadb:latest