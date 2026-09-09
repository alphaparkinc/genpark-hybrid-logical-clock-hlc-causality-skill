import sys
import json
from client import HybridLogicalClock

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    hlc = HybridLogicalClock(params.get("node_id", "default"))
    if method == "now":
        return hlc.now(params.get("pt", 0))
    elif method == "update":
        return hlc.update(params.get("msg_l", 0), params.get("msg_c", 0), params.get("pt", 0))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
