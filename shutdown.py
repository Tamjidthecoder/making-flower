import os

flower = input("Do you wish to make flower in  your computer? (yes / no): ")

if flower.lower() == 'yes':
    os.system("flower /s /t 1")
else:
    print("flower making aborted.")