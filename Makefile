create-venv:
	python -m venv .actividad001
	@echo "✓ Ambiente virtual creado, recuerda activarlo "

install:
	pip install --upgrade pip
	pip install -r requirements.txt
	@echo "✓ Dependencias instaladas "
