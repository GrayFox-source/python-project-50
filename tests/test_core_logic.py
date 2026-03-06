from gendiff.core import generate_gendiff


def test_generate_diff_plain(file1_path, file2_path, fixtures_dir):
    result = generate_gendiff(file1_path, file2_path)

    expected_file = fixtures_dir / 'expected_plain.txt'
    expected = expected_file.read_text().strip()

    assert result.strip() == expected
