from shared_memory_dict import SharedMemoryDict
import time

def Shared():
    sha_b = SharedMemoryDict(name="haffman", size=1024)
    for _ in range(180):
        if sha_b:
            break
        time.sleep(1)
    print(sha_b)
    sha_b["shifr"] = ''
    sha_b.shm.close()  
    
Shared()