

def get_solution(day, part, example, type="int"):
    solution_path = make_path_sln(day, part, example)
    with open(solution_path, 'r') as h:
        content = h.readlines()
    if type == "int":
        solution = int(content[0])
    elif type == "str":
        solution = str(content[0])
    else:
        return "Solution generation error."
    return solution


def make_path(day, part, example):
    #return a string with the following format: "./sample_data/sd_d01/sd_01_2_a.txt"
    day_formatted = f"{day:02d}"
    return f"./sample_data/sd_d{day_formatted}/sd_{day_formatted}_{part}_{example}.txt"


def make_path_sln(day, part, example):
    #return a string with the following format: "./sample_data/sd_d01/sd_01_2_a_solution.txt"
    day_formatted = f"{day:02d}"
    return f"./sample_data/sd_d{day_formatted}/sd_{day_formatted}_{part}_{example}_solution.txt"
