\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T2A]{fontenc}
\usepackage[russian]{babel}
\usepackage{amsmath, amssymb, amsfonts}
\usepackage{booktabs}
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{verbatim}
\usepackage{algorithmic}
\usepackage{array}
\geometry{top=2cm, bottom=2cm, left=2.5cm, right=2cm}

\title{Методы байесовской фильтрации для локализации и построения карт (SLAM)}
\author{}
\date{}

\begin{document}

\maketitle

Для эффективной обработки данных сенсоров (включая LiDAR) и решения задач локализации и построения карт в мобильной робототехнике широко применяются байесовские методы фильтрации. Эти методы позволяют оценивать состояние системы (положение робота, параметры карты) на основе зашумленных измерений.

\section{Байесовский подход к оценке состояния}

Задача навигации мобильного робота может быть сформулирована как задача оценки состояния в вероятностной постановке. Байесовский фильтр обеспечивает рекурсивную оценку состояния $\mathbf{x}_t$ (положение и ориентация робота) на основе управляющих воздействий $\mathbf{u}_t$ и измерений $\mathbf{z}_t$ [Cyrill Stachniss, Course 04].

\textbf{Шаг предсказания (Prediction):}
\[
\overline{bel}(\mathbf{x}_t) = \int p(\mathbf{x}_t \mid \mathbf{u}_t, \mathbf{x}_{t-1}) \; bel(\mathbf{x}_{t-1}) \, d\mathbf{x}_{t-1}
\]

\textbf{Шаг коррекции (Correction):}
\[
bel(\mathbf{x}_t) = \eta \; p(\mathbf{z}_t \mid \mathbf{x}_t) \; \overline{bel}(\mathbf{x}_t)
\]
где $bel(\mathbf{x}_t)$ — вера (belief) в состояние робота в момент времени $t$, $\eta$ — нормировочная константа.

\section{Фильтр Калмана (Kalman Filter)}

Фильтр Калмана представляет собой реализацию байесовского фильтра для линейных гауссовских систем. Он обеспечивает оптимальное решение при условии линейности моделей движения и наблюдения, а также гауссовского характера шумов [Course 04].

\subsection{Основные свойства}

\begin{table}[h]
\centering
\begin{tabular}{ll}
\toprule
\textbf{Свойство} & \textbf{Описание} \\
\midrule
Распределение & Всё описывается гауссовскими распределениями \\
Параметры & Математическое ожидание $\bm{\mu}$ и ковариационная матрица $\bm{\Sigma}$ \\
Линейная модель & $\mathbf{x}_t = \mathbf{A}_t \mathbf{x}_{t-1} + \mathbf{B}_t \mathbf{u}_t + \bm{\epsilon}_t$, $\mathbf{z}_t = \mathbf{C}_t \mathbf{x}_t + \bm{\delta}_t$ \\
Сложность & $O(k^{2.4} + n^2)$, где $k$ — размерность наблюдения \\
\bottomrule
\end{tabular}
\end{table}

\subsection{Алгоритм фильтра Калмана [Course 04]}

\begin{verbatim}
1: Kalman_filter(μ_{t-1}, Σ_{t-1}, u_t, z_t)
2:   μ̄_t = A_t μ_{t-1} + B_t u_t
3:   Σ̄_t = A_t Σ_{t-1} A_t^T + R_t
4:   K_t = Σ̄_t C_t^T (C_t Σ̄_t C_t^T + Q_t)^{-1}
5:   μ_t = μ̄_t + K_t (z_t - C_t μ̄_t)
6:   Σ_t = (I - K_t C_t) Σ̄_t
7:   return μ_t, Σ_t
\end{verbatim}

\textbf{Преимущества:} Оптимальность для линейных систем, вычислительная эффективность.

\textbf{Ограничения:} Неприменим к нелинейным системам, которые характерны для большинства реальных робототехнических задач.

\section{Расширенный фильтр Калмана (Extended Kalman Filter – EKF)}

Реальные робототехнические системы, как правило, описываются нелинейными функциями движения и наблюдения [Course 04, Course 05]:
\[
\mathbf{x}_t = g(\mathbf{u}_t, \mathbf{x}_{t-1}) + \bm{\epsilon}_t
\]
\[
\mathbf{z}_t = h(\mathbf{x}_t) + \bm{\delta}_t
\]

Для работы с такими системами используется расширенный фильтр Калмана (EKF), который выполняет локальную линеаризацию нелинейных функций с помощью разложения в ряд Тейлора первого порядка [Course 04].

