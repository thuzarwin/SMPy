num_takers, total_takers = 100, 0

qs, agent_list =  [q1, q2, q3, q4], [CollegeStudent() for _ in range(num_takers)]

survey = Survey(qs)

def stop_condition():
    total_takers = total_takers + 1
    return num_takers < total_takers
