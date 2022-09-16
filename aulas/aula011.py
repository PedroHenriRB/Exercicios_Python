nome = 'Pedro'
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7;97m'}
print(f'Olá! Muito prazer em te conhecer, {cores["pretoebranco"]}{nome}{cores["limpa"]}!!!')