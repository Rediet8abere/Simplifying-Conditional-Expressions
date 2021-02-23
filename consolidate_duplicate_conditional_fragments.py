# by Kami Bigdely
# Consolidate duplicate conditional fragments
def add(mix, something):
    mix.append(something)
    return mix

def mixer_ice_with_cream():
    print('mixed ice with cream.')
    return ['ice', 'cream']

def make_drink(drink, addons):
    mix = []
    if flavor == 'coffee':
        mix = add(mix, 'coffee')
    else:
        mix = mixer_ice_with_cream()
        mix = add(mix, 'strawberry')
        mix = add(mix, addons)
    return mix

final_drink = make_drink('strawberry milkshake', ['milk','sugar'])
print(final_drink)
