import json

def handler(request):
    equity = [
        {"time": "01:00", "value": 0.98},
        {"time": "05:00", "value": 1.01},
        {"time": "09:00", "value": 1.04},
        {"time": "13:00", "value": 1.12},
        {"time": "17:00", "value": 1.08},
        {"time": "21:00", "value": 1.06}
    ]

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"equity": equity}, ensure_ascii=False)
    }
