class Setting:
    def __init__(self, server_id='',
            change_room_number_enable=False, change_room_number_id='', change_room_number_now = '',
            afterlive_room_number_enable=False, afterlive_room_number_id='', afterlive_room_number_now = '',
            cat_enable=False, cat_id='',
            reminder_finish_enable = False, reminder_finish_id = '', reminder_finish_message = '',
            reminder_announce_enable = False, reminder_announce_id = '', reminder_announce_message = '',
            reminder_charge_enable = False, reminder_charge_id = '', reminder_charge_message = '',
            reminder_bug_enable = False, reminder_bug_id = '', reminder_bug_message = ''):
        self.server_id = server_id
        self.change_room_number_enable = change_room_number_enable
        self.change_room_number_id = change_room_number_id
        self.change_room_number_now = change_room_number_now
        self.afterlive_room_number_enable = afterlive_room_number_enable
        self.afterlive_room_number_id = afterlive_room_number_id
        self.afterlive_room_number_now = afterlive_room_number_now
        self.cat_enable = cat_enable
        self.cat_id = cat_id
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
    
       