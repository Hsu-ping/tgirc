## Telegram bot 

- 到 Telegram 中找 [@BotFather](https://t.me/BotFather)  -> /newbot ... 記下 token 不要外流

- 概念：Updater、Dispatcher、Handler

- 架構：

  ```python
  from telegram.ext import Updater, CommandHandler
  
  def hello(bot, update): ...
  
  updater = Updater('xxx') # 根據 TOKEN 創建 dispatcher 與 bot
  # Updater 建立新的 Thread 將 telegram bot 新資訊傳給 dispatcher
  updater.dispatcher.add_handler(CommandHandler('hello', hello)) # 傳給相對應的 Handler
  
  updater.start_polling() # 用 long polling 的方式接收 update
  updater.idle()
  ```

- 回覆：

  ```python
  1. update.message.reply_text 文字回覆
  2. InlineKeyboardMarkup + InlineKeyboardButton 按鈕回覆
  ```

- 因不需給予不同功能，沒有寫到儲存使用者資訊的功能