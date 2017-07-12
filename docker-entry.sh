#!/usr/bin/env bash

py.test --alluredir=allure-results $@ &
pid="$!"

trap "echo '=== Stopping PID $pid ==='; kill -SIGTERM $pid" SIGINT SIGTERM

wait $pid