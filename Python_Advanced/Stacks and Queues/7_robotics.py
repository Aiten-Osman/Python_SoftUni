from collections import deque

robots = []
for r in input().split(';'):
    name, t = r.split('-')
    robots.append({'name': name, 'time': int(t), 'free': 0})

h, m, s = map(int, input().split(':'))
sec = h * 3600 + m * 60 + s

products = deque()
while True:
    p = input()
    if p == "End":
        break
    products.append(p)

while products:
    sec += 1
    p = products.popleft()
    
    bot = None
    for r in robots:
        if r['free'] <= sec:
            bot = r
            break 
            
    if bot:
        bot['free'] = sec + bot['time']
        h_out = (sec // 3600) % 24
        m_out = (sec % 3600) // 60
        s_out = sec % 60
        print(f"{bot['name']} - {p} [{h_out:02d}:{m_out:02d}:{s_out:02d}]")
    else:
        products.append(p)