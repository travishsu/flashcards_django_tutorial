
env:
	python -m venv env

.PHONY: install
install: env
	. env/bin/activate; pip install -r requirements.txt

runserver:
	. env/bin/activate; python manage.py runserver
