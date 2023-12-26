|Blend Mode|식|색상 변화|색상 대비|명도 변화|명도 대비|채도 변화|채도 대비|
|---|---|---|---|---|---|---|---|
|Darken|$R'=\min(R'_B, R'_F)$|섞이는 느낌은 아님|강해짐|같거나 낮아짐|같거나 낮아짐|강해지거나 없음||
|Multiply|$R'=R'_B\times R'_F$|섞임|그대로|같거나 낮아짐|그대로|||
|Color Burn|$R'=\frac{R'_B+R'_F−1}{R'_F}$|강해짐|||||
|Linear Burn|$R'=\max(0, R'_B+R'_F−1)$|강해짐|||||
|Subtract|$R'=\max(0, R'_B-R'_F)$|강해짐|||||

Lighten|$\max(R'_B, R'_F)$|강해짐|
Screen|$1-(1-R'_B)\times (1-R'_F)$|그대로|
Color Dodge|$R'=\frac{R'_B}{1-R'_F}$|강해짐
Linear Dodge|$R'=R'_B+R'_F$|강해짐
더하기||강해짐
발광 더하기||강해짐
Overlay||그대로
소프트라이트||그대로
하드라이트||그대로
