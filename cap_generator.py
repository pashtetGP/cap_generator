"""
This file is subject to the terms and conditions defined in
file 'LICENSE.txt', which is part of this source code package.
 """
from pathlib import Path

MAX_NUM_SCENARIOS = 5000 # according to the article and data
NUM_SCENARIOS = [5, 50, 250, 1000, 2000, 3000, 4000, 5000]
INPUT_PATH = "input"
OUTPUT_PATH = "output"
TEST_NAME = "cap_test"
PROBLEMS = [TEST_NAME, "cap101", "cap102", "cap103", "cap111", "cap112", "cap113", "cap114", "cap121", "cap122", "cap123", "cap124", "cap131", "cap132", "cap133", "cap134"]
# cap104 is excluded since it has an error in the data (matrix W has more than needed rows)

def parse_vector_line(line):
    """
    Takes a line from the .dat file formated according to Bodur style and creates a list of its values.
    E.g., "[10,10,10]" -> [10, 10, 10]

    :param line: string - the line with vector values, e.g., "[10,10,10]" or "[[10,10,10]," if it is the first vector of matrix.
    :return: list with vector elements
    """

    old_line_size = len(line)
    line = line.strip() # sometimes we have trailing spaces
    if (old_line_size != len(line)):
        print(f"WARNING: Spaces at the beginning or at the end of the line are found in the .dat file.")

    line_start = line[:2]
    line_end = line[-2:]
    if line_start == "[[" and line_end == "]]": # vector of the matrix that has only one row, e.g., [[10,10,10]]
        clean_line = line[2:-2]
    elif line_start == "[[": # first vector of matrix, e.g., [[10,10,10],
        clean_line = line[2:-2]
    elif line_end == "],": # vector of matrix, e.g., [10,10,10],
        clean_line = line[1:-2]
    elif line_end == "]]": # last vector of matrix, e.g., [10,10,10]]
        clean_line = line[1:-2]
    else: # vector, e.g., [10,10,10]
        assert(line[0] == "[" and line[-1] == "]")
        clean_line = line[1:-1]

    vector = clean_line.split(",")
    vector_numerical = []
    for element in vector:
        element_numerical = float(element)
        # keep it as integer if it is one
        if element_numerical.is_integer(): element_numerical = int(element)
        vector_numerical.append(element_numerical)

    return vector_numerical

def parse_matrix_lines(starting_line: int, lines: list):
    '''
    Starts from the starting_line and parses all the subsequent lines into the list of rows. The line with the last row is defined automatically.

    :param starting_line: int - the line with the first row of the vector
    :param num_cols: int (default None) - number of the first elements in the line to include in row vector, e.g., if num_cols := 3 and line is [10,10,10,0,0] -> [10,10,10]. If None, than all elements are included.
    :return: list of rows - every row is the list of vector elements.
    '''

    first_line = lines[starting_line].strip()
    if first_line[:2] != "[[":
        raise ValueError(f"Line {starting_line} is not a first vector in matrix because it does not start with '[['")

    matrix = []
    for line in lines[starting_line:]:
        row = parse_vector_line(line)
        matrix.append(row)
        if line[-2:] == "]]": # last row in matrix
            break
    else:
        raise RuntimeError("Matrix parse error: row ending with ']]' was not found, i.e., there is no last row for the matrix.")

    return matrix

def calculate_b(matrix_h: list, J: int):
    '''
    Calculates the values of vector b = max[sum(for rows)]

    :param matrix_h: list of row - every row is related to scenario and every column to the row in matrices T and W
    :return: list of vector values (it has size 1 in CAP)
    '''

    sum_for_rows = [sum(row[:J]) for row in matrix_h]
    b = max(sum_for_rows)

    return [b]

def vector_to_text(vector: list):
    '''
    [1, 2, 3.1] -> "1,2,3.1"
    There is no \n at the end of the output

    :param vector: list of numbers which are vector elements
    :return: string
    '''
    return ', '.join([str(elem) for elem in vector])

def matrix_to_text(matrix: list):
    '''
    [[11,12,13], [21,22,23]] -> "11,12,13\n21,22,23"
    There is no \n at the end of the output

    :param matrix: list of vectors which are rows of matrix
    :return: string
    '''

    list_of_row_strings = [vector_to_text(row) for row in matrix] # e.g., ["11,12,13", "21,22,23"]

    return '\n'.join(list_of_row_strings)

