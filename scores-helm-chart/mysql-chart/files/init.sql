USE games;

CREATE TABLE IF NOT EXISTS users_scores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    score INT NOT NULL
);


