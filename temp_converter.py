def c_to_f(c):
    return(c * 9/5)+32

def c_to_k(c):
    return c + 273.15

def f_to_c(f):
    return (f -32) * 9/5

def f_to_k(f):
    return (f - 32) * 9/5 + 273.15

def k_to_c(k):
    return k - 273.15

def k_to_f(k):
    return (k - 273.15) * 9/5 + 32

def main():
    print("\n Temprature Converter") # Application for weather temperature 
    print("1. Celcius to fehrenhit") # Celcius to fehrenhit
    print("2. Celsious to kelvin")   # Celsious to kelvin
    print("3. Fehrenhit to celsius") # Fehrenhit to celsius
    print("4. Fehrenhite to kelvin") #Test PR
    print("5. Kelvin to celcius")
    print("6. Kelvin to Fehrenhite")

    choice = int(input("\n Choose an option 1-6: "))
    value = float(input("Enter temperature value: "))
    if choice == 1:
        print(f"{value} \N{DEGREE SIGN} C ={c_to_f(value):.2f} \N{DEGREE SIGN}F")
    elif choice == 2:
        print(f"{value} \N{DEGREE SIGN} C={c_to_k(value):.2f}\N{DEGREE SIGN}K")
    elif choice == 3:
        print(f"{value}\N{DEGREE SIGN}F={f_to_c(value):.2f}\N{DEGREE SIGN}C")
    elif choice == 4:
        print(f"{value}\N{DEGREE SIGN}F={f_to_k(value):.2f}\N{DEGREE SIGN}K")
    elif choice == 5:
        print(f"{value}\N{DEGREE SIGN}K={k_to_c(value):.2f}\N{DEGREE SIGN}C")
    elif choice == 6:
        print(f"{value}\N{DEGREE SIGN}K={k_to_f(value):.2f}\N{DEGREE SIGN}F")
    else:
        print("Invalid option please choose valid option 1-6")

if __name__ == "__main__":
    main()