def generate_cor_text(instance_name: str, matrix_T: list, matrix_A: list, matrix_W: list, vector_c: list, vector_d: list, vector_b: list) -> str:
    n_rows = len(matrix_T)
    assert(len(matrix_W) == n_rows)
    I = len(vector_c) # n_first_stage_cols
    assert(len(vector_b) == 1) # we always have one constraint on the first stage
    assert(len(matrix_A) == 1)

    contents = f'NAME          {instance_name} (MIN)\n'

    contents += 'ROWS\n'
    contents += '  N Objective\n  G FirstStCnstr\n'
    for row_index in range(n_rows):
        contents += f'  G SecondStCnstr{row_index+1}\n'

    contents += 'COLUMNS\n'
    # 1st stage
    for var_index, c_value in enumerate(vector_c):
        contents += f'    x{var_index+1}        Objective           {c_value}\n'
        contents += f'    x{var_index+1}        FirstStCnstr        {matrix_A[0][var_index]}\n'
        for row_index in range(0, n_rows):
            if matrix_T[row_index][var_index] != 0:
                contents += f'    x{var_index+1}        SecondStCnstr{row_index+1}     {matrix_T[row_index][var_index]}\n'
    # 2nd stage
    for var_index, d_value in enumerate(vector_d):
        contents += f'    y{var_index+1}        Objective           {d_value}\n'
        for row_index in range(0, n_rows):
            if matrix_W[row_index][var_index] != 0:
                contents += f'    y{var_index+1}        SecondStCnstr{row_index+1}      {matrix_W[row_index][var_index]}\n'

    contents += 'RHS\n'
    first_stage_coef = vector_b[0]
    contents += f'    RHS1      FirstStCnstr         {first_stage_coef}\n'
    for row_index in range(0, n_rows-I): # last I values are 0 and can be omitted in MPS
        contents += f'    RHS1      SecondStCnstr{row_index+1}         12345.0\n' # 12345.0 is a dummy value. Correct value will be provided in .sto

    contents += 'BOUNDS\n'
    for bin_index in range(I):
        contents += f' BV BOUND1    x{bin_index+1}                 1.0\n'

    contents += 'ENDATA'

    return contents

def generate_tim_text(instance_name) -> str:
    contents = f'''TIME          {instance_name}  (MIN)
PERIODS       IMPLICIT
    x1        FirstStCnstr                 Stage1    
    y1        SecondStCnstr1               Stage2    
ENDATA
    '''

    return contents

def generate_sto_text(instance_name, matrix_H: list, I: int) -> str:
    contents = f'STOCH         {instance_name} (MIN)\nSCENARIOS\n'
    num_scen = len(matrix_H)
    scen_prob = 1/num_scen
    for scen_index, scen_rhs in enumerate(matrix_H):
        if scen_index == 0:
            scen_name = "'ROOT'"
            scen_stage = 1
        else:
            scen_name = f'SCEN1'
            scen_stage = 2
        contents += f' SC Scen{scen_index+1}     {scen_name}             {scen_prob}   Stage{scen_stage}    \n'
        for rhs_row_index, rhs_element in enumerate(scen_rhs[:-I]):
            contents += f'    RHS1      SecondStCnstr{rhs_row_index+1}          {rhs_element}\n'
    contents += 'ENDATA'

    return contents

