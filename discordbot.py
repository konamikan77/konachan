# インストールした discord.py を読み込む
import discord
import re
import datetime
import asyncio
import random
from discord.ext import tasks
from common import env
from common import consts
from common import operate_settings

# 自分のBotのアクセストークンに置き換えてください
TOKEN = env.TOKEN

# 接続に必要なオブジェクトを生成
intents = discord.Intents.all()
client = discord.Client(intents=intents)

###################
# ループ処理
###################

@tasks.loop(seconds=10)
async def send_message_every_10sec():
    # 現在時刻取得
    dt_now = datetime.datetime.now()
    print(dt_now)
    guild = client.get_guild(1209326912594247721)
    # 毎時00分処理
    if re.match(consts.PATTERN_HOUR, str(dt_now)):
     # # 死活監視メッセージ
     await guild.get_channel(1230903380705021973).send("-----こ、こんにちは　今の時間は、" +str(dt_now) + "　だよ-----")
   # 毎時50分処理
    if re.match(consts.PATTERN_50_MINUITE, str(dt_now)):
        targets = operate_settings.get_reminder_finish_targets()
        print(targets)
        for target in targets:
            c_guild = client.get_guild(target["server_id"])
            await c_guild.get_channel(target["reminder_finish_id"]).send('たいて！交代10分前！')
    # 毎時55分処理
    if re.match(consts.PATTERN_55_MINUITE, str(dt_now)):
        targets = operate_settings.get_reminder_announce_targets()
        for target in targets:
            c_guild = client.get_guild(target["server_id"])
            message = operate_settings.get_reminder_announce_message(target["server_id"])
            await c_guild.get_channel(target["reminder_announce_id"]).send('時速とってね')
            # await c_guild.get_channel(target["reminder_announce_id"]).send(';1位から5位までのポイントをどなたか撮っていただけると助かります！')
    # 15分毎処理
    if re.match(consts.PATTERN_15_MINUITE, str(dt_now)):
        # await guild.get_channel(0000000000000).send("☆15分経ったよ : " + str(dt_now))
        targets = operate_settings.get_reminder_charge_targets()
        for target in targets:
            c_guild = client.get_guild(target["server_id"])
            message = operate_settings.get_reminder_charge_message(target["server_id"])
            await c_guild.get_channel(target["reminder_charge_id"]).send('たいてね')
        return

###################
# 開始イベント
###################

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    send_message_every_10sec.start()

