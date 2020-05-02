import pytest

from workouts import print_workout_days


def test_print_workout_days(capsys):
    param = "lower body"
    expected = "Tue, Fri\n"
    print_workout_days(workout=param)
    captured = capsys.readouterr()
    assert captured.out == expected

    param = "n/a"
    expected = "No matching workout\n"
    print_workout_days(workout=param)
    captured = capsys.readouterr()
    assert captured.out == expected

    param = "e"
    expected = "Mon, Tue, Thu, Fri\n"
    print_workout_days(workout=param)
    captured = capsys.readouterr()
    assert captured.out == expected

    param = "30 min cardio"
    expected = "Wed\n"
    print_workout_days(workout=param)
    captured = capsys.readouterr()
    assert captured.out == expected
