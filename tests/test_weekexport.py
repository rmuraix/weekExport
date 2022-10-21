from src import weekexport
import datetime

# import pytest
# import io


def test_check_config():
    config = {"style": "JP", "start": 1, "loop": 1, "days": 1}
    assert weekexport.check_config(config) is True

    config = {"style": "EN", "start": 1, "loop": 1, "days": 1}
    assert weekexport.check_config(config) is True

    config = {"style": "EU", "start": 1, "loop": 1, "days": 1}
    assert weekexport.check_config(config) is False

    config = {"style": "EN", "start": 1, "loop": -1, "days": 1}
    assert weekexport.check_config(config) is False

    config = {"style": "EN", "start": 1, "loop": 1, "days": -1}
    assert weekexport.check_config(config) is False

    # type error
    config = {"style": 1, "start": 1, "loop": 1, "days": 1}
    assert weekexport.check_config(config) is False

    config = {"style": "JP", "start": "text", "loop": 1, "days": 1}
    assert weekexport.check_config(config) is False

    config = {"style": "JP", "start": 1, "loop": "text", "days": 1}
    assert weekexport.check_config(config) is False

    config = {"style": "JP", "start": 1, "loop": 1, "days": "text"}
    assert weekexport.check_config(config) is False

    config = {"style": "EN", "start": 1, "loop": 1, "days": 1}
    assert weekexport.check_config(config) is True


def test_get_monday():
    today = datetime.datetime(2022, 10, 7)
    assert weekexport.get_monday(today, -2) == datetime.datetime(2022, 9, 19)
    assert weekexport.get_monday(today, -1) == datetime.datetime(2022, 9, 26)
    assert weekexport.get_monday(today, 0) == datetime.datetime(2022, 10, 3)
    assert weekexport.get_monday(today, 1) == datetime.datetime(2022, 10, 10)
    assert weekexport.get_monday(today, 2) == datetime.datetime(2022, 10, 17)


def test_genarate_str():
    monday = datetime.datetime(2022, 10, 3)
    config = {"style": "JP", "start": 1, "loop": 1, "days": 1}
    assert weekexport.genarate_str(monday, config) == "10/03(月)\n"

    config = {"style": "JP", "start": 1, "loop": 1, "days": 2}
    assert weekexport.genarate_str(monday, config) == "10/03(月)\n10/04(火)\n"

    config = {"style": "JP", "start": 1, "loop": 2, "days": 2}
    assert (
        weekexport.genarate_str(monday, config)
        == "10/03(月)\n10/04(火)\n10/10(月)\n10/11(火)\n"
    )

    config = {"style": "EN", "start": 1, "loop": 1, "days": 1}
    assert weekexport.genarate_str(monday, config) == "10/03(Mon)\n"


# def test_main(monkeypatch):
#    monkeypatch.setattr('sys.stdin', io.StringIO("1\n4\n"))
#    with pytest.raises(SystemExit) as e:
#        weekexport.main()
#    assert e.type == SystemExit
#    assert e.value.code == 0
