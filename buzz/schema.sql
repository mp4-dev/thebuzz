DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    created  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);