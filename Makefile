sync:
	uv sync

install:
	uv pip install -e .

gendiff:
	uv run gendiff

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check gendiff

test:
	uv run pytest tests/ -v


