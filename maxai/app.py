from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from .agent import Agent
from .voice import VoiceManager

KV = """
#:import dp kivy.metrics.dp
BoxLayout:
    orientation: "vertical"
    padding: dp(14)
    spacing: dp(10)
    canvas.before:
        Color:
            rgba: .035, .055, .09, 1
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        size_hint_y: None
        height: dp(65)
        Label:
            text: "MAX AI"
            font_size: "28sp"
            bold: True
            color: .2, .8, 1, 1
            halign: "left"
            valign: "middle"
            text_size: self.size
        Label:
            text: root.status
            font_size: "12sp"
            color: .7, .75, .8, 1
            halign: "right"
            valign: "middle"
            text_size: self.size

    Label:
        text: "Intelligent Phone Agent"
        size_hint_y: None
        height: dp(25)
        color: .65, .7, .78, 1
        font_size: "13sp"

    ScrollView:
        do_scroll_x: False
        Label:
            text: root.chat
            size_hint_y: None
            text_size: self.width, None
            height: self.texture_size[1] + dp(20)
            padding: dp(10), dp(10)
            font_size: "16sp"
            color: .92, .95, 1, 1
            halign: "right"

    BoxLayout:
        size_hint_y: None
        height: dp(55)
        spacing: dp(8)
        TextInput:
            id: inp
            hint_text: "اكتب أمراً لـ MAX AI..."
            multiline: False
            font_size: "16sp"
            halign: "right"
            on_text_validate: root.send(inp.text)
        Button:
            text: "إرسال"
            size_hint_x: None
            width: dp(80)
            on_release: root.send(inp.text)

    Button:
        text: "🎤  تحدث مع MAX AI"
        size_hint_y: None
        height: dp(60)
        font_size: "17sp"
        on_release: root.voice()

"""

class MaxAIApp(App):
    status = StringProperty("● جاهز")
    chat = StringProperty(
        "MAX AI: أهلاً بك 👋\n"
        "أنا MAX AI — مساعد الهاتف الذكي.\n"
        "جرّب «افتح يوتيوب».\n"
    )

    def build(self):
        self.title = "MAX AI"
        self.agent = Agent()
        self.voice_manager = VoiceManager()
        return Builder.load_string(KV)

    def send(self, text):
        text = text.strip()
        if not text:
            return
        self.root.ids.inp.text = ""
        self.chat += f"\\nأنت: {text}\\n"
        self.status = "● يفكر..."
        self.chat += f"MAX AI: {self.agent.handle(text)}\\n"
        self.status = "● جاهز"

    def voice(self):
        self.status = "● الصوت"
        self.chat += f"MAX AI: {self.voice_manager.start()}\\n"
        self.status = "● جاهز"
