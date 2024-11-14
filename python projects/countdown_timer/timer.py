import time
time_to_count=int(input('enter your time in seconds:'))
for i in range(time_to_count,0,-1):
    hours=int(i/3600)
    minute=int(i/60)%60
    seconds=int(i%60)
    print(f'{hours:02}:{minute}{seconds:02}')
    time.sleep(1)
print(f'time is up')