import hashlib
import datetime

class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = str(datetime.datetime.now())
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + self.timestamp + str(self.transactions) + self.previous_hash
        return hashlib.sha256(data.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        index = len(self.chain)
        previous_hash = self.get_latest_block().hash
        new_block = Block(index, transactions, previous_hash)
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print("\n-----------------------------")
            print(f"Index: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Transactions: {block.transactions}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return False

            if current.previous_hash != previous.hash:
                return False

        return True


# Entities in the voting system: Voters and Candidates

class Voter:
    def __init__(self, voter_id, name):
        self.voter_id = voter_id
        self.name = name
        self.has_voted = False


class Candidate:
    def __init__(self, candidate_id, name):
        self.candidate_id = candidate_id
        self.name = name
        self.vote_count = 0


# System

blockchain = Blockchain()
voters = {}
candidates = {}

while True:
    print("\n====== Voting Blockchain System ======")
    print("1. Add Candidate")
    print("2. Add Voter")
    print("3. Cast Vote")
    print("4. Print Blockchain")
    print("5. Validate Chain")
    print("6. Exit")

    choice = input("Enter choice: ")

    # Add Candidate
    if choice == "1":
        cid = input("Enter Candidate ID: ")

        if cid in candidates:
            print("Candidate ID already exists!")
            continue

        name = input("Enter Candidate Name: ")
        candidates[cid] = Candidate(cid, name)
        print("Candidate Added Successfully")

    # Add Voter
    elif choice == "2":
        vid = input("Enter Voter ID: ")

        if vid in voters:
            print("Voter ID already exists!")
            continue

        name = input("Enter Voter Name: ")
        voters[vid] = Voter(vid, name)
        print("oter Added Successfully")

    # Cast Vote
    elif choice == "3":
        vid = input("Enter Voter ID: ")

        if vid not in voters:
            print("Voter not found")
            continue

        voter = voters[vid]

        if voter.has_voted:
            print("Voter has already voted!")
            continue

        cid = input("Enter Candidate ID: ")

        if cid not in candidates:
            print("Candidate not found")
            continue

        candidate = candidates[cid]
        candidate.vote_count += 1
        voter.has_voted = True

        transaction = f"Voter {voter.name} voted for {candidate.name}"
        blockchain.add_block(transaction)

        print("Vote Cast Successfully (Added to Blockchain)")

    # Print Blockchain
    elif choice == "4":
        blockchain.print_chain()

    # Validate Chain
    elif choice == "5":
        if blockchain.is_chain_valid():
            print("Blockchain is VALID")
        else:
            print("Blockchain is CORRUPTED")

    # Exit
    elif choice == "6":
        print("Exiting system...")
        break

    else:
        print("Invalid Choice")