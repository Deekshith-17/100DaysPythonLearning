from enum import Enum
class subjects(Enum):
    English="E"
    Maths="M"
    Physics="P"
    kannada="K"
for sub in subjects:
    print(sub.name,sub.value)