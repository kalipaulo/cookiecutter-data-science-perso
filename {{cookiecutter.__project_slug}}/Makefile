.PHONY: help install test notebooks

help:
	@echo "Commandes disponibles : install, test, notebooks"

install:
	python -m pip install -e .

test:
	python -m pytest tests -v

notebooks:
	python -m jupyter lab notebooks
