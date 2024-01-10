class Computation:
    def __init__(self):
        pass
    def Factorial(self,n):
        for i in range(n-1,0,-1):
            n*=i
        print(n)

    def naturalSum(self,n):
        for i in range(n-1,0,-1):
            n+=i
        print(n)

    def testPrime(self,n):
        c = 0
        for i in range(1,n+1):
            if n%i==0:
                c+=1

        if c==2:
            print('Yes it is prime')

        else:
            print('No it is not prime')

    def testPrims(self,a,b):
        minimum = min(a,b)

        for i in range(1,minimum+1):
            if a%i==0 and b%i==0:
                hcf = i

        if hcf == 1:
            print(True)

        else:
            print(False)

    def tableMult(self,n):
        for i in range(1,11):
            print(f"{n}x{i}={n*i}\n")

    def allTablesMult(self):
        for i in range(1,10):
            for j in range(1,11):
                print(f"{i}x{j}={i*j}")
            print("--------------")

    def listDiv(self,n):
        lDiv=[]

        for i in range(1,n+1):
            if n%i==0:
                lDiv.append(i)

        print(lDiv)

    def listDivPrim(self,n):
        listDivPrim = []

        for i in range(1, n + 1):
            if n % i == 0:
                c=0
                for j in range(1,i+1):
                    if i%j==0:
                        c+=1

                if c==2:
                    listDivPrim.append(i)
        print(listDivPrim)

obj = Computation()
obj.listDivPrim(74)