def main():

    folder = Path(INPUT_PATH)
    if not folder.exists():
        raise FileNotFoundError(f"{INPUT_PATH} folder not found.")

    for problem_name in PROBLEMS:
        # generate instances for the different number of scenarios
        for n_sc in NUM_SCENARIOS:
            assert(n_sc <= MAX_NUM_SCENARIOS)
            if problem_name == TEST_NAME: assert(n_sc == 5) # for test there is only one instance of 5 scen. We will quit the scenarios loop after one iteration for this problems
            print(f"Parsing instance {problem_name} with {n_sc} scenarios.")
            dat_file = Path(INPUT_PATH + "\\" + problem_name + ".dat")
            if not dat_file.exists():
                raise FileNotFoundError(f"File {dat_file} not found in {INPUT_PATH}.")

            lines = dat_file.read_text().splitlines()

            vector_c = parse_vector_line(lines[0])
            I = len(vector_c)
            n_first_stage_cols = I
            print(f" -- I = {n_first_stage_cols}")
            print(f" -- Number 1st stage columns: {n_first_stage_cols}")

            vector_d = parse_vector_line(lines[1])
            n_second_stage_cols = len(vector_d)
            J = int(n_second_stage_cols/I)
            print(f" -- J = {J}")
            print(f" -- Number 2nd stage columns: {n_second_stage_cols}")

            matrix_T_start = 2 # starting line
            matrix_T = parse_matrix_lines(matrix_T_start, lines)
            n_rows = len(matrix_T)
            assert(n_rows == J+I)
            print(f" -- Number rows in T and W: {n_rows}")

            matrix_W_start = matrix_T_start + n_rows
            matrix_W = parse_matrix_lines(matrix_W_start, lines)
            assert(len(matrix_W) == n_rows)
            assert (len(matrix_W[0]) == n_second_stage_cols)

            # it is a stochastic vector: every row is related to scenario
            matrix_h_start = matrix_W_start + n_rows
            matrix_h_all = parse_matrix_lines(matrix_h_start, lines)
            matrix_h = matrix_h_all[:n_sc] # we need only the first n_sc rows
            h_for_first_sc = matrix_h[0]
            assert (len(h_for_first_sc) == n_rows)
            assert(all(value == 0 for value in h_for_first_sc[-I:])) # last I elements should be 0

            first_stage_ub_index = matrix_h_start + MAX_NUM_SCENARIOS # jump over the whole matrix_h_all
            if problem_name == TEST_NAME: first_stage_ub_index = matrix_h_start  + 15 # in test we can have max 15 scen
            first_stage_ub = parse_vector_line(lines[first_stage_ub_index])
            assert(len(first_stage_ub) == n_first_stage_cols)

            matrix_A_index = first_stage_ub_index + 1
            matrix_A = parse_matrix_lines(matrix_A_index, lines)
            assert(len(matrix_A) == 1) # it is 1 row matrix
            assert (len(matrix_A[0]) == n_first_stage_cols)

            # it should be the last row
            assert(len(lines) == matrix_A_index+1)

            # ..._SETS.dat file
            instance_name = f"{problem_name}_{n_sc}"
            path_prefix = f"{OUTPUT_PATH}\\{instance_name}"
            sets_path = f"{path_prefix}_SETS.dat"
            sets_file = Path(sets_path)
            sets_file.write_text(f"""! I
{I}
! J
{J}
! K
{n_sc}""")
            print(f" -- Created {sets_path}")

            # ..._RANDOM.dat file
            random_path = f"{path_prefix}_RANDOM.dat"
            rand_file = Path(random_path)
            text = "! Vector_h[k, Row]\n" + matrix_to_text(matrix_h)
            rand_file.write_text(text)
            print(f" -- Created {random_path}")

            # ..._DATA.dat file
            vector_b = calculate_b(matrix_h, J)
            if (problem_name == TEST_NAME):
                assert(vector_b[0] == 156)
            comments = ["! Vector_c[FirstStCol]","! Vector_d[SecondStCol]","! Vector_b",
                        "! Matrix_A[FirstStCol]","! Matrix_T[Row, FirstStCol]","! Matrix_W[Row, SecondStCol]","! Vector x_ub[FirstStCol]"]
            contents = [vector_c, vector_d, vector_b, matrix_A, matrix_T, matrix_W, first_stage_ub]
            assert(len(comments) == len(contents))
            text = ""
            for i, comment in enumerate(comments):
                text += (comment + "\n")
                if comment[2:8] == "Vector":
                    text += vector_to_text(contents[i])
                elif comment[2:8] == "Matrix":
                    text += matrix_to_text(contents[i])
                else:
                    assert(False)
                text += "\n"

            data_path = f"{path_prefix}_DATA.dat"
            data_file = Path(data_path)
            data_file.write_text(text[:-1]) # get rid of the last \n
            print(f" -- Created {data_path}")

            # ..._CAP_extensive_form.mpl
            template_mpl_path = INPUT_PATH + "\\" + "TEMPLATE_cap_mpl.txt"
            template_mpl = Path(template_mpl_path)
            if not dat_file.exists():
                raise FileNotFoundError(f"File {template_mpl_path} not found in {INPUT_PATH}.")
            template_instance_formulation = template_mpl.read_text()
            # actualize for the current instance
            instance_formulation = template_instance_formulation.replace("???instance???", instance_name)

            instance_mpl_path = f"{path_prefix}.mpl"
            instance_mpl = Path(instance_mpl_path)
            instance_mpl.write_text(instance_formulation)

            print(f" -- Created {instance_mpl_path}. You can transform it to SMPS with opt_convert.\n")

            #  ... .cor
            cor_path = f"{path_prefix}.cor"
            cor_file = Path(cor_path)
            text = generate_cor_text(instance_name, matrix_T, matrix_A, matrix_W, vector_c, vector_d, vector_b)
            cor_file.write_text(text)
            print(f" -- Created {cor_path}")

            # ... .tim
            tim_path = f"{path_prefix}.tim"
            tim_file = Path(tim_path)
            text = generate_tim_text(instance_name)
            tim_file.write_text(text)
            print(f" -- Created {tim_path}")

            #  ... .sto
            sto_path = f"{path_prefix}.sto"
            sto_file = Path(sto_path)
            text = generate_sto_text(instance_name, matrix_h, I)
            sto_file.write_text(text)
            print(f" -- Created {sto_path}.\n")

            # for test there is only one instance of 5 scen
            if problem_name == TEST_NAME:
                break

    # for loop end: instances
    return 0

if __name__ == "__main__":
    main()
