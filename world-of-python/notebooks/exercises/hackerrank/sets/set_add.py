if __name__ == "__main__":
    n = int(input())
    country_list = set()
    for _ in range(n):
        country_name = input()
        country_list.add(country_name)
    print(len(country_list))
        