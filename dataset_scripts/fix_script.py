import re

filepath = "generate_matematik_full.py"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Fix {"key": "X", "%10"} => {"key": "X", "text": "%10"}
fixed = re.sub(r'\{"key": "([A-E])", "([^"]*)"\}', r'{"key": "\1", "text": "\2"}', content)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(fixed)

print("Fix completed!")
