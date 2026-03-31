import json

def handler(request):
    history = [
        {
            "time": "27.03 · 09:12",
            "symbol": "ETHUSDT",
            "type": "Лонг",
            "entry": "3 253",
            "exit": "3 360",
            "pnl": "+1.8R"
        },
        {
            "time": "27.03 · 08:05",
            "symbol": "SOLUSDT",
            "type": "Шорт",
            "entry": "188.4",
            "exit": "178.5",
            "pnl": "-0.6R"
        },
        {
            "time": "26.03 · 15:40",
            "symbol": "WIFUSDT",
            "type": "Лонг",
            "entry": "4.92",
            "exit": "5.60",
            "pnl": "+2.4R"
        }
    ]

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"history": history}, ensure_ascii=False)
    }
