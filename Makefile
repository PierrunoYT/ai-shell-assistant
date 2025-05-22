.PHONY: help clean test lint format build install check all

help:
	@echo "Available commands:"
	@echo "  clean      - Clean build artifacts"
	@echo "  test       - Run tests"
	@echo "  lint       - Run linting"
	@echo "  format     - Format code"
	@echo "  build      - Build package"
	@echo "  install    - Install in development mode"
	@echo "  check      - Check package"
	@echo "  all        - Run all steps"

clean:
	python scripts/build.py clean

test:
	python scripts/build.py test

lint:
	python scripts/build.py lint

format:
	python scripts/build.py format

build:
	python scripts/build.py build

install:
	python scripts/build.py install

check:
	python scripts/build.py check

all:
	python scripts/build.py all
