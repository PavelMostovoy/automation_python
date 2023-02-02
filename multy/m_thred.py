import concurrent.futures
# from concurrent.futures.thread import ThreadPoolExecutor  as Executor
from concurrent.futures.process import ProcessPoolExecutor as Executor



import requests
import time

url = 'https://en.wikipedia.org/wiki/Political_impact_of_the_COVID-19_pandemic'




def req(url=url):
    print("starting")
    r = requests.get(url)
    print("ending")
    # print(f"response time {r.elapsed.total_seconds()}")
    return r




tasks = [url for x in range(100)]

# start = time.time()
# for url in tasks :
#     req(url)
#
# print(time.time()-start)

for_loop = 10.93333888053894



if __name__ == "__main__":
    start_time = time.time()
    with Executor(max_workers=100) as executor:
        pool = [executor.submit(req, url) for x in range(100)]
        for result in concurrent.futures.as_completed(pool):
            pass
            # print(result.result())

    print(time.time() - start_time)