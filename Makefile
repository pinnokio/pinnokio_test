MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=pinnokio_test.settings $(MANAGE) test contact logger

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=pinnokio_test.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=pinnokio_test.settings $(MANAGE) syncdb --noinput