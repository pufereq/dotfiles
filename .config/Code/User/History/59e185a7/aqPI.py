from rich.prompt import IntPrompt

test = IntPrompt.ask('sys')

print(type(test))
print(type(int))