from collections import defaultdict
from datetime import datetime

# User balances and proofs by guild and user
user_balances = defaultdict(lambda: defaultdict(int))
user_proofs = defaultdict(lambda: defaultdict(list))
treasury_balances = defaultdict(int)

def add_balance(guild_id, user_id, amount):
    user_balances[guild_id][user_id] += amount

def del_balance(guild_id, user_id, amount):
    user_balances[guild_id][user_id] = max(0, user_balances[guild_id][user_id] - amount)

def get_balance(guild_id, user_id):
    return user_balances[guild_id][user_id]

def add_proof(guild_id, user_id, proof_url, amount):
    proof = {
        "url": proof_url,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    user_proofs[guild_id][user_id].append(proof)

def get_proofs(guild_id, user_id):
    return user_proofs[guild_id][user_id]

def clear_proofs(guild_id, user_id):
    user_proofs[guild_id][user_id] = []

def get_total_balance(guild_id):
    return sum(user_balances[guild_id].values())

def update_treasury(guild_id, amount):
    treasury_balances[guild_id] += amount

def get_treasury_balance(guild_id):
    return treasury_balances[guild_id]

def get_leaderboard(guild_id):
    return sorted(user_balances[guild_id].items(), key=lambda x: x[1], reverse=True)[:10]
