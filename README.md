[![License](https://img.shields.io/github/license/jbarbadillo/reactivemqtt.svg)](https://github.com/jbarbadillo/reactivemqtt/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/jbarbadillo/reactivemqtt.svg?branch=master)](https://travis-ci.org/jbarbadillo/reactivemqtt)


# reactivemqtt

Examples with reactive python and mqtt
* simple app that connects to a remote broker and gathers data using rxpy
* some samples for [rxpy](https://github.com/ReactiveX/RxPY), [mqtt](https://pypi.org/project/paho-mqtt/)
* a suite of tests

## Requirements

To run this examples you will need rxpy, paho-mqtt and [pytest](https://docs.pytest.org/en/latest/)

Install this libraries in your environment

    pip install rx
    pip install paho-mqtt
    pip install pytest

## Run code and samples

### Main module app

You can launch the app running this command

    python -m reactivemqtt.app

### Samples

For launching each sample just run
 
    python -m samples.merging_infinite_sources.py
    python -m samples.merging_observables.py
    python -m samples.simple_observer.py
