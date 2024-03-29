"""
Intermediate Exercises
Estimate: 30 minutes
Actual:   32 minutes
"""
from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)
print(ruby)
print(visual_basic)

language_list = [python, ruby, visual_basic]

print("\nThe dynamically typed languages are:")
for language in language_list:
    if language.is_dynamic():
        print(language.name)