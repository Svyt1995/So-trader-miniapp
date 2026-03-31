import json


def handler(request):
    data = {
        "time": "27 марта 2026 · 06:40 МСК",
        "account": {
            "balance": 98420,
            "equity": 101080,
            "freeMargin": 28200,
            "ddDay": "-1.8% / -5%",
            "ddMonth": "-3.2% / -10%"
        },
        "message": "Текущие сигналы выровнены с дневным риск-профилем."
    }
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(data, ensure_ascii=False)
    }
