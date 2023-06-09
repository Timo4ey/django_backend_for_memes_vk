MANAGE := poetry run python manage.py

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) bot_backend.wsgi

test-django:lint
	 @$(MANAGE) test bot_backend.bot_db_models.tests.test_models.test_model --keepdb

check:
	poetry run pytest -vv


up:
	docker compose up

down:
	docker compose down

build:
	docker build . -t django_backend

run-server:
	docker run -p 8000:8000 -d --name django_backend django_backend

collectstatic:
	poetry run python manage.py collectstatic --noinput

dev:
	@$(MANAGE) runserver

syncdb:
	@$(MANAGE) migrate --run-syncdb

makemigrations:
	@$(MANAGE) makemigrations

migrate:
	@$(MANAGE) migrate


inspectdb:
	@$(MANAGE) inspectdb

super-user:
	@$(MANAGE) createsuperuser

lint:
	poetry run flake8 bot_backend

black:
	poetry run black .

pep-isort:
	poetry run isort . 

mypy:
	poetry run mypy . 

.PHONY: shell
shell:
	@$(MANAGE) shell_plus --ipython


install:
	poetry install

schema:
	@$(MANAGE) sqldsn bot_db_models