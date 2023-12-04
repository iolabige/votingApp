import tkinter as tk
from voting_gui import VotingApp

def main() -> None:
    """
    Main function to run the voting application.
    """
    try:
        root = tk.Tk()
        app = VotingApp(root)
        root.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
