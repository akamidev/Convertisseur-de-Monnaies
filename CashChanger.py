import requests
import tkinter as tk
from tkinter import ttk, messagebox

# Clé API et URL de base (remplace "YOUR_API_KEY" avec ta clé API)
API_KEY = '41ea3f2878803fa935604357'
URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

# Fonction pour obtenir les taux de change
def get_exchange_rates(base_currency="USD"):
    response = requests.get(URL + base_currency)
    if response.status_code == 200:
        return response.json()['conversion_rates']
    else:
        messagebox.showerror("Erreur", "Impossible de récupérer les taux de change.")
        return None

# Fonction pour convertir la monnaie
def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = combo_from.get()
        to_currency = combo_to.get()
        rates = get_exchange_rates(from_currency)
        
        if rates and to_currency in rates:
            converted_amount = amount * rates[to_currency]
            label_result.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            messagebox.showerror("Erreur", "Impossible de convertir la monnaie.")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un montant valide.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Convertisseur de Monnaies AKAMI")
root.geometry("400x300")
root.configure(bg="#2c3e50")  # Couleur de fond attrayante

# Style moderne
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#2c3e50", foreground="#ecf0f1", font=("Helvetica", 12))
style.configure("TButton", background="#3498db", foreground="#ffffff", font=("Helvetica", 12, "bold"), padding=10)
style.map("TButton", background=[("active", "#2980b9")])  # Couleur au survol pour le bouton
style.configure("TCombobox", fieldbackground="#34495e", background="#2c3e50", foreground="#ffffff", font=("Helvetica", 12))

# Création des widgets
label_amount = ttk.Label(root, text="Montant:")
label_amount.grid(row=0, column=0, padx=10, pady=10)

# Entry avec placeholder
entry_amount = ttk.Entry(root, font=("Helvetica", 12))
entry_amount.insert(0, "Entrez le montant")  # Placeholder
entry_amount.bind("<FocusIn>", lambda event: entry_amount.delete(0, tk.END))  # Effacer le placeholder au focus
entry_amount.grid(row=0, column=1, padx=10, pady=10)

label_from = ttk.Label(root, text="De:")
label_from.grid(row=1, column=0, padx=10, pady=10)

combo_from = ttk.Combobox(root, values=["USD", "EUR", "MAD"], font=("Helvetica", 12))  # Ajout de MAD pour la devise marocaine
combo_from.grid(row=1, column=1, padx=10, pady=10)
combo_from.set("USD")

label_to = ttk.Label(root, text="À:")
label_to.grid(row=2, column=0, padx=10, pady=10)

combo_to = ttk.Combobox(root, values=["USD", "EUR", "MAD"], font=("Helvetica", 12))  # Ajout de MAD
combo_to.grid(row=2, column=1, padx=10, pady=10)
combo_to.set("EUR")

# Bouton avec style moderne
button_convert = ttk.Button(root, text="Convertir", command=convert_currency)
button_convert.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

label_result = ttk.Label(root, text="", font=("Helvetica", 12, "bold"), foreground="#ecf0f1")
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Lancement de la boucle principale
root.mainloop()
