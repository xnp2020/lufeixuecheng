import json

json_string = '''{
    "15579186772": {
        "name": "\u6c6a\u6c6a",
        "age": "1",
        "phone": "15579186772",
        "ID": "111",
        "course": "Python"
    },
    "12345678900": {
        "name": "aa",
        "age": "3",
        "phone": "12345678900",
        "ID": "112",
        "course": "Python"
    },
    "15111111111": {
        "name": "xxx",
        "age": "19",
        "phone": "15111111111",
        "ID": "113",
        "course": "\u524d\u7aef"
    },
    "13333333333": {
        "name": "\u738b\u7fb2\u4e4b",
        "age": "40",
        "phone": "13333333333",
        "ID": "114",
        "course": "\u6570\u636e\u5206\u6790"
    }
}'''

# 将 JSON 字符串转换为字典，确保输出非 ASCII 字符时以原始格式输出
data = json.loads(json_string)

print(data)
