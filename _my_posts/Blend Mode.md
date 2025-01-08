---
title: Blend Mode
slug: blend-mode
created-date: 2023-12-25
---

|Blend Mode|방정식|치역|
|---|---|---|
|Darken|$${O}=\min({B},{F})$$|![Darken](/assets/img/blend-mode/darken.png){: width="120" height="120"}|
|Multiply|$${O}={B}\times{F}$$|![Multiply](/assets/img/blend-mode/multiply.png){: width="120" height="120"}|
|Color Burn|$${O}=\begin{cases}\max\bigg({0},\frac{B+F−1}{F}\bigg)&{F}\neq{0}\\\max({0},{B+F−1})&{F}={0}\end{cases}$$|![Color Burn](/assets/img/blend-mode/color-burn.png){: width="120" height="120"}|
|Linear Burn|$${O}=\max({0},{B+F−1})$$|![Linear Burn](/assets/img/blend-mode/linear-burn.png){: width="120" height="120"}|
|Subtract|$${O}=\max(0,{B-F})$$|![Subtract](/assets/img/blend-mode/subtract.png){: width="120" height="120"}|
|Lighten|$${O}=\max({B},{F})$$|![Lighten](/assets/img/blend-mode/lighten.png){: width="120" height="120"}|
|Screen|$${O}=1-({1-B})\,({1-F})={B}+{F}-{B}\times{F}$$|![Screen](/assets/img/blend-mode/screen.png){: width="120" height="120"}|
|Color Dodge|$${O}=\begin{cases}\frac{B}{1-F}&{F}\neq{1}\\{1}&{F}={1}\end{cases}$$|![Color Dodge](/assets/img/blend-mode/color-dodge.png){: width="120" height="120"}|
|Linear Dodge(Add)|$$\min({1},{O}={B}+{F})$$|![Linear Dodge(Add)](/assets/img/blend-mode/linear-dodge.png){: width="120" height="120"}|
|Linear Dodge(Add)(Light Emission)|$${O_P}={B}\times{B_A}+{F}\times{F_A}$$|![Linear Dodge(Add)](/assets/img/linear-dodge.png){: width="120" height="120"}|
|Overlay|$${O}=\begin{cases}{2}\times{B}\times{F}&{0}\leq{B}\lt{0.5}\\{F}&{B}={0.5}\\1-2\,({1-B})\,({1-F})=({1-B})\,{2F+2}\,({B-1})&{0.5}<{B}\leq{1}\end{cases}$$|![Overlay](/assets/img/blend-mode/overlay.png){: width="120" height="120"}|
|Soft Light|$${O}=\begin{cases}{1}-({1-B})\,({1}-({F-0.5}))&{0.5}<{F}\leq{1}\\{B}{F+0.5}&{0}\leq{F}\leq{0.5}\end{cases}$$|![Soft Light](/assets/img/blend-mode/soft-light.png){: width="120" height="120"}|
|Hard Light|$${O}=\begin{cases}{2BF}&{0}\leq{F}\lt{0.5}\\{B}&{F}={0.5}\\{1}-{2}\,({1-F})\,({1-B})=({1-F})\,({2B+2})\,({F-1})&{0.5}<{F}\leq{1}\end{cases}$$|![Hard Light](/assets/img/blend-mode/hard-light.png){: width="120" height="120"}|
|difference|$${O}=\vert{B-F}\vert$$|![Linear Dodge(Add)](/assets/img/linear-dodge.png){: width="120" height="120"}|
|Pin Light|$${O}=\begin{cases}{B}&{0.5}<{F}\,\text{and}\,{B}<{1}-{2F}\\{2F}&{0.5}<{F}\,\text{and}\,{B}>{1-2F}\\{2F-1}&{F}<{0.5}\,\text{and}\,{B}<{2F-1}\\{B}&{F}<{0.5}\,\text{and}\,{2F-1}<{B}\end{cases}$$|![Linear Dodge(Add)](/assets/img/linear-dodge.png){: width="120" height="120"}|
|Hard Mix|$${O}=\begin{cases}{0}&{B+F}<{1}\\{1}&{1}<{B+F}\end{cases}$$|![Linear Dodge(Add)](/assets/img/linear-dodge.png){: width="120" height="120"}|
|Except|$${O}=({1-F}){B}+({1-B}){F}$$|![Linear Dodge(Add)](/assets/img/linear-dodge.png){: width="120" height="120"}|
