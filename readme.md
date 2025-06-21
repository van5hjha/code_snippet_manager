## 🧠 Code Snippet Organizer API

A Django REST API for saving, tagging, searching, and sharing code snippets. This project features user authentication, a robust tagging system, syntax highlighting, and public sharing capabilities. It's built with Django, Django REST Framework (DRF), and Docker.

### 🔧 Features
🔐 JWT Authentication: Secure user login and registration.
✍️ CRUD Operations: Full Create, Read, Update, and Delete functionality for snippets and tags.
🏷️ Tagging System: User-scoped tags for efficient organization.
🔍 Search, Filter & Pagination: Easily find and manage snippets with comprehensive search, filtering, and pagination options.
🌈 Syntax Highlighting: Beautifully rendered code snippets using Pygments.
🔗 Shareable Snippets: Publicly share snippets via unique UUIDs.
📄 API Documentation: Interactive API documentation with Swagger/OpenAPI.
🐳 Dockerized: Build and run the entire project with a single command.
🚀 Running the Project with Docker
Follow these steps to get the project up and running using Docker:

1. Clone the Repository

Bash
```git clone https://github.com/<your-username>/code-snippet-manager.git```

cd code-snippet-manager 2. Build the Docker Image

Bash
`docker build -t new-django .`

3. Run the Container

Bash
`docker run --publish 8000:8000 new-django`

Once the container is running, open your browser and navigate to:

🔗 http://localhost:8000

###🛠️ Post-Setup (Inside Container)
If not automatically handled by the Dockerfile, you may need to run database migrations and create a superuser. Open a new terminal and execute:

First, find your container ID:

Bash
`docker ps`

Then, run the following commands, replacing <container_id> with your actual container ID:

Bash
`docker exec -it <container_id> python manage.py migrate
docker exec -it <container_id> python manage.py createsuperuser`

### 🔎 API Documentation
Access the API documentation at:

Swagger UI: http://localhost:8000/swagger/
ReDoc (optional): http://localhost:8000/redoc/
📂 .env (Optional)
You can pass environment variables to your Docker container using --env flags or by configuring defaults within your Dockerfile:

Bash
`docker run --env SECRET_KEY=abc123 --env ALLOWED_HOSTS=localhost --publish 8000:8000 new-django`

### 👨‍💻 Stack
Django
Django REST Framework
PostgreSQL (optional, for database)
JWT (SimpleJWT for authentication)
Swagger (drf-yasg for API documentation)
Docker

### 📄 License
This project is licensed under the MIT License.
