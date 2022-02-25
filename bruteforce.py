
import datetime

# file_name='a_an_example'
# file_name='b_better_start_small'
# file_name='c_collaboration'
# file_name='d_dense_schedule'
# file_name='e_exceptional_skills'
file_name='f_find_great_mentors'

file_name_in = f'input/{file_name}.in.txt'
file_name_out=f'output/{file_name}.out.txt'


from utils import read_input, read_output,simulate, calculate_score, reset, save_output, brute_force

 #,draw,draw_signals





start = datetime.datetime.now()


# score=simulate()

read_input(file_name_in)

# read_output(file_name_out)




reset()

brute_force()

# simulate()

# score=calculate_score()



save_output(file_name_out)


# print(f'Final Score: {score}')

# draw()
# draw_signals()



end = datetime.datetime.now()
# print(f'Ended {end}')

timetaken=end-start

print(f'Time Taken {timetaken}')
