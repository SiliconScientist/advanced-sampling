from config import Config
import toml


def main():
    config = Config(**toml.load("config.toml"))

    print(f"Hello, world #{config.random_seed}")


if __name__ == "__main__":
    main()
