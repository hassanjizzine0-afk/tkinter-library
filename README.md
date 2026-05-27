# 🎯 **Графический интерфейс для планирования траектории 5-звенного механизма**

## 📋 **Общая информация**

### **Что это за программа?**
Это **графический пользовательский интерфейс (GUI)** для планирования траектории движения роботизированного механизма с **5 степенями свободы (СО)**. Программа позволяет пользователю задавать несколько опорных точек (координатных систем), через которые должен пройти механизм.

### **Зачем нужен этот интерфейс?**
- **Удобный ввод данных**: не нужно писать код или вручную редактировать текстовые файлы
- **Визуальная организация**: все параметры траектории собраны в понятные разделы
- **Защита от ошибок**: проверка ввода перед сохранением
- **Гибкость**: поддержка двух режимов ввода координат

---

## 🔧 **Как работает программа**

```
┌─────────────────────────────────────────────────────────────────┐
│                     АЛГОРИТМ РАБОТЫ                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. ПОЛЬЗОВАТЕЛЬ ВЫБИРАЕТ РЕЖИМ ВВОДА                            │
│     ├── Декартовы координаты (X, Y, Z, Alpha, Beta, Gamma)       │
│     └── Обобщенные координаты (Q1, Q2, Q3, Q4, Q5)               │
│                         ↓                                        │
│  2. ПОЛЬЗОВАТЕЛЬ ВВОДИТ КОЛИЧЕСТВО ТОЧЕК (N)                     │
│     Пример: N = 3 означает 3 опорные точки                       │
│                         ↓                                        │
│  3. ПОЛЬЗОВАТЕЛЬ НАЖИМАЕТ "Создать поля"                         │
│     → Программа автоматически создает N строк для ввода          │
│                         ↓                                        │
│  4. ПОЛЬЗОВАТЕЛЬ ЗАПОЛНЯЕТ КООРДИНАТЫ ДЛЯ КАЖДОЙ ТОЧКИ           │
│     Точка 1: X₁, Y₁, Z₁, α₁, β₁, γ₁                              │
│     Точка 2: X₂, Y₂, Z₂, α₂, β₂, γ₂                              │
│     Точка 3: X₃, Y₃, Z₃, α₃, β₃, γ₃                              │
│                         ↓                                        │
│  5. ПОЛЬЗОВАТЕЛЬ НАЖИМАЕТ "Сохранить все точки"                  │
│     → Программа сохраняет все данные в текстовый файл            │
│                         ↓                                        │ 
│  6. MATLAB ЧИТАЕТ ФАЙЛ                                           │
│     → Выполняет расчет траектории (динамика, скорости и т.д.)    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 **Два режима ввода**

### **Режим 1: Декартовы координаты**
```
Ввод: X, Y, Z, Alpha, Beta, Gamma

Назначение: 
- X, Y, Z = положение рабочего органа (конечная точка)
- Alpha, Beta, Gamma = ориентация (углы поворота)

Когда использовать:
Когда вы знаете, ГДЕ должен находиться инструмент в пространстве
```

### **Режим 2: Обобщенные координаты (Q1-Q5)**
```
Ввод: Q1, Q2, Q3, Q4, Q5

Назначение:
- Это УГЛЫ СОЕДИНЕНИЙ или положения приводов
- 5 значений, потому что механизм имеет 5 двигателей

