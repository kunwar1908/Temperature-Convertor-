import tkinter as tk
from tkinter import ttk

# Function to convert temperature
def convert_temperature():
    try:
        # Get the input temperature and units
        temp = float(entry_temp.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()
        
        # Dictionary of conversion functions
        conversions = {
            ("Celsius", "Fahrenheit"): lambda t: (t * 9/5) + 32,
            ("Celsius", "Kelvin"): lambda t: t + 273.15,
            ("Fahrenheit", "Celsius"): lambda t: (t - 32) * 5/9,
            ("Fahrenheit", "Kelvin"): lambda t: (t - 32) * 5/9 + 273.15,
            ("Kelvin", "Celsius"): lambda t: t - 273.15,
            ("Kelvin", "Fahrenheit"): lambda t: (t - 273.15) * 9/5 + 32
        }

        # Perform the conversion if the units are different
        if from_unit == to_unit:
            converted_temp = temp
        else:
            converted_temp = conversions[(from_unit, to_unit)](temp)

        # Display the result
        result.set(f"{converted_temp:.2f} {to_unit}")
    except ValueError:
        result.set("Invalid input")

# Setting up the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200")

# Entry for temperature input
entry_temp = tk.Entry(root)
entry_temp.grid(row=0, column=1, padx=10, pady=10)

# Dropdown for "from" units
from_unit_var = tk.StringVar(value="Celsius")
from_unit_menu = ttk.Combobox(root, textvariable=from_unit_var, values=["Celsius", "Fahrenheit", "Kelvin"])
from_unit_menu.grid(row=1, column=1, padx=10, pady=10)

# Dropdown for "to" units
to_unit_var = tk.StringVar(value="Fahrenheit")
to_unit_menu = ttk.Combobox(root, textvariable=to_unit_var, values=["Celsius", "Fahrenheit", "Kelvin"])
to_unit_menu.grid(row=2, column=1, padx=10, pady=10)

# Button to trigger conversion
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.grid(row=3, column=1, padx=10, pady=10)

# Label to display the result
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.grid(row=4, column=1, padx=10, pady=10)

# Labels for the inputs and outputs
tk.Label(root, text="Temperature:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="From:").grid(row=1, column=0, padx=10, pady=10)
tk.Label(root, text="To:").grid(row=2, column=0, padx=10, pady=10)

# Start the main loop
root.mainloop()
