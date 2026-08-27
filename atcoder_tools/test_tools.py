import json
from pathlib import Path

import pytest

from atcoder_tools.download import infer_contest_id, parse_tasks
from atcoder_tools.scaffold import contest_spec, create_contest, normalize_input


def test_normalize_input_accepts_short_and_split_forms():
    assert normalize_input(["abc468"]) == "abc468"
    assert normalize_input(["ABC", "468"]) == "abc468"


@pytest.mark.parametrize(
    ("contest_id", "relative_path", "last_label"),
    [
        ("abc468", Path("ABC/468"), "G"),
        ("arc219", Path("ARC/219"), "F"),
        ("awc0141", Path("AWC/0141"), "E"),
        ("adt_all_20260827_1", Path("ADT/ALL/20260827_1"), "I"),
    ],
)
def test_contest_spec(contest_id: str, relative_path: Path, last_label: str):
    path, labels = contest_spec(contest_id)
    assert path == relative_path
    assert labels[-1] == last_label


def test_create_contest_builds_offline_workspace(tmp_path: Path):
    destination = create_contest("awc0141", repository_root=tmp_path)

    assert destination == tmp_path / "AWC/0141"
    assert (destination / "dl.py").is_file()
    assert (destination / "E/main.py").is_file()
    assert (destination / "E/test_main.py").is_file()
    config = json.loads((destination / "contest.json").read_text())
    assert config == {"contest_id": "awc0141", "labels": list("ABCDE")}


def test_infer_contest_id_from_config_and_path(tmp_path: Path):
    contest = tmp_path / "ABC/468"
    contest.mkdir(parents=True)
    assert infer_contest_id(contest) == "abc468"

    adt = tmp_path / "ADT/ALL/20260827_1"
    adt.mkdir(parents=True)
    assert infer_contest_id(adt) == "adt_all_20260827_1"


def test_parse_tasks_uses_real_task_links_for_adt_compatible_downloads():
    html = """
    <table><tbody><tr>
      <td><a href="/contests/adt_all_20260827_1/tasks/abc470_a">A</a></td>
      <td>Reused problem</td>
    </tr></tbody></table>
    """
    assert parse_tasks(html, "adt_all_20260827_1") == {
        "A": "https://atcoder.jp/contests/adt_all_20260827_1/tasks/abc470_a"
    }
