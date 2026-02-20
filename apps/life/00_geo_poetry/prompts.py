support_language = ['zh_CN','en_US','en_GB','en_CA','Unknown']
system_prompts = {
    "zh_CN":{
        "reply":"注意用中文回复。"
    },
    "en_US":{
        "reply":"Please reply in English."
    },
    "en_GB":{
        "reply":"Please reply in English."
    },
    "en_CA":{
        "reply":"Please reply in English."
    },
    "Unknown":{
        "reply":"注意用中文回复。"
    }
}
user_prompts = {
    "zh_CN":{
        "short":"zh",
        "name":"中文",
        "author":"诗词的作者",
        "title_of_poem":"这首诗或词的名字",
        "line_of_poem":"你推送的这句诗",
        "entire_poem":"整首诗的内容",
        "reason":"推荐理由",
        "season":["初春","春天","春末夏初","初夏","盛夏","夏末秋初","初秋","深秋","秋末冬初","初冬","严冬","冬末春初"],
        "time":["凌晨", "清晨", "上午", "中午", "下午","傍晚","晚上","深夜"],
        "geo_wrong":"输入的经纬度不合法！请重新输入（示例：纬度 39.9，经度 116.4）",
        "generate_season":"从以下时间中分析并提取信息，注意，只提取'TimeFomatOutPut' 这个class中定义的信息。"
    },
    "Unknown":{
        "short":"zh",
        "name":"中文",    
        "author":"诗词的作者",
        "title_of_poem":"这首诗或词的名字",
        "line_of_poem":"你推送的这句诗",
        "entire_poem":"整首诗的内容",
        "reason":"推荐理由",
        "season":["初春","春天","春末夏初","初夏","盛夏","夏末秋初","初秋","深秋","秋末冬初","初冬","严冬","冬末春初"],
        "time":["凌晨", "清晨", "上午", "中午", "下午","傍晚","晚上","深夜"],
        "geo_wrong":"输入的经纬度不合法！请重新输入（示例：纬度 39.9，经度 116.4）",
        "generate_season":"从以下时间中分析并提取信息，注意，只提取'TimeFomatOutPut' 这个class中定义的信息。"
    },
    "en_US":{
        "short":"en",
        "name":"English",
        "author":"The author of the poem",
        "title_of_poem":"The name of the poem",
        "line_of_poem":"The line of poetry you recommended",
        "entire_poem":"The content of the entire poem",
        "reason":"Reason for recommendation",
        "season":["Early Spring", "Spring", "Late Spring/Early Summer", "Early Summer", "Midsummer", "Late Summer/Early Autumn", "Early Autumn", "Late Autumn", "Late Autumn/Early Winter", "Early Winter", "Severe Winter", "Late Winter/Early Spring"],
        "time":["Early Morning", "Morning", "Noon", "Afternoon", "Evening", "Night", "Late Night"],
        "geo_wrong":"The entered latitude and longitude are invalid! Please re-enter (Example: Latitude 39.9, Longitude 116.4)",
        "generate_season":"Analyze and extract information from the following time periods. Note that only information defined in the 'TimeFormatOutPut' class should be extracted."
    },
    "en_GB":{
        "short":"en",
        "name":"English",
        "author":"The author of the poem",
        "title_of_poem":"The name of the poem",
        "line_of_poem":"The line of poetry you recommended",
        "entire_poem":"The content of the entire poem",
        "reason":"Reason for recommendation",
        "season":["Early Spring", "Spring", "Late Spring/Early Summer", "Early Summer", "Midsummer", "Late Summer/Early Autumn", "Early Autumn", "Late Autumn", "Late Autumn/Early Winter", "Early Winter", "Severe Winter", "Late Winter/Early Spring"],
        "time":["Early Morning", "Morning", "Noon", "Afternoon", "Evening", "Night", "Late Night"],
        "geo_wrong":"The entered latitude and longitude are invalid! Please re-enter (Example: Latitude 39.9, Longitude 116.4)",
        "generate_season":"Analyze and extract information from the following time periods. Note that only information defined in the 'TimeFormatOutPut' class should be extracted."
    },
    "en_CA":{
        "short":"en",
        "name":"English",
        "author":"The author of the poem",
        "title_of_poem":"The name of the poem",
        "line_of_poem":"The line of poetry you recommended",
        "entire_poem":"The content of the entire poem",
        "reason":"Reason for recommendation",
        "season":["Early Spring", "Spring", "Late Spring/Early Summer", "Early Summer", "Midsummer", "Late Summer/Early Autumn", "Early Autumn", "Late Autumn", "Late Autumn/Early Winter", "Early Winter", "Severe Winter", "Late Winter/Early Spring"],
        "time":["Early Morning", "Morning", "Noon", "Afternoon", "Evening", "Night", "Late Night"],
        "geo_wrong":"The entered latitude and longitude are invalid! Please re-enter (Example: Latitude 39.9, Longitude 116.4)",
        "generate_season":"Analyze and extract information from the following time periods. Note that only information defined in the 'TimeFormatOutPut' class should be extracted."
    },

}