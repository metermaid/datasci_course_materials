import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: sequence id
    # value: sequence
    key = record[0]
    value = record[1][0:-10]
    mr.emit_intermediate(value, 1)

def reducer(key, list_of_values):
    # key: dba pairs
    # value: # occured
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
