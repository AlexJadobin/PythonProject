CREATE TABLE users
(
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(20) UNIQUE NOT NULL,
    email    VARCHAR(80) UNIQUE,
    PRIMARY KEY (id)
);


CREATE TABLE posts
(
    id INT NOT NULL AUTO_INCREMENT,
    body TEXT NOT NULL DEFAULT '',
    user_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

INSERT INTO users (username, email)
values ('alex', 'alex@mal.com');

INSERT INTO users (username, email)
values ('pavel', 'pavel@mal.com');

INSERT INTO posts (body, user_id)
values ('ONE', '1');

INSERT INTO posts (body, user_id)
values ('TWO', '2');

INSERT INTO posts (body, user_id)
values ('THREE', '1');

INSERT INTO posts (body, user_id)
values ('FOUR', '2');