\subsection{Линеаризация}

Для модели движения:
\[
g(\mathbf{u}_t, \mathbf{x}_{t-1}) \approx g(\mathbf{u}_t, \bm{\mu}_{t-1}) + \mathbf{G}_t (\mathbf{x}_{t-1} - \bm{\mu}_{t-1})
\]

Для модели наблюдения:
\[
h(\mathbf{x}_t) \approx h(\bar{\bm{\mu}}_t) + \mathbf{H}_t (\mathbf{x}_t - \bar{\bm{\mu}}_t)
\]
где $\mathbf{G}_t$ и $\mathbf{H}_t$ — матрицы Якоби, вычисленные в точке линеаризации.

\subsection{Алгоритм EKF [Course 04]}

\begin{verbatim}
1: Extended_Kalman_filter(μ_{t-1}, Σ_{t-1}, u_t, z_t)
2:   μ̄_t = g(u_t, μ_{t-1})
3:   Σ̄_t = G_t Σ_{t-1} G_t^T + R_t
4:   K_t = Σ̄_t H_t^T (H_t Σ̄_t H_t^T + Q_t)^{-1}
5:   μ_t = μ̄_t + K_t (z_t - h(μ̄_t))
6:   Σ_t = (I - K_t H_t) Σ̄_t
7:   return μ_t, Σ_t
\end{verbatim}

\subsection{Достоинства EKF}

\begin{itemize}
\item Первое практическое решение проблемы SLAM
\item Доказательство сходимости для линейного гауссовского случая
\item Эффективен для среднеразмерных сцен
\end{itemize}

\subsection{Недостатки EKF [Course 05]}

\begin{itemize}
\item Может расходиться при больших нелинейностях
\item Работает только с одномодальными распределениями
\item Квадратичная сложность $O(n^2)$ по числу ориентиров $n$
\item Требует вычисления якобианов
\end{itemize}

\section{Применение EKF в SLAM (EKF SLAM)}

EKF SLAM является одним из первых и наиболее известных решений задачи одновременной локализации и построения карты [Course 05].

\subsection{Постановка задачи SLAM}

\textbf{Дано:}
\begin{itemize}
\item Управляющие воздействия $\mathbf{u}_{1:T} = \{\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_T\}$
\item Наблюдения $\mathbf{z}_{1:T} = \{\mathbf{z}_1, \mathbf{z}_2, \ldots, \mathbf{z}_T\}$
\end{itemize}

\textbf{Требуется найти:}
\begin{itemize}
\item Карту среды $m$
\item Траекторию робота $\mathbf{x}_{0:T} = \{\mathbf{x}_0, \mathbf{x}_1, \ldots, \mathbf{x}_T\}$
\end{itemize}

\subsection{Представление состояния в EKF SLAM [Course 05]}

Состояние системы включает положение робота и координаты всех ориентиров:
\[
\bm{\mu}_t = \begin{pmatrix}
\mu_{t,x} \\
\mu_{t,y} \\
\mu_{t,\theta} \\
\mu_{1,x} \\
\mu_{1,y} \\
\vdots \\
\mu_{n,x} \\
\mu_{n,y}
\end{pmatrix}, \qquad
\bm{\Sigma}_t = \begin{pmatrix}
\Sigma_{rr} & \Sigma_{r1} & \cdots & \Sigma_{rn} \\
\Sigma_{1r} & \Sigma_{11} & \cdots & \Sigma_{1n} \\
\vdots & \vdots & \ddots & \vdots \\
\Sigma_{nr} & \Sigma_{n1} & \cdots & \Sigma_{nn}
\end{pmatrix}
\]

Размерность пространства состояний составляет $2N + 3$, где $N$ — количество ориентиров.

\subsection{Модель наблюдения дальность-угол (Range-Bearing)}
\[
\hat{\mathbf{z}}_t^i = \begin{pmatrix}
\sqrt{q} \\
\operatorname{atan2}(\delta_y, \delta_x) - \mu_{t,\theta}
\end{pmatrix}
\]
где $\delta_x = \mu_{j,x} - \mu_{t,x}$, $\delta_y = \mu_{j,y} - \mu_{t,y}$, $q = \delta_x^2 + \delta_y^2$.

\subsection{Замыкание цикла (Loop Closing) [Course 05]}

Важнейшей особенностью EKF SLAM является возможность замыкания цикла — распознавания уже посещённых участков карты. При успешном замыкании цикла неопределённость в оценках положения робота и ориентиров существенно уменьшается.

