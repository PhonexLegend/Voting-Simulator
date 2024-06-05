import logging
import time

# Configure logging
logging.basicConfig(filename='results.log', level=logging.INFO, format='%(message)s')

# List to hold candidates
candidates = []

# Dictionary to hold votes
votes = {}

# Set to keep track of voters who have voted
voted_users = set()

def CreateCandidates():
    global candidates
    print("Enter the names of candidates. Type 'done' when finished.")
    while True:
        candidate = input("Enter candidate name: ").strip()
        if candidate.lower() == 'done':
            break
        if candidate and candidate not in candidates:
            candidates.append(candidate)
    # Initialize votes for each candidate
    for candidate in candidates:
        votes[candidate] = 0
    print("Candidates created:", candidates)
    print("_____________________________")
    time.sleep(2)

def VoteCandidates(voter_number, candidate):
    if candidate in candidates:
        votes[candidate] += 1
        logging.info('Voter ' + voter_number + ' voted for ' + candidate)
        print('Voter ' + voter_number + ' voted for ' + candidate)
    else:
        print('Candidate ' + candidate + ' does not exist.')
    print("_____________________________")
    time.sleep(2)

def DisplayResults():
    print("Voting Results:")
    print("_____________________________")
    time.sleep(2)
    for candidate in votes:
        print(candidate + ': ' + str(votes[candidate]) + ' votes')
        print("_____________________________")
        time.sleep(2)
    # Optionally, log the results to the log file
    logging.info("Voting Results:")
    for candidate in votes:
        logging.info(candidate + ': ' + str(votes[candidate]) + ' votes')

def DeclareWinner():
    max_votes = max(votes.values())
    winners = [candidate for candidate, vote_count in votes.items() if vote_count == max_votes]

    if len(winners) == 1:
        print("The winner is " + winners[0] + " with " + str(max_votes) + " votes!")
        logging.info("The winner is " + winners[0] + " with " + str(max_votes) + " votes!")
    else:
        print("It's a tie between: " + ', '.join(winners) + " with " + str(max_votes) + " votes each!")
        logging.info("It's a tie between: " + ', '.join(winners) + " with " + str(max_votes) + " votes each!")
    print("_____________________________")
    time.sleep(2)

def is_valid_voter_number(voter_number):
    return len(voter_number) == 13 and voter_number.isdigit()

def main():
    CreateCandidates()

    while True:
        user_input = input("Do you want to vote? (yes/no): ").strip().lower()
        if user_input == 'no':
            break
        elif user_input == 'yes':
            voter_number = input("Enter your 13-digit voter number: ").strip()
            if not is_valid_voter_number(voter_number):
                print("Invalid voter number. It must be a 13-digit number.")
                print("_____________________________")
                time.sleep(2)
                continue
            if voter_number in voted_users:
                print("You have already voted.")
                print("_____________________________")
                time.sleep(2)
                continue
            print("Candidates are:", candidates)
            print("_____________________________")
            time.sleep(2)
            candidate = input("Enter the name of the candidate you want to vote for: ").strip()
            VoteCandidates(voter_number, candidate)
            voted_users.add(voter_number)
        else:
            print("Invalid input, please enter 'yes' or 'no'.")
            print("_____________________________")
            time.sleep(2)

    # Display the results
    DisplayResults()

    # Declare the winner
    DeclareWinner()

# Run the main function
main()
