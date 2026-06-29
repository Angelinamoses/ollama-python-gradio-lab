def count_numbers():

    print("Starting...")

    yield "Artificial"

    print("Contributing..")
    
    yield "Intelligence"
    
    print("Almost done...")

    yield "is"

    print("Almost...")

    yield "Amazing"

    print("Finished!")

numbers = count_numbers()

for number in numbers:
 print(number)