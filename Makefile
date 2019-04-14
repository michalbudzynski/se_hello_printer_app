.PHONY: test
deps:
	pip install -r requirements.txt; \
	pip install -r test_requirements.txt
lint:
	flake8 hello_world test
run:
	python main.py
test:
	$ PYTHONPATH=. py.test
docker_build:
	docker build -t hello-world-printer .
docker_run: docker_build
	docker run \
		--name hello-world-printer-dev \
		-p 5000:5000 \
	  -d hello-world-printer

USERNAME= 6pawel9
TAG=$(USERNAME)/hello-world-printer

docker_push: docker_build
	@docker login --username $(USERNAME) --password $${DOCKER_PASSWORD}; \
	docker tag hello-world-printer $(TAG); \
	docker push $(TAG); \
	docker logout;

test_smoke:
	curl -s -o /dev/null -w "%{http_code}" --fail 127.0.0.1:5000

test_xunit:
	PYTHONPATH=. py.test --verbose -s --cov=. --cov-report xml --junit-xml=test_results.xml

test_cov:
	PYTHONPATH=. py.test --verbose -s --cov=. --cov-report xml

