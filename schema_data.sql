CREATE TABLE money changer (
    id int NOT NULL,
    want char(32)NOT NULL,
    total int NOT NULL,
    corse float(20) NOT NULL,
    phone int(20) NOT NULL,
    city char(50) NOT NULL,
    area char(50) NOT NULL,
    comment char(7999),
    relevant datetime,
    pub_date = datetime
    PRIMARY KEY (id)
);

CREATE TABLE users (
    id INTEGER NOT NULL,
    username VARCHAR(50),
    email VARCHAR(120),
    password VARCHAR(32),
    PRIMARY KEY (id),
    UNIQUE (name),
    UNIQUE (email)
);

INSERT INTO users (name, email, password) VALUES ('test', 'test@test.test', 'test')