from typing import List
from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[
            Pokemon] = []  # tipizaciq it helps you down the code to see the methods when typing it helps you

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"  # call the method from the pokemon project file REUSE IT 'DRY' - DO NOT REPEAT YOURSELF

    def release_pokemon(self, pokemon_name: str):
        # for p in self.pokemons:
        #     if p.name == pokemon_name:
        #         self.pokemons.remove(p)
        #         return f"You have released {pokemon_name}"

        pokemon_to_release = next((p for p in self.pokemons if p.name == pokemon_name), None) #faster and more optimised than 'for' cycle
        if pokemon_to_release:
            self.pokemons.remove(pokemon_to_release)
            return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self):
        result = [f"Pokemon Trainer {self.name}",
                  f"Pokemon count {len(self.pokemons)}"]
        for p in self.pokemons:
            result.append(f" - {p.pokemon_details()}")

            return "\n".join(result)
