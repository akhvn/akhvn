import os, re, time, random
import threading

def th_func(suffix):
    time.sleep(random.randint(2,5))
    ip = "192.168.178." + str(suffix)
    ping_out = os.popen("ping -q -c2 " + ip, "r") 
    with lock:
        print("... pinging ", ip)
        while True:
            line = ping_out.readline()
            if not line:
                break
            n_received = received_packages.findall(line)
            if n_received:
                print(ip + ": " + status[int(n_received[0])])


lock = threading.Lock()
received_packages = re.compile(r"(\d) received")
status = ("no response", "alive but losses", "alive")
th = [threading.Thread(target=th_func,args=(_,)) for _ in range(20,30)]
for thread in th:
    thread.start()
for thread in th:
    thread.join()
