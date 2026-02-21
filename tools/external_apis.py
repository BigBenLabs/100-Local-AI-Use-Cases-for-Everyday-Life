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

            return {"ok": True, "data": {"temp":temp,"humidity":humidity,"wind_speed":wind_speed,"wind_direction":wind_direction,"weather_code":weather_code}, "error": None}
        except httpx.HTTPStatusError as e:
            return {"ok": False, "data": None, "error": f"HTTP_{e.response.status_code}"}
        except (KeyError, TypeError) as e:
            return {"ok": False, "data": None, "error": "PARSE_ERROR"}
        except Exception as e:
            return {"ok": False, "data": None, "error": ("UNKNOWN_ERROR", str(e))}


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
                "accept-language": language if language else "zh"
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
            if language == "zh":
                # Chinese: country + state + city (allowing empties)
                parts = [p for p in [country, state, city] if p]
                location_str = "".join(parts) or "未知地区"
            else:  # English (default)
                # En: city, state, country — only non-empty components
                parts = [p for p in [city, state, country] if p]
                location_str = ", ".join(parts) or "Unknown Location"
            return {"ok": True, "data": location_str, "error": None}
        except httpx.HTTPStatusError as e:
            return {"ok": False, "data": None, "error": f"HTTP_{e.response.status_code}"}
        except (KeyError, TypeError) as e:
            return {"ok": False, "data": None, "error": "PARSE_ERROR"}
        except Exception as e:
            return {"ok": False, "data": None, "error": ("UNKNOWN_ERROR", str(e))}