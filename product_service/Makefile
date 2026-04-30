PRODUCT_HOST ?= 127.0.0.1
PRODUCT_PORT ?= 8001
create-structure:
	mkdir src tests docs
	touch README.md setup.py requirements.txt
	touch docs/DOMAIN.md docs/SPECIFICATION.md
	touch src/.gitkeep tests/.gitkeep

install-dep:
	pip install -r requirements.txt
install-e:
	pip install -e .
test-pytest:
	pytest
test: install-dep install-e test-pytest
run-product:
	poetry run python -m uvicorn src.app.main:app --host $(PRODUCT_HOST) --port $(PRODUCT_PORT)
