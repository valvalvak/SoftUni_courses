class EncryptionGenerator:
    def __init__(self, text: str):
        self.text = text

    def __add__(self, other: int):
        if not isinstance(other, int):
            raise ValueError("You must add a number.")
        result = ""

        for ch in self.text:
            encoded_ch = ord(ch) + other
            while encoded_ch < 32:
                encoded_ch += 95
            while encoded_ch > 126:
                encoded_ch -= 95
            result += chr(encoded_ch)
        return result
