persona={"firs_name":"Edem", "last_name":"Terraza", "age":31, "country":"peru", "is_married":True, "skills":["JavaScript", "React", "Node", "MongoDE", "Python"], "address":{"street":"Space_street", "zipcode":"02210"}}
if "skills" in persona:
    print("Si existe la clave habilidades.")
    print(persona["skills"][2])
if "skills" in persona:
    print("Si existe la clave habilidades.")
    if "Python" in persona["skills"]:
        print("La persona si tiene la habilidad python")
if ("JavaScript" and "React") in persona["skills"]:
    print("El es un desarrollador frontend")
elif("Node" and "Python" and "MongoDE") in persona["skills"]:
    print("El es un desarrollador backend")
elif("React" and "Node" and "MongoDE") in persona["skills"]:
    print("El es un desarrollador fullstack")
else:
    print("Titulo desconocido")