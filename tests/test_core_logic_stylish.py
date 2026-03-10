from gendiff.core import generate_gendiff


def test_generate_diff_json(file1_path_json, file2_path_json, fixtures_dir):
    result = generate_gendiff(file1_path_json, file2_path_json)

    expected_file = fixtures_dir / "expected_json_stylish.txt"
    expected = expected_file.read_text().strip()

    assert result.strip() == expected


def test_generate_diff_yaml(file1_yaml, file2_yaml, fixtures_dir):
    result = generate_gendiff(file1_yaml, file2_yaml)

    expected_file = fixtures_dir / "expected_yaml_stylish.txt"
    expected = expected_file.read_text().strip()

    assert result.strip() == expected
