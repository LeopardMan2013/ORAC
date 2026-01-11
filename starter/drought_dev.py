# this function takes a file name and returns a list containing the lines
# sample call: get_lines("blah.txt")
def get_lines(fn):
    try:
        lines = []
        # Use 'with open' to ensure the file is automatically closed
        with open(filename, 'r') as file:
            for line in file:
                # The 'line' variable includes the trailing newline character ('\n')
                # Use line.strip() to remove leading/trailing whitespace, including '\n'
                processed_line = line.strip()

                lines.append(processed_line)

            return lines

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

filename = "drought_sample.txt"
lines = get_lines(filename)

# the first line in lines has 2 integers - we store in n and c
# n = number of days
# c = capacity of tank
# the following lines an integers that measure rainfall for the day

n = 0
c = 0
total_rainfall = 0
day_ct = 0

for index, l in enumerate(lines):
    if index == 0:
        n,c = l.split()
        n = int(n)
        c = int(c)
    else:
        total_rainfall = total_rainfall + int(l)
        day_ct = day_ct + 1
        if total_rainfall >= c:
            break

#print(f"n is {n} c is {c} total rainfall is {total_rainfall}")
#print(f"day counter was {day_ct}")
print(day_ct)
