PYTHON=python3.9
ENV=.env_$(PYTHON)
IN_ENV=. $(ENV)/bin/activate &&

build-env:
	@virtualenv $(ENV) -p $(PYTHON)
	@$(IN_ENV) pip install -e .[dev]

clean-env:
	@rm -r $(ENV)
	@rm -r Cron_Explainer.egg-info

setup:
	@if [ ! -d $(ENV) ]; then make build-env; fi

test: setup
	@$(IN_ENV) pytest -vv .

format-code:
	@$(IN_ENV) black .

check-format-code:
	@$(IN_ENV) black --check .

shell: setup
	@$(IN_ENV) python

example: setup
	@$(IN_ENV) cron-explainer "*/15 0 1,15 * 1-5 /usr/bin/find"
