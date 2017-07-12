#!/usr/bin/env bash

ALLURE_IMAGE=automationwizards/allure:2.0-BETA1

ALLURE_CONFIG_DIR=allure-config
ALLURE_REPORT_DIR=allure-report
ALLURE_RESULTS_DIR=allure-results
PROJECT_DIR=${1:-blazedemo-app}

# Delete any previous allure reports
rm -rf $PROJECT_DIR/$ALLURE_REPORT_DIR

docker run --rm \
    -v $(pwd)/$PROJECT_DIR/$ALLURE_REPORT_DIR:/$ALLURE_REPORT_DIR \
    -v $(pwd)/$PROJECT_DIR/$ALLURE_RESULTS_DIR:/$ALLURE_RESULTS_DIR \
    -v $(pwd)/$PROJECT_DIR/$ALLURE_CONFIG_DIR:/$ALLURE_CONFIG_DIR \
    $ALLURE_IMAGE allure generate /$ALLURE_RESULTS_DIR -o /$ALLURE_REPORT_DIR