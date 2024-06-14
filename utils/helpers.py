# utils/helpers.py
from collections import defaultdict
from datetime import datetime

# User balances and treasury
user_balances = defaultdict(int)
user_proofs = defaultdict(list)
proofs = defaultdict(list)
treasury_balance = 0

def add_balance(user_id, amount):
    user_balances[user_id] += amount

def del_balance(user_id, amount):
    user_balances[user_id] = max(0, user_balances[user_id] - amount)

def get_balance(user_id):
    return user_balances[user_id]

def add_proof(user_id, proof_url, amount):
    proof = {
        "url": proof_url,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    user_proofs[user_id].append(proof)

def get_proofs(user_id):
    return user_proofs[user_id]

def clear_proofs(user_id):
    user_proofs[user_id] = []

def get_total_balance():
    return sum(user_balances.values())

def update_treasury(amount):
    global treasury_balance
    treasury_balance += amount

def get_treasury_balance():
    return treasury_balance

def get_leaderboard():
    return sorted(user_balances.items(), key=lambda x: x[1], reverse=True)[:10]