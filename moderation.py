from bot_setup import bot
import discord
from discord.ext import commands 

@bot.command()
@commands.has_permissons(kick_member = True)
async def kick(ctx, member: discord.Member, *, reason="No reason provided"):
    """Kicks a member from the server."""
    await member.kick(reason=reason)
    await ctx.send(f'{member.name} has beem kicked from the server. Reason: {reason}.')

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, reason= None):
    """Bans a member from the server."""
    await member.ban(reason=reason)
    await ctx.send(f'{member.name} has been banned from the server. Reason: {reason}.')

@bot.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount: int):
    """Clears a specified amount of messages from the chat."""
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f'Cleared {amount} of messages.')
    

