from config.settings import PROJECT_NAME
from collectors.symbol_collector import SymbolCollector


def main():

    print(f"{PROJECT_NAME} Started")

    try:
        print("1 - MAIN OK")

        collector = SymbolCollector()

        print("2 - COLLECTOR CREATED")

        data = collector.collect()

        print("3 - DATA RECEIVED")

        print(type(data))

        print(data)

    except Exception as e:
        print("ERROR:")
        print(type(e))
        print(e)


if __name__ == "__main__":
    main()