\textbf{Важно:} Ошибочное замыкание цикла может привести к расходимости фильтра.

\subsection{Корреляции в EKF SLAM [Course 05]}

В пределе оценки ориентиров становятся полностью коррелированными. Корреляция между положением робота и ориентирами не может игнорироваться — предположение о независимости приводит к слишком оптимистичным оценкам неопределённости.

\subsection{Сложность EKF SLAM}

\begin{table}[h]
\centering
\begin{tabular}{ll}
\toprule
\textbf{Характеристика} & \textbf{Значение} \\
\midrule
Временная сложность & $O(n^2)$ на шаг \\
Память & $O(n^2)$ \\
Основной фактор & Количество ориентиров $n$ \\
\bottomrule
\end{tabular}
\end{table}

Для больших карт EKF становится вычислительно нереализуемым, что привело к разработке методов аппроксимации (субкарты, разреженные методы).

\section{Сигма-точечный фильтр Калмана (Unscented Kalman Filter – UKF)}

Альтернативой линеаризации через разложение Тейлора является сигма-точечное преобразование (Unscented Transform), используемое в UKF [Course 06].

\subsection{Принцип сигма-точечного преобразования [Course 06]}

\begin{enumerate}
\item Выбирается набор сигма-точек ($\bm{\chi}^{[i]}$) с весами ($w^{[i]}$)
\item Каждая точка преобразуется через нелинейную функцию
\item Из преобразованных точек восстанавливается гауссовское распределение
\end{enumerate}

\subsection{Выбор сигма-точек [Course 06]}

\[
\mathbf{X}^{[0]} = \bm{\mu}
\]
\[
\mathbf{X}^{[i]} = \bm{\mu} + \left( \sqrt{(n + \lambda) \bm{\Sigma}} \right)_i \quad \text{для } i = 1, \ldots, n
\]
\[
\mathbf{X}^{[i]} = \bm{\mu} - \left( \sqrt{(n + \lambda) \bm{\Sigma}} \right)_{i-n} \quad \text{для } i = n+1, \ldots, 2n
\]

\subsection{Веса сигма-точек}

\[
w_m^{[0]} = \frac{\lambda}{n + \lambda}
\]
\[
w_c^{[0]} = w_m^{[0]} + (1 - \alpha^2 + \beta)
\]
\[
w_m^{[i]} = w_c^{[i]} = \frac{1}{2(n + \lambda)} \quad \text{для } i = 1, \ldots, 2n
\]

\subsection{Преимущества UKF перед EKF [Course 06]}

\begin{table}[h]
\centering
\begin{tabular}{lcc}
\toprule
\textbf{Характеристика} & \textbf{EKF} & \textbf{UKF} \\
\midrule
Точность аппроксимации & 1-й порядок & 2-й порядок и выше \\
Необходимость вычисления якобианов & Да & Нет \\
Работа с сильной нелинейностью & Плохо & Хорошо \\
Вычислительная сложность & Ниже & Незначительно выше \\
\bottomrule
\end{tabular}
\end{table}

\subsection{Сравнение EKF и UKF [Course 06]}

\begin{itemize}
\item Для линейных моделей дают одинаковые результаты
\item Для нелинейных моделей UKF даёт лучшее приближение
\item Различия часто «относительно небольшие»
\item UKF не требует вычисления якобианов
\item UKF всё ещё ограничен гауссовскими распределениями
\end{itemize}

\section{Информационный фильтр (Extended Information Filter – EIF)}

Наряду с моментальным представлением гауссовских распределений (математическое ожидание $\bm{\mu}$ и ковариация $\bm{\Sigma}$) существует каноническое представление через информационную матрицу $\bm{\Omega}$ и информационный вектор $\bm{\xi}$ [Course 07].

\subsection{Каноническое представление [Course 07]}

\[
\bm{\Omega} = \bm{\Sigma}^{-1}, \qquad \bm{\xi} = \bm{\Sigma}^{-1} \bm{\mu}
\]

\subsection{Сравнение сложности операций [Course 07]}

\begin{table}[h]
\centering
\begin{tabular}{lcc}
\toprule
\textbf{Операция} & \textbf{Моментальное представление (KF)} & \textbf{Каноническое представление (IF)} \\
\midrule
Предсказание (Prediction) & Быстрое & Медленное \\
Коррекция (Correction) & Медленное & Быстрое \\
\bottomrule
\end{tabular}
\end{table}

