from click.testing import CliRunner
from auto_gmail_creator.cli import cli
import json


def test_cli_generates_and_exports_json(tmp_path):
    runner = CliRunner()
    out_file = tmp_path / "out.json"
    result = runner.invoke(
        cli,
        [
            "generate",
            "--count", "3",
            "--output", "json",
            "--output-path", str(out_file),
            "--acknowledge-simulation",
            "--seed", "123",
        ],
    )
    assert result.exit_code == 0, result.output
    assert out_file.exists()
    data = json.loads(out_file.read_text(encoding="utf-8"))
    assert isinstance(data, list)
    assert len(data) == 3
    assert all("@gmail.com" in d["email"] for d in data)
