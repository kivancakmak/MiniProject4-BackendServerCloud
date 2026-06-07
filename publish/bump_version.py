import sys


def main():
    if len(sys.argv) < 2:
        print("Error: No version argument provided.")
        sys.exit(1)

    new_version = sys.argv[1]

    with open("VERSION", "w", encoding="utf-8") as f:
        f.write(new_version + "\n")

    print(f"VERSION file updated to {new_version}")


if __name__ == "__main__":
    main()
