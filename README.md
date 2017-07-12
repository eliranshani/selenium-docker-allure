# selenium-docker-allure
Running Selenium tests under py.test convention with docker support.

## Requirements

- Docker

### Run tests and generate results
```bash
# Run with default command
$ ./scripts/run-tests.bash

# Run with extra py.test arguments
$ ./scripts/run-bza-gui.bash --env=$ENV tests/test_purhcase_tickets.py --verbose
```

### Run allure to generate allure report
```bash
$ ./scripts/generate-allure-report.bash blazedemo-app
```

### Open allure report
```bash
$ cd ./bza-gui/allure-report/
$ python -m SimpleHTTPServer 8000
$ open http://localhost:8000
```

## Motivation

This project allows other developers to understand how to:
1. Create auto tests in python under py.test convention
2. Run tests with Docker
3. Export results into Allure report

## Links

# [Additional links here](./additional_info.md)

## Contributors

Gilad Peleg
Eliran Shani

