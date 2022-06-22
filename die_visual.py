from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

die1 = Die()
die2 = Die()

results = []

for roll in range(10000):
    results.append(die1.rool()+die2.rool())

frequencie = []
for value in range(1, die1.num_sides*2+1):
    frequency = results.count(value)
    frequencie.append(frequency)

x_values = list(range(1, die1.num_sides*2+1))
data = [Bar(x=x_values, y=frequencie)]
x_axis_config = {'title': '结果', 'dtick': 1}
y_axis_config = {'title': '结果的频率'}
my_layout = Layout(title='投一个D6 1000次的结果',
                    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout,}, filename='D6.html')

# print(results)