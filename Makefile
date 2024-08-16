.DEFAULT_GOAL := help
.PHONY: changes checkout-master start-app start-celery-worker test mypy install-deps install-test-deps install-all-deps update-deps-lock-file coverage

checkout-master:
		git fetch && git checkout master && git pull origin master

changes: checkout-master
		@echo Changes from `git describe --abbrev=0 --tags` tag:
		@git log --no-merges --format=%s%b `git describe --abbrev=0 --tags`...origin/master | tee -p changes.txt

start-app:
		python manage.py runserver

start-dev-server:
		gunicorn -k uvicorn.workers.UvicornWorker tra.infra.asgi:application --reload -b "0.0.0.0:8000"

start-celery-worker:
		celery -A tra.infra.celery worker -l INFO

install-deps:  ## Install only production needed dependencies
		poetry shell
		poetry install --no-root --without test,local

install-test-deps:  ## Install only test/lint dependencies
		poetry shell
		poetry install --no-root --only test

install-all-deps:
		poetry shell
		poetry install --no-root

update-deps-lock-file:
		poetry lock --no-update

mypy:
		mypy tra/

test:
		pytest -s -v tests/

coverage:  ## Run tests with coverage
		coverage erase
		coverage run --include=tra/* -m pytest
		coverage report -m
