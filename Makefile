.SILENT:

DOCKER_IMAGE_NAME := "dns-record"

# docker build . -t $(DOCKER_IMAGE_NAME)
install:
	python3 -m venv venv && \
	source venv/bin/activate && \
	pip install -r requirements.txt
.PHONY: install

test:
	source venv/bin/activate && \
	pip install pytest && \
	pytest
.PHONY: test