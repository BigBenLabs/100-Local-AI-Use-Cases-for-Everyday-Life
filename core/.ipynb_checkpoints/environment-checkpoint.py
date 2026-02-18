from datetime import datetime
import locale
import time

def get_current_time():
    """获取当前时间（格式：YYYY-MM-DD HH:MM:SS）"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_current_timezone():
    """获取当前系统时区（例如：Asia/Shanghai）"""
    # 尝试使用 zoneinfo（Python 3.9+），否则回退到 time.tzname
    try:
        from zoneinfo import ZoneInfo
        # 获取本地时区名称（在大多数系统上，UTC 可能需要显式指定；这里尝试用 'localtime'）
        # 但 Python zoneinfo 没有直接获取本地时区的 API，因此改用 tzlocal
        try:
            from tzlocal import get_localzone_name
            return get_localzone_name()
        except ImportError:
            # 如果 tzlocal 不可用，尝试用 os.name 和 platform fallback
            import os, platform
            if os.name == 'nt':
                # Windows: 从注册表获取时区（简化版）
                import winreg
                try:
                    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\TimeZoneInformation")
                    tz_name = winreg.QueryValueEx(key, "TimeZoneKeyName")[0]
                    # 转换为 IANA 时区名（部分映射）
                    mapping = {
                        "China Standard Time": "Asia/Shanghai",
                        "Pacific Standard Time": "America/Los_Angeles",
                        # 可扩展更多映射，此处为示例
                    }
                    return mapping.get(tz_name, tz_name)
                except Exception:
                    # 回退到 time.tzname
                    return time.tzname[0]
            else:
                # Unix-like 系统：读取 /etc/localtime 链接
                import os.path
                try:
                    link = os.readlink("/etc/localtime")
                    # 提取时区名，如 "/usr/share/zoneinfo/Asia/Shanghai"
                    if "zoneinfo" in link:
                        tz = link.split("zoneinfo/")[-1]
                        return tz
                except Exception:
                    pass
                # 最终回退：time.tzname[0]
                return time.tzname[0]
    except ImportError:
        # Python <3.9，仅用 time.tzname
        return time.tzname[0]

def get_system_language():
    """获取当前操作系统的语言区域（例如：en_US, zh_CN）"""
    try:
        # 优先使用 locale.getdefaultlocale（在部分平台已弃用，但兼容性好）
        lang, _ = locale.getdefaultlocale()
        return lang or "Unknown"
    except Exception:
        try:
            # 更现代的 locale 模块方式（Python 3.10+）
            lang = locale.getlocale()[0]
            return lang or "Unknown"
        except Exception:
            # 最终回退：尝试环境变量
            import os
            lang = os.getenv('LANG', '')
            if not lang:
                lang = os.getenv('LC_ALL', '')
            # 从形如 'en_US.UTF-8' 提取语言代码
            if lang:
                return lang.split('.')[0].split('_')[0] + '_' + (lang.split('.')[0].split('_')[1] if len(lang.split('.')) > 0 and '_' in lang.split('.')[0] else '')
            return "Unknown"