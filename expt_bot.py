import asyncio
from twitchio.ext import commands

# --- 設定項目 ---
ACCESS_TOKEN = 'oauth:hpl3u0ys8i3r2kwovgjfni0wijk7p6' # oauth:を含めた全文字列
CLIENT_ID = 'your_client_id' # Twitch Developer Portalで取得したClient ID
CLIENT_SECRET = 'your_client_secret' # Twitch Developer Portalで取得したClient Secret
BOT_ID = 'your_bot_id' # BotのTwitchユーザーID(数値)
CHANNEL_NAME = 'kato_junichi0817'
TEST_MESSAGE = "おー"
# ----------------

class Bot(commands.Bot):
    def __init__(self):
        # プレフィックス（!等）が必要ですが、今回は使いません
        super().__init__(token=ACCESS_TOKEN, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, bot_id=BOT_ID, prefix='!', initial_channels=[CHANNEL_NAME])

    async def event_ready(self):
        print(f'ログイン成功: {self.nick}')
        
        # チャンネルを取得してメッセージを送信
        channel = self.get_channel(CHANNEL_NAME)
        if channel:
            await channel.send(TEST_MESSAGE)
            print(f'メッセージを送信しました: "{TEST_MESSAGE}"')
        
        # 送信したらすぐに接続を閉じてプログラムを終了する
        await self.close()
        print("プログラムを終了しました。")

bot = Bot()
bot.run()