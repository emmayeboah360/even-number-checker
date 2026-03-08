# a python function to accept 20 inputs and check whether they are even numbers


def even_checker():
    count = 0
    even = 0
    while count < 10:
        count += 1
        try:

            request_input = int(input(" Enter the number "))
            if request_input % 2 == 0:

                print("Number is even")
                even += 1

            else:
                print("Number entered is not an even number")

        except ValueError:
            print("Please enter a number")

    print(f"We have {even} even numbers")


even_checker()