Когда использовать:
Когда вы точно знаете, как должен быть расположен каждый сустав
```

---

## 🗂️ **Формат выходных файлов**

### **Вывод для декартового режима (coordinates.txt):**
```
Point,X,Y,Z,Alpha,Beta,Gamma,Time
1,10,10,5,0,0,0,2
2,20,15,8,10,5,0,2
3,30,20,10,20,10,0,2
```

### **Вывод для обобщенного режима (generalized_coordinates.txt):**
```
Point,Q1,Q2,Q3,Q4,Q5,Time
1,15,25,30,10,5,2
2,30,40,45,20,15,2
3,45,55,60,30,25,2
```

---

## 📐 **Внешний вид интерфейса**

```
┌─────────────────────────────────────────────────────────────────────┐
│  Параметры траектории                                                │
├─────────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │ ТИП ВВОДА                                                    │     │
│  │ ○ Декартовы координаты    ○ Обобщенные координаты (Q1-Q5)   │      │
│  └─────────────────────────────────────────────────────────────┘      │
│                                                                       │
│  ┌─────────────────────────────────────────────────────────────┐      │
│  │ КОЛИЧЕСТВО КООРДИНАТНЫХ СИСТЕМ                               │     │ 
│  │ Количество точек (N): [___]  [Создать поля]                  │     │
│  └─────────────────────────────────────────────────────────────┘      │
│                                                                       │ 
│  ┌─────────────────────────────────────────────────────────────┐      │ 
│  │ КООРДИНАТНЫЕ СИСТЕМЫ (точки траектории)                      │     │
│  │ ┌────────┬─────┬─────┬─────┬───────┬──────┬───────┐          │     │
│  │ │ Точка  │ X   │ Y   │ Z   │ Alpha │ Beta │ Gamma │          │     │
│  │ ├────────┼─────┼─────┼─────┼───────┼──────┼───────┤          │     │
│  │ │Система1│[__] │[__] │[__] │ [__]  │ [__] │ [__]  │          │     │
│  │ │Система2│[__] │[__] │[__] │ [__]  │ [__] │ [__]  │          │     │
│  │ │Система3│[__] │[__] │[__] │ [__]  │ [__] │ [__]  │          │     │
│  │ └────────┴─────┴─────┴─────┴───────┴──────┴───────┘          │     │
│  └─────────────────────────────────────────────────────────────┘      │
│                                                                       │
│  ┌─────────────────────────────────────────────────────────────┐      │
│  │ ПАРАМЕТРЫ ВРЕМЕНИ                                             │    │
│  │ Время между точками (с): [___]                                │    │
│  └─────────────────────────────────────────────────────────────┘      │
│                                                                       │
│  ┌─────────────────────────────────────────────────────────────┐      │
│  │ [СОХРАНИТЬ ВСЕ ТОЧКИ]                                         │    │
│  └─────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────┘
```

```python
import tkinter as tk
from tkinter import ttk
import os

class TrajectoryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Параметры траектории")
        self.root.geometry("1100x750")
        
        # Хранение данных для обоих режимов
        self.points_data_cartesian = []
        self.points_data_generalized = []
        
        # === РАЗДЕЛ 1: Выбор режима ===
        mode_frame = ttk.LabelFrame(root, text="Тип ввода")
        mode_frame.pack(padx=10, pady=10, fill="x")
        
        self.input_mode = tk.StringVar(value="coordinates")
        
        coordinates_radio = ttk.Radiobutton(mode_frame, text="Декартовы координаты", 
                                            variable=self.input_mode, value="coordinates", 
                                            command=self.switch_mode)
        coordinates_radio.pack(side=tk.LEFT, padx=10, pady=5)
        
        generalized_radio = ttk.Radiobutton(mode_frame, text="Обобщенные координаты (Q1-Q5)", 
                                            variable=self.input_mode, value="generalized", 
                                            command=self.switch_mode)
        generalized_radio.pack(side=tk.LEFT, padx=10, pady=5)
        
        # === РАЗДЕЛ 2: Количество точек ===
        n_points_frame = ttk.LabelFrame(root, text="Количество координатных систем")
        n_points_frame.pack(padx=10, pady=10, fill="x")
        
        ttk.Label(n_points_frame, text="Количество точек (N):").pack(side=tk.LEFT, padx=5, pady=5)
        self.n_points_entry = ttk.Entry(n_points_frame, width=10)
        self.n_points_entry.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.generate_btn = ttk.Button(n_points_frame, text="Создать поля", command=self.generate_fields)
        self.generate_btn.pack(side=tk.LEFT, padx=10, pady=5)
        
        # === РАЗДЕЛ 3: Динамические поля ===
        self.points_frame = ttk.LabelFrame(root, text="Координатные системы (точки траектории)")
        self.points_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        # === РАЗДЕЛ 4: Время ===
        time_frame = ttk.LabelFrame(root, text="Параметры времени")
        time_frame.pack(padx=10, pady=10, fill="x")
        
        ttk.Label(time_frame, text="Время между точками (с):").grid(row=0, column=0, padx=5, pady=5)
        self.time_entry = ttk.Entry(time_frame, width=10)
        self.time_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # === РАЗДЕЛ 5: Кнопка сохранения ===
        self.save_btn = ttk.Button(root, text="Сохранить все точки", command=self.save_all_points)
        self.save_btn.pack(padx=10, pady=10)
        
        # Начальное состояние
        self.save_btn.config(state='disabled')
        self.current_mode = "coordinates"
    
    def switch_mode(self):
        """Переключение между режимами"""
        self.current_mode = self.input_mode.get()
        if hasattr(self, 'n_points_entry') and self.n_points_entry.get():
            self.generate_fields()
    
    def generate_fields(self):
        """Создание полей для каждой точки"""
        
        # Очистка существующих полей
        for widget in self.points_frame.winfo_children():
            widget.destroy()
        
        self.points_data_cartesian = []
        self.points_data_generalized = []
        
        # Получение количества точек
        try:
            n = int(self.n_points_entry.get())
        except ValueError:
            n = 0
        
        if n <= 0:
            return
        
        # Заголовки в зависимости от режима
        if self.current_mode == "coordinates":
            headers = ["Точка", "X", "Y", "Z", "Alpha", "Beta", "Gamma"]
        else:
            headers = ["Точка", "Q1", "Q2", "Q3", "Q4", "Q5"]
        
        for col, header in enumerate(headers):
            ttk.Label(self.points_frame, text=header, font=('Arial', 10, 'bold')).grid(
                row=0, column=col, padx=5, pady=10)
        
        # Создание строк для каждой точки
        for i in range(n):
            if self.current_mode == "coordinates":
                point_entries = {}
                
                ttk.Label(self.points_frame, text=f"Система {i+1}:").grid(
                    row=i+1, column=0, padx=5, pady=5)
                
                entry_x = ttk.Entry(self.points_frame, width=10)
                entry_x.grid(row=i+1, column=1, padx=5, pady=5)
                point_entries['x'] = entry_x
                
                entry_y = ttk.Entry(self.points_frame, width=10)
                entry_y.grid(row=i+1, column=2, padx=5, pady=5)
                point_entries['y'] = entry_y
                
                entry_z = ttk.Entry(self.points_frame, width=10)
                entry_z.grid(row=i+1, column=3, padx=5, pady=5)
                point_entries['z'] = entry_z
                
                entry_alpha = ttk.Entry(self.points_frame, width=10)
                entry_alpha.grid(row=i+1, column=4, padx=5, pady=5)
                point_entries['alpha'] = entry_alpha
                
                entry_beta = ttk.Entry(self.points_frame, width=10)
                entry_beta.grid(row=i+1, column=5, padx=5, pady=5)
                point_entries['beta'] = entry_beta
                
                entry_gamma = ttk.Entry(self.points_frame, width=10)
                entry_gamma.grid(row=i+1, column=6, padx=5, pady=5)
                point_entries['gamma'] = entry_gamma
                
                self.points_data_cartesian.append(point_entries)
                
            else:
                point_entries = {}
                
                ttk.Label(self.points_frame, text=f"Система {i+1}:").grid(
                    row=i+1, column=0, padx=5, pady=5)
                
                entry_q1 = ttk.Entry(self.points_frame, width=10)
                entry_q1.grid(row=i+1, column=1, padx=5, pady=5)
                point_entries['q1'] = entry_q1
                
                entry_q2 = ttk.Entry(self.points_frame, width=10)
                entry_q2.grid(row=i+1, column=2, padx=5, pady=5)
                point_entries['q2'] = entry_q2
                
                entry_q3 = ttk.Entry(self.points_frame, width=10)
                entry_q3.grid(row=i+1, column=3, padx=5, pady=5)
                point_entries['q3'] = entry_q3
                
                entry_q4 = ttk.Entry(self.points_frame, width=10)
                entry_q4.grid(row=i+1, column=4, padx=5, pady=5)
                point_entries['q4'] = entry_q4
                
                entry_q5 = ttk.Entry(self.points_frame, width=10)
                entry_q5.grid(row=i+1, column=5, padx=5, pady=5)
                point_entries['q5'] = entry_q5
                
                self.points_data_generalized.append(point_entries)
        
        self.save_btn.config(state='normal')
        
        if self.current_mode == "coordinates":
            print(f"✅ Создано {n} координатных систем (Декартовы: X,Y,Z,Alpha,Beta,Gamma)")
        else:
            print(f"✅ Создано {n} координатных систем (Обобщенные: Q1,Q2,Q3,Q4,Q5)")
    
    def save_all_points(self):
        """Сохранение всех точек в файл"""
        
        time_between = self.time_entry.get() or "1"
        
        if self.current_mode == "coordinates":
            if not self.points_data_cartesian:
                print("❌ Нет точек для сохранения!")
                return
            
            with open('coordinates.txt', 'w') as f:
                f.write("Point,X,Y,Z,Alpha,Beta,Gamma,Time\n")
                
                for i, point in enumerate(self.points_data_cartesian):
                    x = point['x'].get() or "0"
                    y = point['y'].get() or "0"
                    z = point['z'].get() or "0"
                    alpha = point['alpha'].get() or "0"
                    beta = point['beta'].get() or "0"
                    gamma = point['gamma'].get() or "0"
                    
                    f.write(f"{i+1},{x},{y},{z},{alpha},{beta},{gamma},{time_between}\n")
            
            print(f"✅ Сохранено {len(self.points_data_cartesian)} координатных систем в coordinates.txt")
            
        else:
            if not self.points_data_generalized:
                print("❌ Нет точек для сохранения!")
                return
            
            with open('generalized_coordinates.txt', 'w') as f:
                f.write("Point,Q1,Q2,Q3,Q4,Q5,Time\n")
                
                for i, point in enumerate(self.points_data_generalized):
                    q1 = point['q1'].get() or "0"
                    q2 = point['q2'].get() or "0"
                    q3 = point['q3'].get() or "0"
                    q4 = point['q4'].get() or "0"
                    q5 = point['q5'].get() or "0"
                    
                    f.write(f"{i+1},{q1},{q2},{q3},{q4},{q5},{time_between}\n")
            
            print(f"✅ Сохранено {len(self.points_data_generalized)} координатных систем в generalized_coordinates.txt")
        
        print("\n📁 Содержимое файла:")
        if self.current_mode == "coordinates":
            with open('coordinates.txt', 'r') as f:
                print(f.read())
        else:
            with open('generalized_coordinates.txt', 'r') as f:
                print(f.read())


# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = TrajectoryGUI(root)
    root.mainloop()
```

---

## 🚀 **Как запустить**

```bash
# Сохраните код как trajectory_gui.py
# Затем выполните:
python3 trajectory_gui.py
```



![image_alt](https://github.com/hassanjizzine0-afk/tkinter-library/blob/main/image.png?raw=true)












---

## 📝 **Резюме**

| Функция | Описание |
|---------|----------|
| **Режимы ввода** | Декартовы (X,Y,Z,α,β,γ) ИЛИ Обобщенные (Q1-Q5) |
| **Несколько точек** | Пользователь задает N опорных точек |
| **Динамические поля** | Поля создаются автоматически в зависимости от N |
| **Время** | Время между последовательными точками |
| **Выходной формат** | CSV текстовый файл для MATLAB |

Этот графический интерфейс служит **интерфейсом переднего плана** для вашей системы планирования траектории, позволяя легко вводить множество опорных точек, которые затем будут обработаны MATLAB для расчета динамики и оптимизации траектории.
