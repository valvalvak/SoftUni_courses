from typing import List

from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details(pokemon)}"

    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"
            else:
                return "Pokemon is not caught"

    def trainer_data(self):
        nl = "\n"
        # return \
        #     f"Pokemon Trainer {self.name}{nl}"\
        #     f"Pokemon count {len(self.pokemons)}{nl}"\
        #     f"- {nl.join([pokemon.pokemon_details() for pokemon in self.pokemons])}"
        print_solution = ''
        print_solution += f'Pokemon Trainer {self.name}{nl}'
        print_solution += f'Pokemon count {len(self.pokemons)}{nl}'
        for pokemon in self.pokemons:
            print_solution += f'- {pokemon.pokemon_details()}{nl}'
        return print_solution


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
second3_pokemon = Pokemon("Charizard3", 330)
second4_pokemon = Pokemon("Charizard4", 440)
second5_pokemon = Pokemon("Charizard5", 555)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second3_pokemon))
print(trainer.add_pokemon(second4_pokemon))
print(trainer.add_pokemon(second5_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
