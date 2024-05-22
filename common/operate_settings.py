from . import utils
from . import consts
import os
from common.model import Setting
import json
import glob

def init_settings(server_id):
    x = Setting.Setting(server_id)
    y = json.dumps(x.__dict__, indent=2)
    utils.write_file(consts.SETTING_FILE.format(server_id), y)

""" 時速取得設定開始 """
def start_event_track(server_id, channel_id):
    change_event_track(server_id, channel_id, True)

""" 時速取得設定終了 """
def end_event_track(server_id):
    change_event_track(server_id, "", False)

    """ 時速取得設定変更 """
def change_event_track(server_id, channel_id, event_track_enable):
    is_file = os.path.isfile(consts.SETTING_FILE.format(server_id))
    if not is_file:
        init_settings(server_id)
    setting_json = utils.read_file(consts.SETTING_FILE.format(server_id))
    setting = json.loads(setting_json)
    setting["event_track_enable"] = event_track_enable
    setting["event_track_id"] = channel_id
    utils.write_file(consts.SETTING_FILE.format(server_id), json.dumps(setting, indent=2))


""" 炊きリマインダー設定開始 """
def start_reminder_charge(server_id, channel_id, message):
    _change_reminder_charge(server_id, channel_id, True, message)

""" 炊きリマインダー設定終了 """
def end_reminder_charge(server_id):
    _change_reminder_charge(server_id, "", False, "")

""" 炊きリマインダー設定変更 """
def _change_reminder_charge(server_id, channel_id, reminder_charge_enable, message):
    setting_json = utils.read_file(consts.SETTING_FILE.format(server_id))
    setting = json.loads(setting_json)
    setting["reminder_charge_enable"] = reminder_charge_enable
    setting["reminder_charge_id"] = channel_id
    setting["reminder_charge_message"] = message if message != "" else consts.DEFAULT_REMINDER_CHARGE_MESSAGE
    utils.write_file(consts.SETTING_FILE.format(server_id), json.dumps(setting, indent=2))

""" シフト終了リマインダー設定開始 """
def start_reminder_finish(server_id, channel_id, message):
    _change_reminder_finish(server_id, channel_id, True, message)

""" シフト終了リマインダー設定終了 """
def end_reminder_finish(server_id):
    _change_reminder_finish(server_id, "", False, "")

""" シフト終了リマインダー設定変更 """
def _change_reminder_finish(server_id, channel_id, reminder_finish_enable, message):
    setting_json = utils.read_file(consts.SETTING_FILE.format(server_id))
    setting = json.loads(setting_json)
    setting["reminder_finish_enable"] = reminder_finish_enable
    setting["reminder_finish_id"] = channel_id
    setting["reminder_finish_message"] = message if message != "" else consts.DEFAULT_REMINDER_FINISH_MESSAGE
    utils.write_file(consts.SETTING_FILE.format(server_id), json.dumps(setting, indent=2))

""" 交代前アナウンスリマインダー設定開始 """
def start_reminder_annouce(server_id, channel_id, message):
    _change_reminder_annouce(server_id, channel_id, True, message)

""" 交代前アナウンスリマインダー設定終了 """
def end_reminder_announce(server_id):
    _change_reminder_annouce(server_id, "", False, "")

""" 交代前アナウンスリマインダー設定変更 """
def _change_reminder_annouce(server_id, channel_id, reminder_announce_enable, message):
    setting_json = utils.read_file(consts.SETTING_FILE.format(server_id))
    setting = json.loads(setting_json)
    setting["reminder_announce_enable"] = reminder_announce_enable
    setting["reminder_announce_id"] = channel_id
    setting["reminder_announce_message"] = message if message != "" else consts.DEFAULT_REMINDER_ANNOUNCE_MESSAGE
    utils.write_file(consts.SETTING_FILE.format(server_id), json.dumps(setting, indent=2))

""" 部屋番変更設定開始 """
def start_change_room_number(server_id, channel_id):
    _change_change_room_number(server_id, channel_id, True)

""" 部屋番変更設定終了 """
def end_change_room_number(server_id):
    _change_change_room_number(server_id, "", False)

""" アフターライブ部屋番変更設定開始 """
def start_afterlive_room_number(server_id, channel_id):
    _change_afterlive_room_number(server_id, channel_id, True)

""" アフターライブ部屋番変更設定終了 """
def end_afterlive_room_number(server_id):
    _change_afterlive_room_number(server_id, "", False)

""" 部屋番変更設定変更 """
def _change_change_room_number(server_id, channel_id, change_room_number_enable):
    setting_json = utils.read_file(consts.SETTING_FILE.format(server_id))
    setting = json.loads(setting_json)
    setting["change_room_number_enable"] = change_room_number_enable
    setting["change_room_number_id"] = channel_id
    utils.write_file(consts.SETTING_FILE.format(server_id), json.dumps(setting, indent=2))

