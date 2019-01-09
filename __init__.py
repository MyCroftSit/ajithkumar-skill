from mycroft import MycroftSkill, intent_file_handler


class Ajithkumar(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ajithkumar.intent')
    def handle_ajithkumar(self, message):
        self.speak_dialog('ajithkumar')


def create_skill():
    return Ajithkumar()

