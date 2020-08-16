# pylint: disable=invalid-name,missing-module-docstring
from feature_change import change


def test_change_logs_on_diff(mocker):
    """
    Tests if the decorator works on different output
    """
    mock = mocker.Mock()

    @change(new=mock.new, on_diff=mock.log)
    def old_sum(a, b):
        """
        Sample wrong sum
        """
        return a + b + 1

    result = old_sum(1, 2)

    mock.log.assert_called()
    mock.new.assert_called()
    assert result == 4


def test_change_logs_on_call(mocker):
    """
    Tests if the decorator works on every call
    """
    mock = mocker.Mock()

    @change(new=mock.new, on_call=mock.log)
    def old_sum(a, b):
        """
        Sample wrong sum
        """
        return a + b + 1

    result = old_sum(1, 2)

    mock.log.assert_called()
    mock.new.assert_called()
    assert result == 4
