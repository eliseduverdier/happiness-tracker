.PHONY: fetch
SHELL := /bin/bash

env:
	cp -i .env.dist .env.Csdvsd
migrate:
	python3 manage.py migrate
install:
	make env && make migrate
run:
	python3 manage.py runserver
