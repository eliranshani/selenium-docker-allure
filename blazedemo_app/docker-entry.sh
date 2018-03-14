#!/usr/bin/env bash

# run py.test ($@ to derive parameters from commandline)
py.test --alluredir=allure-results $@ &
pid="$!"

# trap process id to stop script using Control+C
trap "echo '=== Stopping PID $pid ==='; kill -SIGTERM $pid" SIGINT SIGTERM

wait $pid