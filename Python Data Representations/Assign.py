IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    length = min(len(line1), len(line2))
    if (length == 0):
        if len(line1) == len(line2):
            return IDENTICAL
        else:
            return 0
    for index in range(length):
        if line1[index] != line2[index]:
            return index
    if len(line1) == len(line2):
        return IDENTICAL
    else:
        return index + 1


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if ('\n' not in line1) and ('\n' not in line1):
        if ('\r' not in line1) and ('\r' not in line1):
            if (idx >= 0) and (idx <= min(len(line1), len(line2))):
                seperator = str()
                for index in range(idx):
                    seperator = seperator + '='
                seperator = seperator + '^'
                final = line1 + '\n' + seperator + '\n' + line2 + '\n'
                return final

    return ""


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    length = min(len(lines1), len(lines2))
    if (length == 0):
        if len(lines1) == len(lines2):
            return (IDENTICAL, IDENTICAL)
        else:
            return (0, 0)
    for index in range(length):
        idx = singleline_diff(lines1[index], lines2[index])
        if idx != -1:
            return (index, idx)
    if len(lines1) == len(lines2):
        return (IDENTICAL, IDENTICAL)
    else:
        return (index +1, 0)

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    file = open(filename, 'rt')
    line_string = list()
    for line in file:
        line = line.rstrip()
        line_string.append(line)
    return line_string

def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)
    i, idx = multiline_diff(lines1, lines2)
    seperator = str()
    for j in range(idx):
        seperator = seperator + '='
    seperator = seperator + '^'
    diff_string = 'Line ' + str(i) + ':' + '\n' + lines1[i] + '\n' + seperator + '\n' + lines2[i] + '\n'
    return diff_string