import requests


def recipe_search(ingredient):

    app_id = '46c678f9'
    app_key = '98b90d6e3f70e675e33e5e31eaf13b1e'
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = result.json()

    return data['hits']


def save_recipes(ingredient, results):
    choice = input('\nDo you want to save these recipes? ')
    results = recipe_search(ingredient)

    if choice == 'y' or choice == 'Yes' or choice == 'yes' or choice == 'YES':
        file = open('recipes.txt', 'a+')
        try:
            file.write('Saved recipes for {}:'.format(ingredient))
            for result in results:
                recipe = result['recipe']

                file.write('\n' + recipe['label'])
                file.write('\nCooking time:' + str(recipe['totalTime']))
                file.write('\n' + 'Diet labels:' + str(recipe['dietLabels']))
                file.write('\n' + 'Health labels:' + str(recipe['healthLabels']))
                file.write('\n' + recipe['shareAs'] + '\n')

            file.write('\n')
        finally:
            file.close()
        print('Done! Thank you! Enjoy your meal.')
    else:
        print('Okay, that\'s it then. Enjoy!')


def run():
    ingredient = input('Enter an ingredient: ')
    # in theory, you can also search for a certain cuisine, diet (i.e. vegan) or meal type
    # and it will still display recipes that match that criteria

    results = recipe_search(ingredient)
    for result in results:
        recipe = result['recipe']
        print('\n' + recipe['label'])
        print('\nCooking time:' + str(recipe['totalTime']))
        print('Diet labels:' + str(recipe['dietLabels']))
        print('Health labels:' + str(recipe['healthLabels']))
        print(recipe['shareAs'])

    save_recipes(ingredient, results)


run()
