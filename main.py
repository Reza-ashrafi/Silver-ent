from config.settings import PROJECT_NAME
from collectors.symbol_collector import SymbolCollector


def main():

    print(f"{PROJECT_NAME} Started")

    try:
        print("MAIN FUNCTION RUNNING")

        collector = SymbolCollector()

        data = collector.collect()

        print("TSETMC Connected")

        print(type(data))

        if isinstance(data, dict):
            print(data.keys())

        else:
            print(data[:500])

    except Exception as e:
        print("ERROR:")
        print(e)


if __name__ == "__main__":
    main()
