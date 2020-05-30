migrate:
	python pythonblog/manage.py makemigrations bitly users posts pythonblog
	python pythonblog/manage.py migrate