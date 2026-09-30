class VoiceManager:
    def __init__(self):
        self.listening = False

    def start(self):
        self.listening = True
        return "وضع الصوت جاهز. سيتم ربط SpeechRecognizer في طبقة Android."

    def stop(self):
        self.listening = False
        return "توقف الاستماع."
