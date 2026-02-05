def number_pipeline(numbers):
    # Implement the generator-based pipeline here
    for i in numbers:
        if i % 2 == 0:
            even_num = i
            sqr_num = even_num **2
            if sqr_num > 20:
                yield sqr_num
                

# Example usage:
result = number_pipeline([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for value in result:
    print(value)
