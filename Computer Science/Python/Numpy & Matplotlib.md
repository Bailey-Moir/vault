---
tags:
  - comp
---
[Exam Resource](https://preuc.canterbury.ac.nz/mod/resource/view.php?id=4820)
_matplotlib_ is a very flexible graph and figure plotting package for Python that can display a wide range of 2D graphs and charts of publication quality.
# Numpy Arrays
Numpy arrays are better for doing numeric calculations on large sequences of numbers because:
1. It is much faster.
2. It takes less memory.
3. It behaves in a more mathematically intuitive way when multiplied, added, etc.
4. It is supported by a wide range of mathematical functions.
`ndarray`s are n-dimensional arrays of numbers or booleans with a _fixed size_. This means that the array size is specified on creation.

Unlike standard python collections (such as [[Basic Python#Lists|lists]], [[Basic Python#tuples|tuples]], [[Basic Python#Sets|sets]], etc), these arrays can only have one type. Slicing Numpy Arrays also creates an alias, unlike normal sequences.

1D Numpy Arrays are [[Math/Linear Algebra/Vectors/Vectors|vectors]].
2D Numpy Arrays with consistent widths are matrices.
## Generating Numpy Arrays 
All of the below function shave the optional `dtype=None` parameter, which specifies the type of elements the array has.
### `np.array`
Converts lists into arrays.
### `np.arange`
`np.arange` Creates an array of numbers with a parameter style similar to that of the [[Basic Python#Ranges|range function]], but it can generate floats. This function returns an `ndarray`.
`np.arange(0.0, 5.0, 1/3)`
`[0.         0.33333333 0.66666667 ... 4.66666667]`
###  `np.linspace`
`np.linspace` does the same thing as `np.arange`, except the third parameter defines the number of values to be linearly (equally) spaced, whereas `np.arange` defines the spacing in the array. Another key difference is `np.linspace` is **inclusive** of the end.
`np.linspace(0, 10, 5)`
`[ 0.   2.5  5.   7.5 10. ]`
### `np.full`, `np.ones`, `np.zeros`
`np.ones` and `np.zeros` create a Numpy Array of ones and zeros respectively, with parameter (excluding optional parameters): the shape. `np.full` does the same thing except it has a second parameter for what the array will be filled with (instead of zeros or ones).
## Advanced Indexing
Numpy Arrays can be indexed with lists and arrays. This returns another Numpy Arrays. 
They can also be indexed with booleans which dictate whether or not the corresponding element will be present. However, when indexing with a list or array of booleans, the list/array must be of the same shape as the array that is being index.
```python
import numpy as np
v = np.arange(10, 60, 10)
print(v[[4, 0, 2, -1]]) # out: [50 10 30 50]
print(v[[True, False, False, True, False]]) # out: [10 40]
```
> [!example]-
> ```python
> 	import numpy as np
> 	data = np.array([7.3, 9.5, -1, 11.1, 7.0, -1, 3.0])
> 	print(data[data >= 0]) # out: [ 7.3  9.5 11.1  7.   3. ]
> ```
### `np.any` and `np.all`
- `np.any` returns True if _any_ of the elements in its argument are True.  
- `np.all` returns True if _all_ of the elements in its argument are True.
>[!example]-
>```python
>import numpy as np
> table = np.array([[-1, 0, 1], [10, 20, 30]])
> print("All elements in row are positive:", np.all(table > 0, axis=1)) # [False True]
> print("At least one element in column is negative:", np.any(table < 0, axis=0)) # [True False False]
> ```
## 2D Arrays
```python
import numpy as np
data = np.array([[1, 2,  3, 4],
                 [10, 20, 30, 40],
                 [100, 200, 300, 400]])
print(data)
print(f"size: {data.size}") # number of elements, out: 12
print(f"shape: {data.shape}") # matrix order, (m, n), out: (3, 4)
```
\[[[_Matrices]]\]
### Indexing 2D Arrays
Indexing 2D arrays is fairly simple: `arr[m,n]` $=$ `arr[(m,n)]` $= a_{mn}$. Note that when an index is plugged into a function, it is always in tuple form.
# Plots
## Line Graphs
![700|center](line-chart-eg.png)
```python
import matplotlib.pyplot as plt
import numpy as np
import math

NUM_CYCLES = 2  # Number of cycles to plot
    
def main():
    xs = np.arange(0, NUM_CYCLES * 360)  # An x-value every degree
    ys = np.cos(2 * math.pi * xs / 360)  
    axes = plt.axes()
    
    axes.plot(xs, ys)
    
    axes.set_title("cos (x)")
    axes.grid(True)
    plt.show()
    
main()
```
## Bar Charts
[[Visualizing Data#Bar Charts|Bar charts]] are created in the same way as line chart, but with the `bar` function:
`axes.plot(xs, ys)` $\to$ `axes.bar(xs, ys)`
![700|center](bar-chart-eg.png)
```python
import numpy as np
import matplotlib.pyplot as plt

def main():
    rainfalls = np.loadtxt("laketaylorstation2005.txt", delimiter=",", skiprows=9, usecols=3) # 1D nparray, rainfall
    axes = plt.axes()
    
    axes.bar(np.arange(1,len(rainfalls)+1), rainfalls)
    
    axes.set_title("Lake Taylor Station Rainfalls, 2005")
    axes.set_xlabel("Day number")
    axes.set_ylabel("Rainfall (mm)")
    axes.grid(True)
    plt.show()
    
main()
```
*Note: this is a poor bar diagram statistically speaking.*

## Histograms
[[Visualizing Data#Histograms|Histograms]] a sort arrays into bins, and displays the number of occurrences in each bin. Unlike [[#Line Graphs|line graphs]] or [[#Bar Charts|bar charts]], these only have one array of input, although you can specify the bins that the array is sorted into.
![700|center](histogram-eg.png)
```python
import numpy as np
import matplotlib.pyplot as plt

def main():
    rainfalls = np.loadtxt('laketaylorstation2005.txt', delimiter=',', skiprows=9, usecols=3)
    axes = plt.axes()
    
    axes.hist(rainfalls, bins=np.arange(0, 36))
    
    axes.grid(True)
    axes.set_title("Lake Taylor Station Rainfalls, 2005")
    axes.set_xlabel('Daily rainfall (mm)')
    axes.set_ylabel('Number of occurrences')
    plt.show()
    
main()
```

# Ticks
```python
axes.set_xticks(years)  # Set the ticks on the x-axis
axes.set_xticklabels(labels, rotation=45)  # Set the labels for the tick marks
```
note that `len(years) == len(labels)`.

# Customizing Plots
All of the below options are customized as optional inputs in the creation of a plot.
- `color`: string or RGB, e.g. `"red"`.
- `marker`: specifies the marker type (`o` circle, `+` plus sign).
- `linestyle`: specifies the line style (`-` solid line, `:` dots, `--` dashes, etc).
- `linewidth` and `markersize`: both take a numeric value to specify the width of the line and the size of the markers respectively.
- `label`: this will be displayed in a legend if present with `axes.legend()`. 
<p class="note">Note: scatter plots can be made with normal line plots, but with no lines and the marker as a circle</p>

> [!example]-
> ![600|center](plot-customization.png)
> ```python
> import numpy as np
> import matplotlib.pyplot as plt
> def plot_demo():
>     """Plot some graphs"""
>     xs = np.linspace(0, 10, 21)  # 21 points in the range 0 to 10 inclusive
>     ys = xs ** 2  # A quadratic
>     axes = plt.axes()
>     axes.plot(xs, ys, label="Default - no markers")
>     axes.plot(xs, ys - 10, color="green", marker="o", linestyle="", label="No line with green circle markers")
>     axes.plot(xs, ys - 20, color="orange", marker="^", linestyle="-", label="Orange line with up-triangle markers")
>     axes.plot(xs, ys - 30, color="red", marker="+", linestyle=":", label="Red dotted line with plus markers")
>     axes.legend()  # Display a legend
>     axes.set_title("Different line and marker styles")
>     plt.show()
> plot_demo()
> ```
# Loading data from a file 
```python
# Creates a 1D nparray
np.loadtxt('data.txt', delimeter=',', skiprows=9, usecols=3)
```
Use `help(np.loadtxt)` for more information.
> [!example]-
> ```python
> def print_rainfall_stats(filename):
>     """Read and print rainfall statistics"""
>     rainfalls = np.loadtxt(filename, delimiter=',', skiprows=9, usecols=3)
>     print(f"{rainfalls.size} records read")
>     print(f"Minimum: {np.min(rainfalls):.1f} mm")
>     print(f"Maximum: {np.max(rainfalls):.1f} mm")
>     print(f"Average: {np.mean(rainfalls):.1f} mm")
>     print(f"Standard deviation: {np.std(rainfalls):.1f} mm")
> ```
<p class="note">Note the functions used to get each statistic</p>

\[[[#Numpy Arrays]]\]
# Curve-fitting
`np.polyfit(xs, ys, degree)` fits the points formed by `xs` and `ys` to a polynomial of the specified `degree`/order. This function returns a [[#Numpy Arrays|numpy array]] of the polynomial coefficients.
```python
a, b, c = np.polyfit(xs, ys, 2)
```
> [!example]-
> ![600|center](curve-fitting-eg.png)
> ```python
> import numpy as np
> import matplotlib.pyplot as plt
> 
> def main():
>     data = np.loadtxt("contdrift.csv", delimiter=",", skiprows=1, usecols=[0,1]).transpose()
>     xs = data[0]
>     ys = data[1]
>     
>     axes = plt.axes()
>     axes.plot(xs, ys, marker="o", color="blue")
>     a, b = np.polyfit(xs, ys, 1)
>     axes.plot(xs, a * xs + b, color="orange")
>     axes.set_xlabel("Time (Year)")
>     axes.set_ylabel("Distance (m)")
>     axes.set_title("Change in distance between Westford, USA and Wettzell, Germany")
>     axes.grid(True)
>     plt.show()
>     
>     print(f"The average speed the continents are moving is: {100*a:.2f} cm/year")
>     
> main()
> ```

# Matrix Multiplication
See [[_Matrices#Multiplication of Matrices by Scalars|Matrix Multiplication]] for the linear algebra explanation of matrix multiplication. There are 3 ways to do matrix multiplication.
`m1 @ m2` $=$ `m1.dot(m2)` $=$ `np.matmul(m1,m2)`
> [!example]-
> $$ \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix}1\\2\end{bmatrix} = \begin{bmatrix}-2\\1\end{bmatrix} $$
> ```python
> import numpy as np
> R = np.array([[0, -1], [1, 0]])  # Rotation by 90
> print(R @ np.array([[1], [2]]))
> print(R @ np.array([1,2]))
> print(R @ (1,2))
> 
> out:
> [[-2]
>  [ 1]]
> [-2  1]
> [-2  1]
> ```
