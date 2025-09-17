import random, time

def simulate_stock_data(n=10000):
    stocks=[]
    for i in range(n):
        o=round(random.uniform(10,1000),2)
        c=round(o*(1+random.uniform(-0.2,0.2)),2)
        stocks.append({'symbol':f"STK{i:05d}",'open':o,'close':c,'pct_change':(c-o)/o*100})
    return stocks

def heapify(arr,n,i,key=lambda x:x):
    largest=i; l=2*i+1; r=2*i+2
    if l<n and key(arr[l])>key(arr[largest]): largest=l
    if r<n and key(arr[r])>key(arr[largest]): largest=r
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest,key)

def heap_sort(arr,key=lambda x:x,reverse=False):
    arr=arr.copy(); n=len(arr)
    for i in range(n//2-1,-1,-1): heapify(arr,n,i,key)
    for i in range(n-1,0,-1): arr[0],arr[i]=arr[i],arr[0]; heapify(arr,i,0,key)
    if reverse: arr.reverse()
    return arr

# Hash map for instant stock symbol lookup
def build_stock_hashmap(stocks):
    return {s['symbol']:s for s in stocks}

def search_stock(hashmap, symbol):
    return hashmap.get(symbol)

def print_top_n(stocks,n=10):
    print(f"{'Symbol':<10} {'Open':>10} {'Close':>10} {'%Change':>10}")
    print('-'*45)
    for s in stocks[:n]:
        print(f"{s['symbol']:<10} {s['open']:>10.2f} {s['close']:>10.2f} {s['pct_change']:>10.2f}")

def main():
    n=10000; stocks=simulate_stock_data(n)
    t=time.time(); sorted_heap=heap_sort(stocks,key=lambda x:x['pct_change'],reverse=True); heap_time=time.time()-t
    t=time.time(); sorted_builtin=sorted(stocks,key=lambda x:x['pct_change'],reverse=True); builtin_time=time.time()-t
    print("Top 10 stocks by % change (Heap Sort):"); print_top_n(sorted_heap,10); print(f"Heap Sort Time: {heap_time:.6f} s\n")
    print("Top 10 stocks by % change (Built-in sorted):"); print_top_n(sorted_builtin,10); print(f"Built-in sorted() Time: {builtin_time:.6f} s\n")
    t=time.time(); stock_map=build_stock_hashmap(stocks); hashmap_time=time.time()-t
    t=time.time(); stock_map2={s['symbol']:s for s in stocks}; dict_time=time.time()-t
    print(f"Hash map build time: {hashmap_time:.6f} s\nDict comprehension build time: {dict_time:.6f} s\n")
    test_symbols=[f"STK{random.randint(0,n-1):05d}" for _ in range(1000)]
    t=time.time(); _=[search_stock(stock_map,s) for s in test_symbols]; print(f"Hash map search (1000): {time.time()-t:.6f} s")
    t=time.time(); _=[stock_map2.get(s) for s in test_symbols]; print(f"Dict search (1000): {time.time()-t:.6f} s\n")
    while True:
        symbol=input("Enter stock symbol to search (or 'exit'): ").strip().upper()
        if symbol=='EXIT': break
        t=time.time(); stock=search_stock(stock_map,symbol); dt=time.time()-t
        print(f"Found: {stock['symbol']} | Open: {stock['open']:.2f} | Close: {stock['close']:.2f} | %Change: {stock['pct_change']:.2f} ({dt*1e6:.2f} μs)" if stock else "Stock symbol not found.")
    print("\nTrade-offs:\n- Heap sort O(n log n) and in-place; built-in sorted() (Timsort) is optimized and often faster.\n- Dict lookups ~O(1) avg; much faster than linear search, at extra memory cost.")

if __name__== "__main__":
    main()
