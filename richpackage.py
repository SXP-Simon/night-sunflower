from rich.console import Console
console = Console()

test_data = [
    {"专业": "模式识别与智能系统", "学科": "人工智能", "params": [None, 1, 2, 4, False, True], "id": "1",},
    {"专业": "模式识别与智能系统", "学科": "深度学习", "params": [7]},
    {"专业": "模式识别与智能系统", "学科": "机器视觉", "params": [42, 23], "id": "2"},
]

def test_log():
    enabled = False
    context = {
        "天气": "阴",
    }
    movies = ["误杀2", "江照黎明"]
    console.log("Hello from", console, "!")
    console.log(test_data, log_locals=True)

test_log()