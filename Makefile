migrate:
	python pythonblog/manage.py makemigrations bitly users posts pythonblog
	python pythonblog/manage.py migrate


test:
	pycodestyle .
	python pythonblog/manage.py test users posts bitly pythonblog