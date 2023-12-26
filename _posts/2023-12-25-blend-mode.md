|Blend Mode|식|
|---|---|
|Darken|$R'=\min(R'_B, R'_F)$|
|Multiply|$R'=R'_B\times R'_F$|
|Color Burn|$R'=\frac{R'_B+R'_F−1}{R'_F}$|
|Linear Burn|$R'=\max(0, R'_B+R'_F−1)$|
|Subtract|$R'=\max(0, R'_B-R'_F)$|강해짐|||||
|Lighten|$R'=\max(R'_B, R'_F)$|강해짐|
|Screen|$1-(1-R'_B)\times (1-R'_F)$|그대로|
|Color Dodge|$R'=\frac{R'_B}{1-R'_F}$|강해짐|
|Linear Dodge|$R'=R'_B+R'_F$|강해짐|
|더하기||강해짐|
|발광 더하기||강해짐|
|Overlay|$R'=\begin{cases} 2\times R'_B\times R'_F, & R'_B<0.5 \\ 2\times R'_B\times R'_F, & R'_B<0.5\end{cases}$|그대로|
소프트라이트||그대로
하드라이트||그대로
