ai_tools = ["python", "java"]

ai_tools.append("docker")
print(ai_tools)

ai_tools.extend(["AWS", "Azure"])
print(ai_tools)

ai_tools.insert(1, "Linux")
print(ai_tools)