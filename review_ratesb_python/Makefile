review: sanity_checks.py.run \
	run_readme_complex_example.py.run

%.py.run: %.py
	@echo "Executing $<"
	uv run -s $<


lint:
	uv run ruff check 
	uv run mypy .

fmt:
	uv run ruff format .
