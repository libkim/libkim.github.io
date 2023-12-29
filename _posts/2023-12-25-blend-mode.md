---
title: Blend Mode
layout: post
---

|Blend Mode|방정식|치역|
|---|---|---|
|Darken|$${O}=\min({B},{F})$$|$${0}\leq{O}\leq{1}$$|
|Multiply|$${O}={B}\times{F}$$|$${0}\leq{O}\leq{1}$$|
|Color Burn|$${O}=\begin{cases}\max\big({0},\frac{B+F−1}{F}\big)&{F}\neq{0}\\\max({0},{B+F−1})&{F}={0}\end{cases}$$|$${0}\leq{O}\leq{1}$$|
|Linear Burn|$${O}=\max({0},{B+F−1})$$|
|Subtract|$${O}=\max(0,{B-F})$$|
|Lighten|$${O}=\max({B},{F})$$|
|Screen|$${O}=1-({1-B})\,({1-F})=({1-B})\,({F+B})$$|
|Color Dodge|$${O}=\frac{B}{1-F}$$|
|Linear Dodge(Add)|$${O}={B}+{F}$$|
|Linear Dodge(Add)(Light Emission)|$${O}={B}+{F}\times{F_A}$$|
|Overlay|$${O}=\begin{cases}{2}\times{B}\times{F}&{0}\leq{B}\lt{0.5}\\{F}&{B}={0.5}\\1-2\,({1-B})\,({1-F})=({1-B})\,{2F+2}\,({B-1})&{0.5}<{B}\leq{1}\end{cases}$$|
|Soft Light|$${O}=\begin{cases}{1}-({1-B})\,({1}-({F-0.5}))&{0.5}<{F}\leq{1}\\{B}{F+0.5}&{0}\leq{F}\leq{0.5}\end{cases}$$|
|Hard Light|$${O}=\begin{cases}{2BF}&\text{if}\,{0}\leq{F}\lt{0.5}\\{B}&\text{if}{F}={0.5}\\{1}-{2}\,({1-F})\,({1-B})=({1-F})\,({2B+2})\,({F-1})&\text{if}{0.5}<{F}\leq{1}\end{cases}$$|
|difference|$${O}=\vert{B-F}\vert$$|
|Pin Light|$${O}=\begin{cases}{B}&\text{if}\,{0.5}<{F}\,\text{and}\,{B}<{1}-{2F}\\{2F}&\text{if}\,{0.5}<{F}\,\text{and}\,{B}>{1-2F}\\{2F-1}&\text{if}\,{F}<{0.5}\,\text{and}\,{B}<{2F-1}\\{B}&\text{if}\,{F}<{0.5}\,\text{and}\,{2F-1}<{B}\end{cases}$$|
|Hard Mix|$${O}=\begin{cases}{0}&\text{if}{B+F}<{1}\\{1}&\text{if}{1}<{B+F}\end{cases}$$|
|Except|$${O}=({1-F}){B}+({1-B}){F}$$|
