import time
import webbrowser
total_breaks=3
break_count=0
print("Let's see timer program"+time.ctime())//it displays the current time of the system
while(break_count<total_breaks):
	time.sleep (3600)//It is in seconds
	webbrowser.open("https://www.youtube.com/watch?v=JjrqiIfF8to")//add ur fav video to distract from monotous work pressure
	break_count=break_count+1;
