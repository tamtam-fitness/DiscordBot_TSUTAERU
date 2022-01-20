from discordwebhook import Discord

import datetime
import pytz


#<<AWS Lambda>>
def lambda_handler(event, context):
  discord = Discord(url="https://discord.com/api/webhooks/933731843524669510/lbNupyG7ai8271NkQPn7FdUoRW2iao_B8ijDTdO7LMESaT43OVnQgQFrbEUnMQMcT-FZ")
  dt_now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
  discord.post(content=f'@everyone あと5分でデイリースクラムが始まります！ {dt_now.strftime("%Y年%m月%d日 %H:%M:%S")}')

if __name__ == "__main__":
    lambda_handler(None, None)