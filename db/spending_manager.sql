DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS merchants;

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    activated_merchant BOOLEAN
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    activated_tag BOOLEAN
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    amount DECIMAL (6,2),
    transaction_date DATE,
    merchant_id INT NOT NULL REFERENCES merchants(id),
    tag_id INT NOT NULL REFERENCES tags(id)
);