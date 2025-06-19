CREATE DATABASE IF NOT EXISTS portfolio;
USE portfolio;

CREATE TABLE IF NOT EXISTS projects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    image_url VARCHAR(512),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS gallery (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image_path VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO projects (title, description, image_url)
VALUES 
('Portfolio Website', 'A personal portfolio website.', 'images/project1.jpg'),
('E-commerce Store', 'An online store for products.', 'images/project2.jpg');

INSERT INTO gallery (image_path, description)
VALUES 
('images/gallery1.jpg', 'Image 1 description'),
('images/gallery2.jpg', 'Image 2 description'),
('images/gallery3.jpg', 'Image 3 description'),
('images/gallery4.jpg', 'Image 4 description'),
('images/gallery5.jpg', 'Image 5 description'),
('images/gallery6.jpg', 'Image 6 description');

