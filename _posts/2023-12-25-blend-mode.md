---
title: Blend Mode
layout: post
---

|Blend Mode|방정식|
|---|---|
|Darken|$${O}=\min({B},{F})$$|
|Multiply|$${O}={B}\times{F}$$|
|Color Burn|$${O}=\frac{B+F−1}{F}$$|
|Linear Burn|$${O}=\max(0,{B+F−1})$$|
|Subtract|$${O}=\max(0,{B-F})$$|
|Lighten|$$\max(B, F)$$|
|Screen|$$1-(1-B)\,(1-F)=(1-B)\,F+B$$|
|Color Dodge|$$\frac{B}{1-F}=-\frac{B}{F-1}$$|
|Linear Dodge(Add)|$$B+F$$|
|발광 더하기| |
|Overlay|$$\begin{cases} 2BF & \text{if } 0 \leq B \lt 0.5 \\ F & \text{if } B = 0.5 \\ 1-2 \,(1-B) \,(1-F) = (1-B) \, 2F+2 \, B-1 & \text{if } 0.5 < B \leq 1 \end{cases}$$|
|소프트라이트| |
|Hard Light|$$\begin{cases} 2BF & \text{if } 0 \leq F \lt 0.5 \\ B & \text{if } F = 0.5 \\ 1-2 \,(1-F) \,(1-B) = (1-F) \, 2B+2 \, F-1 & \text{if } 0.5 < F \leq 1 \end{cases}$$|
|difference|$$\vert B-F \vert$$|
|Pin Light|$$\begin{cases} B & \text{if }0.5<F\text{ and }B<1-2F \\ 2F & \text{if }0.5<F\text{ and }B>1-2F \\ 2F-1 & \text{if }F<0.5\text{ and }B<2F-1 \\ B & \text{if }F<0.5\text{ and }2F-1<B \end{cases}$$|
|Hard Mix|$$\begin{cases} 0 & \text{if }B+F<1 \\ 1 & \text{if }1<B+F \end{cases}$$|
|Except|$$(1-F)B+(1-B)F$$|
