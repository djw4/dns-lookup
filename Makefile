.SILENT:

DOCKER_IMAGE_NAME := "dns-record"
PYTHON_TEST_SUMMARYNAME := "test-summary.xml"
PYTHON_TEST_DIR ?= "temp"

# docker build . -t $(DOCKER_IMAGE_NAME)
install:
	python3 -m venv venv; \
	. venv/bin/activate; \
	pip install -r requirements.txt
.PHONY: install

test:
	. venv/bin/activate; \
	pip install pytest; \
	if [ -f $(PYTHON_TEST_DIR)/$(PYTHON_TEST_SUMMARYNAME) ]; then rm -f $(PYTHON_TEST_DIR)/$(PYTHON_TEST_SUMMARYNAME); else true; fi; \
	mkdir -p $(PYTHON_TEST_DIR); \
	pytest --junit-xml=$(PYTHON_TEST_DIR)/test-summary.xml
.PHONY: test

clean:
	rm -rf venv
.PHONY: clean