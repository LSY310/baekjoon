a,b=input().split()
if "5" in a or "6" in a or "5" in b or "6" in b:
    min=int(a.replace("6","5"))+int(b.replace("6","5"))
    max=int(a.replace("5","6"))+int(b.replace("5","6"))
print(f"{min} {max}")
