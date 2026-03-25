from cards_module.tests.test_mapper import run_test as mapper_test
from cards_module.tests.test_validator import run_test as validator_test


if __name__ == "__main__":
    validator_test()
    mapper_test()
    print("All smoke tests: OK")
