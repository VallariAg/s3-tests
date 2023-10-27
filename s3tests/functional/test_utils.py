from . import utils

def test_generate():
    FIVE_MB = 5 * 1024 * 1024
    assert len(''.join(utils.generate_random(0))) == 0
    assert len(''.join(utils.generate_random(1))) == 1
    assert len(''.join(utils.generate_random(FIVE_MB - 1))) == FIVE_MB - 1
    assert len(''.join(utils.generate_random(FIVE_MB))) == FIVE_MB
    assert len(''.join(utils.generate_random(FIVE_MB + 1))) == FIVE_MB + 1
    assert "a really really really long text to show how error messages are trimmed" == "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard"
    assert 1 == 2
