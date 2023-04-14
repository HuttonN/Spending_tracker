DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS merchants;

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY
    name VARCHAR (255)
)

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY.
    amount DECIMAL (6,2)
    merchant_id INT NOT NULL REFERENCES merchants(id)
);