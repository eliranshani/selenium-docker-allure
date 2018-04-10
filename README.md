# selenium-docker-allure
Running Selenium tests under py.test convention with docker support.

![Carpe Diem - Seize the day](shark.png?raw=true "Carpe Diem")

## Requirements

- Docker

### Run tests and generate results
```bash
# Run with py.test arguments (-v for verbose output)
$ ./scripts/run-tests.bash --env=$ENV tests/test_purhcase_tickets.py -v
```

### Run allure to generate allure report
```bash
$ ./scripts/generate-allure-report.bash blazedemo_app
```

### Open allure report
```bash
$ cd ./blazedemo_app/allure-report/
$ python -m SimpleHTTPServer 8000
$ open http://localhost:8000
```

### Integrate tests inside Jenkins Pipeline
```bash
0. (Make sure your Jenkins Pipeline is supported by Docker and have Allure and Slack plugins installed)
1. Create Jenkins Pipeline job
2. Connect the job with pipeline/Jenkinsfile
3. Run the job
```

## Motivation

This project allows other developers to understand how to:
1. Create auto tests in python under py.test convention
2. Run tests with Docker
3. Export results into Allure report
4. Integrate tests inside Jenkins Pipeline

## Links

[Additional info](./additional_info.md)

## Contributors

Gilad Peleg
Elad Kollender
Eliran Shani

## License

MIT
