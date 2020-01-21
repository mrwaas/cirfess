# libraries
import matplotlib.pyplot as plt
import squarify    # pip install squarify (algorithm for treemap)
 
# If you have 2 lists
squarify.plot(sizes=[3971, 1180, 109, 34, 256, 69, 13, 394], alpha=.1 )
plt.axis('off')
plt.savefig('SPtree.svg', format = 'svg')

# If you have 2 lists
squarify.plot(sizes=[3971, 1180, 109, 34, 256, 69, 13, 394], alpha=.1 )
plt.axis('off')
plt.savefig('TMtree.svg', format = 'svg')

