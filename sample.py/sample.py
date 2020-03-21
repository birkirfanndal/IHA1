def add(numbers):
    if numbers == "":
        return "0"
    elif "," not in numbers:
        return str(numbers)
    else:
        num_list = numbers.split(",")
        num_sum = int(num_list[0])+ int(num_list[1])
        return str(num_sum)
