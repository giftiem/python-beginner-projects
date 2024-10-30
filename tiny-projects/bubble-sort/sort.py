def swap(numbers, a, b):
    """
    Swap the numbers at the indices a and b.
    """
    num_a = numbers[a]
    num_b = numbers[b]
    numbers[a] = num_b
    numbers[b] = num_a



def sort(numbers):
    """
    Sort the numbers using bubble sort.
    """
    #not optimal method but works lol
    length = len(numbers)
    for i in range(length):
        for j in range(length-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j] 

    return numbers
#assume they research bubble sort themselves?
#approx 10min

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

for i in range(3):
    for j in range(3):
        print(i, j)

original_string = "I like cats, cats are cute."
new_string = original_string.replace("cats", "dogs",1)
print(new_string)
