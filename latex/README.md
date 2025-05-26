# Introduction

Common code snippets for LaTeX.

## Prompt boxes

### Fancy prompt box

Import tcolorbox package
```tex
\usepackage[breakable]{tcolorbox}
```

Define `promptbox` command at the beginning of the document
```tex
\newtcolorbox[auto counter]{promptbox}[2][]{
    colback=white!95!gray,
    colframe=gray!50!black,
    breakable,
    rounded corners,
    title={Box \thetcbcounter: #2},
    #1
}
```

Use the promptbox command to create a prompt box with a label, title, and content.
```tex
\begin{promptbox}[label={box:label_name}]{Prompt title}
    Prompt content
\end{promptbox}
```

### Less fancy prompt box

Define `prompt` command at the beginning of the document.
```tex
\newcommand{\prompt}[2]{
    \vspace{0.1in}
    \fbox{
        \parbox{0.9\columnwidth}{
            \underline{\textbf{{#1}:}}
            \newline
            {#2}
            }
        }
    \vspace{0.1in}
}
```

Use the prompt command to create a prompt box with a label and content.
```tex
\prompt{Prompt title}{
    Prompt
    }
```

## Tables

### Resize table size

```tex
\begin{table}
    \centering
    \caption{Caption}
    \label{tab}
    \resizebox{\columnwidth}{!}{
        \begin{tabular}{ll}
        \end{tabular}
    }
\end{table}
```
