# Taken from PorePy
import glob
import os
import sys

import pytest

# Alternatively (safer): collect from all lab*, then filter manually
all_notebooks = glob.glob("lab/lab*/ex*.ipynb")

# Filter out lab0 and files containing "text"
TUTORIAL_FILENAMES = [
    f
    for f in all_notebooks
    if not os.path.basename(f)
    .lower()
    .__contains__("text")  # exclude "text" in filename
    and not f.startswith("lab/lab0/")  # exclude lab0 folder
    and not f.startswith("lab/lab1/")  # exclude lab1 folder
]
print(all_notebooks)


@pytest.mark.tutorials
@pytest.mark.parametrize("tutorial_path", TUTORIAL_FILENAMES)
def test_run_tutorials(tutorial_path: str):
    """We run the tutorial and check that it didn't raise any error.
    This assumes we run pytest from the pygeon directory.

    """
    new_file = tutorial_path.removesuffix(".ipynb") + ".py"

    # This command might fail in github actions.
    cmd_convert = "jupyter-nbconvert --to script " + tutorial_path
    status = os.system(cmd_convert)
    if status != 0:
        raise RuntimeError(
            ".ipynb file is not converted to .py file. Is jupyter-nbconvert available?"
        )
    edit_imports(new_file)

    cmd_run = "python " + str(new_file)
    status = os.system(cmd_run)

    assert status == 0

    # Removing the generated source file after the assertion. If the test fails, it is
    # useful to keep it in order to see what went wrong there.
    os.remove(new_file)


def edit_imports(filename: str):
    """Matplotlib opens a new window for each figure in the interactive mode.
    Here, we prevent it by setting the noninteractive matplotlib backend.
    "template" backend is a dummy backend that does nothing.
    Also, we cd to the tutorials directory.

    """
    with open(filename, encoding="utf-8") as f:
        content = f.readlines()

    folder = os.path.dirname(filename)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"import os; os.chdir('{folder}')\n")
        f.write("import matplotlib; matplotlib.use('template')\n")
        f.writelines(content)


if __name__ == "__main__":
    try:
        filenames = [sys.argv[1]]
    except IndexError:
        filenames = TUTORIAL_FILENAMES
    print(filenames)
    # for tut_path in filenames:
    #    test_run_tutorials(tutorial_path=tut_path)
