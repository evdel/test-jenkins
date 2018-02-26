from program import add


class TestProgram(object):

  def test_add(self):
    assert add(1, 1) == 2
