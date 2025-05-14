import sys

input_filename = input("Please enter the input filename: ")

try:
    # >>> CORRECTED: Attempt to open the file FIRST within the try block <<<
    # If the file doesn't exist, the FileNotFoundError will happen immediately here.
    with open(input_filename, 'r', encoding='utf-8') as infile:

        # >>> Now get the keyword *after* successfully opening the file <<<
        # This code will only run if the 'with open' line above did NOT cause an error
        keyword = input("Please enter the keyword to filter lines by: ")
        if not keyword:
            print("Error: Keyword cannot be empty.")
            sys.exit(1)

        # Initialize the list to store matching lines
        matching_lines = []

        # Loop through each line in the file (which is now guaranteed to be open)
        for line in infile:
            # Check for Keyword and Store
            if keyword.lower() in line.lower():
                matching_lines.append(line.rstrip('\n'))

    # The 'with open(infile...):' block ends here.
    # Now that the input file is closed (or wasn't opened due to error handled below),
    # proceed with getting the output filename and writing.

    # Get the Output Filename
    output_filename = input("Please enter the output filename: ")
    if not output_filename:
        print("Error: Output filename cannot be empty.")
        sys.exit(1)

    # Open the Output File Safely
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        # Handle No Matches
        if not matching_lines:
            outfile.write(f"No lines containing '{keyword}' were found in the input file '{input_filename}'.")
            print(f"No lines containing '{keyword}' were found. An informative message was written to '{output_filename}'.")
        else:
            # Loop Through Matching Lines and Write with Line Numbers
            line_num = 1
            for processed_line in matching_lines:
                formatted_line = f"{line_num}: {processed_line}\n"
                outfile.write(formatted_line)
                line_num += 1

    # Print Success Message (if lines were written)
    if matching_lines:
        print(f"Successfully filtered and saved matching lines to '{output_filename}'.")

# --- The except blocks remain the same ---
except FileNotFoundError:
    print(f"Error: The input file '{input_filename}' was not found.")
    sys.exit(1)

except IOError:
    # This would catch other errors *during* the 'with open(infile...):' block,
    # like permission errors, although FileNotFoundError is more specific and caught first.
    print(f"Error: Could not read the input file '{input_filename}'. Check permissions.")
    sys.exit(1)

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)