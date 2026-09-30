import re
import urllib.parse
from .planner import Planner
from .memory import Memory
from .android_bridge import AndroidBridge

class Agent:
    def __init__(self):
        self.planner = Planner()
        self.memory = Memory()
        self.android = AndroidBridge()

    def handle(self, text):
        text = text.strip()
        if not text:
            return "قل لي ماذا تريد أن أفعل."

        m = re.match(r"^(?:احفظ|تذكر)\\s+أن\\s+(.+?)\\s+(?:هو|هي|:|=)\\s+(.+)$", text)
        if m:
            self.memory.save(m.group(1).strip(), m.group(2).strip())
            return "تم حفظ المعلومة في ذاكرة MAX AI."

        if text in ("ماذا تتذكر", "ماذا تتذكر عني", "ذاكرتي"):
            rows = self.memory.all()
            return "ذاكرتي فارغة حاليًا." if not rows else "\n".join(f"• {k}: {v}" for k, v in rows)

        plan = self.planner.plan(text)
        if plan["action"] == "open_app":
            return self.android.open_app(plan["target"])[1]
        if plan["action"] == "web_search":
            q = urllib.parse.quote(plan["query"])
            return self.android.open_url("https://www.google.com/search?q=" + q)[1]
        if plan["action"] == "help":
            return "جرّب: افتح يوتيوب، افتح تيليجرام، ابحث عن Python، أو احفظ معلومة."
        return "فهمت الأمر، لكن الأداة المطلوبة غير مفعلة في هذه النسخة."
