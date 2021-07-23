class Trainer:
    tariner_counter = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Trainer.tariner_counter
        Trainer.tariner_counter += 1

    @staticmethod
    def get_next_id():
        return Trainer.tariner_counter

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
