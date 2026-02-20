import httpx



EXTERNAL_APIS = {
    "geo":{
        "base_url":"https://nominatim.openstreetmap.org/reverse?"
        # lat=31.2304&lon=121.4737&format=json&accept-language=en
    },
    "weather":{
        "base_url":"https://api.open-meteo.com/v1/forecast?"
        # https://api.open-meteo.com/v1/forecast?latitude=25.04&longitude=121.56&current_weather=true&temperature_unit=celsius&timezone=Asia/Taipei
    }
}

async def get_weather(lat,lon,language):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=10.0)
            data = response.json()
            # 关键步骤：只返回 Agent 需要的核心信息，节省 Token
            return f"当前的天气是：{data['weather']}, 温度：{data['temp']}°C……"
        except Exception as e:
            return f"查询失败: {str(e)}"


async def get_location(lat,lon,language): 
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=10.0)
            data = response.json()
            # 关键步骤：只返回 Agent 需要的核心信息，节省 Token
            return f"你所在的城市是：{data['city']}"
        except Exception as e:
            return f"查询失败: {str(e)}"