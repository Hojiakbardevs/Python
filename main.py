import random
print(random.randrange(1,11))
avtolar = ["kia","hyundai","toyota","sonata","bmw","honda","gm"]
for avto in avtolar:
    if len(avto) <= 3:
        print(avto.upper())
    else:
        print(avto.title())
