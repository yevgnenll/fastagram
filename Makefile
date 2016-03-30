migrate:
	python fastagram/manage.py makemigrations fastagram users posts tags
	python fastagram/manage.py migrate
