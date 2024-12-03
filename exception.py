try:
    # result = 45/0
    result = 45/5
    print(int(result))
except:
    print("Error happened")
finally:
    print("finally here")
print("Done")