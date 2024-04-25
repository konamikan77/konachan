###################
# 環境定数
###################
# botトークン
TOKEN = "[トークンを入力]"
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
PATTERN_15_MINUITE = '^\d{4}-\d{2}-\d{2} \d{2}:(02|12|22|32|42|52):0\d\..*$'
# 毎時50分
PATTERN_50_MINUITE = r'^\d{4}-\d{2}-\d{2} \d{2}:50:0\d\..*$'
# 毎時55分
PATTERN_55_MINUITE = r'^\d{4}-\d{2}-\d{2} \d{2}:55:0\d\..*$'
# 毎時00分
PATTERN_HOUR = r'^\d{4}-\d{2}-\d{2} \d{2}:00:0\d\..*$'
# 1時55分
PATTERN_TWO = r'^\d{4}-\d{2}-\d{2} 01:55:00\..*$'
# 当bot呼び出し
PATTERN_THIS = '^!kona3.*'
# 初期化
PATTERN_INIT = '^!kona3 init$'
# 時速取得開始
PATTERN_CAT_START = '^!kona3 et s$'
# 時速取得終了
PATTERN_CAT_END = '^!kona3 et e$'
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
# 部屋番変更開始
PATTERN_AFTERLIVE_ROOM_NUMBER_START = '^!kona3 arn s$'
# 部屋番変更終了
PATTERN_AFTERLIVE_ROOM_NUMBER_END = '^!kona3 arn e$'
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
;コマンド一覧\n[試験コマンド]\n!kona d　または　;!kona d\n　→botが動くかどうか確認できる\n　　　(返事なければ動かない)\n!kona t　または　;!kona t\n　→単発で炊き通知を入れられる\n\n[おみくじコマンド]\n!omikuji　または　;!omikuji\n　→おみくじが引ける\n!kakuritsu　または　;!kakuritsu\n　→おみくじの確率一覧\n\n[その他　助けてこなちゃん]\n!kona help　または　;!kona help\n　→このヘルプを出す
"""
