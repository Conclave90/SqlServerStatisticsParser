import re
import chardet


inputfile = "input.txt"

# identify the text file encoding and use it for the input file parsing
bin = open(inputfile, "rb").read()
result = chardet.detect(bin)
encoding = result['encoding']

file = open(inputfile, "r", encoding=encoding)

content = file.readlines()

total_cpu_time = 0
total_logical_reads = 0
total_elapsed_time = 0
total_physical_reads = 0
total_read_aheads = 0

for line in content:

    match = re.search("CPU time = \d+ ms", line)
    if match is not None:
        cpu_time_text = match.group(0)
        cpu_time_regex = re.search("\d+",cpu_time_text)
        cpu_time_value = cpu_time_regex.group(0)

        total_cpu_time += int(cpu_time_value)


    match = re.search("logical reads \d+,", line)
    if match is not None:
        logical_reads_text = match.group(0)
        logical_reads_regex = re.search("\d+", logical_reads_text)
        logical_reads_value = logical_reads_regex.group(0)

        print(line)

        total_logical_reads += int(logical_reads_value)

    #if '\'Worktable' in line.upper():
    match = re.search("physical reads \d+,", line)
    if match is not None:
        physical_reads_text = match.group(0)
        physical_reads_regex = re.search("\d+", physical_reads_text)
        physical_reads_value = physical_reads_regex.group(0)

        total_physical_reads += int(physical_reads_value)


    match = re.search("read-ahead reads \d+,", line)
    if match is not None:
        read_aheads_text = match.group(0)
        read_aheads_regex = re.search("\d+", read_aheads_text)
        read_aheads_value = read_aheads_regex.group(0)

        total_read_aheads += int(read_aheads_value)


    match = re.search("elapsed time = \d+ ms", line)
    if match is not None:
        elapsed_time_text = match.group(0)
        elapsed_time_regex = re.search("\d+", elapsed_time_text)
        elapsed_time_value = elapsed_time_regex.group(0)

        total_elapsed_time += int(elapsed_time_value)

print("CPU time: " + str(total_cpu_time) + " ms")
print("Logical reads: " + str(total_logical_reads))
print("Physical reads: " + str(total_physical_reads))
print("Read aheads: " + str(total_read_aheads))
print("Elapsed time: " + str(total_elapsed_time) + " ms")