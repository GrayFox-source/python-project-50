import pytest
from pathlib import Path

@pytest.fixture
def fixtures_dir():
    return Path(__file__).parent / 'test_data'

@pytest.fixture
def file1_path(fixtures_dir):
    return fixtures_dir / 'file1.json'

@pytest.fixture
def file2_path(fixtures_dir):
    return fixtures_dir / 'file2.json'