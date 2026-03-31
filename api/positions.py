import json


def handler(request):
    positions = [
        {
            "symbol": "ETHUSDT",
            "type": "long",
            "entry": "3 253",
            "stop": "3 210",
            "target": "3 360",
            "pnl": "+1.8R",
            "status": "В работе"
        },
        {
            "symbol": "SOLUSDT",
            "type": "short",
            "entry": "188.4",
            "stop": "191.0",
            "target": "178.5",
            "pnl": "-0.6R",
            "status": "Контроль"
        },
        {
            "symbol": "WIFUSDT",
            "type": "long",
            "entry": "4.92",
            "stop": "4.70",
            "target": "5.60",
            "pnl": "+2.4R",
            "status": "Частично"
        }
    ]

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"positions": positions}, ensure_ascii=False)
    }
