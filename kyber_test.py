from kyber import *
from nistkat import Kyber512_nistkats, Kyber768_nistkats

# Assertions used in the draft.

assert pow(zeta, 128, q) == q-1

assert smod(3325) == -4
assert smod(-3320) == 9

assert Round(.4) == 0
assert Round(.5) == 1
assert Round(-.5) == 0
assert Round(-.6) == -1

assert brv(91) == 109
assert brv(1) == 64

assert Poly([1,1] + [0]*254).NTT() == Poly([1]*256)

range256NTT = Poly((
    2429, 2845, 425, 795, 1865, 1356, 624, 31, 2483, 2197, 2725,
    2668, 2707, 517, 1488, 2194, 1971, 803, 922, 231, 2319, 613,
    1075, 606, 306, 3143, 1380, 2718, 1155, 531, 818, 1586, 2874,
    155, 304, 1442, 2619, 1712, 2169, 2159, 1479, 2634, 2864, 2014,
    1679, 3200, 102, 1923, 1603, 558, 681, 316, 517, 931, 1732,
    1999, 2024, 1094, 2276, 2159, 2187, 1973, 2637, 2158, 2373,
    198, 2986, 247, 1482, 449, 1157, 1290, 1057, 2220, 1124, 1019,
    400, 2206, 1225, 2233, 1376, 2880, 2664, 614, 1960, 1974, 2934,
    2679, 2860, 2217, 2897, 3234, 1905, 36, 2306, 2145, 219, 581,
    3000, 1378, 2392, 2835, 1685, 1091, 1054, 2150, 543, 3192, 2518,
    3246, 2277, 570, 239, 2522, 838, 1990, 126, 2637, 126, 818,
    3232, 1075, 940, 742, 2617, 630, 650, 2776, 2606, 482, 2208,
    868, 1949, 2149, 3066, 1896, 2996, 2306, 63, 883, 2463, 1313,
    1951, 2999, 97, 1806, 2830, 2104, 1771, 2453, 370, 2605, 871,
    1467, 2426, 1985, 2363, 658, 1015, 655, 501, 664, 1249, 3120,
    106, 3100, 1274, 1919, 1890, 2147, 1961, 1949, 1738, 461, 2772,
    1270, 3095, 2089, 1051, 2576, 1628, 1735, 3195, 2034, 655, 524,
    3195, 901, 2007, 1419, 157, 2334, 2344, 2825, 634, 850, 2523,
    2642, 672, 1604, 216, 3280, 1317, 905, 1165, 1532, 3059, 777,
    242, 1752, 2052, 533, 1006, 1858, 2336, 1183, 1656, 1668, 2037,
    2946, 2184, 1048, 104, 2825, 877, 111, 1363, 1989, 1995, 659,
    12, 506, 1551, 2022, 3212, 1591, 1637, 2330, 1625, 2795, 774,
    70, 1002, 3194, 928, 987, 2717, 3005, 2883, 149, 2594, 3105,
    2502, 2134, 2717, 2303,
))

assert Poly(range(256)).NTT().InvNTT() == Poly(range(256))
assert Poly(range(256)).NTT() == Poly(range(256)).RefNTT()
assert range256NTT.InvNTT() == Poly(range(256))
assert Poly(range(256)).NTT() == range256NTT

assert WordsToBits([12,45], 8) == [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0]

p = sampleUniform(io.BytesIO(hashlib.shake_128(b'').digest(length=1344)))
assert p.cs[:4] == (3199, 697, 2212, 2302)
assert p.cs[-3:] == (255, 846, 1)

p = CBD(range(64*2), 2)
assert p.cs[:6] == (0, 0, 1, 0, 1, 0)
assert p.cs[-4:] == (3328, 1, 0, 1)

p = CBD(range(64*3), 3)
assert p.cs[:5] == (0, 1, 3328, 0, 2)
assert p.cs[-4:] == (3328, 3327, 3328, 1)


