class User:
    
    def __init__(self, username: str, password: str, cod_profile: str):
        self.username = username
        self.cod_profile = cod_profile
        self._password = password


    @staticmethod
    def generate_cod_profile(username):
        new_username = username.replace(' ', '') 
        letters = [letter for letter in new_username] # Quebra o username letra por letra
        letters_size = len(letters)
        for _ in range(letters_size):
            random_letter = hash(str(username) + str(_)) % letters_size # Pega o hash de usernamme junto de letter e faz divisão inteira pelo tamanho do nome
            letters[_], letters[random_letter] = letters[random_letter], letters[_] # Embaralha a leita
        four_letters = ''.join(letters)[0:4] # Cria uma string com o nome embaralhado e pega as 4 primeiras letras
        hash_four_letters = hash(four_letters) # Gera um hash das 4 primeiras letras
        if hash_four_letters < 0:
            hash_four_letters = hash_four_letters * -1 # Passa positivo se for negativo
        str_hash = str(hash_four_letters)
        if len(str_hash) < 6:
            str_hash = str_hash.zfill(6) # Preenche com zero se quantidade caracteres for menor que 6
        five_numbers = str_hash[0:6]
        return four_letters + '@' + five_numbers