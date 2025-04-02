# Introduction

Common code snippets for LaTeX.

## Fancy prompt box

Import tcolorbox package
```tex
\usepackage{tcolorbox}
```

Define `promptbox` command at the beginning of the document
```tex
\newcommand{\promptbox}[3]{
    \begin{tcolorbox}[
        colback=white!95!gray,
        colframe=gray!50!black,
        rounded corners,
        label={#1},
        title={#2}
    ]
        #3
    \end{tcolorbox}
}
```

Use the promptbox command to create a prompt box with a label, title, and content.
```txt
\promptbox{box:label_name}{Prompt title}{
    Prompt
    }
```

## Less fancy prompt box

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
```txt
\prompt{Prompt title}{
    Prompt
    }
```
