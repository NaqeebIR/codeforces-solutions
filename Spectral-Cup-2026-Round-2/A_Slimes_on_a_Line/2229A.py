import sys

NaqeebIr = sys.stdin.readline

for Naqeeb_Irtaza_AkASH in range(int(NaqeebIr())):
    n = int(NaqeebIr())
    
    Akash = list(map(int, NaqeebIr().split()))
    
    Naqeeb = min(Akash)
    Irtaza = max(Akash)
    
    print((Irtaza - Naqeeb + 1) // 2)