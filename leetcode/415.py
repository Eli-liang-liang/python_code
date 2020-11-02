class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        a = []
        z = ""
        num1 = list(num1)
        num2 = list(num2)
        c = 0
        if len(num1) >= len(num2):
            longer = num1
            shorter = num2
        else:
            longer = num2
            shorter = num1 
        j = longer[:]
        longer.reverse()
        shorter.reverse()
        e = len(longer) - len(shorter)
        for i in range(len(shorter)):
            # bug1: longer[i] = 8, shorter[i] = 1, c=1
            if (int(longer[i])+int(shorter[i])+c) >= 10:
                a.append(int(longer[i])+int(shorter[i])-10 + c)
                c = 1                   
            else:
                a.append(int(longer[i])+int(shorter[i]) + c)
                # bug3
                c = 0
        # bug2: 9999+1  
        while e > 0:
            if (int(j[e-1]) + c) >= 10:
                a.append(int(j[e-1])-10 + c)
                c = 1                   
            else:
                a.append(int(j[e-1]) + c)
                # bug3
                c = 0
            e -= 1
        if c == 1:
            a.append(c)
        a.reverse()
        for u in a:
            z += str(u)
        return z 