\subsection{Алгоритм расширенного информационного фильтра (EIF) [Course 07]}

\begin{verbatim}
1: Extended_information_filter(ξ_{t-1}, Ω_{t-1}, u_t, z_t)
2:   μ_{t-1} = Ω_{t-1}^{-1} ξ_{t-1}
3:   Ω̄_t = (G_t Ω_{t-1}^{-1} G_t^T + R_t)^{-1}
4:   μ̄_t = g(u_t, μ_{t-1})
5:   ξ̄_t = Ω̄_t μ̄_t
6:   Ω_t = Ω̄_t + H_t^T Q_t^{-1} H_t
7:   ξ_t = ξ̄_t + H_t^T Q_t^{-1} (z_t - h(μ̄_t) + H_t μ̄_t)
8:   return ξ_t, Ω_t
\end{verbatim}

\subsection{Вывод [Course 07]}

EIF — это EKF в информационной форме. Выбор между KF и IF определяется конкретным применением:
\begin{itemize}
\item KF: эффективное предсказание, медленная коррекция
\item IF: медленное предсказание, эффективная коррекция
\end{itemize}
На практике EKF более популярен, чем EIF.

\section{Сравнительный анализ методов фильтрации}

\begin{table}[h]
\centering
\begin{tabular}{lcccc}
\toprule
\textbf{Метод} & \textbf{Линеаризация} & \textbf{Вычисление якобианов} & \textbf{Точность} & \textbf{Сложность} \\
\midrule
KF & Не требуется (линейный) & Нет & Оптимальная (для линейных) & $O(k^{2.4})$ \\
EKF & Тейлор 1-го порядка & Да & Хорошая (умеренные нелинейности) & $O(n^2)$ \\
UKF & Сигма-точки & Нет & Лучшая (сильные нелинейности) & Незначительно выше EKF \\
EIF & Тейлор 1-го порядка & Да & Как у EKF & $O(n^2)$ \\
\bottomrule
\end{tabular}
\end{table}

\section{Практическая реализация SLAM на примере Hector SLAM}

Теоретические методы фильтрации, рассмотренные выше, находят непосредственное применение в реальных SLAM-системах. Одним из популярных opensource-решений является Hector SLAM — пакет для ROS (Robot Operating System), предназначенный для 2D SLAM, который способен строить карту без использования одометрии робота. Это делает его идеальным для платформ, где нет колёсных энкодеров (например, дроны, роботы на гусеницах или ручной перенос LiDAR). В данном разделе описывается практическая интеграция LiDAR (RPLIDAR A1) с Hector SLAM в среде ROS Noetic.

\subsection{Установка необходимых пакетов}

\textbf{Шаг 1: Установка ROS Noetic} \\
Установка выполняется по официальной инструкции.

\textbf{Шаг 2: Установка драйвера RPLIDAR}
\begin{verbatim}
cd ~/catkin_ws/src
git clone https://github.com/Slamtec/rplidar_ros.git
cd ~/catkin_ws
catkin_make
source devel/setup.bash
\end{verbatim}

\textbf{Шаг 3: Установка Hector SLAM}
\begin{verbatim}
sudo apt-get install ros-noetic-hector-slam
\end{verbatim}

\textbf{Шаг 4: Установка Map Server (для сохранения карт)}
\begin{verbatim}
sudo apt-get install ros-noetic-map-server
\end{verbatim}

\textbf{Шаг 5: Проверка установки}
\begin{verbatim}
rospack list | grep -E "rplidar_ros|hector"
\end{verbatim}

\subsection{Система координат и TF (Transform Library)}

В ROS каждый сенсор и часть робота имеют свою систему координат (frame). Для корректной работы SLAM необходимо связать эти системы между собой.

\textbf{Используемые фреймы}
\begin{table}[h]
\centering
\begin{tabular}{ll}
\toprule
\textbf{Фрейм} & \textbf{Назначение} \\
\midrule
map & Глобальная неподвижная система координат (мир) \\
laser & Система координат лазерного дальномера \\
\bottomrule
\end{tabular}
\end{table}

\textbf{Цепочка фреймов}
\begin{verbatim}
map ──────→ laser
  │            │
  │            └─ положение LiDAR
  └─ мировая система отсчёта (неподвижна)
\end{verbatim}

\textbf{Статическое преобразование (Static Transform)}
\begin{verbatim}
rosrun tf static_transform_publisher 0 0 0 0 0 0 map laser 100
\end{verbatim}
Эта команда сообщает ROS, что фрейм laser находится в точности в том же месте и ориентации, что и фрейм map.

