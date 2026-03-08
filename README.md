# EduStream LMS Backend

Scalable Django backend for school/college LMS with REST APIs (Django Ninja), JWT auth, PostgreSQL, Redis, and Django Channels websocket chat.

## Architecture

- **Domain apps**: `users`, `courses`, `chapters`, `streaming`, `articles`, `quizzes`, `chat`, `notifications`
- **API layer**: `edustream/api.py` composes all app routers
- **Realtime layer**: `chat/consumers.py` + Channels + Redis
- **Infra**: PostgreSQL, Redis, MediaMTX via Docker Compose

## Project structure

```bash
edustream/
├── edustream/                # project config
│   ├── api.py                # root Ninja API + JWT controller
│   ├── asgi.py               # HTTP + websocket protocol routing
│   ├── settings.py           # env-driven settings
│   └── urls.py
├── users/                    # custom user + roles
├── courses/
├── chapters/                 # Chapter + LectureVideo
├── streaming/                # LiveStreamSession (RTMP)
├── articles/                 # student articles + approval workflow
├── quizzes/                  # Quiz + Question
├── chat/                     # ChatMessage + websocket consumer
├── notifications/            # Notification
├── Dockerfile
├── docker-compose.yml
└── .env.example
```

## Environment setup

1. Copy `.env.example` to `.env`.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run with docker:
   ```bash
   docker compose up --build
   ```

## API overview

Base URL: `/api/`

- JWT endpoints are available via Ninja JWT controller.
- App endpoints:
  - `/api/users/`
  - `/api/courses/`
  - `/api/chapters/`
  - `/api/chapters/videos`
  - `/api/streaming/sessions`
  - `/api/articles/`
  - `/api/quizzes/`
  - `/api/quizzes/questions`
  - `/api/chat/messages`
  - `/api/notifications/`

All app endpoints are protected with JWT auth (`Authorization: Bearer <token>`).

## Realtime chat

WebSocket endpoint:

```bash
ws://localhost:8000/ws/chat/<session_id>/
```

Messages are broadcast to all users connected in the same lecture chat room.

## React / React Native readiness

- CORS is configurable through environment variables.
- CSRF trusted origins are configurable.
- API-first design with JSON schemas in each app for frontend integration.

## Core models implemented

- `User` (role-based)
- `Course`
- `Chapter`
- `LectureVideo`
- `LiveStreamSession`
- `Article`
- `Quiz`
- `Question`
- `ChatMessage`
- `Notification`
