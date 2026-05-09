personas = [
    {"nombre": "María", "edad": 17},
    {"nombre": "Juan", "edad": 22},
    {"nombre": "Lucía", "edad": 19},
    {"nombre": "Pedro", "edad": 16}
]

mayores = [p for p in personas if p["edad"] > 18]
print(mayores)