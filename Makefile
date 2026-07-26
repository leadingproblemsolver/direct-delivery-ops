.PHONY: install test smoke verify
install:
	python -m pip install -e '.[test]'
test:
	python -m pytest -q
smoke:
	rm -rf var/example-run
	PYTHONPATH=src python -m direct_delivery_ops.cli init var/example-run
	PYTHONPATH=src python -m direct_delivery_ops.cli validate var/example-run
	PYTHONPATH=src python -m direct_delivery_ops.cli manifest var/example-run --output var/example-run/manifest.json
verify: test smoke
