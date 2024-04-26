import datetime
import argparse
import discord


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("botToken")
    parser.add_argument("channelId", type=int)
    parser.add_argument("msg")
    args = parser.parse_args()

    print(f'[{time_str()}] Start')

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'[{time_str()}] Discord client ready')
        game = discord.CustomActivity('Working...')
        await client.change_presence(status=discord.Status.online, activity=game)
        channel = client.get_channel(args.channelId)
        await channel.send(str(args.msg))
        await client.close()

    client.run(args.botToken)
    print(f'[{time_str()}] End')


def time_str():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    main()
