S = list(map(int,input()))
cnt = 1
for i in range(len(S)-1):
    if S[i]==S[i+1]:
        cnt+=1
    else:
        print('('+str(cnt)+', '+str(S[i])+')',end=' ')
        cnt=1
        
print('('+str(cnt)+', '+str(S[-1])+')',end=' ')