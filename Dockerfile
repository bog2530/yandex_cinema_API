FROM python:3.11-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/app/.venv/bin:$PATH"

COPY [ \
  "pyproject.toml", \
  "uv.lock", \
  "README.md", \
"./"]
COPY src ./src

RUN uv sync --frozen --no-dev

ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0","--port", "8000"]