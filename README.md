# 🎬 Movie Website - Django REST API

A comprehensive Django-based movie streaming platform featuring AI-powered chat recommendations, secure JWT authentication with Google OAuth integration, social features including threaded comments and bookmarks, Docker containerization, PostgreSQL database with Redis caching, and Celery background task processing for scalable performance.

## 🛠 Technology Stack

### 🎯 Backend
![Django](https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django)
![DRF](https://img.shields.io/badge/Django%20REST%20Framework-3.16-ff1709?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python)

### 🗄 Database & Cache
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-316192?style=for-the-badge&logo=postgresql)
![Redis](https://img.shields.io/badge/Redis-7-DC382D?style=for-the-badge&logo=redis)

### 🔐 Authentication & Security
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens)
![Google OAuth](https://img.shields.io/badge/Google%20OAuth-4285F4?style=for-the-badge&logo=google)

### 🤖 AI & External Services
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5--turbo-412991?style=for-the-badge&logo=openai)
![Celery](https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=celery)

### 🐳 DevOps & Deployment
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker)
![Docker Compose](https://img.shields.io/badge/Docker%20Compose-2496ED?style=for-the-badge&logo=docker)
![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=gunicorn)

### 📦 Development Tools
![Pipenv](https://img.shields.io/badge/Pipenv-000000?style=for-the-badge&logo=pipenv)
![DRF YASG](https://img.shields.io/badge/DRF%20YASG-1.21.8-ff1709?style=for-the-badge)

## 🏗 Architecture

```
Frontend Client ←→ Django API ←→ Background Tasks (Celery)
                      ↓
                PostgreSQL Database
                      ↓
                Redis (Cache/MQ)
```

## 📁 Project Structure

```
movie_website/
├── apis/                    # API endpoints
│   ├── chat_ai_apis/       # AI chat
│   ├── interaction_apis/    # Social features
│   ├── movie_apis/         # Movie management
│   ├── relation_apis/      # Actor/Category/Director
│   └── user_apis/          # Authentication
├── chat_ai/                # AI functionality
├── interactions/           # Social features
├── movies/                # Movie management
├── relations/             # Related entities
├── users/                 # User management
└── utils/                 # Utilities
```

## 🚀 Quick Start

### Docker Setup
```bash
# Clone and setup
git clone <repository-url>
cd movie-website

# Create .env file with required variables
cp .env.example .env

# Start services
docker-compose up -d

# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser
```

### Local Setup
```bash
cd movie_website
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 🔧 Environment Variables

```env
# Django
SECRET_KEY=your-secret-key
DEBUG=True

# Database
POSTGRES_DB=movie_db
POSTGRES_USER=movie_user
POSTGRES_PASSWORD=your-password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0

# Celery
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

# JWT
ACCESS_TOKEN_LIFETIME_MINUTES=60
REFRESH_TOKEN_LIFETIME_DAYS=7
JWT_ALGORITHM=HS256

# External Services
GOOGLE_OAUTH_CLIENT_ID=your-google-client-id
OPENAI_TOKEN=your-openai-api-key
```

## 📚 API Endpoints

### Authentication

POST /api/v1/auth/register/     # User registration
POST /api/v1/auth/login/        # User login
POST /api/v1/auth/logout/       # User logout
POST /api/v1/auth/google/       # Google OAuth
GET  /api/v1/auth/google/client-id/  # Get Google client ID
```

### Movies

GET /api/v1/movies/             # List all movies
GET /api/v1/movies/{slug}/      # Movie details
```

### Social Features

POST /api/v1/comments/          # Create comment
GET  /api/v1/comments/          # List comments
POST /api/v1/likes/             # Like comment
DELETE /api/v1/likes/{id}/      # Unlike comment
POST /api/v1/bookmarks/         # Add bookmark
DELETE /api/v1/bookmarks/{id}/  # Remove bookmark
```

### Relations (Actors, Directors, Categories)

GET /api/v1/actors/             # List actors
GET /api/v1/actors/{id}/        # Actor details
GET /api/v1/directors/          # List directors
GET /api/v1/directors/{id}/     # Director details
GET /api/v1/categories/         # List categories
GET /api/v1/categories/{id}/    # Category details
```

### AI Chat

POST /api/v1/chat/request/      # Start AI chat
GET  /api/v1/chat/response/{task_id}/  # Get AI response
```

### User Profile

GET /api/v1/users/profile/      # User profile
PUT /api/v1/users/profile/      # Update profile
```

## 🗄 Database Models

### Core Models
- **Movie**: title, description, duration, rating, poster, video, trailer_url, slug
- **CustomerUser**: email, username, birthday, bio, profile_image
- **Comment**: user, movie, parent, text, like_count
- **Like**: user, comment (unique constraint)
- **Bookmark**: user, movie (unique constraint)

### Relation Models
- **Actor**: name, biography, birth_date, photo
- **Director**: name, biography, birth_date, photo
- **Category**: name, description
- **ReleaseDate**: date, country

## 🔐 Authentication

- **JWT Tokens**: Access (60min) + Refresh (7 days)
- **Google OAuth**: Social login integration
- **Token Blacklist**: Secure logout
- **Age Validation**: Minimum 13 years old

## 🤖 AI Features

- **Async Processing**: Celery background tasks
- **OpenAI Integration**: GPT-3.5-turbo for responses
- **Movie Search**: Searches database for relevant movies
- **Context Awareness**: Knows about available movies

## 🐳 Docker Services

```yaml
services:
  web:          # Django app (Gunicorn)
  celery:       # Background tasks
  db:           # PostgreSQL database
  redis:        # Cache & message broker
```

## 💻 Development

```bash
# Run tests
python manage.py test

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Start Celery worker
celery -A movie_website worker --loglevel=info
```

## 📄 License

MIT License

---

**Built with Django REST Framework**

```

