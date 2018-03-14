#!/usr/bin/env bash

# pull allure report image from docker hub
ALLURE_IMAGE=beeete2/docker-allure2

# create relevant folder structure for allure report
ALLURE_CONFIG_DIR=allure-config
ALLURE_REPORT_DIR=allure-report
ALLURE_RESULTS_DIR=allure-results
PROJECT_DIR=${1:-blazedemo_app}

# Delete any previous allure reports
rm -rf $PROJECT_DIR/$ALLURE_REPORT_DIR

# run allure image to generate allure report based on latest test results
docker run --rm \
    -v $(pwd)/$PROJECT_DIR/$ALLURE_REPORT_DIR:/$ALLURE_REPORT_DIR \
    -v $(pwd)/$PROJECT_DIR/$ALLURE_RESULTS_DIR:/$ALLURE_RESULTS_DIR \
    -v $(pwd)/$PROJECT_DIR/$ALLURE_CONFIG_DIR:/$ALLURE_CONFIG_DIR \
    $ALLURE_IMAGE allure generate /$ALLURE_RESULTS_DIR -o /$ALLURE_REPORT_DIR