import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# final matrix size
n = 5
m = 5

def mapper(record):
    # key: matrix id
    # i: row
    # j: column
    # value: value
    key, i, j, value = record

    if (key == "a"):
      for k in range(m):
        mr.emit_intermediate((i, k), record)
    if (key == "b"):
      for k in range(n):
        mr.emit_intermediate((k, j), record)

def reducer(key, list_of_values):
    # key: (i,j)
    # value: list of records
    total = 0
    for record in list_of_values:
      # matrix: matrix
      # i: row
      # j: column
      # val: value
      matrix = record[0]
      i = record[1]
      j = record[2]
      val = record[3]
      if matrix == 'a':
        b_cell = [r for r in list_of_values if (r[0] == 'b' and r[1] == j)]
        if b_cell != []:
          total += val * b_cell[0][3]

    if total != 0:
      mr.emit((key[0], key[1], total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
