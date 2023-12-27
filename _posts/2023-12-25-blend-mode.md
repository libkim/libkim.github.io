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
|Overlay|$$begin{cases} 2BF & \text{if }B<0.5 \\ begin{align} 1-2(1-B)\,(1-F) \\ (1-B)\,2F+2\,B-1 \end{align} & \text{if }B>0.5 \end{cases}$$|
|소프트라이트| |
|하드라이트| |
