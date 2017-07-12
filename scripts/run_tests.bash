#!/usr/bin/env bash

PYTEST_ARGUMENTS=${@:-tests/test_purchase_tickets.py}

AUTOMATION_IMAGE=blazemeter/selenium-framework
PROJECT_IMAGE=blazemeter/blazedemo-app-selenium

ALLURE_RESULTS_DIR=allure-results
PROJECT_DIR=blazedemo-app


docker build -t $AUTOMATION_IMAGE .
docker build -t $PROJECT_IMAGE ./$PROJECT_DIR

# Run Selenium py.test with script arguments
docker run --rm \
    -v $(pwd)/$PROJECT_DIR/$ALLURE_RESULTS_DIR:/code/$ALLURE_RESULTS_DIR \
    $PROJECT_IMAGE \
    "$PYTEST_ARGUMENTS"