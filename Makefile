.PHONY: help env migrate install run test style clear-cache update
SHELL := /bin/bash

#- ——  Help —————————————————————————————————————————————————————
help: #- Outputs this help screen
	@grep -hE '(^[a-zA-Z0-9_-]+:.*?#-.*$$)|(^#-)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?#- "}{printf "\033[32m%-25s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m#-/[33m/'

#- —— ⚙️ Install —————————————————————————————————————————————————————
env: #- Copies the .env file
	cp -i .env.dist .env.local
install: #- Installs the dependencies
	make env && make depts && make migrate

#- —— 🐍️ Python —————————————————————————————————————————————————————
migrate: #- Runs the migrations
	python3 manage.py makemigrations && python3 manage.py migrate
run: #- Runs the server
	python3 manage.py runserver
clear-cache: #- Clears the cache
	django-admin.py clean_pyc --settings=$(SETTINGS)
depts: #- Updates the dependencies
	pip install -U -r requirements.pip
test: #- Runs the tests
	django-admin.py test --settings=$(TEST_SETTINGS)
style: #- Runs the style checker
	pylint happiness_tracker --recursive=y
