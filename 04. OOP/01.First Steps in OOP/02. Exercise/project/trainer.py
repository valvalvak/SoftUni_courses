from pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon.name not in self.pokemons:
            self.pokemons.append(pokemon.name)
            return f"Caught {pokemon.name} with health {pokemon.health}"
        else:
            return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        if pokemon_name not in self.pokemons:
            return "Pokemon is not caught"
        else:
            self.pokemons.remove(pokemon_name)
            return "You have released {pokemon_name}"

    def trainer_data(self):
        pass