\subsection{Параметры Hector SLAM}

В таблицах ниже приведены основные параметры узла \texttt{hector\_mapping}, их значения по умолчанию и выбранные в данной работе.

\textbf{Параметры фреймов}
\begin{table}[h]
\centering
\begin{tabular}{llll}
\toprule
\textbf{Параметр} & \textbf{По умолчанию} & \textbf{Наше значение} & \textbf{Причина} \\
\midrule
\_map\_frame & map\_link & map & Глобальный фрейм карты \\
\_base\_frame & base\_link & laser & Лидар выступает центром робота \\
\_odom\_frame & odom & laser & Нет колёсной одометрии \\
\bottomrule
\end{tabular}
\end{table}

\textbf{Параметры построения карты}
\begin{table}[h]
\centering
\begin{tabular}{llll}
\toprule
\textbf{Параметр} & \textbf{По умолчанию} & \textbf{Наше значение} & \textbf{Причина} \\
\midrule
\_map\_resolution & 0.025 & 0.05 & 5 см на пиксель – хороший баланс \\
\_map\_size & 1024 & 2048 & Карта 102×102 метра \\
\bottomrule
\end{tabular}
\end{table}

\textbf{Пороги обновления (критически важны!)}
\begin{table}[h]
\centering
\begin{tabular}{llll}
\toprule
\textbf{Параметр} & \textbf{По умолчанию} & \textbf{Наше значение} & \textbf{Зачем изменять?} \\
\midrule
\_map\_update\_distance\_thresh & 0.4 м & 0.05 м & Обновлять карту после смещения всего на 5 см \\
\_map\_update\_angle\_thresh & 0.9 рад (51°) & 0.05 рад (3°) & Обновлять карту после малого поворота \\
\bottomrule
\end{tabular}
\end{table}

⚠️ \textbf{Почему карта не обновлялась?} Значения по умолчанию слишком велики для ручного перемещения лидара. Их уменьшение делает отклик системы очень чувствительным даже к малым движениям.

\textbf{Фильтрация данных лазера}
\begin{table}[h]
\centering
\begin{tabular}{llll}
\toprule
\textbf{Параметр} & \textbf{По умолчанию} & \textbf{Наше значение} & \textbf{Причина} \\
\midrule
\_laser\_min\_dist & 0.4 м & 0.4 м & Игнорировать объекты ближе 40 см \\
\_laser\_max\_dist & 30.0 м & 5.0 м & RPLIDAR A1 имеет максимальную дальность 6 м \\
\_scan\_topic & /scan & /scan & Стандартное имя топика лазера \\
\bottomrule
\end{tabular}
\end{table}

\subsection{Запуск системы (5 терминалов)}

\textbf{Предварительное действие (один раз после подключения лидара)}
\begin{verbatim}
sudo chmod 666 /dev/ttyUSB0
\end{verbatim}

\textbf{Терминал 1: ROS Core (мастер)}
\begin{verbatim}
roscore
\end{verbatim}
Не закрывать! Это основа ROS.

\textbf{Терминал 2: Драйвер RPLIDAR}
\begin{verbatim}
rosrun rplidar_ros rplidarNode \
    _serial_port:=/dev/ttyUSB0 \
    _serial_baudrate:=115200 \
    _frame_id:=laser \
    _inverted:=false \
    _angle_compensate:=true
\end{verbatim}
Краткое описание параметров драйвера:
\begin{table}[h]
\centering
\begin{tabular}{lll}
\toprule
\textbf{Параметр} & \textbf{Действие} & \textbf{Наше значение} \\
\midrule
frame\_id & Имя системы координат лидара & laser \\
inverted & Нормальное или обратное направление сканирования & false (нормальное) \\
angle\_compensate & Заполнение пропусков в данных & true (сглаживание) \\
\bottomrule
\end{tabular}
\end{table}

\textbf{Терминал 3: Статическое TF-преобразование}
\begin{verbatim}
rosrun tf static_transform_publisher 0 0 0 0 0 0 map laser 100
\end{verbatim}
Не закрывать! Нормально, если нет вывода.

\textbf{Терминал 4: Узел Hector SLAM}
\begin{verbatim}
rosrun hector_mapping hector_mapping \
    _map_frame:=map \
    _base_frame:=laser \
    _odom_frame:=laser \
    _scan_topic:=/scan \
    _map_resolution:=0.05 \
    _map_size:=2048 \
    _map_update_distance_thresh:=0.05 \
    _map_update_angle_thresh:=0.05 \
    _laser_max_dist:=5.0
