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
