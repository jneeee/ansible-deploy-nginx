import sys
import threading
import time
import urllib2
import collections

req = urllib2.Request("http://%s" % sys.argv[1])
res = collections.defaultdict(list)

def get_url():
    try:
        resp_body = urllib2.urlopen(req).read()
        if len(resp_body) < 20:
            res[resp_body].append('0')
    except Exception as err:
        raise err

if __name__ == "__main__":
    for i in range(100):
        threading.Thread(target=get_url).start()
    time.sleep(5)
    print("container_id: res_count  ")
    print(["{}: {}".format(k[:-2], len(v)) for k, v in res.items()])
