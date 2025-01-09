#1
student = {
    'student1': {'name': 'Alice', 'age': 18, 'grade': 'A'},
    'student2': {'name': 'Bob', 'age': 17, 'grade': 'B'},
    'student3': {'name': 'Charlie', 'age': 16, 'grade': 'C'}
}
print(f"{student['student2']["name"]}の年齢は{student['student2']["age"]}歳です")
print("---------")
#2
nested_dict = {

    "user": {

        "name": "Alice",

        "age": 30,

        "location": "Tokyo",

        "preferences": {

            "food": ["sushi", "ramen", "tempura"],

            "music": ["jazz", "classical", "pop"]

        }

    },

    "order": {

        "id": 12345,

        "items": [

            {"name": "Laptop", "price": 1000, "quantity": 1},

            {"name": "Mouse", "price": 50, "quantity": 2}

        ],

        "status": "shipped"

    },

    "company": {

        "name": "TechCorp",

        "address": {

            "street": "123 Main St",

            "city": "San Francisco",

            "state": "CA",

            "zip": "94105"

        },

        "employees": [

            {"name": "Bob", "position": "Manager"},

            {"name": "Carol", "position": "Developer"}

        ]

    }

}
print(nested_dict['user']["name"])
print(nested_dict['user']["preferences"]["food"])
print(nested_dict["order"]["items"][0]["name"])
print(nested_dict["company"]["address"]["city"])
print(nested_dict["company"]["employees"][1]["position"])