from config.settings import PROJECT_NAME
from collectors.symbol_collector import SymbolCollector


def main():

    print(f"{PROJECT_NAME} Started")

    collector = SymbolCollector()

    symbols = collector.collect()

    print(symbols.keys())


if __name__ == "__main__":
    main()
