import discord
from discord.ext import commands
from interactive_conditional_samples import interact_model
client = commands.Bot(command_prefix='!')
from my_token import token


class Bot:

    memories = []       # <-- Contains the last few messages
                        #     so that the bot's replies can
                        #     maintain context.

    recollections = ""  # <-- Contains the last few messages
                        #     in string form. GPT-2 only
                        #     interprets memory this way.

    def __init__(self, memory_length):
        self.memory_length = memory_length
    
    # Saves the input message to the bot's memory
    def remember(self, message):

        # Adding to memories
        self.memories.append(message)
        if (len(self.memories) > self.memory_length):
            self.memories.pop(0)

        # Adding to recollections
        self.recollections = ""
        for memory in self.memories:
            self.recollections = self.recollections + memory + "\r\n"

    # Prints the bot's memory
    def dump_memory(self):
        print("_" * 30)
        print("BOT MEMORY:")
        for memory in self.memories:
            print(memory)
        print("\nRECOLLECTIONS")
        print(self.recollections)
        print("_" * 30)

    # Clears the bot's memory
    def obliviate(self):
        self.memories = []
        self.recollections = ""

Jargobot = Bot(4)

# @client.command()
# async def obliviate(ctx):

#     await ctx.channel.send("*Forgets everything*")
#     await ctx.channel.trigger_typing()
#     await ctx.channel.send("Hmm... Must have hit my head...")
#     Jargobot.obliviate()

#     Jargobot.dump_memory()

@client.event
async def on_message(message):

    if message.author.id != 699023487188074562:   # <-- JargoBot's ID.

        if message.content ==  "!obliviate":
            await message.channel.send("*Forgets everything*\nHmm... Must have hit my head...")
            Jargobot.obliviate()
            Jargobot.dump_memory()
        else:
            await message.channel.trigger_typing()
            Jargobot.remember(message.content)
            response = interact_model(prompt=Jargobot.recollections).splitlines()[0]

            while response == "<|endoftext|>":
                await message.channel.trigger_typing()
                print("TRYING AGAIN! GOT ENDOFTEXT.")
                response = interact_model(prompt=Jargobot.recollections).splitlines()[0]

            await message.channel.send(response)
            Jargobot.remember(response)
            Jargobot.dump_memory()

client.run(token)