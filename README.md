# Demo Playwright

1) Create Python venv
2) Install Playwright `pip install pytest-playwright`
3) Install browsers `playwright install`

## Playwright Debug Mode

Command below allows to go through test step by step:
`PWDEBUG=1 pytest -s -k <name of test (not a file!)>`

Next command allows to save a result of run in specific file with manager:
`pytest --tracing=retain-on-failure`
`playwright show-trace path/to/trace.zip`

## Parrarel test run

Install additional package for parrarel running:
`pip install pytest-xdist`

Then use this command to parrarel run:
`pytest --numprocesses 2`
