# Kittygram

Проект Kittygram — приложение для публикации фотографий котиков с API на Django REST Framework и React-фронтендом.

## Стек технологий

- **Backend:** Python, Django, Django REST Framework, Djoser, PostgreSQL, Gunicorn
- **Frontend:** React, JavaScript
- **Инфраструктура:** Docker, Docker Compose, Nginx, GitHub Actions

## Функции проекта

- Регистрация и аутентификация пользователей
- Публикация фотографий котиков с описанием и цветами
- API для работы с данными
- Админ-панель Django

## Развёртывание проекта

### 1. Клонирование репозитория

```bash
git clone https://github.com/ваш-логин/kittygram_final.git
cd kittygram_final
```

### 2. Настройка переменных окружения

Создайте файл `.env` в корне проекта на основе `.env.example`:

```bash
cp .env.example .env
```

Заполните переменные в `.env`:

- `POSTGRES_PASSWORD` — надёжный пароль для PostgreSQL
- `SECRET_KEY` — секретный ключ Django (сгенерируйте новый для продакшена)
- `ALLOWED_HOSTS` — домены через запятую (например, `your-domain.com,www.your-domain.com`)
- `DOCKERHUB_USERNAME` — ваш логин на Docker Hub (для docker-compose.production.yml)

### 3. Запуск в режиме разработки (сборка образов)

```bash
docker-compose up -d --build
```

Приложение будет доступно по адресу: http://localhost:9000

### 4. Запуск в продакшене (готовые образы с Docker Hub)

```bash
docker-compose -f docker-compose.production.yml up -d
```

Убедитесь, что в `.env` указан `DOCKERHUB_USERNAME` с вашим логином Docker Hub.

## CI/CD

При пуше в ветку `main` или `master`:
1. Запускаются тесты (ruff, pytest, npm test)
2. Собираются и публикуются образы на Docker Hub
3. Отправляется уведомление в Telegram

### Секреты GitHub

В настройках репозитория добавьте секреты:
- `DOCKERHUB_USERNAME` — логин Docker Hub
- `DOCKERHUB_TOKEN` — токен доступа Docker Hub
- `TELEGRAM_BOT_TOKEN` — токен бота Telegram
- `TELEGRAM_CHAT_ID` — ID чата для уведомлений

## Как проверить работу с помощью автотестов

В корне репозитория создайте файл `tests.yml`:

```yaml
repo_owner: ваш_логин_на_гитхабе
dockerhub_username: ваш_логин_на_докерхабе
```

Скопируйте содержимое `.github/workflows/main.yml` в `kittygram_workflow.yml`.

Для локального запуска тестов:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r backend/requirements.txt
pytest
```

## Чек-лист для проверки перед отправкой задания

- Пуш в ветку main запускает тестирование Kittygram, а после вам приходит сообщение в телеграм.
- В корне проекта есть файл `kittygram_workflow.yml`.
