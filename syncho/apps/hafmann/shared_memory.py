from shared_memory_dict import SharedMemoryDict
import time

def Shared(data: dict):
    if not data:
        return
    sha_a = SharedMemoryDict(name="haffman", size=1024)
    sha_a["shifr"] = data
    for _ in range(10):
        if not sha_a["shifr"]:
            break
        time.sleep(1)
    sha_a.shm.close()
    sha_a.shm.unlink()