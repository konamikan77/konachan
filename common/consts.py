# ver1.1.4.4　exeコマンド
# 対応ver
# discordbot.py：1.1.6.4以降　operate_setting：1.1.2.1以降　utils：1.0.0以降　Setting：1.1.2.1以降

###################
# 環境定数
###################
# サーバー設定ディレクトリ
SETTING_DIR = "./export/settings/"
# サーバー設定ファイル
SETTING_FILE = "./export/settings/{}.json"
# サーバー設定一覧
SETTINGS = "./export/settings/*"

###################
# 入力判定文字
###################
# 毎分
PATTERN_MINUITE = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:0\d\..*$'
# 10分毎
PATTERN_10_MINUITE = r'^\d{4}-\d{2}-\d{2} \d{2}:\d0:0\d\..*$'
# 15分毎
PATTERN_15_MINUITE = r'^\d{4}-\d{2}-\d{2} \d{2}:(05|20|35):0\d\..*$'
# PATTERN_15_MINUITE = r'^\d{4}-\d{2}-\d{2} \d{2}:(00|02|04|06|08|10|12|14|16|18|20|22|24|26|28|30|32|34|36|38|40|42|44|46|48|52|54|56|58):0\d\..*$'
#PATTERN_15_MINUITE = r'^\d{4}-\d{2}-\d{2} \d{2}:(00|10|20|30|40):0\d\..*$'
# 毎時50分
PATTERN_50_MINUITE = r'^\d{4}-\d{2}-\d{2} \d{2}:50:0\d\..*$'
# 毎時55分
PATTERN_55_MINUITE = r'^\d{4}-\d{2}-\d{2} \d{2}:57:0\d\..*$'
# 毎時00分
PATTERN_HOUR = r'^\d{4}-\d{2}-\d{2} \d{2}:00:0\d\..*$'
# 1時55分
PATTERN_TWO = r'^\d{4}-\d{2}-\d{2} 01:55:00\..*$'
# こはねたいむ
PATTERN_KOHANE_TIME_THREEHOURTWOMINUTES = r'^\d{4}-\d{2}-\d{2} 03:02:0\d\..*$'
# ねねたいむ
PATTERN_NENE_TIME_SEVENHOURTWENTYMINUTES = r'^\d{4}-\d{2}-\d{2} 07:20:0\d\..*$'
# みのりたいむ
PATTERN_MINORI_TIME_FOURHOURFOURTEENMINUTES = r'^\d{4}-\d{2}-\d{2} 04:14:0\d\..*$'
# こいしたいむ
PATTERN_KOISHI_TIME_FIVEHOURFOURTEENMINUTES = r'^\d{4}-\d{2}-\d{2} 05:14:0\d\..*$'
# 当bot呼び出し
# PATTERN_THIS = '^!kona3.*'
# 初期化
PATTERN_INIT = r'^;?\s?!kona3 init$'
# 時速取得開始
PATTERN_EVENT_TRACK_START = r'^;?\s?!kona3 et s$'
# 時速取得終了
PATTERN_EVENT_TRACK_END = r'^;?\s?!kona3 et e$'
# 炊きリマインダー開始
PATTERN_REMINDER_CHARGE_START = r'^;?\s?!kona3 rc s($| .*$)'
# 炊きリマインダー終了
PATTERN_REMINDER_CHARGE_END = r'^;?\s?!kona3 rc e$'
# シフト交代リマインダー開始
PATTERN_REMINDER_FINISH_START = r'^;?\s?!kona3 rf s($| .*$)'
# シフト交代リマインダー終了
PATTERN_REMINDER_FINISH_END = r'^;?\s?!kona3 rf e$'
# 交代前アナウンスマインダー開始
PATTERN_REMINDER_ANNOUNCE_START = r'^;?\s?!kona3 ra s($| .*$)'
# 交代前アナウンスリマインダー終了
PATTERN_REMINDER_ANNOUNCE_END = r'^;?\s?!kona3 ra e$'
# 部屋番変更開始
PATTERN_CHANGE_ROOM_NUMBER_START = r'^;?\s?!kona3 crn s$'
# 部屋番変更終了
PATTERN_CHANGE_ROOM_NUMBER_END = r'^;?\s?!kona3 crn e$'
# アフライ部屋番変更開始
PATTERN_AFTERLIVE_ROOM_NUMBER_START = r'^;?\s?!kona3 arn s$'
# アフライ部屋番変更終了
PATTERN_AFTERLIVE_ROOM_NUMBER_END = r'^;?\s?!kona3 arn e$'
# テストコマンド
PATTERN_TEST_COMMAND = r'^;?\s?!kona3 test$'
# コマンド実行
PATTERN_EXE_COMMAND = r'^;?\s?!kona3 exe$'
# 話題提供
PATTERN_WADAI = r'^;?\s?!wadai$'
# おみくじ機能
PATTERN_OMIKUJI = r'^;?\s?!omikuji$'
PATTERN_KAKURITSU = r'^;?\s?!kakuritsu$'
# こはねたいむ
PATTERN_KOHANE_START = r'^;?\s?!kohane s$'
PATTERN_KOHANE_END = r'^;?\s?!kohane e$'
# ねねたいむ
PATTERN_NENE_START = r'^;?\s?!nene s$'
PATTERN_NENE_END = r'^;?\s?!nene e$'
# みのりたいむ
PATTERN_MINORI_START = r'^;?\s?!minori s$'
PATTERN_MINORI_END = r'^;?\s?!minori e$'
# こいしたいむ
PATTERN_KOISHI_START = r'^;?\s?!koishi s$'
PATTERN_KOISHI_END = r'^;?\s?!koishi e$'
# ビンゴシート作成
PATTERN_BINGO_SHEET = r'^;?\s?!bingo sheet$'
PATTERN_RANDOM_NUMBER_1_to_75 = r'^;?\s?!bingo$'
# 楽曲ランダム返答機能
PATTERN_RANDOM_MUSIC_ONE = '^!music 1$'
PATTERN_RANDOM_MUSIC_TWO = '^!music 2$'
PATTERN_RANDOM_MUSIC_THREE = '^!music 3$'
PATTERN_RANDOM_MUSIC_FOUR = '^!music 4$'
PATTERN_RANDOM_MUSIC_FIVE = '^!music 5$'
PATTERN_RANDOM_MUSIC_SIX = '^!music 6$'
# 初期メッセージ
PATTERN_FIRST = r'^;?\s?!kona3 first$'
# セカンドメッセージ
PATTERN_SECOND = r'^;?\s?!kona3 second$'
# ヘルプ（一般向け）
PATTERN_HELP = r'^;?\s?!kona3 help$'
# ヘルプ（管理者向け）
PATTERN_HELP_FOR_ADMIN = '^!kona3 help admin$'
# 部屋番変更
PATTERN_CHANGE_ROOM_NUMBER = r'^;?\s?\d{5}$'
# 部屋番変更
PATTERN_AFTERLIVE_ROOM_NUMBER = r'^;?\s?\d{6}$'