\end{verbatim}
Не закрывать! Строит карту по данным лидара.

\textbf{Терминал 5: Визуализация RViz}
\begin{verbatim}
rviz
\end{verbatim}

\subsection{Настройка RViz (критически важно!)}

После открытия RViz выполните действия строго по порядку:
\begin{enumerate}
\item Установите фиксированный фрейм: \textbf{Global Options → Fixed Frame} → введите \texttt{map} → Enter.
\item Добавьте отображение лазерных сканов: кнопка \textbf{Add} → вкладка \textbf{By topic} → найдите \texttt{/scan} → выберите \texttt{LaserScan} → OK.
\item Добавьте отображение карты: кнопка \textbf{Add} → вкладка \textbf{By topic} → найдите \texttt{/map} → выберите \texttt{Map} → OK.
\item Настройте вид:
  \begin{itemize}
  \item Масштабирование – колёсико мыши
  \item Панорамирование – перетаскивание правой кнопкой
  \item Вращение – перетаскивание левой кнопкой
  \end{itemize}
\end{enumerate}

\subsection{Сохранение построенной карты}

Когда карта готова, в новом терминале выполните:
\begin{verbatim}
source /opt/ros/noetic/setup.bash
rosrun map_server map_saver -f ~/my_map
\end{verbatim}
Будут созданы два файла:
\begin{itemize}
\item \texttt{my\_map.pgm} – изображение карты (можно открыть любым просмотрщиком)
\item \texttt{my\_map.yaml} – конфигурационный файл карты
\end{itemize}

\subsection{Краткая сводка по терминалам}

\begin{table}[h]
\centering
\begin{tabular}{cll}
\toprule
\textbf{Терминал} & \textbf{Команда} & \textbf{Назначение} \\
\midrule
1 & \texttt{roscore} & ROS мастер \\
2 & \texttt{rplidarNode} & Чтение данных с лидара \\
3 & \texttt{static\_transform\_publisher} & Связь фреймов map→laser \\
4 & \texttt{hector\_mapping} & Построение карты \\
5 & \texttt{rviz} & Визуализация \\
\bottomrule
\end{tabular}
\end{table}

\subsection{Диагностика и типичные проблемы}

\begin{table}[h]
\centering
\begin{tabular}{ll}
\toprule
\textbf{Проблема} & \textbf{Решение} \\
\midrule
Permission denied на /dev/ttyUSB0 & \texttt{sudo chmod 666 /dev/ttyUSB0} \\
Карта не обновляется & Уменьшить \texttt{map\_update\_distance\_thresh} и \texttt{map\_update\_angle\_thresh} \\
Нет лазерных лучей в RViz & Проверить Fixed Frame = map \\
Hector SLAM не найден & Выполнить \texttt{source /opt/ros/noetic/setup.bash} \\
Карта пустая (все серая) & Физически перемещать лидар! \\
"Failed to contact master" & Не запущен roscore (Терминал 1) \\
\bottomrule
\end{tabular}
\end{table}

\textbf{Как проверить работоспособность}
\begin{verbatim}
# Частота публикации сканов (должна быть 5–10 Гц)
rostopic hz /scan

# Частота публикации карты (0.5–1 Гц)
rostopic hz /map

# Список активных узлов
rosnode list                     # Должен содержать /hector_mapping и /rplidar_node

# Визуализация дерева фреймов
rosrun tf view_frames
evince frames.pdf                # Должна быть связь map → laser
\end{verbatim}

В RViz вы должны увидеть:
\begin{itemize}
\item[✅] Серую сетку (фрейм map)
\item[✅] Красные точки (лазерные измерения)
\item[✅] Чёрно-белые квадраты (строящаяся карта)
\end{itemize}

\subsection{Ключевые выводы по практической реализации}

\begin{itemize}
\item Карта обновляется только при движении LiDAR – необходимо перемещать датчик или робота.
\item Уменьшение порогов (\texttt{map\_update\_distance\_thresh}, \texttt{map\_update\_angle\_thresh}) делает систему чувствительной к малым перемещениям.
\item Имена фреймов должны строго совпадать – в драйвере \texttt{\_frame\_id:=laser}, в TF \texttt{map laser}, в Hector \texttt{\_base\_frame:=laser}.
\item Без статического TF ROS не сможет понять, где находится лидар относительно карты.
\end{itemize}

\end{document}
