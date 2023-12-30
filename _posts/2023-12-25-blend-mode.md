---
title: Blend Mode
layout: post
---

|Blend Mode|방정식|치역|
|---|---|---|
|Darken|$${O}=\min({B},{F})$$|![Linear Dodge(Add)](/assets/img/linear-dodge.png)|
|Multiply|$${O}={B}\times{F}$$|![Linear Dodge(Add)](/assets/img/linear-dodge.png)|
|Color Burn|$${O}=\begin{cases}\max\bigg({0},\frac{B+F−1}{F}\bigg)&{F}\neq{0}\\\max({0},{B+F−1})&{F}={0}\end{cases}$$|![Linear Dodge(Add)](/assets/img/linear-dodge.png)|
|Linear Burn|$${O}=\max({0},{B+F−1})$$|![Linear Dodge(Add)](/assets/img/linear-dodge.png)|
|Subtract|$${O}=\max(0,{B-F})$$|![Linear Dodge(Add)](/assets/img/linear-dodge.png)|
|Lighten|$${O}=\max({B},{F})$$|![Linear Dodge(Add)](/assets/img/linear-dodge.png)|
|Screen|$${O}=1-({1-B})\,({1-F})={B}+{F}-{B}\times{F}$$|![Linear Dodge(Add)](/assets/img/linear-dodge.png)|
|Color Dodge|$${O}=\begin{cases}\frac{B}{1-F}&{F}\neq{1}\\{1}&{F}={1}\end{cases}$$|![Linear Dodge(Add)](/assets/img/linear-dodge.png)|
|Linear Dodge(Add)|$$\min({1},{O}={B}+{F})$$|![Linear Dodge(Add)](/assets/img/linear-dodge.png)|
|Linear Dodge(Add)(Light Emission)|$${O_P}={B}\times{B_A}+{F}\times{F_A}$$|![Linear Dodge(Add)](/assets/img/linear-dodge.png)|
|Overlay|$${O}=\begin{cases}{2}\times{B}\times{F}&{0}\leq{B}\lt{0.5}\\{F}&{B}={0.5}\\1-2\,({1-B})\,({1-F})=({1-B})\,{2F+2}\,({B-1})&{0.5}<{B}\leq{1}\end{cases}$$|![Linear Dodge(Add)](/assets/img/linear-dodge.png)|
|Soft Light|$${O}=\begin{cases}{1}-({1-B})\,({1}-({F-0.5}))&{0.5}<{F}\leq{1}\\{B}{F+0.5}&{0}\leq{F}\leq{0.5}\end{cases}$$|![Linear Dodge(Add)](/assets/img/linear-dodge.png)|
|Hard Light|$${O}=\begin{cases}{2BF}&{0}\leq{F}\lt{0.5}\\{B}&{F}={0.5}\\{1}-{2}\,({1-F})\,({1-B})=({1-F})\,({2B+2})\,({F-1})&{0.5}<{F}\leq{1}\end{cases}$$|![Linear Dodge(Add)](/assets/img/linear-dodge.png)|
|difference|$${O}=\vert{B-F}\vert$$|![Linear Dodge(Add)](/assets/img/linear-dodge.png)|
|Pin Light|$${O}=\begin{cases}{B}&{0.5}<{F}\,\text{and}\,{B}<{1}-{2F}\\{2F}&{0.5}<{F}\,\text{and}\,{B}>{1-2F}\\{2F-1}&{F}<{0.5}\,\text{and}\,{B}<{2F-1}\\{B}&{F}<{0.5}\,\text{and}\,{2F-1}<{B}\end{cases}$$|![Linear Dodge(Add)](/assets/img/linear-dodge.png)|
|Hard Mix|$${O}=\begin{cases}{0}&{B+F}<{1}\\{1}&{1}<{B+F}\end{cases}$$|![Linear Dodge(Add)](/assets/img/linear-dodge.png)|
|Except|$${O}=({1-F}){B}+({1-B}){F}$$|![Linear Dodge(Add)](/assets/img/linear-dodge.png)|
