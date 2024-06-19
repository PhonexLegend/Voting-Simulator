"""
def AFIND(CITIES):
    for i in CITIES:
        if i[0] == 'A':
            print(i)

    return ""

CITIES = ["AGRA", "AMRITSAR", "DELHI"]

AFIND(CITIES)
"""
"""
def word(st):

    s = st.split()

    l = len(s)

    for i in range(l):

        J = len(s[i])

        print(J)

    return ""

st = ("This is an apple")

word(st)

"""
import logging
import tkinter as tk
from tkinter import messagebox

# Configure logging
logging.basicConfig(filename='results.log', level=logging.INFO, format='%(message)s')

# List to hold candidates
candidates = []

# Dictionary to hold votes
votes = {}

# Set to keep track of voters who have voted
voted_users = set()

# Tkinter setup
root = tk.Tk()
root.title("Voting System")

# Functions
def create_candidates():
    global candidates
    candidate_name = candidate_entry.get().strip()
    if candidate_name and candidate_name not in candidates:
        candidates.append(candidate_name)
        votes[candidate_name] = 0
        candidate_listbox.insert(tk.END, candidate_name)
        update_candidate_menu()
    candidate_entry.delete(0, tk.END)

def vote_candidates():
    voter_number = voter_entry.get().strip()
    candidate = candidate_var.get().strip()
    if not is_valid_voter_number(voter_number):
        messagebox.showerror("Error", "Invalid voter number. It must be a 13-digit number.")
        return
    if voter_number in voted_users:
        messagebox.showerror("Error", "You have already voted.")
        return
    if candidate not in candidates:
        messagebox.showerror("Error", "Candidate does not exist.")
        return
    
    votes[candidate] += 1
    logging.info('Voter ' + voter_number + ' voted for ' + candidate)
    messagebox.showinfo("Success", f'Voter {voter_number} voted for {candidate}')
    voted_users.add(voter_number)
    voter_entry.delete(0, tk.END)

def display_results():
    result_window = tk.Toplevel(root)
    result_window.title("Voting Results")
    for candidate in votes:
        result_label = tk.Label(result_window, text=f"{candidate}: {votes[candidate]} votes")
        result_label.pack()
    logging.info("Voting Results:")
    for candidate in votes:
        logging.info(candidate + ': ' + str(votes[candidate]) + ' votes')

def declare_winner():
    max_votes = max(votes.values())
    winners = [candidate for candidate, vote_count in votes.items() if vote_count == max_votes]

    if len(winners) == 1:
        messagebox.showinfo("Winner", f"The winner is {winners[0]} with {max_votes} votes!")
        logging.info("The winner is " + winners[0] + " with " + str(max_votes) + " votes!")
    else:
        messagebox.showinfo("Winner", f"It's a tie between: {', '.join(winners)} with {max_votes} votes each!")
        logging.info("It's a tie between: " + ', '.join(winners) + " with " + str(max_votes) + " votes each!")

def is_valid_voter_number(voter_number):
    return len(voter_number) == 13 and voter_number.isdigit()

def update_candidate_menu():
    menu = candidate_menu["menu"]
    menu.delete(0, "end")
    for candidate in candidates:
        menu.add_command(label=candidate, command=lambda value=candidate: candidate_var.set(value))

# UI Components
candidate_label = tk.Label(root, text="Enter candidate name:")
candidate_label.pack()

candidate_entry = tk.Entry(root)
candidate_entry.pack()

add_candidate_button = tk.Button(root, text="Add Candidate", command=create_candidates)
add_candidate_button.pack()

candidate_listbox = tk.Listbox(root)
candidate_listbox.pack()

voter_label = tk.Label(root, text="Enter your 13-digit voter number:")
voter_label.pack()

voter_entry = tk.Entry(root)
voter_entry.pack()

candidate_var = tk.StringVar(root)
candidate_var.set("Select a candidate")

# Initialize OptionMenu with a placeholder option
candidate_menu = tk.OptionMenu(root, candidate_var, "Select a candidate")
candidate_menu.pack()

vote_button = tk.Button(root, text="Vote", command=vote_candidates)
vote_button.pack()

results_button = tk.Button(root, text="Display Results", command=display_results)
results_button.pack()

winner_button = tk.Button(root, text="Declare Winner", command=declare_winner)
winner_button.pack()

# Run the Tkinter event loop
root.mainloop()
