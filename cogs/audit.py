# cogs/audit.py
import nextcord
from nextcord.ext import commands

class AuditCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        await self.check_audit_log(channel.guild, action_type=nextcord.AuditLogAction.channel_delete)
    
    async def check_audit_log(self, guild, action_type):
        async for entry in guild.audit_logs(limit=1, action=action_type):
            if entry.user.id == self.bot.user.id:
                print(f"Bot detected creating/deleting channel in {guild.name}. Leaving the server to prevent potential hijacking.")
                await guild.leave()
                break

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        await self.check_audit_log(channel.guild, action_type=nextcord.AuditLogAction.channel_create)

def setup(bot):
    bot.add_cog(AuditCog(bot))
