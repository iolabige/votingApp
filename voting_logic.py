import csv
import os

def save_vote(voter: str, candidate: str) -> None:
    """
    Saves a vote to a CSV file. If the file doesn't exist, it creates one with a header.

    Args:
        voter (str): The name of the voter.
        candidate (str): The name of the candidate voted for.
    """
    file_exists = os.path.isfile('voting_results.csv')
    with open('voting_results.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Voter", "Candidate"])  # Write header if file doesn't exist
        writer.writerow([voter, candidate])
