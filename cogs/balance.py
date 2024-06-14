# cogs/balance.py
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
from utils.helpers import (
    add_balance,
    get_balance,
    add_proof,
    get_proofs,
    get_total_balance,
    update_treasury,
    get_treasury_balance,
    del_balance,
    clear_proofs,
    get_leaderboard
)
import config

class BalanceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="my", description="My balance commands", guild_ids=config.GUILD_IDS)
    async def my_balance(self, interaction: Interaction):
        pass

    @my_balance.subcommand(name="bal", description="Show my balance")
    async def show_my_balance(self, interaction: Interaction):
        user_id = interaction.user.id
        balance = get_balance(user_id)
        await interaction.response.send_message(f"{interaction.user.mention}'s balance: {balance} silver")   
    
    @nextcord.slash_command(name="bal", description="Balance commands", guild_ids=config.GUILD_IDS)
    async def balance(self, interaction: Interaction):
        pass

    @balance.subcommand(name="add", description="Add balance")
    async def add_balance_command(self, interaction: Interaction, amount: int, attachment: nextcord.Attachment = SlashOption(description="Proof attachment", required=True)):
        user_id = interaction.user.id
        add_balance(user_id, amount)
        proof_url = attachment.url
        add_proof(user_id, proof_url, amount)

        await interaction.response.send_message(f"Adding {amount} silver to your balance. Processing the proof...", ephemeral=True)

        try:
            file = await attachment.to_file()
            await interaction.channel.send(content=f"User {interaction.user.mention} added {amount} silver. Proof:", file=file)
        except Exception as e:
            await interaction.channel.send(content=f"Failed to process the proof for {interaction.user.mention}. Error: {e}")
    
    @balance.subcommand(name="del", description="Delete balance")
    async def del_balance_command(self, interaction: Interaction, amount: int, user: nextcord.Member = SlashOption(description="User to show balance for", required=True)):
        user_id = user.id
        del_balance(user_id, amount)
        await interaction.response.send_message(f"Deleted {amount} silver from {user.mention} balance.")

    @balance.subcommand(name="show", description="Show balance")
    async def show_balance(self, interaction: Interaction, user: nextcord.Member = SlashOption(description="User to show balance for", required=True)):
        user_id = user.id
        balance = get_balance(user_id)
        await interaction.response.send_message(f"{user.mention}'s balance: {balance} silver")

    @balance.subcommand(name="proof", description="Show proof")
    async def show_proof(self, interaction: Interaction, user: nextcord.Member = SlashOption(description="User to show proof for", required=True)):
        user_id = user.id
        proofs = get_proofs(user_id)
        if proofs:
            proof_list = "\n".join([f"Proof {idx+1} [{proof['date']}]: {proof['amount']} silver. URL: {proof['url']}" for idx, proof in enumerate(proofs)])
            await interaction.response.send_message(f"{user.mention}'s proofs:\n{proof_list}")
        else:
            await interaction.response.send_message(f"No proofs found for {user.mention}")
    
    @balance.subcommand(name="proof_clear", description="Clear proof")
    async def clear_proof(self, interaction: Interaction, user: nextcord.Member = SlashOption(description="User to clear proofs for", required=True)):
        user_id = user.id
        clear_proofs(user_id)
        await interaction.response.send_message(f"Cleared all proofs for {user.mention}")

    @balance.subcommand(name="total", description="Show total balance")
    async def total_balance(self, interaction: Interaction):
        total = get_total_balance()
        await interaction.response.send_message(f"Total balance across the server: {total} silver")

    @balance.subcommand(name="treasury", description="Guild treasury balance commands")
    async def treasury(self, interaction: Interaction):
        pass

    @balance.subcommand(name="leaderboard", description="Show top 10 user balances")
    async def leaderboard(self, interaction: Interaction):
        leaderboard = get_leaderboard()
        leaderboard_str = "\n".join([f"{idx+1}. <@{user_id}>: {balance} silver" for idx, (user_id, balance) in enumerate(leaderboard)])
        await interaction.response.send_message(f"Top 10 balances:\n{leaderboard_str}")
    
    @treasury.subcommand(name="show", description="Guild treasury balance commands")
    async def show_treasury(self, interaction: Interaction):
        balance = get_treasury_balance()
        await interaction.response.send_message(f"Treasury balance: {balance} silver")

    @treasury.subcommand(name="add", description="Add to treasury")
    async def add_treasury(self, interaction: Interaction, amount: int):
        update_treasury(amount)
        await interaction.response.send_message(f"Added {amount} silver to the treasury. New treasury balance: {get_treasury_balance()} silver")

    @treasury.subcommand(name="del", description="Remove from treasury")
    async def del_treasury(self, interaction: Interaction, amount: int):
        update_treasury(-amount)
        await interaction.response.send_message(f"Removed {amount} silver from the treasury. New treasury balance: {get_treasury_balance()} silver")

def setup(bot):
    bot.add_cog(BalanceCog(bot))
