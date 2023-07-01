import tkinter as tk

# Conversion rates
conversion_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.73,
    "CAD": 1.23,
    "AUD": 1.33,
    "JPY": 110.94,
    "CNY": 6.45,
    "INR": 74.65,
    "BRL": 5.15,
    "RUB": 72.51,
    "NZD": 1.42,
    "SEK": 8.66,
    "CHF": 0.92,
    "NOK": 9.49,
    "MXN": 20.14,
    "SGD": 1.35,
    "HKD": 7.77,
    "KRW": 1178.76,
    "ZAR": 14.32,
    "TRY": 8.52
}

def convert_currency():
    amount = float(amount_entry.get())
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()

    # Perform the currency conversion calculation
    converted_amount = amount / conversion_rates[from_currency] * conversion_rates[to_currency]

    # Display the converted amount
    converted_label.config(text=f"{converted_amount:.2f} {to_currency}")

# Create the main window
window = tk.Tk()
window.title("Currency Converter")

# Create the GUI components
amount_label = tk.Label(window, text="Amount:")
amount_label.pack()
amount_entry = tk.Entry(window)
amount_entry.pack()

from_currency_label = tk.Label(window, text="From Currency:")
from_currency_label.pack()
from_currency_var = tk.StringVar(window)
from_currency_option = tk.OptionMenu(window, from_currency_var, *conversion_rates.keys())
from_currency_option.pack()

to_currency_label = tk.Label(window, text="To Currency:")
to_currency_label.pack()
to_currency_var = tk.StringVar(window)
to_currency_option = tk.OptionMenu(window, to_currency_var, *conversion_rates.keys())
to_currency_option.pack()

convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.pack()

converted_label = tk.Label(window, text="")
converted_label.pack()

# Start the GUI event loop
window.mainloop()

