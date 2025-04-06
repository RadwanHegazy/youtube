# YouTube Clone - Django Project

A YouTube-like platform built with Django, Docker, MySQL, Redis, Celery, and Elasticsearch. This project features video hosting, user management, comments, playlists, and notifications.

## Features

- User authentication and management
- Video upload and streaming
- Comment system
- Playlist functionality
- Notifications system
- Elasticsearch for powerful search capabilities
- Scalable architecture with multiple Django instances
- Load balancing with Apache
- Background tasks with Celery and Redis

## System Architecture

- [Mindmap](https://lucid.app/lucidspark/f4356206-4e08-4a44-9471-71ae04195d79/edit?viewport_loc=-4329%2C-1935%2C6327%2C2812%2C0_0&invitationId=inv_b4e40f39-c1c5-484f-aeff-875591a6ce2d)

- [Database Schema](https://drawsql.app/teams/test-1748/diagrams/youtube)

## Technology Stack

- **Backend**: Django (Python)
- **Database**: MySQL
- **Cache**: Redis
- **Search**: Elasticsearch
- **Task Queue**: Celery
- **Web Server**: Apache (load balancing)
- **Containerization**: Docker
- **Message Broker**: Redis

## Prerequisites

- Docker 20.10+
- Docker Compose 1.29+
- Python 3.9+

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/RadwanHegazy/youtube
   ```
   
2. Enter the repository 
   ```bash
   cd youtube/code/core/
   ```

3. Create `.env` file & copy this content:

    ```
    # Database
    DB_HOST="db"
    DB_PORT="3306"
    DB_NAME="yt_db"
    DB_USER="root"
    DB_PASSWORD="root"

    # Redis
    REDIS_URL = "redis://redis:6379"

    # Google Keys
    GOOGLE_CLIENT_ID = "<YOUR_GOOGLE_CLIENT_ID>"
    GOOGLE_CLIENT_SECRET = "<YOUR_GOOGLE_CLIENT_SECRET>"
    GOOGLE_REDIRECT_URL = "<YOUR_GOOGLE_REDIRECT_URL>"

    ELASTIC_SEARCH_URL = "elasticsearch:9200"
    ```

## Build & Start The Container

1. Build the container via `docker-compose` : 
    ```bash
    docker-compose up --build -d
    ```

2. Apply database migrations:
    ```bash
    docker-compose exec django1 python manage.py makemigrations
    docker-compose exec django1 python manage.py migrate
    ```

3. Create Elasticsearch indices (if needed):
    ```bash
    docker-compose exec django1 python manage.py search_index --rebuild
    ```

## Running The Project

- **Just Type** 
    ```
    docker-compose up
    ```

- **After Running the server go to**
    - [`http://localhost/`](http://localhost/)

- **API Documentation**
    - [`http://localhost/__docs__/v1/`](http://localhost/__docs__/v1/)

- **Health Check**
    - [`http://localhost/__health_check__/`](http://localhost/__health_check__/)

## API Endpoints

| Service           | Endpoint                          | Description                     |
|-------------------|-----------------------------------|---------------------------------|
| Users             | `/api/users/`                     | User management and auth        |
| Videos            | `/api/video/`                     | Video upload and streaming      |
| Comments          | `/api/comment/`                   | Comment system                  |
| Playlists         | `/api/playlist/`                 | Playlist management             |
| Notifications     | `/api/notifications/`            | User notifications              |
