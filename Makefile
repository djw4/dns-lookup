.SILENT:

DOCKER_IMAGE_NAME := "dns-record"

# docker build . -t $(DOCKER_IMAGE_NAME)
install:
	pip install -r requirements.txt
.PHONY: install
