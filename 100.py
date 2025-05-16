def vector_sum(vector):
    if len(vector) == 0:
        return 0
    else:
        return vector[0] + vector_sum(vector[1:])
