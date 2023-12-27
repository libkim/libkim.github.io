---
title: Blend Mode
layout: post
---

|Blend Mode|식|
|---|---|
|Darken|$$R'=\min(R'_B, R'_F)$$|
|Multiply|$$R'=R'_B\times R'_F$$|
|Color Burn|$$R'=\frac{R'_B+R'_F−1}{R'_F}$$|
|Linear Burn|$$R'=\max(0, R'_B+R'_F−1)$$|
|Subtract|$R'=\max(0, R'_B-R'_F)$|
|Lighten|$$\max(B, F)$$|
|Screen|$$1-(1-B)\,(1-F)=(1-B)\,F+B$$|
|Color Dodge|$$\frac{B}{1-F}=-\frac{B}{F-1}$$|
|Linear Dodge(Add)|$$B+F$$|
|발광 더하기| |
|Overlay|$$R'=\begin{cases} -1 & \text{if }t \leq 0 \\ 1 & \text{if }t > 0 \end{cases}$$|
|소프트라이트| |
|하드라이트| |
