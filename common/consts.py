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
# 当bot呼び出し
# PATTERN_THIS = '^!kona3.*'
# 初期化
PATTERN_INIT = '^!kona3 init$'
# 時速取得開始
PATTERN_EVENT_TRACK_START = '^!kona3 et s$'
# 時速取得終了
PATTERN_EVENT_TRACK_END = '^!kona3 et e$'
# 炊きリマインダー開始
PATTERN_REMINDER_CHARGE_START = '^!kona3 rc s($| .*$)'
# 炊きリマインダー終了
PATTERN_REMINDER_CHARGE_END = '^!kona3 rc e$'
# シフト交代リマインダー開始
PATTERN_REMINDER_FINISH_START = '^!kona3 rf s($| .*$)'
# シフト交代リマインダー終了
PATTERN_REMINDER_FINISH_END = '^!kona3 rf e$'
# 交代前アナウンスマインダー開始
PATTERN_REMINDER_ANNOUNCE_START = '^!kona3 ra s($| .*$)'
# 交代前アナウンスリマインダー終了
PATTERN_REMINDER_ANNOUNCE_END = '^!kona3 ra e$'
# 部屋番変更開始
PATTERN_CHANGE_ROOM_NUMBER_START = '^!kona3 crn s$'
# 部屋番変更終了
PATTERN_CHANGE_ROOM_NUMBER_END = '^!kona3 crn e$'
# アフライ部屋番変更開始
PATTERN_AFTERLIVE_ROOM_NUMBER_START = '^!kona3 arn s$'
# アフライ部屋番変更終了
PATTERN_AFTERLIVE_ROOM_NUMBER_END = '^!kona3 arn e$'
# 話題提供
PATTERN_WADAI = '^!wadai$'
PATTERN_WADAI_SEMI = '^;!wadai$'
PATTERN_WADAI_SEMISPACE = '^; !wadai$'
# おみくじ機能
PATTERN_OMIKUJI = '^!omikuji$'
PATTERN_OMIKUJI_SEMI = '^;!omikuji$'
PATTERN_OMIKUJI_SEMISPACE = '^; !omikuji$'
PATTERN_KAKURITSU = '^!kakuritsu$'
PATTERN_KAKURITSU_SEMI = '^;!kakuritsu$'
PATTERN_KAKURITSU_SEMISPACE = '^; !kakuritsu$'
# ヘルプ（一般向け）
PATTERN_HELP = '^!kona3 help$'
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

# HELPメッセージ
HELP_MESSAGE="""
;コマンド一覧\n!kona3 rc s\n　→ 炊きリマインド開始(毎時05/20/35分)\n!kona3 rc e\n　→ 炊きリマインド終了\n!kona3 rf s\n　→ 交代前アナウンス開始(毎時50分)\n!kona3 rf e\n　→ 交代前アナウンス終了\n!kona3 ra s\n　→ 時速リマインド開始(毎時57分)\n!kona3 ra e\n　→ 時速リマインド終了\n\n(次のコマンドは部屋番号チャンネルで実行してください)\n!kona3 crn s\n　→ 部屋番号変更開始\n!kona3 crn e\n　→ 部屋番号変更終了\n\n----------------------------------------\n\n遊び機能\n!wadai　または　;!wadai\n　→ 話題提供してくれるよ！\n!omikuji　または　;!omikuji\n　→ おみくじが引けるよ\n!kakuritsu　または　;!kakuritsu\n　→ おみくじの確率を教えてくれる\n\n----------------------------------------\n\nその他(助けてこなちゃん)\n!kona3 help\n　→ このヘルプメニューを表示\n\n(他にほしい機能などあれば、みかんに教えてください)
"""
# 確率一覧
KAKURITSU_LIST = '; \n大吉：5% \n中吉：20% \n末吉：25% \n吉　：25% \n凶　：15% \n大凶：10%'