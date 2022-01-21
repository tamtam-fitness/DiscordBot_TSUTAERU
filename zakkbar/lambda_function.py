from discordwebhook import Discord

import datetime
import pytz


#<<AWS Lambda>>
def lambda_handler(event, context):
  discord = Discord(url="<<channel webhook url of your discord server>>")
  dt_now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
  discord.post(content=f'@everyone あと5分でデイリースクラムが始まります！ {dt_now.strftime("%Y年%m月%d日 %H:%M:%S")}')

if __name__ == "__main__":
    lambda_handler(None, None)
