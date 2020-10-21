def write_array(array, file_name):
	with open(file_name,'w') as f:
		f.write('\n'.join(array))
pass

ar = ["Hello, it's me", "I was wondering if after all these years you'd like to meet", 'To go over everything', "They say that time's supposed to heal ya", "But I ain't done much healing", 'Hello, can you hear me?', "I'm in California dreaming about who we used to be", 'When we were younger and free', "I've forgotten how it felt before the world fell at our feet"]
write_array(ar,'2.txt')
