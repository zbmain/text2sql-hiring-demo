up:
    docker compose -f docker/docker-compose.yml up

test:
    uv run pytest

start:
    uv run python -m src.main

down:
    docker compose -f docker/docker-compose.yml down

down-all:
    docker compose -f docker/docker-compose.yml down -v
