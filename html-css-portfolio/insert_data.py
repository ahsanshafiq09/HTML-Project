from app import db, Project, Gallery
from app import app  # Import the app to get the app context

# Start application context
with app.app_context():
    # Sample data for Projects
    projects = [
        Project(title="Portfolio Website", description="A personal portfolio website.", image_url="https://example.com/image1.jpg"),
        Project(title="E-commerce Store", description="An online store for products.", image_url="https://example.com/image2.jpg"),
    ]

    # Sample data for Gallery Images
    gallery_images= [
        {"image_path": "images/gallery1.jpg", "description": "Image 1 description"},
        {"image_path": "images/gallery2.jpg", "description": "Image 2 description"},
        {"image_path": "images/gallery3.jpg", "description": "Image 3 description"},
        {"image_path": "images/gallery4.jpg", "description": "Image 4 description"},
        {"image_path": "images/gallery5.jpg", "description": "Image 5 description"},
        {"image_path": "images/gallery6.jpg", "description": "Image 6 description"}
    ]

    # Insert data into the database
    with db.session.begin():
        db.session.add_all(projects)
        for data in gallery_images:
                image = Gallery(image_path=data["image_path"], description=data["description"])
                db.session.add(image)

    print("Sample data added successfully!")
