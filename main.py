def get_base_16_from_2(n):
    '''
    Transformă un număr dat din baza 2 în baza 16.
    :param n: str
    :return: str
    '''
    dig = "0123456789ABCDEF"
    n_16 = ""
    n_10 = 0
    p = 1
    num = int(n)
    while num != 0:
        cif = num % 10
        n_10 = n_10 + cif * p   ## nr in baza 10
        p *= 2
        num //= 10
    while n_10 != 0:
        i = n_10 % 16
        n_16 = dig[i] + n_16
        n_10 //= 16
    return n_16

def test_get_base_16_from_2():
    assert get_base_16_from_2(11010010) == "D2"
    assert get_base_16_from_2(100) == '4'
    assert  get_base_16_from_2(1001) == '9'

def get_n_choose_k(n,k):
    '''
    Calculeaza combinari de n luate cate k
    :param n: int
    :param k: int
    :return: int
    '''
    fact_n = 1
    fact_k = 1
    fact_nk = 1
    if n < k:
        return 0

    elif k == 1:
        return n

    else:
        i = n
        while i != 1:
            fact_n = fact_n * i
            i -= 1
        i = k
        while i != 1:
            fact_k = fact_k * i
            i -= 1
        i = n-k
        while i != 0:
            fact_nk = fact_nk * i
            i -= 1
        comb = fact_n // (fact_nk * fact_k)
        return comb

def test_get_n_choose_k():
    assert get_n_choose_k(1,2) == 0
    assert get_n_choose_k(2,1) == 2
    assert get_n_choose_k(10,5) == 252


def main():
    test_get_n_choose_k()
    test_get_base_16_from_2()
    ok = '0'
    while ok != 'x':
        print('''
1.Transformă un număr dat din baza 2 în baza 16. Numărul se dă în baza 2.
2.Calculează combinări de n luate câte k (n și k date).
x.Iesire
        ''')
        ok = input('NR: ')

        if ok == '1':
            n = input('Nr in baza 2: ')
            print('Nr in baza 16: ', get_base_16_from_2(n))
        elif ok == '2':
            n = int(input("N = "))
            k = int(input('K = '))
            if get_n_choose_k(n,k) == 0:
                print('N >= K!!!')
            else:
                print('Rezultat = ', get_n_choose_k(n,k))

if __name__ == '__main__':
    main()