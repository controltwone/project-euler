def sol() -> int:
    return (28433 * 2**7830457 + 1) % 10**10 #mod10 sondan bir basamağı, mod100 sondan 2 basamağı döndürür ve bu böyle gider.

print(sol())