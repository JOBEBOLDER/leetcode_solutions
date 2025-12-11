'''
好，那我就当你说“开搞吧”了 😄
给你一整套「面试版题目 + 思路 + 代码」一次性打包。

⸻

1️⃣ 面试版题目描述（英文版）

Problem: Implement JSON Serialization

You are given an object that is guaranteed to be one of the following types:
	•	str
	•	list (whose elements are themselves str, list, or dict)
	•	dict (whose keys are str, and whose values are str, list, or dict)

Implement a function serialize(obj) that returns a JSON-formatted string representing this object.

You are not allowed to use any built-in JSON libraries (e.g., json.dumps in Python).
You only need to support the three types mentioned above.

You should follow these rules:
	1.	Strings
	•	Must be wrapped in double quotes: "abc".
	•	You must escape:
	•	" as \"
	•	\ as \\
	2.	Lists
	•	Represented with square brackets: [elem1,elem2,...]
	•	Elements are serialized using the same rules (recursively).
	•	No extra spaces are required.
	3.	Dictionaries
	•	Represented with curly braces: {key1:value1,key2:value2,...}
	•	Keys are always strings and must be serialized as JSON strings.
	•	The order of keys does not matter unless the interviewer says otherwise.

You can assume there are no cycles in the input (no self-references).

Function signature (Python)

def serialize(obj) -> str:
    ...


⸻

2️⃣ 示例（Examples）

Example 1

input_obj = {"a": "b", "c": "d"}
serialize(input_obj)
# Possible output: '{"a":"b","c":"d"}'

(Key order may differ, e.g. {"c":"d","a":"b"} also acceptable.)

⸻

Example 2

input_obj = ["x", "y", "z"]
serialize(input_obj)
# Output: '["x","y","z"]'


⸻

Example 3

input_obj = {
    "a": "hello \"world\"",
    "b": ["x", "y", {"c": "d"}]
}
serialize(input_obj)
# One valid output (no spaces required):
# '{"a":"hello \"world\"","b":["x","y",{"c":"d"}]}'


⸻

3️⃣ 思路（你在面试时可以怎么讲）
这种题的典型套路：递归 + 按类型分类处理。

你可以按这个结构说：
	1.	统一用递归处理嵌套结构
	•	输入可能是三种类型：str / list / dict
	•	我写一个 serialize(obj)：
	•	如果是 str → 返回 "..." 并处理转义
	•	如果是 list → 对每个元素递归调用 serialize，用逗号拼起来，加上 []
	•	如果是 dict → 对每个 key, value：
	•	key 是 string，用 string 规则处理
	•	value 递归处理
	•	拼成 "key":value，用逗号连接，外面加 {}
	2.	字符串转义
	•	为了简单，可以只处理两种最重要的：
	•	\ → \\
	•	" → \"
	•	如果面试官追问，再说可以扩展处理 \n、\t 等。
	3.	复杂度
	•	每个字符、每个元素只处理一遍。
	•	时间复杂度：O(N)，N 是整个结构展开后的总字符数/节点数。
	•	空间复杂度：O(N)（递归栈 + 输出字符串）。

⸻


'''

def serialize(obj) -> str:
    """
    Serialize an object (str, list, dict) into a JSON string.
    Supported:
        - str
        - list of (str / list / dict)
        - dict with str keys and (str / list / dict) values
    """

    # helper：转义字符串里的特殊字符
    def escape_string(s: str) -> str:
        # 顺序很重要：先替换反斜杠，再替换双引号
        s = s.replace("\\", "\\\\")
        s = s.replace("\"", "\\\"")
        return s

    # 主递归函数
    def _serialize(x) -> str:
        # 1. string
        if isinstance(x, str):
            return "\"" + escape_string(x) + "\""

        # 2. list
        if isinstance(x, list):
            parts = [_serialize(elem) for elem in x]
            return "[" + ",".join(parts) + "]"

        # 3. dict
        if isinstance(x, dict):
            items = []
            for k, v in x.items():
                if not isinstance(k, str):
                    raise TypeError("Only string keys are supported")
                key_str = "\"" + escape_string(k) + "\""
                val_str = _serialize(v)
                items.append(key_str + ":" + val_str)
            return "{" + ",".join(items) + "}"

        # 4. 不支持其他类型
        raise TypeError(f"Unsupported type: {type(x)}")

    return _serialize(obj)


#obj:(str/list/dict)
#wrap as a API,inside this API where handle two functions
# “This looks like a recursive serialization problem. 
# I’ll write a helper function that handles each type and calls itself for nested values.”
def serialize(obj) -> str:
    #structure:
    def escape_String(s):
        s = s.replace("\\", "\\\\")
        s = s.replace("\"", "\\\"")
        return s


    def _serialize(x):
        #handle string如果是 str → 按字符串规则处理
        if isinstance(x,str):
            return "\"" + escape_String(x) + "\""
        #handle list如果是 list → 对每个元素递归调用 _serialize
        if isinstance(x,list):
            parts = [_serialize(elem) for elem in x]
            return "[" + ",".join(parts) + "]"
        #handle dict如果是 dict → 对每个 key, value 递归调用 _serialize 处理 value
        if isinstance(x,dict):
            items = []
            for k,v in x.items():
                if not isinstance(k,str):
                    raise TypeError("only string keys are supported")
                key_str = "\"" + escape_String(k) + "\""
                val_str = _serialize(v) #recursively handle this string
                items.append(key_str + ":" + val_str)
            return "{" + ",".join(items) + "}"

        else:
            raise TypeError

    return _serialize(obj)
