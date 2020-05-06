from datetime import date


users = [
    {
        'email': 'cvander@platzi.com',
        'firt_name': 'Christian',
        'last_name': 'Van der Henst',
        'password': 'secret',
        'is_admin': True
    },
    {
        'email': 'freddier@platzi.com',
        'firt_name': 'Freddy',
        'last_name': 'Vega',
        'password': 'secret1'        
    },
        {
        'email': 'yesica@platzi.com',
        'firt_name': 'Yesica',
        'last_name': 'Cortes',
        'password': 'qerty',
        'birthdate': date(1990, 12, 19)
    },
        {
        'email': 'arturo@platzi.com',
        'firt_name': 'Arturo',
        'last_name': 'Martinez',
        'password': 'msicomputer',
        'is_admin': True,
        'birthdate': date(1981, 11, 6),
        'bio': "The path of the rigtheous man is best on all sides by the inquities of the selfish and"
    },
]

from posts.models import User

for user in users:
    obj = User.object.create(**user)
    print(obj.pk)