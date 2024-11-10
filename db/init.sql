CREATE TABLE appeals (
    id SERIAL PRIMARY KEY,
    last_name VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    middle_name VARCHAR(255),
    phone VARCHAR(20) NOT NULL,
    appeal TEXT NOT NULL
);