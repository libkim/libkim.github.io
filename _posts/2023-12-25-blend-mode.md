|Blend Mode|식|
|---|---|
|Darken|$R'=\min(R'_B, R'_F)$|
|Multiply|$R'=R'_B\times R'_F$|
|Color Burn|$R'=\frac{R'_B+R'_F−1}{R'_F}$|
|Linear Burn|$R'=\max(0, R'_B+R'_F−1)$|
|Subtract|$R'=\max(0, R'_B-R'_F)$|
|Lighten|$R'=\max(R'_B, R'_F)$|
|Screen|$1-(1-R'_B)\times (1-R'_F)$|
|Color Dodge|$R'=\frac{R'_B}{1-R'_F}$|
|Linear Dodge|$R'=R'_B+R'_F$|
|더하기||
|발광 더하기||
|Overlay|
$R'=\begin{cases}
2\times R'_B\times R'_F, \; if\; R'_B<0.5\\
2\times R'_B\times R'_F, \; if\; R'_B\geq 0
\end{cases}$|
|소프트라이트|$x'_i=
\begin{cases}
{x_i^\lambda - 1 \over \lambda},\quad \;if\;\lambda \ne 0\\
log(x_i) ,  \; otherise
\end{cases}$|
|하드라이트||