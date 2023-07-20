# https://github.com/gvlk/page-replacement-algorithm
# Leia o README.md
from sys import exit
from argparse import ArgumentParser
from page_replacement_algorithm import PageReplacement

# 0 - Aging
# 1 - WSClock

if __name__ == '__main__':
    parser = ArgumentParser(description="Page Replacement Algorithm")

    parser.add_argument(
        "-a", "--algorithm",
        type=int,
        choices=[0, 1],
        default=0,
        help="Select the algorithm: 0 - Aging, 1 - WSClock (default: 0)",
    )

    parser.add_argument(
        "-m", "--memory-length",
        type=int,
        default=67108864,
        help="Specify the length of physical memory (default: 67108864)",
    )

    parser.add_argument(
        "-i", "--input-file",
        type=str,
        required=True,
        help="Path to the input file containing memory accesses",
    )

    args = parser.parse_args()

    pr_algorithm = args.algorithm
    memory_length = args.memory_length
    input_file = args.input_file

    pr_instance = PageReplacement(pr_algorithm, memory_length, input_file)
    exit(pr_instance.run())

