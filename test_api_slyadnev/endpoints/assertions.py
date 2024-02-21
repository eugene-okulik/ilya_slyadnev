class Assertion:
    @staticmethod
    def equal(actual, expected, message=None):
        """
        Проверяет, что два значения равны.
        """
        assert actual == expected, message or f"{actual} != {expected}"

    @staticmethod
    def not_equal(actual, expected, message=None):
        """
        Проверяет, что два значения не равны.
        """
        assert actual != expected, message or f"{actual} == {expected}"

    @staticmethod
    def contains(substring, string, message=None):
        """
        Проверяет, что подстрока содержится в строке.
        """
        assert substring in string, message or f"{substring} not found in {string}"
