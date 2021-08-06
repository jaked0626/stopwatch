import time
import math
import random
import fibonacci as f

class StopWatch():
    def __init__(self):
        self.reset()
    
    def start(self):
        self.start_time = time.time()
        self.t0 = self.start_time
    
    def stop(self):
        self.stop_time = time.time()
        self.time += self.stop_time - self.start_time
        #print(self.time)

    def lap(self):
        t1 = time.time()
        self.num_laps += 1
        self.laps["lap{}".format(self.num_laps)] = t1 - self.t0
        self.t0 = t1

    def split(self):
        t1 = time.time()
        self.num_splits += 1
        self.splits["split{}".format(self.num_splits)] = t1 - self.start_time

    def convert(self, t):
        '''
        Converts time in seconds to hours:minutess:seconds:miliseconds.

        Inputs:
          t (float): number of seconds
        Returns: time in hrs:mins:secs:milisecs format. 
        '''
        hrs = t // 3600
        mins = t // 60 % 60
        secs = math.floor(t % 60)
        milisecs = t - math.floor(t)
        return "{}:{}:{}:{}".format(round(hrs), round(mins), secs, 
                                    round(milisecs * 10 ** 4))
    
    def converted_time(self):
        return self.convert(self.time)
    
    def reset(self):
        self.t0 = 0
        self.start_time = 0
        self.stop_time = 0
        self.time = 0
        self.laps = {}
        self.num_laps = 0
        self.splits = {}
        self.num_splits = 0

    def __str__(self):
        s = "Time Elapsed:  {}".format(self.converted_time())
        if self.laps:
            s += "\nLaps:"
            for lap, t in self.laps.items():
                s += "\n  {}: {}".format(lap, t)
        if self.splits:
            s += "\nSplits:"
            for split, t in self.splits.items():
                s += "\n  {}: {}".format(split, t)
        
        return s

    def __repr__(self):
        return self.__str__()
        
        
def main():
    '''
    フィボナッチ数をランダムに5つその項数から計算する速度を測る．
    また，計算したごとにラップタイムとスプリットタイムを記録する．
    フィボナッチ数は回帰的な計算を要し，計算に一定の時間がかかるため，
    ストップウォッチの機能を測るために使用した．
    '''
    w = StopWatch()
    w.start()
    fibonaccis_s = "計算されたフィボナッチ数："
    # compute 5 fibonacci numbers, take lap time and split time for each 
    # computation. The greater the term number, the longer it takes to compute.

    for i in range(1, 6):
        n = random.randint(20, 38)
        fib_n = f.Fibonacci(n)
        w.lap()
        w.split()
        fibonaccis_s += "\n  {}番: n = {}, Fibonacci(n) = {}".format(i, n, fib_n)
    w.stop()
    print(fibonaccis_s)
    print(w)

    return w

if __name__ == "__main__":
    main()
        
