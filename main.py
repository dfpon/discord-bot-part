#coding:utf-8
import discord
from discord.ext import commands
from discord_buttons_plugin import *
cl=commands.Bot(command_prefix='p!')
button=ButtonsClient(cl)
token='OTIyNDE3MTM3ODcwNTg5OTk1.YcBJ5w.KCtOBJtDpWLAFD0cb8KGAKUYpMk'
@cl.event
async def on_ready():
    print('Booting Bot ...')

@cl.command()
async def create_panel(ctx):
    await button.send(
        content='チケット作成',
        channel=ctx.channel.id,
        components=[
            ActionRow([
                Button(
                    label='お問い合わせ',
                    style=ButtonType().Primary,
                    custom_id='create_inquiry'
                )
            ]),ActionRow([
                Button(
                    label='購入',
                    style=ButtonType().Danger,
                    custom_id='create_buy'
                )
            ])
        ]
    )

@button.click
async def create_inquiry(ctx):
    return

@button.click
async def create_buy(ctx):
    return

cl.run(token)