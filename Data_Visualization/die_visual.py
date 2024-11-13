import plotly.express as px

from die import Die

#Create two D6 Dies
die_1=Die()
die_2=Die()

#Make some rolls, and store reults in a list
results=[]
for roll in range(10000):
    result=die_1.roll()+die_2.roll()
    results.append(result)

frequencies=[]
poss_results=range(2,die_1.num_sides+die_2.num_sides+1)
for value in poss_results:
    frequency=results.count(value)
    frequencies.append(frequency)
title='Result of rolling one D6 die 10000 times'
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()