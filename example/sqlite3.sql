PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users (id INTEGER NOT NULL PRIMARY KEY, salt VARCHAR(12) NOT NULL, username VARCHAR(50) NOT NULL, password VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL);
CREATE TABLE posts (id INTEGER NOT NULL PRIMARY KEY, title VARCHAR(100) NOT NULL, slug VARCHAR(100) NOT NULL, content TEXT NOT NULL, tags VARCHAR(255) NOT NULL, category VARCHAR(30) NOT NULL, published VARCHAR(30) NOT NULL);
CREATE TABLE tags (id INTEGER NOT NULL PRIMARY KEY, name VARCHAR(50) NOT NULL, post_id INTEGER NOT NULL);
CREATE UNIQUE INDEX users_id ON users(id);
CREATE UNIQUE INDEX posts_id ON posts(id);
CREATE INDEX posts_slug ON posts(slug);
CREATE INDEX tags_name ON tags(name);
CREATE UNIQUE INDEX tags_id ON tags(id);
COMMIT;