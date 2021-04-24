import requests


def recipe_search(ingredient):

    app_id = '46c678f9'
    app_key = '98b90d6e3f70e675e33e5e31eaf13b1e'
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = result.json()

    return data['hits']


def run():
    ingredient = input('Enter an ingredient: ')

    results = recipe_search(ingredient)

    for result in results:
        recipe = result['recipe']

        print('\n' + recipe['label'])
        print(recipe['uri'])


run()