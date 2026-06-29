import sys


def pytest_collect_file(parent, file_path):
    """Isolate each problem's solution.py before pytest imports its test file.

    Without this, the second test file's `from solution import Solution` hits
    the sys.modules cache and gets the wrong Solution class.
    """
    if file_path.name.startswith("test_") and file_path.suffix == ".py":
        problem_dir = str(file_path.parent)
        sys.modules.pop("solution", None)
        if problem_dir in sys.path:
            sys.path.remove(problem_dir)
        sys.path.insert(0, problem_dir)
    return None
