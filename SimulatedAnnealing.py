from TSI import TSI
from SA import SA
import datetime as dt

# TODO ADD COMENTARIOS


def mount_instance(data, format):
    matrix = mount_matrix(data, format)
    instance = TSI(data[0], data[1], data[2],
                   data[3], data[4], data[5],
                   data[6], data[7], matrix)
    return instance


def read_tsp_data(tsp_name):
    tsp_name = tsp_name
    with open(tsp_name) as f:
        content = f.read().splitlines()
        cleaned = [x.lstrip() for x in content if x != ""]
        return cleaned


def print_matrix(matrix):
    f = open("FullMatrix.txt", "w+")
    for i in matrix:
        f.write(str(i))
        f.write("\n")


def mount_matrix(data, format):
    matrix_string = ""
    for i in data[7:-1]:
        if matrix_string != "":
            matrix_string = matrix_string + " " + i
        else:
            matrix_string = matrix_string + i
    matrix = matrix_string.split(sep=" ")
    if format == "si":
        matrix = matrix[::-1]
    else:
        matrix = matrix[:-1]
    new_matrix = []
    row = []
    for i in matrix:
        if int(i) == 0:
            row.append(int(i))
            new_matrix.append(row)
            row = []
        else:
            row.append(int(i))
    # COMPLETANDO A MATRIZ
    for i in new_matrix:
        for j in range(new_matrix.index(i)+1, len(new_matrix)):
            i.append(new_matrix[j][new_matrix.index(i)])
    # MATRIZ SEM OS 0's new_matrix[1:]
    return new_matrix


def main():
    f = open("Results.txt", "w+")
    for _ in range(1):
        file = "Instancias/si1032.tsp"
        # file = "Instancias/gr48.tsp"
        data = read_tsp_data(file)
        tsi = mount_instance(data, "si")
        # tsi = mount_instance(data, "gr")
        print_matrix(tsi.matrix)
        initial_time = dt.datetime.utcnow()
        sa = SA(tsi.matrix, stopping_iter=50000)
        sa.sa(f)
        final_time = dt.datetime.utcnow()
        final_time = (final_time - initial_time).total_seconds()
        f.write("Final Time: {} \n\n".format(str(final_time)))
        # sa.plot_learning()
    f.close()


if __name__ == "__main__":
    main()