import httpx

EXTERNAL_APIS = {
    "geo": {
        "base_url": "https://nominatim.openstreetmap.org/reverse?",
    },
    "weather": {
        "base_url": "https://api.open-meteo.com/v1/forecast?",
    }
}

async def get_weather(lat: float, lon: float, language: str) -> str:
    """Fetch current weather for given coordinates and return a concise summary."""
    async with httpx.AsyncClient() as client:
        try:
            # Construct URL with parameters
            base = EXTERNAL_APIS["weather"]["base_url"]
            params = {
                "latitude": lat,
                "longitude": lon,
                "current":"temperature_2m,relative_humidity_2m,wind_speed_10m,wind_direction_10m,weather_code"
            }
            response = await client.get(base, params=params, timeout=10.0)
            response.raise_for_status()
            data = response.json()

            # Extract current weather data
            current = data.get("current", {})

            # Safely extract each field (match API response structure exactly)
            temp = current.get("temperature_2m")
            humidity = current.get("relative_humidity_2m")
            wind_speed = current.get("wind_speed_10m")
            wind_direction = current.get("wind_direction_10m")
            weather_code = current.get("weather_code")

            # Map WMO weather codes to simplified descriptions
            # Ref: https://open-meteo.com/en/docs
            weather_descriptions = {
                0: "晴",
                1: "少云",
                2: "多云",
                3: "阴",
                45: "雾",
                48: "冻雾",
                51: "毛毛雨",
                53: "小雨",
                55: "大雨",
                56: "冻毛毛雨",
                57: "冻小雨",
                61: "小雨",
                63: "中雨",
                65: "大雨",
                66: "冻毛毛雨",
                67: "冻小雨",
                71: "小雪",
                73: "中雪",
                75: "大雪",
                76: "冰晶（地表）",
                77: "雪粒",
                80: "阵雨",
                81: "中阵雨",
                82: "强阵雨",
                95: "雷阵雨",
                96: "雷阵雨有冰雹",
                99: "强雷阵雨有冰雹"
            }

            # Format direction as cardinal direction if possible (simplified)
            def deg_to_cardinal(deg):
                dirs = ["北", "东北", "东", "东南", "南", "西南", "西", "西北"]
                idx = round(deg / 45) % 8
                return dirs[idx]

            wind_dir_text = deg_to_cardinal(wind_direction) if wind_direction is not None else "未知"
            temp_str = f"{temp}°C" if temp is not None else "无数据"
            humidity_str = f"{humidity}%" if humidity is not None else ""
            wind_str = f"风速 {wind_speed} km/h，风向 {wind_dir_text}" if wind_speed is not None and wind_direction is not None else "风力无数据"
            weather_text = weather_descriptions.get(weather_code, f"天气代码 {weather_code}") if weather_code is not None else "无数据"
            return f"现在天气：{weather_text}；温度：{temp_str}；湿度：{humidity_str}；{wind_str}"
        except httpx.HTTPStatusError as e:
            return f"天气查询失败：HTTP {e.response.status_code}"
        except (KeyError, TypeError) as e:
            return f"天气数据解析异常：{e}"
        except Exception as e:
            return f"查询失败: {str(e)}"


async def get_location(lat: float, lon: float, language: str) -> str:
    """Reverse geocode coordinates to obtain location name (e.g., city/town)."""
    async with httpx.AsyncClient() as client:
        try:
            # Construct URL with parameters
            base = EXTERNAL_APIS["geo"]["base_url"]
            params = {
                "lat": lat,
                "lon": lon,
                "format": "json",
                "accept-language": language if language else "cn"
            }
            # Nominatim requires User-Agent header
            headers = {
                "User-Agent": "100-Local-AI-Use-Cases-for-Everyday-Life (contact: xbenben2011@gmail.com)",
                "Accept": "application/json",
                "Accept-Language": "en",
                "Connection": "keep-alive",
            }
            response = await client.get(base, params=params, headers=headers, timeout=10.0)
            response.raise_for_status()
            data = response.json()

            # Extract address fields
            address = data.get("address", {})

            # Get country, state, city; may be None or missing
            country = address.get("country", "")
            state = address.get("state", "")
            city = address.get("city") or address.get("town") or address.get("village", "")

            # Format based on language
            if language == "cn":
                # Chinese: country + state + city (allowing empties)
                parts = [p for p in [country, state, city] if p]
                location_str = "".join(parts) or "未知地区"
            else:  # English (default)
                # En: city, state, country — only non-empty components
                parts = [p for p in [city, state, country] if p]
                location_str = ", ".join(parts) or "Unknown Location"
            return f"所在的位置是：{location_str}"
        except httpx.HTTPStatusError as e:
            return f"位置查询失败：HTTP {e.response.status_code}"
        except (KeyError, TypeError) as e:
            return f"位置数据解析异常：{e}"
        except Exception as e:
            return f"查询失败: {str(e)}"
