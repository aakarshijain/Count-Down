import time
seconds=input("Enter the number of seconds")

def count_down(seconds):
    while seconds>0:
        mins=int(seconds/60)
        secs=int(seconds%60)
        timer=f'{mins}:{secs}'
        print(timer)
        seconds=seconds-1
        time.sleep(1)
    print("Time Up!!")

count_down(int(seconds))