class TestText:
    def test_check_text(self):
        text = input("Set а text less than 15 characters long: ")
        assert len(text) < 14, f"Your text has length more then 15 characters"

