# Introduction

Common code snippets.

# matplotlib

## Set default font size

```python
plt.rcParams.update({'font.size': 14})
```

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

Or

```python
plt.yticks([], [])
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

## Grid

```python
plt.gca().xaxis.grid(True)
```

Put grid behind plot

```python
plt.rcParams.update({'axes.axisbelow': True})
```


## Text

```python
plt.text(-0.1, 1.1, plot_label, transform = plt.gca().transAxes)
```

## Legend

```python
plt.legend(frameon=False, fontsize=12, labelspacing=0.1, columnspacing=1, bbox_to_anchor=(-0.01, 1.03), loc="upper left")
```

## Adjust subplot spacing
```python
plt.tight_layout()
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=0.4)
```
