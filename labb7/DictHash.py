from labb1.PokemonFile import Pokemon


class HashNode:
    def __init__(self, key="", data=None):
        self.key = key
        self.data = data


class HashTable:

    def __init__(self, size):
        """ size: size of hashtable"""
        # Create slots to put key,val pairs into
        # The number of available slots should be
        # higher than the maximum input of keys,
        # there should be sufficient "empty room"
        self.total_size = round(size * 1.3)

        self.hashtable = [[] for _ in range(self.total_size)]

        # kind of type overloading a la python
        # used in the hashing function
        self.type_map = {
            str: self.hash_string,
            int: self.hash_int
        }

    def hash_string(self, string):
        hash_sum = 0
        for i in range(len(string)):
            hash_sum += ord(string[i]) * (i+1)
        return hash_sum % self.total_size

    def hash_int(self, number):
        # Using the mid-square method
        # Square, then convert to str to get the middle digits
        num_hash = str(number**2)

        # Getting the middle value, use floor division
        # to avoid fractions
        middle = len(num_hash) // 2

        # Make it return an index in the span of the
        # table size
        return int(num_hash[middle:middle+2]) % self.total_size

    def store(self, key, data):
        """
        :param key: key to retrieve data
        :param data: data stored
        """
        hash_val = self.hashfunction(key)
        already_exists = False
        new_node = HashNode(key, data)

        krocklist = self.hashtable[hash_val]

        # Go through the chain/krocklist and see if the key already exists, as well
        # as getting the index of where to insert the new node
        for i, node in enumerate(krocklist):
            # Could just use "key == ...", but this is clearer in my opinion
            if new_node.key == node.key:
                already_exists = True
                break

        # i gets assigned and keeps value out of scope in the enumerate
        if already_exists:
            # if key already exists, replace it
            krocklist[i] = new_node
        else:
            krocklist.append(new_node)

    def search(self, key):
        """
        :param key: key to search after
        :return: data
        """
        hash_val = self.hashfunction(key)
        data = None
        # get the chain/krocklist at the supposed
        # index of the key
        krocklist = self.hashtable[hash_val]
        for node in krocklist:
            if node.key == key:
                data = node.data
                break
        # return data if we find it
        if data is not None:
            return data
        # if not, it means the key didnt exist, and we raise an error
        else:
            raise KeyError

    def hashfunction(self, key):
        """
        :param key:
        :return: index of key
        Calculates index for key
        """
        # depending on the type of the key, we use redirect to
        # the appropriate function, instead of cluttering
        # the function with "if isinstance(str): [...]" and
        # getting a huge function.
        return self.type_map[type(key)](key)



class DictHash:

    def __init__(self):
        self.hashdict = dict()

    def store(self, key, data):
        self.hashdict[key] = data

    def search(self, key):
        return self.hashdict[key]

    def __getitem__(self, key):
        return self.search(key)

    def __contains__(self, key):
        if key in self.hashdict:
            return True
        else:
            return False


def read_pokemon_hash(poke_csv):
    poke_dict = DictHash()

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

            poke_dict.store(new_pokemon.name, new_pokemon)

    return poke_dict


def main():
    poke_dict = read_pokemon_hash("pokemon.csv")

    print(poke_dict.search("Charizard"))


if __name__=="__main__":
    main()
