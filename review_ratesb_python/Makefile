review: sanity_checks

sanity_checks: ./sanity_checks.py
	uv run -s $<

lint:
	uv run ruff check 
	uv run mypy .

fmt:
	uv run ruff format .
