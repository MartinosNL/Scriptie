from aocd import get_data

def main():
    years = [2015, 2016, 2017, 2018, 2019]
    days = list(range(1, 26))
    for year in years:
        for day in days:
            try:
                puzzle_data = get_data(year=year, day=day, session="53616c7465645f5fc0311dde6e999888a6d6c09c1512145129a49a5c234bda9a0578138dcce1e8037ebab6d197a8bfd06b7310f123d6df27a514be225d8e6e6c; _ga_MHSNPJKWC7=GS2.2.s1777929877$o2$g1$t1777930340$j60$l0$h0")
                print(f"Year {year} Day {day} data: {puzzle_data[:100]}...")  # Print first 100 characters
                with open(f"aoc_inputs/year_{year}_day_{day}.txt", "w", encoding="utf-8") as f:
                    f.write(puzzle_data)
            except Exception as e:
                print(f"Could not fetch data for Year {year} Day {day}: {e}")

if __name__ == "__main__":
    main()