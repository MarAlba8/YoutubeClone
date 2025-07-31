# YouTube Clone

This project is a simplified version of YouTube, built with Django. It allows users to upload, view, like, or dislike videos, comment, and see their viewing history.

## What you can do

* **Users:** Register, log in, and manage your account.

* **Videos:** Upload videos (using external video links).

* **Watch videos:** Play videos.

* **Reactions:** Like or dislike videos.

* **Comments:** Leave comments on videos.

* **History:** View the videos you have watched.

* **User Dashboard:** View your uploaded videos and your history.

## Technologies

* **Backend:** Django

* **Database:** PostgreSQL

* **Dependencies:** Poetry

* **Containers:** Docker and Docker Compose

* **Styling:** Bootstrap 5

* **Version Control:** Git

## How to Get Started (Local)

Follow these steps to get the project running on your computer.

### Requirements

* Python 3.11+

* Poetry

* Docker and Docker Compose

* Git

### 1. Clone the Project

     git clone https://github.com/MarAlba8/YoutubeClone.git
     cd YoutubeClone # Or the name of your folder


### 2. Configure Poetry

Install the project dependencies:

     poetry install


### 3. Environment Variables

Create a `.env` in `src.config`. You can use `.env.sample` for guidance:

.env

     DATABASE_URL=postgres://your_db_user:your_db_password@db:5432/your_database_name


Make sure that `your_db_user`, `your_db_password`, and `your_database_name` match your `docker-compose.yml`.

### 4. Start the Database (Docker)

     docker-compose up -d db


Wait a moment for the database to be ready.

### 5. Apply Django Migrations

     python manage.py migrate


### 6. Create a Superuser (Admin)

     python manage.py createsuperuser


Follow the instructions to create your administrator user.

### 7. Start the Server

     python manage.py runserver


Access the application at `http://127.0.0.1:8000/`. The admin panel is at `http://127.0.0.1:8000/admin/`.

## Run with Docker Compose (Full Setup)

To start the database and the application in containers:

     docker-compose up --build


This will build the images, start everything, and automatically apply migrations.

## Tests

To run the tests:

     python manage.py test
