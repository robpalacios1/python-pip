import matplotlib.pyplot as plt


def generate_bar_chart(name,labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig('./imgs/{}.png'.format(name))
  plt.close()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('pie.png')

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 100, 260]
  generate_pie_chart(labels,values)
