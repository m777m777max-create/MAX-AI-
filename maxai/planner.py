class Planner:
    def plan(self, text):
        t = text.strip().lower()
        apps = {
            "يوتيوب": "youtube", "youtube": "youtube",
            "تيليجرام": "telegram", "telegram": "telegram",
            "واتساب": "whatsapp", "whatsapp": "whatsapp",
            "كروم": "chrome", "chrome": "chrome",
            "الإعدادات": "settings", "الاعدادات": "settings"
        }
        for name, key in apps.items():
            if f"افتح {name}" in t or f"فتح {name}" in t:
                return {"action": "open_app", "target": key, "label": name}
        if t.startswith("ابحث عن "):
            return {"action": "web_search", "query": text[len("ابحث عن "):].strip()}
        if t in ("مساعدة", "help"):
            return {"action": "help"}
        return {"action": "chat", "text": text}
