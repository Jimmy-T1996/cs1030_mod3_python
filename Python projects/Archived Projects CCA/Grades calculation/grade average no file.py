
gradelist = []

def input_function():
    while True:
        user_input = input("Please enter a grade (or type 'done' to finish): ")
        
        if user_input.lower() == "done":
            if gradelist:
                avgfun(gradelist)
            else:
                print("No grades were entered.")
            break
        
        if user_input.isdigit():
            gradelist.append(int(user_input))
        else:
            print("Please enter a whole number or 'done' to finish.")

def avgfun(gradelist):
    mean = sum(gradelist) / len(gradelist)
    print("Average grade:", mean)
    return mean

input_function()

