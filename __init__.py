from mycroft import MycroftSkill, intent_file_handler


class DailyUpdate(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('update.daily.intent')
    def handle_update_daily(self, message):
        self.speak_dialog('update.daily')


def create_skill():
    return DailyUpdate()

