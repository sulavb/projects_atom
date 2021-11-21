import matplotlib.pyplot as plt

x = int(input('Enter a number: '))
t_value = x
y = 0
x_list = []
y_list = []

while x != 1:
    y = y + 1
    if x % 2 == 0:
        x = x / 2
    else:
        x = (3*x) + 1

    x_list.append(y)
    y_list.append(x)

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(x_list, y_list) # for lines
ax.scatter(x_list, y_list, c='red', s=20) # for dots

# labeling the graph
ax.set_title(f"3x+1 Graph for {t_value}", fontsize=24)
ax.set_xlabel("Intervals", fontsize=14)
ax.set_ylabel("Formula value", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()