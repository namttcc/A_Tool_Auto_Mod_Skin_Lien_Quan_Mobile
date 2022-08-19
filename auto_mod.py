#os.system('pip install termcolor')
from os import listdir
import os
from termcolor import colored
import re

os.system('TITLE AoV Auto Modify File 1.0')
os.system('color')

print(colored('Auto Mod', 'green'))

if os.path.isdir('INP')== 0 :
    os.mkdir('INP')
    print(colored('\n\tPut file in INP/\n', 'red'))
else:
    havefile=0
    for file in listdir(DIR_PATH):
        file_ext = file.split('.')[-1]
        if file_ext == 'xml':
                havefile=havefile+1
    if havefile>0:
        allfile=0
        modfile=0
        notmodfile=0
        AI = b'prefab_skill_effects/hero_skill_effects/'
        V = b'Prefab_Skill_Effects/Hero_Skill_Effects/'
        
        K = b'" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="use1P3PSwitch" value="true" refParamName="" useRefParam="false"/>'
        H = b'" refParamName="" useRefParam="false" />\r\n        <bool name="use1P3'
        W = b'_SKIN'
        Q = b'" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName2" value="" refParamName="" useRefParam="false"/>'
        N = b'_mid" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName2" value="" refParamName="" useRefParam="false"/>'
        L = b'_mid" refParamName="" useRefParam="false" />\n    <String name="resourceName2'
        M = b'" refParamName="" useRefParam="false" />\n    <String name="resourceName2'

        print(colored('\n\tCheck file from "INP/"...','yellow'))
        print(colored('\t\tFound: {} file'.format(havefile),'yellow'))
        
        P = bytes(input(colored('\t\tId hero + namehero(ex: 520_veres): ','yellow')),encoding="utf-8")
        print(colored('\t\t{}'.format(P.decode()),'red'))
        
        Z = bytes(input(colored('\t\tId hero + namehero(ex: 520_Veres): ','green')),encoding="utf-8")
        print(colored('\t\t{}'.format(Z.encode()),'red'))
        
        Y=(input(colored('\tSkin ID(15009): ', 'green')))
        X=(input(colored('\tK ID(9): ', 'green')))
        
        T=int(int(Y,base=10)/100)
        A = AI + P
        F = AI+ P + str.encode(Y)  + b'\x2f'
        
        B = V + Z
        E = V+ Z + str.encode(Y)  + b'\x2f'
        
        D = effect + Z
        C = V + P
        
        I = W + K + str.encode(X)
        G = W + H + str.encode(X)
        
        for file in listdir(DIR_PATH):
            file_ext = file.split('.')[-1]
            if file_ext in EXT:
                with open(f'./INP/{file}', 'rb') as f:
                    strin = f.read()
                    allfile=allfile+1
                    pos = re.search(effect,strin)
                    if pos != -1:
                        haveeffect=1
                        strin =  re.sub(A,F,strin)
                        strin =  re.sub(D,F,strin)
                        strin =  re.sub(C,F,strin)
                        strin =  re.sub(B,E,strin)
                        strin =  re.sub(K,I,strin)
                        strin =  re.sub(H,G,strin)
                        strin =  re.sub(Q,N,strin)
                        strin =  re.sub(M,L,strin)

                        with open(f'./inp/{file}', 'wb') as f1:
                            f1.write(strin)
                        modfile=modfile+1

                    else:
                        notmodfile=notmodfile+1
                
        print(colored('\n\tSee INP/','green'))
        print(colored('\tComplete {} file'.format(allfile),'green'))
        print(colored('\tModified {} file'.format(modfile),'yellow'))
        print(colored('\tSkip {} file'.format(notmodfile),'red'))
    else:
        print(colored('\n\t\tINP\\ HAVE 0 File!!!','red'))
print(colored('\nEND.','green'))

os.system('pause')
