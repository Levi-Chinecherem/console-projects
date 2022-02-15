from itertools import cycle, repeat, count


choices = ["baby", "rose", "benjamin", "japan"]
st = 17

  
for i in cycle(choices):
    print(i)
    st = st - 1
    if st == 0:
     break