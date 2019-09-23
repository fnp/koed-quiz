.PHONY: deploy


deploy: koedquiz/localsettings.py
	pip install -r requirements.txt
	src/manage.py migrate --noinput
	src/manage.py collectstatic --noinput

