def temperature():
    
    temp = float(input("Enter the temperature: "))
    
    
    choice = input(" Please enter 'C' for Convert to Celsius or 'F' for Convert to Fahrenheit : ").strip().upper()
    
    
    if choice == 'C':
        converted_temp = (temp - 32) * 5/9
        print(f"{temp} Fahrenheit is {converted_temp:.2f} Celsius.")
    elif choice == 'F':
        converted_temp = (temp * 9/5) + 32
        print(f"{temp} Celsius is {converted_temp:.2f} Fahrenheit.")
    else:
        print("Invalid choice. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    

temperature()
