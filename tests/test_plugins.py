import json
import os
from subprocess import check_call
from tempfile import NamedTemporaryFile

from tests.data import demo
from tests.data import demo_testsuite

expected_nose = [{
    "method": "test_bar",
    "module": "tests.data.demo_testsuite",
    "namespace": None,
    "unique_id": "tests.data.demo_testsuite:test_bar",
    "location": demo_testsuite.__file__,
    "tests": [{
        "module": "tests.data.demo",
        "method": "bar",
        "namespace": None,
        "unique_id": "tests.data.demo:bar(F)",
        "location": demo.__file__,
        "uncovered_lines": [],
        "covered_lines": [12]
    }]},
    {
        "method": "test_bar2",
        "module": "tests.data.demo_testsuite",
        "namespace": None,
        "unique_id": "tests.data.demo_testsuite:test_bar2",
        "location": demo_testsuite.__file__,
        "tests": [{
            "module": "tests.data.demo",
            "method": "bar",
            "namespace": None,
            "unique_id": "tests.data.demo:bar(F)",
            "location": demo.__file__,
            "uncovered_lines": [],
            "covered_lines": [12]
        }],
    }]

expected_pytest = [{
    "method": "test_bar",
    "module": "tests.data.demo_testsuite",
    "namespace": None,
    "unique_id": "tests.data.demo_testsuite:test_bar",
    "location": demo_testsuite.__file__,
    "tests": [{
        "module": "tests.data.demo",
        "method": "bar",
        "namespace": None,
        "unique_id": "tests.data.demo:bar(F)",
        "location": demo.__file__,
        "uncovered_lines": [],
        "covered_lines": [12]
    }]},
    {
        "method": "test_bar2",
        "module": "tests.data.demo_testsuite",
        "namespace": None,
        "unique_id": "tests.data.demo_testsuite:test_bar2",
        "location": demo_testsuite.__file__,
        "tests": [{
            "module": "tests.data.demo",
            "method": "bar",
            "namespace": None,
            "unique_id": "tests.data.demo:bar(F)",
            "location": demo.__file__,
            "uncovered_lines": [],
            "covered_lines": [12]
        }],
    }]


def test_nose_collection():
    with NamedTemporaryFile() as report, open(os.devnull, 'w') as devnull:
        check_call(
            ['nosetests',
             'tests/data/demo_testsuite.py',
             '--with-comfortsmother',
             '--comfortsmother-package=tests.data.demo',
             '--comfortsmother-output={}'.format(report.name)
             ],
            stdout=devnull,
            stderr=devnull)

        report.seek(0)
        contents = report.read().decode('utf8')
        assert json.loads(contents) == expected_nose


def test_pytest_collection():
    with NamedTemporaryFile() as report, open(os.devnull, 'w') as devnull:
        check_call(
            ['py.test',
             'tests/data/demo_testsuite.py',
             '--comfortsmother=tests.data.demo',
             '--comfortsmother-output={}'.format(report.name)
             ],
            stdout=devnull,
            stderr=devnull)

        report.seek(0)
        contents = report.read().decode('utf8')
        assert json.loads(contents) == expected_pytest