###################
# 出力テンプレート
###################
# 部屋番号テンプレート
CHANGE_ROOM_NUMBER_TEMPLATE = "部屋番号【{}】"
# アフターライブ部屋番号テンプレート
AFTERLIVE_ROOM_NUMBER_TEMPLATE = "アフライ【{}】"

###################
# メッセージ
###################
# 炊きリマインダーデフォルトメッセージ
DEFAULT_REMINDER_CHARGE_MESSAGE = 'たこうね'
# シフト終了リマインダーデフォルトメッセージ
DEFAULT_REMINDER_FINISH_MESSAGE = 'シフト終了10分前です'
# 交代前アナウンスリマインダーデフォルトメッセージ
DEFAULT_REMINDER_ANNOUNCE_MESSAGE = 'シフト終了5分前です'
# こはねたいむデフォルトメッセージ
DEFAULT_KOHANE_MESSAGE = '3時2分だよ'
# ねねたいむデフォルトメッセージ
DEFAULT_NENE_MESSAGE = '7時20分だよ'
# みのりたいむデフォルトメッセージ
DEFAULT_MINORI_MESSAGE = '4時14分だよ'
# こいしたいむデフォルトメッセージ
DEFAULT_KOISHI_MESSAGE = '5時14分だよ'

###################
# しょーもないコマンド
###################
# こゆコマンド
PATTERN_KOYU_1 = r'^;?\s?!koyu$'
# らいるめコマンド
PATTERN_RAIRUME_1 = r'^;?\s?!rairume$'

