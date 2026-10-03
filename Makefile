.PHONY: setup build validate test serve all

setup:
	python -m pip install -r requirements.txt

build:
	python scripts/generate_deliverables.py

validate:
	python scripts/validate_project.py

test:
	python -m unittest discover -s tests -v

serve:
	python -m http.server 8000

all: build validate test
