from solution import strict
import pytest


@pytest.mark.parametrize(
    "arg_1, arg_2, arg_1_type, arg_2_type, expected_result", [
        (1, 2, int, int, '1 & 2'),
        (1, 2, int, float, ValueError),
        (True, 2, bool, bool, ValueError),
        ('1', 2, str, int, '1 & 2'),
        (1.3, False, str, bool, ValueError),
    ]
)
def test_strict(arg_1, arg_2, arg_1_type, arg_2_type, expected_result):
    @strict
    def get_sum_str(a: arg_1_type, b: arg_2_type) -> str:
        return f'{a} & {b}'

    try:
        result = get_sum_str(arg_1, arg_2)
    except ValueError:
        result = ValueError

    assert result == expected_result