noise3Test = Poly(x%q for x in [
    0, 0, 1, -1, 0, 2, 0, -1, -1, 3, 0, 1, -2, -2, 0, 1, -2,
    1, 0, -2, 3, 0, 0, 0, 1, 3, 1, 1, 2, 1, -1, -1, -1, 0, 1,
    0, 1, 0, 2, 0, 1, -2, 0, -1, -1, -2, 1, -1, -1, 2, -1, 1,
    1, 2, -3, -1, -1, 0, 0, 0, 0, 1, -1, -2, -2, 0, -2, 0, 0,
    0, 1, 0, -1, -1, 1, -2, 2, 0, 0, 2, -2, 0, 1, 0, 1, 1, 1,
    0, 1, -2, -1, -2, -1, 1, 0, 0, 0, 0, 0, 1, 0, -1, -1, 0,
    -1, 1, 0, 1, 0, -1, -1, 0, -2, 2, 0, -2, 1, -1, 0, 1, -1,
    -1, 2, 1, 0, 0, -2, -1, 2, 0, 0, 0, -1, -1, 3, 1, 0, 1, 0,
    1, 0, 2, 1, 0, 0, 1, 0, 1, 0, 0, -1, -1, -1, 0, 1, 3, 1,
    0, 1, 0, 1, -1, -1, -1, -1, 0, 0, -2, -1, -1, 2, 0, 1, 0,
    1, 0, 2, -2, 0, 1, 1, -3, -1, -2, -1, 0, 1, 0, 1, -2, 2,
    2, 1, 1, 0, -1, 0, -1, -1, 1, 0, -1, 2, 1, -1, 1, 2, -2,
    1, 2, 0, 1, 2, 1, 0, 0, 2, 1, 2, 1, 0, 2, 1, 0, 0, -1, -1,
    1, -1, 0, 1, -1, 2, 2, 0, 0, -1, 1, 1, 1, 1, 0, 0, -2, 0,
    -1, 1, 2, 0, 0, 1, 1, -1, 1, 0, 1
])
assert noise3Test == CBD(PRF(bytes(range(32)), 37).read(3*64), 3)
noise2Test = Poly(x%q for x in [
    1, 0, 1, -1, -1, -2, -1, -1, 2, 0, -1, 0, 0, -1,
    1, 1, -1, 1, 0, 2, -2, 0, 1, 2, 0, 0, -1, 1, 0, -1,
    1, -1, 1, 2, 1, 1, 0, -1, 1, -1, -2, -1, 1, -1, -1,
    -1, 2, -1, -1, 0, 0, 1, 1, -1, 1, 1, 1, 1, -1, -2,
    0, 1, 0, 0, 2, 1, -1, 2, 0, 0, 1, 1, 0, -1, 0, 0,
    -1, -1, 2, 0, 1, -1, 2, -1, -1, -1, -1, 0, -2, 0,
    2, 1, 0, 0, 0, -1, 0, 0, 0, -1, -1, 0, -1, -1, 0,
    -1, 0, 0, -2, 1, 1, 0, 1, 0, 1, 0, 1, 1, -1, 2, 0,
    1, -1, 1, 2, 0, 0, 0, 0, -1, -1, -1, 0, 1, 0, -1,
    2, 0, 0, 1, 1, 1, 0, 1, -1, 1, 2, 1, 0, 2, -1, 1,
    -1, -2, -1, -2, -1, 1, 0, -2, -2, -1, 1, 0, 0, 0,
    0, 1, 0, 0, 0, 2, 2, 0, 1, 0, -1, -1, 0, 2, 0, 0,
    -2, 1, 0, 2, 1, -1, -2, 0, 0, -1, 1, 1, 0, 0, 2,
    0, 1, 1, -2, 1, -2, 1, 1, 0, 2, 0, -1, 0, -1, 0,
    1, 2, 0, 1, 0, -2, 1, -2, -2, 1, -1, 0, -1, 1, 1,
    0, 0, 0, 1, 0, -1, 1, 1, 0, 0, 0, 0, 1, 0, 1, -1,
    0, 1, -1, -1, 2, 0, 0, 1, -1, 0, 1, -1, 0,
])
assert noise2Test == CBD(PRF(bytes(range(32)), 37).read(2*64), 2)

for (params, kats) in [(params512, Kyber512_nistkats), (params768, Kyber768_nistkats)]:
    for kat in kats:
        (pk, sk) = KeyGen(kat.rand1, params)
        assert(pk == kat.pk)
        assert(sk == kat.sk)
        (ct, ss) = Enc(pk, kat.rand2, params)
        assert(ct == kat.ct)
        assert(ss == kat.ss)
        ss = Dec(sk, ct, params)
        assert(ss == kat.ss)
