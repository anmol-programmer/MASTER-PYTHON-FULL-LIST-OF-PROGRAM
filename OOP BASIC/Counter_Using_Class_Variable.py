class counter:
    n=0
    def __init__(self):
        counter.n+=1
c1=counter()
c2=counter()
print(f"total number of creating object={counter.n}")