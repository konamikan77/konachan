import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTIyNjQxODIyNjkxMzg3Mzk5MA.GmY8YK.8q0sPPQzGNUxlmOxENm_E61Rja_6p3r7RM4zYk')