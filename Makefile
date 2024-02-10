build:
	docker build -t galearn .
dev-install:
	pip install -r requirements.txt
fmt:
	black app.py
lint:
	pylint app.py
run: build
	docker run --rm --name galearn \
	galearn
run-compose:
	docker-compose up -d --build
typecheck:
	mypy app.py