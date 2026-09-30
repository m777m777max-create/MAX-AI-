import webbrowser

try:
    from jnius import autoclass
    HAS_JNIUS = True
except Exception:
    HAS_JNIUS = False

class AndroidBridge:
    PACKAGES = {
        "youtube": "com.google.android.youtube",
        "telegram": "org.telegram.messenger",
        "whatsapp": "com.whatsapp",
        "chrome": "com.android.chrome",
        "settings": "com.android.settings",
    }

    def open_app(self, key):
        package = self.PACKAGES.get(key)
        if not package:
            return False, "التطبيق غير معروف."
        if not HAS_JNIUS:
            return False, "هذه الوظيفة تعمل داخل APK فقط."
        try:
            Activity = autoclass("org.kivy.android.PythonActivity")
            activity = Activity.mActivity
            intent = activity.getPackageManager().getLaunchIntentForPackage(package)
            if intent is None:
                return False, "التطبيق غير مثبت على الهاتف."
            activity.startActivity(intent)
            return True, "تم فتح التطبيق."
        except Exception as e:
            return False, "تعذر فتح التطبيق: " + str(e)

    def open_url(self, url):
        try:
            webbrowser.open(url)
            return True, "تم فتح الرابط."
        except Exception as e:
            return False, str(e)
