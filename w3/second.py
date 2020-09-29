def write_array(array,file_name):
	a = open('second_in.txt','r')
	with open('second_out.txt', "w") as file:
		for  line in a:
			file.write(line)



write_array('input.txt','output.txt')
