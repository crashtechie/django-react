import os
import sys

import django  # type: ignore
from django.conf import settings  # type: ignore
from django.test.utils import get_runner  # type: ignore

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "customer_management.settings")
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["customers.tests"])
    if failures:
        sys.exit(bool(failures))
