import matplotlib.pyplot as plt
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.style.use('ggplot')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=50)
ax.set_title('Square Nimbers', fontsize=16)
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel('Square of Values', fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=10)


ax.axis([0, 1100, 0, 1100000])
plt.show()
