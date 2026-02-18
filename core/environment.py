from datetime import datetime
import locale
# import time
# import sys

def get_current_time():
    """Get the current time（Format：YYYY-MM-DD HH:MM:SS）"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_system_language():
    """Retrieve the language region of the current operating system（for example：en_US, zh_CN）"""
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
        
def get_user_coordinates():
    """
    获取用户输入的经纬度
    """
    # 尝试从 IPython 获取 interactive_input 以支持 Jupyter 中的输入
    try:
        from IPython import get_ipython

        if get_ipython() is not None:
            # 在 Jupyter 环境下使用 input 的包装器，避免阻塞
            lat_input = input("请输入纬度（-90 ~ 90）：")
            lon_input = input("请输入经度（-180 ~ 180）：")
            return lat_input.strip(), lon_input.strip()
        else:
            # 纯 Python 脚本环境
            lat_input = input("请输入纬度（-90 ~ 90）：")
            lon_input = input("请输入经度（-180 ~ 180）：")
            return lat_input.strip(), lon_input.strip()
    except Exception:
        # 如果以上都失败（如某些嵌入式环境），退回到简单 input
        lat_input = input("请输入纬度（-90 ~ 90）：")
        lon_input = input("请输入经度（-180 ~ 180）：")
        return lat_input.strip(), lon_input.strip()
    
    
def is_valid_coordinates(lat_input, lon_input):
    """
    校验经纬度是否合法：
    - 纬度：-90 到 90 度
    - 经度：-180 到 180 度
    - 输入应为可转换为 float 的字符串，支持整数或小数
    """
    try:
        lat = float(lat_input)
        lon = float(lon_input)
        if -90 <= lat <= 90 and -180 <= lon <= 180:
            return True, lat, lon
        else:
            return False, None, None
    except (ValueError, TypeError):
        return False, None, None