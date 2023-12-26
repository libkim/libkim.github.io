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
|Lighten|$R'=\max(R'_B, R'_F)$|
|Screen|$R'=1-(1-R'_B)\times (1-R'_F)$|
|Color Dodge|$R'=\frac{R'_B}{1-R'_F}$|
|Linear Dodge|$R'=R'_B+R'_F$|
|더하기| |
|발광 더하기| |
|Overlay|$$K=\begin{cases} -1 & \text{if }t\leq 0 \\ 1 & \text{if }t>0 \end{cases}$$|
|소프트라이트| |
|하드라이트| |
