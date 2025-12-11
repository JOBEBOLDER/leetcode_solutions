'''
create 2 helper funciton where i can handle the x transition and 
do the serialize separately

'''
#right now i created a basic skelton how this API look

def serialize_pretty(obj) -> str:
    def escape_string(s: str) -> str:
        s = s.replace("\\", "\\\\")
        s = s.replace("\"", "\\\"")
        return s

    def _serialize(x) -> str:
        # 1. string
        if isinstance(x, str):
            return "\"" + escape_string(x) + "\""

        # 2. bool（要在 int 前面）
        if isinstance(x, bool):
            return "true" if x else "false"

        # 3. int
        if isinstance(x, int):
            return str(x)

        # 4. None -> null
        if x is None:
            return "null"

        # 5. list
        if isinstance(x, list):
            parts = [_serialize(elem) for elem in x]
            return "[" + ",".join(parts) + "]"

        # 6. dict
        if isinstance(x, dict):
            items = []
            for k, v in x.items():
                if not isinstance(k, str):
                    raise TypeError("Key should be string value")
                key_str = "\"" + escape_string(k) + "\""
                value_str = _serialize(v)
                items.append(key_str + ":" + value_str)
            return "{" + ",".join(items) + "}"

        # 7. 其他类型不支持
        raise TypeError(f"Unsupported type: {type(x)}")

    return _serialize(obj)



print(serialize_pretty({"a": "b", "c": 1, "d": True, "e": None}))
print(serialize_pretty(["x", 1, False, {"y": "z"}]))

    