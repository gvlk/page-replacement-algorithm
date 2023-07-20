# Page Replacement Algorithm
This is a Python implementation of a page replacement algorithm simulation for memory management in operating systems. The two available algorithms are "Aging" and "WSClock."

## Installation
Clone this repository to your local machine:
```bash
git clone # https://github.com/gvlk/page-replacement-algorithm.git
```
No additional installations or dependencies are needed for running the simulation. You can simply execute the main.py script as described in the "Usage" section below.

## Usage
To run the page replacement algorithm simulation, use the main.py script with the following command-line arguments:

```bash
python main.py [-a {0, 1}] [-m MEMORY_LENGTH] -i INPUT_FILE
```
Arguments:

-a, --algorithm: Select the algorithm to use. Options: 0 for Aging, 1 for WSClock (default: 0).  
-m, --memory-length: Specify the length of physical memory in bytes (default: 67108864).  
-i, --input-file: Path to the input file containing memory accesses.  

Example:

Run the simulation with WSClock algorithm, 128MB of physical memory, and using the file accesses.txt for memory access inputs:

```bash
python main.py -a 1 -m 128000000 -i accesses.txt
```
The output will display the results of the page replacement algorithm simulation.

### Input File Format
The input file should contain memory access information, where each line represents an access. The format of each line should be:

"PAG" ACCESS_TYPE PAGE_INDEX  
ACCESS_TYPE: The type of access, either "DADOS" or "INST" (for data or instruction).  
PAGE_INDEX: The index of the page being accessed.  

Here's an example of an input file:

```
PAG DADOS 10
PAG INST 2
PAG DADOS 5
PAG DADOS 10
PAG DADOS 7
PAG INST 4
PAG INST 2
```

## Acknowledgments
This project was inspired by the memory management concepts covered in the operating systems subject.

## Contributions
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to [open an issue](https://github.com/gvlk/page-replacement-algorithm/issues) or create a [pull request](https://github.com/gvlk/page-replacement-algorithm/pulls) with your proposed changes.  

## Credits
This project is maintained by Guilherme Azambuja.