###################
# メッセージ受信イベント
###################

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    if re.match(".*チャンネル名を「部屋番号【.*", message.content):
      if message.author.bot:
       await asyncio.sleep(10)
       await message.delete()
       return
    # 当バッチのメッセージは無処理
    if message.author == client.user:
        return
    # 部屋番変更
    if re.match(consts.PATTERN_CHANGE_ROOM_NUMBER, message.content):
        # 対象チェック
        if not operate_settings.is_change_room_number_target(message.guild.id):
            # 対象外の場合は即時リターン
            return
        # 現在部屋番との重複チェック
        if operate_settings.is_dupli_change_room_number_now(message.guild.id, message.content):
            # 重複時は即時リターン
            return
        target_channel = operate_settings.get_change_room_number_id(message.guild.id)
        channel_name = consts.CHANGE_ROOM_NUMBER_TEMPLATE.format(message.content)
        guild = client.get_guild(message.guild.id)
        channel = guild.get_channel(target_channel)
        operate_settings.change_change_room_number_now(message.guild.id, message.content)
        try:
            await channel.edit(name = channel_name)
        except:
            await message.channel.send(';部屋番号が更新できない :sweat_drops:\n更新できるのは10分で2回までだよ！')
        await message.channel.send(';部屋番号が変わったよ')
        if target_channel != message.channel.id:
            await channel.send('; ' + message.content)
        return
    # 当バッチ呼び出しコマンド以外は無処理
    #if not re.match(consts.PATTERN_THIS, message.content):
    #    return
    # 鯖設定初期化
    if re.match(consts.PATTERN_INIT, message.content):
        operate_settings.init_settings(message.guild.id)
        await message.channel.send('; 初期化おわり')
        return
    # 炊きリマインダー開始
    if re.match(consts.PATTERN_REMINDER_CHARGE_START, message.content):
        # args = message.content.split()
        # reminer_message = args[3] if len(args) > 3 else ""
        operate_settings.start_reminder_charge(message.guild.id, message.channel.id, consts.DEFAULT_REMINDER_CHARGE_MESSAGE)
        await message.channel.send('; 炊いてリマインドはじめ')
        return
    if re.match(consts.PATTERN_REMINDER_CHARGE_END, message.content):
        # args = message.content.split()
        # reminer_message = args[3] if len(args) > 3 else ""
        operate_settings.end_reminder_charge(message.guild.id)
        await message.channel.send('; 炊いてリマインド終了')
        return
            # シフト交代リマインダー開始
    if re.match(consts.PATTERN_REMINDER_FINISH_START, message.content):
        args = message.content.split()
        reminer_message = args[3] if len(args) > 3 else ""
        operate_settings.start_reminder_finish(message.guild.id, message.channel.id, reminer_message)
        await message.channel.send('; シフト終了リマインドはじめ')
        return
    # シフト交代リマインダー終了
    if re.match(consts.PATTERN_REMINDER_FINISH_END, message.content):
        args = message.content.split()
        operate_settings.end_reminder_finish(message.guild.id)
        await message.channel.send('; シフト終了リマインドおわり')
        return
    # 交代前アナウンスリマインダー開始
    if re.match(consts.PATTERN_REMINDER_ANNOUNCE_START, message.content):
        args = message.content.split()
        reminer_message = args[3] if len(args) > 3 else ""
        operate_settings.start_reminder_annouce(message.guild.id, message.channel.id, reminer_message)
        await message.channel.send('; 交代前アナウンスリマインドはじめ')
        return
    # 交代前アナウンスリマインダー終了
    if re.match(consts.PATTERN_REMINDER_ANNOUNCE_END, message.content):
        args = message.content.split()
        operate_settings.end_reminder_announce(message.guild.id)
        await message.channel.send('; 交代前アナウンスリマインドおわり')
        return
    # 部屋番変更開始
    if re.match(consts.PATTERN_CHANGE_ROOM_NUMBER_START, message.content):
        args = message.content.split()
        operate_settings.start_change_room_number(message.guild.id, message.channel.id)
        await message.channel.send('; 部屋番変更はじめ')
        return
    # 部屋番変更終了
    if re.match(consts.PATTERN_CHANGE_ROOM_NUMBER_END, message.content):
        args = message.content.split()
        operate_settings.end_change_room_number(message.guild.id)
        await message.channel.send('; 部屋番変更おわり')
        return
    # 話題提供
    if re.match(consts.PATTERN_WADAI, message.content):
        #num = random.randint(0,99)
        #await message.channel.send('ここはとおったよ')
        #if num < 5:
        #    await message.channel.send(consts.WADAI_1)
        #    return
        #elif 5 <= num <99:
        #    await message.channel.send(consts.WADAI_2)
        #    return
        talk_theme = [
            ";ごはんの話しよ！何たべたい？"   if i < 10 else
            ";みんなの好きな曲教えてほしいな"   if 10 <= i < 20 else
            ";お菓子なにがすき？"     if 20 <= i < 30 else
            ";推しの好きなところ3つ言って！"     if 30 <= i < 40 else
            ";最近うれしかったことって何？"     if 40 <= i < 50 else
            ";100万円手に入れたら何につかう？(※貯金はだめだよ！！)"   if 50 <= i < 60 else
            ";旅行するならどこに行きたい？"     if 60 <= i < 70 else
            ";好きなプロセカのカードイラストは？"   if 70 <= i < 80 else
            ";昨日の晩御飯思い出せる？思い出せたらすごい！思い出せなかったら反省してね"   if 80 <= i < 90 else
            ";願いが1つ叶うなら何を願う？"   if 90 <= i < 95 else
            ";自分で考えろ"   for i in range(99)]
        await message.channel.send(talk_theme[random.randrange(len(talk_theme))])
        return
    if re.match(consts.PATTERN_WADAI_SEMI, message.content):
        talk_theme = [
            ";ごはんの話しよ！何たべたい？"   if i < 10 else
            ";みんなの好きな曲教えてほしいな"   if 10 <= i < 20 else
            ";お菓子なにがすき？"     if 20 <= i < 30 else
            ";推しの好きなところ3つ言って！"     if 30 <= i < 40 else
            ";最近うれしかったことって何？"     if 40 <= i < 50 else
            ";100万円手に入れたら何につかう？(※貯金はだめだよ！！)"   if 50 <= i < 60 else
            ";旅行するならどこに行きたい？"     if 60 <= i < 70 else
            ";好きなプロセカのカードイラストは？"   if 70 <= i < 80 else
            ";昨日の晩御飯思い出せる？思い出せたらすごい！思い出せなかったら反省してね"   if 80 <= i < 90 else
            ";願いが1つ叶うなら何を願う？"   if 90 <= i < 95 else
            ";自分で考えろ"   for i in range(99)]
        await message.channel.send(talk_theme[random.randrange(len(talk_theme))])
        return
    if re.match(consts.PATTERN_WADAI_SEMISPACE, message.content):
        talk_theme = [
            ";ごはんの話しよ！何たべたい？"   if i < 10 else
            ";みんなの好きな曲教えてほしいな"   if 10 <= i < 20 else
            ";お菓子なにがすき？"     if 20 <= i < 30 else
            ";推しの好きなところ3つ言って！"     if 30 <= i < 40 else
            ";最近うれしかったことって何？"     if 40 <= i < 50 else
            ";100万円手に入れたら何につかう？(※貯金はだめだよ！！)"   if 50 <= i < 60 else
            ";旅行するならどこに行きたい？"     if 60 <= i < 70 else
            ";好きなプロセカのカードイラストは？"   if 70 <= i < 80 else
            ";昨日の晩御飯思い出せる？思い出せたらすごい！思い出せなかったら反省してね"   if 80 <= i < 90 else
            ";願いが1つ叶うなら何を願う？"   if 90 <= i < 95 else
            ";自分で考えろ"   for i in range(99)]
        await message.channel.send(talk_theme[random.randrange(len(talk_theme))])
        return
    #おみくじ機能
    if re.match(consts.PATTERN_OMIKUJI, message.content):
        omikuji_result = [
            ";大吉だよ！"   if i < 5 else
            ";中吉！"     if 5 <= i < 25 else
            ";末吉だと思う"   if 25 <= i < 50 else
            ";吉かな"   if 50 <= i < 75 else
            ";残念、凶です"   if 75 <= i < 90 else
            ";大凶、もう寝よう"   for i in range(99)]
        await message.channel.send(omikuji_result[random.randrange(len(omikuji_result))])
        return
    if re.match(consts.PATTERN_OMIKUJI_SEMI, message.content):
        omikuji_result = [
            ";大吉だよ！"   if i < 5 else
            ";中吉！"     if 5 <= i < 25 else
            ";末吉だと思う"   if 25 <= i < 50 else
            ";吉かな"   if 50 <= i < 75 else
            ";残念、凶です"   if 75 <= i < 90 else
            ";大凶、もう寝よう"   for i in range(99)]
        await message.channel.send(omikuji_result[random.randrange(len(omikuji_result))])
        return
    if re.match(consts.PATTERN_OMIKUJI_SEMISPACE, message.content):
        omikuji_result = [
            ";大吉だよ！"   if i < 5 else
            ";中吉！"     if 5 <= i < 25 else
            ";末吉だと思う"   if 25 <= i < 50 else
            ";吉かな"   if 50 <= i < 75 else
            ";残念、凶です"   if 75 <= i < 90 else
            ";大凶、もう寝よう"   for i in range(99)]
        await message.channel.send(omikuji_result[random.randrange(len(omikuji_result))])
        return
    #確率表示
    if re.match(consts.PATTERN_KAKURITSU, message.content):
        await message.channel.send(consts.KAKURITSU_LIST)
        return
    if re.match(consts.PATTERN_KAKURITSU_SEMI, message.content):
        await message.channel.send(consts.KAKURITSU_LIST)
        return
    if re.match(consts.PATTERN_KAKURITSU_SEMISPACE, message.content):
        await message.channel.send(consts.KAKURITSU_LIST)
        return
    # ヘルプ表示（一般向け）
    if re.match(consts.PATTERN_HELP, message.content):
        await message.channel.send(consts.HELP_MESSAGE)
        return
    # ヘルプ表示（管理者向け）
    if re.match(consts.PATTERN_HELP_FOR_ADMIN, message.content):
        await message.channel.send(consts.HELP_MESSAGE)
        return
    # ヘルプ表示（管理者向け）
    if re.match('^!batch test.*$', message.content):
        args = message.content.split()
        reminer_message = (args[2] if len(args) > 2 else "hoge ¥n hoge").format(message.author)
        print(reminer_message)
        await message.channel.send(reminer_message)
        return
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