# HELPメッセージ
HELP_MESSAGE="""
;コマンド一覧  (※すべてセミコロン付きで実行可能)
!kona3 rc s
　→ 炊きリマインド開始(毎時05/20/35分)
!kona3 rc e
　→ 炊きリマインド終了
!kona3 rf s
　→ 交代前アナウンス開始(毎時50分)
!kona3 rf e
　→ 交代前アナウンス終了
!kona3 ra s
　→ 時速リマインド開始(毎時57分)
!kona3 ra e
　→ 時速リマインド終了

!kona3 test
　→ 読み上げテスト

(次のコマンドは部屋番号チャンネルで実行してください)
!kona3 crn s
　→ 部屋番号変更開始
!kona3 crn e
　→ 部屋番号変更終了
!kona3 arn s
　→ アフライ部屋番号変更開始
!kona3 arn e
　→ アフライ部屋番号変更終了

----------------------------------------

遊び機能
!wadai
　→ 話題提供してくれるよ！
!omikuji
　→ おみくじが引けるよ
!kakuritsu
　→ おみくじの確率を教えてくれる

!kohane s
　→ 毎日3時2分にこはねたいむを教えてくれる
!kohane e
　→ こはねたいむ終了
※現在、こはね(kohane)、寧々(nene)、みのり(minori)が対応しています

----------------------------------------

その他(助けてこなちゃん)
!kona3 help
　→ このヘルプメニューを表示
!kona3 first
　→ 導入時の注意点とかを表示

(他にほしい機能などあれば、みかん (<@878070194277347349>) に教えてください)
"""
FIRST_MESSAGE="""
;こんにちは！こなちゃん3の導入ありがとうございます:woman_bowing:
このbotの使用にあたって、最初にお伝えしたいことがあるのでご確認をお願いします！

### １．読み上げについて
(※ここではShabeleAの読み上げ方法について記載してます。他の読み上げbotは仕様が異なる可能性があるので注意してください)
/読み上げ対象ボット 操作:追加 対象ボット:@こなちゃん3#8388
で登録してください。(ShabeleAのスラッシュコマンドです)
おそらくですが、鯖主や管理権限のある方でないと設定できない可能性があるのでご注意ください:sweat_drops:

### ２．初期化について
こなちゃん3はみかんの気分で機能追加めっちゃするときがあります。そのときに一部ファイルを削除等するので、使用の際は最初に「!kona3 init」と入力してください。(この後に好きなコマンドを使って大丈夫です)
基本的に同じイベントの期間内なら初期化の必要はないです◎
(※init：initialize(初期化)の略です)

### ３．使用について
こなちゃん3は使用する際にサーバーの立ち上げが必要になります。(←これはみかんがやること)
そのため、使う際にはみかんにあらかじめ伝えてください！

### ４．その他困ったとき
コマンドで困ったときは「!kona3 help」と入力すればヘルプメニューがでます。
それでもわからないときは、直接みかんに聞いてください。

"""

SECOND_MESSAGE="""
;書いてないのによくこのコマンド気づいたね。
特になにもありません:persevere:
"""
# 確率一覧
KAKURITSU_LIST = '; \n大吉：5% \n中吉：20% \n末吉：25% \n吉　：25% \n凶　：15% \n大凶：10%'


#!bingo sheet
#　→ ビンゴシートを作ってくれる
#!bingo
#　→ 1から75の数字をランダムに出してくれる