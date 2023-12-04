import tkinter as tk
from tkinter import ttk, messagebox
from voting_logic import save_vote

class VotingApp:
    def __init__(self, root: tk.Tk) -> None:
        """
        Initialize the voting application GUI.

        Args:
            root (tk.Tk): The root window of the application.
        """
        self.root = root
        self.root.title("Voting App")

        self.voter_var = tk.StringVar(value="Select Voter")
        self.candidate_var = tk.StringVar(value="Select Candidate")
        self.voters = ["James", "Israel", "Sheldon", "Kate", "Jane"]
        self.candidates = ["John", "Jane"]
        self.voted_voters = set()

        self.setup_gui()

    def setup_gui(self) -> None:
        """
        Sets up the GUI components of the application.
        """
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        voter_dropdown = ttk.Combobox(self.root, textvariable=self.voter_var, values=self.voters)
        voter_dropdown.grid(column=0, row=0, padx=10, pady=10, sticky='ew')

        candidate_dropdown = ttk.Combobox(self.root, textvariable=self.candidate_var, values=self.candidates)
        candidate_dropdown.grid(column=1, row=0, padx=10, pady=10, sticky='ew')

        vote_button = tk.Button(self.root, text="Vote", command=self.vote)
        vote_button.grid(column=0, row=1, columnspan=2, padx=10, pady=10, sticky='ew')

    def vote(self) -> None:
        """
        Handles the voting process when the vote button is clicked.
        """
        try:
            voter = self.voter_var.get()
            candidate = self.candidate_var.get()

            if not voter or voter == "Select Voter":
                messagebox.showerror("Voting Error", "Please select a voter.")
                return
            if not candidate or candidate == "Select Candidate":
                messagebox.showerror("Voting Error", "Please select a candidate.")
                return
            if voter in self.voted_voters:
                messagebox.showerror("Voting Error", "This voter has already voted.")
                return

            save_vote(voter, candidate)
            self.voted_voters.add(voter)
            self.voter_var.set("Select Voter")
            self.candidate_var.set("Select Candidate")
        except Exception as e:
            messagebox.showerror("Voting Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VotingApp(root)
    root.mainloop()
