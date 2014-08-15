import json
from sys import argv
from os.path import basename, splitext


def csv_to_list(csv_data):
    csv_lines = csv_data.split("\n")
    header_fields = csv_lines[0].split(",")
    result = []

    for i in range(1, len(csv_lines)):
        d = {}
        parts = csv_lines[i].split(",")
        parts_index = 0

        if len(parts) != len(header_fields):
            print(parts)
            continue

        for header in header_fields:
            d[header] = parts[parts_index]
            parts_index += 1

        result.append(d)

    return result


def main():
    csv_file = open(argv[1], "r")
    csv_list = csv_to_list(csv_file.read())
    csv_file.close()

    json_filename = splitext(basename(argv[1]))[0] + ".json"
    json_file = open(json_filename, "w")
    json_file.write(json.dumps(csv_list, indent=4))
    json_file.close()


if __name__ == '__main__':
    main()
