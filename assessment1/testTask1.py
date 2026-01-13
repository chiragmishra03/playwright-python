import pytest

def run_test(message):
    print(message)

@pytest.mark.smoke
def test_smoke_example(setup):
    run_test("Executing smoke test")

@pytest.mark.regression
def test_regression_example(setup):
    run_test("Executing regression test")

@pytest.mark.skip(reason="Not required now")
def test_skip_example(setup):
    run_test("Executing skip test")