""" 部屋番の現状値設定 """
def change_change_room_number_now(server_id, room_number):
    setting_json = utils.read_file(consts.SETTING_FILE.format(server_id))
    setting = json.loads(setting_json)
    setting["change_room_number_now"] = room_number
    utils.write_file(consts.SETTING_FILE.format(server_id), json.dumps(setting, indent=2))

""" アフライ部屋番変更設定変更 """
def _change_afterlive_room_number(server_id, channel_id, afterlive_room_number_enable):
    setting_json = utils.read_file(consts.SETTING_FILE.format(server_id))
    setting = json.loads(setting_json)
    setting["afterlive_room_number_enable"] = afterlive_room_number_enable
    setting["afterlive_room_number_id"] = channel_id
    utils.write_file(consts.SETTING_FILE.format(server_id), json.dumps(setting, indent=2))

""" アフライ部屋番の現状値設定 """
def change_afterlive_room_number_now(server_id, room_number):
    setting_json = utils.read_file(consts.SETTING_FILE.format(server_id))
    setting = json.loads(setting_json)
    setting["afterlive_room_number_now"] = room_number
    utils.write_file(consts.SETTING_FILE.format(server_id), json.dumps(setting, indent=2))

def get_event_track_targets():
    files = glob.glob(consts.SETTINGS)
    targets = []
    for file in files:
        f = open(file, 'r', encoding='UTF-8')
        data_json = f.read()
        f.close()
        data = json.loads(data_json)
        if data["event_track_enable"]:
            targets.append(data)
    return targets

def get_reminder_finish_targets():
    files = glob.glob(consts.SETTINGS)
    targets = []
    for file in files:
        f = open(file, 'r', encoding='UTF-8')
        data_json = f.read()
        f.close()
        data = json.loads(data_json)
        if data["reminder_finish_enable"]:
            targets.append(data)
    return targets

def get_reminder_announce_targets():
    files = glob.glob(consts.SETTINGS)
    targets = []
    for file in files:
        f = open(file, 'r', encoding='UTF-8')
        data_json = f.read()
        f.close()
        data = json.loads(data_json)
        if data["reminder_announce_enable"]:
            targets.append(data)
    return targets

def get_reminder_charge_targets():
    files = glob.glob(consts.SETTINGS)
    targets = []
    for file in files:
        f = open(file, 'r', encoding='UTF-8')
        data_json = f.read()
        f.close()
        data = json.loads(data_json)
        if data["reminder_charge_enable"]:
            targets.append(data)
    return targets

def get_reminder_bug_targets():
    files = glob.glob(consts.SETTINGS)
    targets = []
    for file in files:
        f = open(file, 'r', encoding='UTF-8')
        data_json = f.read()
        f.close()
        data = json.loads(data_json)
        if data["reminder_bug_enable"]:
            targets.append(data)
    return targets

def get_reminder_charge_message(server_id):
    setting_json = utils.read_file(consts.SETTING_FILE.format(server_id))
    setting = json.loads(setting_json)
    return setting["reminder_charge_message"]

def get_reminder_finish_message(server_id):
    setting_json = utils.read_file(consts.SETTING_FILE.format(server_id))
    setting = json.loads(setting_json)
    return setting["reminder_finish_message"]

def get_reminder_announce_message(server_id):
    setting_json = utils.read_file(consts.SETTING_FILE.format(server_id))
    setting = json.loads(setting_json)
    return setting["reminder_announce_message"]

def get_reminder_bug_message(server_id):
    setting_json = utils.read_file(consts.SETTING_FILE.format(server_id))
    setting = json.loads(setting_json)
    return setting["reminder_bug_message"]

def is_change_room_number_target(server_id):
    setting_json = utils.read_file(consts.SETTING_FILE.format(server_id))
    setting = json.loads(setting_json)
    return setting["change_room_number_enable"]

def is_dupli_change_room_number_now(server_id, room_number):
    setting_json = utils.read_file(consts.SETTING_FILE.format(server_id))
    setting = json.loads(setting_json)
    return str(setting["change_room_number_now"]) == str(room_number)

def get_change_room_number_id(server_id):
    setting_json = utils.read_file(consts.SETTING_FILE.format(server_id))
    setting = json.loads(setting_json)
    return setting["change_room_number_id"]

def is_afterlive_room_number_target(server_id):
    setting_json = utils.read_file(consts.SETTING_FILE.format(server_id))
    setting = json.loads(setting_json)
    return setting["afterlive_room_number_enable"]

def is_dupli_afterlive_room_number_now(server_id, room_number):
    setting_json = utils.read_file(consts.SETTING_FILE.format(server_id))
    setting = json.loads(setting_json)
    return str(setting["afterlive_room_number_now"]) == str(room_number)

def get_afterlive_room_number_id(server_id):
    setting_json = utils.read_file(consts.SETTING_FILE.format(server_id))
    setting = json.loads(setting_json)
    return setting["afterlive_room_number_id"]