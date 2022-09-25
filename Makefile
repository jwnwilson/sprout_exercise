run:
	docker-compose up

test:
	docker-compose run backend bash -c "pytest"
