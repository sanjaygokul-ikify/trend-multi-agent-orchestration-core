init:	docker-compose up -d

clean:	docker-compose down

test:	poetry run pytest

format:	poetry run black .

lint:	poetry run flake8

bench:	poetry run benchmark/run.sh

doc:	docgen generate

develop:	poetry install

release:	poetry build