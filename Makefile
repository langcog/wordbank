SHELL := /bin/bash
PROJECT = wordbank

githooks:
	git config core.hooksPath .githooks

ci-test:
	python manage.py collectstatic --noinput
	set -o pipefail ; pytest --junitxml=pytest.xml --cov-report=term-missing:skip-covered --cov=  | tee pytest-coverage.txt

test:
	DEPLOY_ENV=test python manage.py collectstatic --noinput
	DEPLOY_ENV=test pytest 

lint:
	flake8 
	black --check 

cleanup:
	black .
	isort

db-setup:
	docker-compose exec -it db bash 
	mysql -U root -p poiuytre12
	CREATE DATABASE wordbank;
	CREATE USER "wordbankadmin" IDENTIFIED BY '4PBNjG37y7Mk83';
	GRANT ALL PRIVILEGES on *.* to 'wordbankadmin';
	exit;

db-populate-db:
	docker-compose exec web python manage.py collectstatic --no-input
	docker-compose exec web python manage.py 01_populate_caregiver_education
	docker-compose exec web python manage.py 02_create_instrument_schemas
	docker-compose exec web python manage.py 03_populate_instrument
	docker-compose exec web python manage.py 04_populate_category
	docker-compose exec web python manage.py 05_populate_items
	docker-compose exec web python manage.py 06_populate_datasets
	docker-compose exec web python manage.py 07_import_datasets
	docker-compose exec web python manage.py 08_populate_vocabulary_size



	
docker-test:
	docker-compose run test manage.py collectstatic --noinput
	docker-compose run test pytest 

docker-lint:
	docker-compose run web flake8 
	docker-compose run web black --check 

docker-cleanup:
	docker-compose run web black 
	docker-compose run web isort -rc 

make sync-dev-db::
	ssh giant-dev mysql:export develop-${PROJECT} > mydump.sql
	cat mydump.sql | docker-compose exec -T db mysql -pgiant ${PROJECT}
	rm mydump.sql

make sync-media::
	rsync -rvz live:/var/lib/dokku/data/storage/live-${PROJECT}/media ./media/

make dev-deploy::
	git push dokku-dev develop:main

make live-deploy::
	git push dokku main:main
