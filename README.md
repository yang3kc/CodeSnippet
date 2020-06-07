# Introduction

Common code snippets.

# matplotlib

## Tick label format

### Scientific notation

```python
plt.gca().ticklabel_format(axis='y', style='sci', scilimits=(0,0))
```

### Percentage

```python
import matplotlib.ticker as mtick

# xmax: the value corresponding to the 100%
# decimals: number of decimal places to place after the point. 
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=100, decimals=None))
````

## Tick labels styles

### Remove tick labels

```python
plt.gca().set_xticklabels([])
```

### customize axis ticks

```python
plt.xticks(xs, list(map(format_date_time, xs)), rotation=35, ha='right', fontsize=fontsize);
```

## Remove axis

```python
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
```
