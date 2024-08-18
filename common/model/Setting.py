# ver1.1.2.1　こいしたいむ実装・軽微な修正
# 対応ver
# consts.py：1.1.4.1以降　discordbot.py：1.1.6.1以降　operate_setting：1.1.2.1以降　utils：1.0.0以降

class Setting:
    def __init__(self, server_id='',
            change_room_number_enable=False, change_room_number_id='', change_room_number_now = '',
            afterlive_room_number_enable=False, afterlive_room_number_id='', afterlive_room_number_now = '',
            event_track_enable=False, event_track_id='',
            reminder_finish_enable = False, reminder_finish_id = '', reminder_finish_message = '',
            reminder_announce_enable = False, reminder_announce_id = '', reminder_announce_message = '',
            reminder_charge_enable = False, reminder_charge_id = '', reminder_charge_message = '',
            reminder_bug_enable = False, reminder_bug_id = '', reminder_bug_message = '',
            kohane_time_enable = False, kohane_time_id = '', kohane_time_message = '',
            nene_time_enable = False, nene_time_id = '', nene_time_message = '',
            minori_time_enable = False, minori_time_id = '', minori_time_message = '',
            koishi_time_enable = False, koishi_time_id = '', koishi_time_message = ''):
        self.server_id = server_id
        self.change_room_number_enable = change_room_number_enable
        self.change_room_number_id = change_room_number_id
        self.change_room_number_now = change_room_number_now
        self.afterlive_room_number_enable = afterlive_room_number_enable
        self.afterlive_room_number_id = afterlive_room_number_id
        self.afterlive_room_number_now = afterlive_room_number_now
        self.event_track_enable = event_track_enable
        self.event_track_id = event_track_id
        self.reminder_finish_enable = reminder_finish_enable
        self.reminder_finish_id = reminder_finish_id
        self.reminder_finish_message = reminder_finish_message
        self.reminder_announce_enable = reminder_announce_enable
        self.reminder_announce_id = reminder_announce_id
        self.reminder_announce_message = reminder_announce_message
        self.reminder_charge_enable = reminder_charge_enable
        self.reminder_charge_id = reminder_charge_id
        self.reminder_charge_message = reminder_charge_message
        self.reminder_bug_enable = reminder_bug_enable
        self.reminder_bug_id = reminder_bug_id
        self.reminder_bug_message = reminder_bug_message
        self.kohane_time_enable = kohane_time_enable
        self.kohane_time_id = kohane_time_id
        self.kohane_time_message = kohane_time_message
        self.nene_time_enable = nene_time_enable
        self.nene_time_id = nene_time_id
        self.nene_time_message = nene_time_message
        self.minori_time_enable = minori_time_enable
        self.minori_time_id = minori_time_id
        self.minori_time_message = minori_time_message
        self.koishi_time_enable = koishi_time_enable
        self.koishi_time_id = koishi_time_id
        self.koushi_time_message = koishi_time_message

    
       