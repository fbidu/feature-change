from feature_change import change


def test_change_logs(mocker):

    mock = mocker.Mock()

    def new_sum(a, b):
        return a + b

    @change(new=new_sum, log=mock.log)
    def old_sum(a, b):
        return a + b + 1

    old_sum(1, 2)

    mock.log.assert_called()
