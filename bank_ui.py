import tkinter as tk
from datetime import datetime
from bank_account import BankAccount


# ==========================================
# BANK ACCOUNT
# ==========================================

account = BankAccount("12345", "John", 1000)

# Store transactions
transactions = []


# ==========================================
# MAIN WINDOW
# ==========================================

window = tk.Tk()

window.title("Bank Account")
window.geometry("500x750")
window.resizable(False, False)

window.configure(bg="#f4f7fb")


# ==========================================
# TITLE
# ==========================================

title_label = tk.Label(
    window,
    text="My Bank",
    font=("Arial", 26, "bold"),
    bg="#f4f7fb",
    fg="#1f2937"
)

title_label.pack(pady=(25, 5))


subtitle_label = tk.Label(
    window,
    text="Personal Banking",
    font=("Arial", 12),
    bg="#f4f7fb",
    fg="#6b7280"
)

subtitle_label.pack(pady=(0, 20))


# ==========================================
# ACCOUNT CARD
# ==========================================

account_card = tk.Frame(
    window,
    bg="white",
    padx=25,
    pady=20
)

account_card.pack(
    padx=30,
    fill="x"
)


holder_label = tk.Label(
    account_card,
    text=f"Account Holder\n{account.account_holder}",
    font=("Arial", 13, "bold"),
    bg="white",
    fg="#1f2937"
)

holder_label.pack(pady=5)


account_number_label = tk.Label(
    account_card,
    text=f"Account Number\n{account.account_number}",
    font=("Arial", 11),
    bg="white",
    fg="#6b7280"
)

account_number_label.pack(pady=5)


balance_label = tk.Label(
    account_card,
    text=f"R {account.balance:,.2f}",
    font=("Arial", 28, "bold"),
    bg="white",
    fg="#2563eb"
)

balance_label.pack(pady=(15, 5))


balance_title = tk.Label(
    account_card,
    text="Available Balance",
    font=("Arial", 10),
    bg="white",
    fg="#6b7280"
)

balance_title.pack()


# ==========================================
# TRANSACTION INPUT
# ==========================================

transaction_label = tk.Label(
    window,
    text="Transaction Amount",
    font=("Arial", 13, "bold"),
    bg="#f4f7fb",
    fg="#1f2937"
)

transaction_label.pack(pady=(20, 8))


amount_entry = tk.Entry(
    window,
    font=("Arial", 14),
    width=25,
    justify="center"
)

amount_entry.pack(
    pady=5,
    ipady=8
)


# ==========================================
# MESSAGE
# ==========================================

message_label = tk.Label(
    window,
    text="",
    font=("Arial", 11),
    bg="#f4f7fb"
)

message_label.pack(pady=10)


# ==========================================
# TRANSACTION HISTORY
# ==========================================

history_title = tk.Label(
    window,
    text="Transaction History",
    font=("Arial", 14, "bold"),
    bg="#f4f7fb",
    fg="#1f2937"
)

history_title.pack(pady=(5, 5))


history_list = tk.Listbox(
    window,
    width=48,
    height=7,
    font=("Arial", 11),
    bg="white",
    fg="#374151",
    borderwidth=0,
    highlightthickness=0
)

history_list.pack(pady=5)


# ==========================================
# UPDATE BALANCE
# ==========================================

def update_balance():

    balance_label.config(
        text=f"R {account.balance:,.2f}"
    )


# ==========================================
# ADD TRANSACTION TO HISTORY
# ==========================================
def add_transaction(transaction):

    current_time = datetime.now().strftime("%H:%M")

    transaction_with_time = f"{current_time}    {transaction}"

    transactions.append(transaction_with_time)

    history_list.insert(
        tk.END,
        transaction_with_time
    )

# ==========================================
# DEPOSIT
# ==========================================

def deposit_money():

    try:

        amount = float(amount_entry.get())

        message = account.deposit(amount)

        update_balance()

        if amount > 0:

            add_transaction(
                f"+ R {amount:,.2f}    Deposit"
            )

            message_label.config(
                text=message,
                fg="#16a34a"
            )

        else:

            message_label.config(
                text=message,
                fg="#dc2626"
            )

        amount_entry.delete(0, tk.END)

    except ValueError:

        message_label.config(
            text="Please enter a valid number.",
            fg="#dc2626"
        )


# ==========================================
# WITHDRAW
# ==========================================

def withdraw_money():

    try:

        amount = float(amount_entry.get())

        message = account.withdraw(amount)

        update_balance()

        if 0 < amount <= account.balance + amount:

            if "Insufficient" not in message:

                add_transaction(
                    f"- R {amount:,.2f}    Withdrawal"
                )

                message_label.config(
                    text=message,
                    fg="#16a34a"
                )

            else:

                message_label.config(
                    text=message,
                    fg="#dc2626"
                )

        else:

            message_label.config(
                text=message,
                fg="#dc2626"
            )

        amount_entry.delete(0, tk.END)

    except ValueError:

        message_label.config(
            text="Please enter a valid number.",
            fg="#dc2626"
        )


# ==========================================
# BUTTONS
# ==========================================

deposit_button = tk.Button(
    window,
    text="Deposit",
    font=("Arial", 12, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    width=20,
    relief="flat",
    cursor="hand2",
    command=deposit_money
)

deposit_button.pack(
    pady=4,
    ipady=6
)


withdraw_button = tk.Button(
    window,
    text="Withdraw",
    font=("Arial", 12, "bold"),
    bg="#111827",
    fg="white",
    activebackground="#374151",
    activeforeground="white",
    width=20,
    relief="flat",
    cursor="hand2",
    command=withdraw_money
)

withdraw_button.pack(
    pady=4,
    ipady=6
)


# ==========================================
# START APPLICATION
# ==========================================

window.mainloop()