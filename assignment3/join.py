import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: record id
    # value: full record
    key = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    # key: record id
    # value: full record
    for v in list_of_values:
        if (v[0] == "order"):
            for p in list_of_values:
                if (p[0] == "line_item"):
                    mr.emit(v + p)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
