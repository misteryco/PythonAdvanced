n, m = input().split()
n_numbers = set()
m_numbers = set()

for _ in range(int(n)):
    n_numbers.add(int(input()))
for _ in range(int(m)):
    m_numbers.add(int(input()))

[print(x) for x in n_numbers.intersection(m_numbers)]
