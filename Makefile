migrate:
	python fastagram/manage.py makemigrations fastagram users posts
	python fastagram/manage.py migrate
