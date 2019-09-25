class Pokemon:
    """
    Pokemon entity
    """

    def __init__(self, index, name, type1, type2, total, hp, attack, defense, special_atk, special_def, speed, gen, is_legendary):
        self.index = index
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.total = total
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_atk = special_atk
        self.special_def = special_def
        self.speed = speed
        self.generation = gen
        self.is_legendary = is_legendary

    def __lt__(self, other):
        return self.index < other.index

    def __gt__(self, other):
        return other < self

    def __eq__(self, other):
        return self.index == other.index

    def __ne__(self, other):
        return not self == other

    def scientific_name(self):
        sci_name = self.name + "ius " + self.type1 + "imus " + self.type2 + "ionis"

        if self.is_legendary:
            sci_name += " Legendarus"

        sci_name = sci_name.replace('e', 'u')
        sci_name = sci_name.replace('y', 'i')

        return sci_name

    def __str__(self):
        leg = "legendary" if self.is_legendary else "not legendary"
        poke_str = """########### - {11} - #############
                   # name: {0} HP: {1}
                   # {2}/{3}  
                   # ATK: {4} DEF: {5}
                   # SP. ATK: {6} SP. DEF: {7}
                   # SPD: {8}
                   # GEN: {9}     {10}
                   ##################################""".format(self.name, self.hp,
                                                      self.type1, self.type2,
                                                      self.attack, self.defense,
                                                      self.special_atk, self.special_def,
                                                      self.speed,
                                                      self.generation, leg, self.index)
        poke_str = '\n'.join([line.strip() for line in poke_str.splitlines()])
        return poke_str


def test_poke():
    test_bulb = Pokemon(3, "Bulbasaur", "Grass", "Poison", 214, 100, 15, 20, 14, 20, 16, 1, False)

    test_gorby = Pokemon(513, "Gorby Pirog", "Fire", "Psychic", 513, 240, 50, 60, 12, 75, 54, 4, True)

    print(test_bulb)
    print(test_bulb.scientific_name())

    print(test_gorby)
    print(test_gorby.scientific_name())

    print("Gorby < Bulbasaur?")
    print(test_gorby < test_bulb)

    print("Bulbasaur < Gorby?")
    print(test_bulb < test_gorby)

    print("Gorby > Bulbasaur?")
    print(test_gorby > test_bulb)

    print("Bulbasaur > Gorby?")
    print(test_bulb > test_gorby)

    print("Gorby == Bulbasaur?")
    print(test_gorby == test_bulb)

    print("Bulbasaur == Gorby?")
    print(test_bulb == test_gorby)

    print("Gorby != Bulbasaur?")
    print(test_gorby != test_bulb)

    print("Bulbasaur != Gorby?")
    print(test_bulb != test_gorby)


def read_pokemon(poke_csv):
    poke_list = list()

    with open(poke_csv, 'r') as poke_file:

        rows = poke_file.readlines()
        rows.pop(0)

        rows = list(map(lambda poke_row: poke_row.strip(), rows))

        poke_attribute_list = list()
        for row in rows:
            row = row.split(',')
            poke_attribute_list.append(row)

        for poke_info in poke_attribute_list:
            legendary = True if poke_info[12] == "True" else False

            #                         Index:           Name:         Type 1:       Type 2:
            new_pokemon = Pokemon(int(poke_info[0]), poke_info[1], poke_info[2], poke_info[3],
                                  #     Total:              HP:               ATK:              DEF:
                                  int(poke_info[4]), int(poke_info[5]), int(poke_info[6]), int(poke_info[7]),
                                  #     Sp. ATK:         Sp. DEF:            Speed:               Gen:
                                  int(poke_info[8]), int(poke_info[9]), int(poke_info[10]), int(poke_info[11]), legendary)

            poke_list.append(new_pokemon)

    return poke_list

def poke_search_name(poke_list):
    query = input("Enter name of Pokemon to search for: \n")

    found = False
    for pokemon in poke_list:
        if pokemon.name.lower() == query.lower():
            print(pokemon.scientific_name())
            found = True

    if not found:
        print("Pokemon not found!")


def poke_search_index(poke_list):
    query = 0
    try:
        query = int(input("Enter the index of the Pokemon to search for: \n"))
    except ValueError:
        print("Please enter a number!")
        return

    found = False
    for pokemon in poke_list:
        if pokemon.index == query:
            print(pokemon)
            found = True

    if not found:
        print("Pokemon not found!")

#poke_search_name(read_pokemon_hash("pokemon.csv"))

#poke_search_index(read_pokemon_hash("pokemon.csv"))