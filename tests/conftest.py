import pytest
from pathlib import Path


@pytest.fixture
def fixtures_dir():
    return Path(__file__).parent / 'test_data'


@pytest.fixture
def file1_path_json(fixtures_dir):
    return fixtures_dir / 'file1.json'


@pytest.fixture
def file2_path_json(fixtures_dir):
    return fixtures_dir / 'file2.json'


@pytest.fixture
def file1_yaml(fixtures_dir):
    return fixtures_dir / 'file1.yaml'


@pytest.fixture
def file2_yaml(fixtures_dir):
    return fixtures_dir / 'file2.yaml'
