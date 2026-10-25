"""Tests de fumée : vérifient que le package peut être importé."""


def test_package_imports():
    import {{ cookiecutter.module_name }}

    assert {{ cookiecutter.module_name }}.__version__


def test_project_paths_are_defined():
    from {{ cookiecutter.module_name }}.config import PROJECT_ROOT, RAW_DATA_DIR

    assert PROJECT_ROOT.exists()
    assert RAW_DATA_DIR.name == "raw"
