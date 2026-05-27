
# 🎯 GUI Interface for Trajectory Planning of a 5-DOF Mechanism

---

## 📋 General Information

### 🔍 What is this program?

This is a **Graphical User Interface (GUI)** for planning trajectories of a robotic mechanism with **5 degrees of freedom (DOF)**. The program allows users to define multiple waypoints (coordinate systems) that the mechanism should follow.

### 💡 Why do we need this interface?

| Feature | Benefit |
|---------|---------|
| **User-friendly input** | Instead of writing code or editing text files manually |
| **Visual organization** | All trajectory parameters are organized in clear sections |
| **Error prevention** | Validates inputs before saving |
| **Flexibility** | Supports two different input modes |

---

## 🔧 How the Program Works

### 📊 Overall Algorithm

```
┌─────────────────────────────────────────────────────────────────┐
│                     PROGRAM FLOW                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. USER SELECTS INPUT MODE                                      │
│     ├── Cartesian Mode (X, Y, Z, Alpha, Beta, Gamma)            │
│     └── Generalized Mode (Q1, Q2, Q3, Q4, Q5)                   │
│                         ↓                                         │
│  2. USER ENTERS NUMBER OF POINTS (N)                             │
│     Example: N = 3 means 3 waypoints                            │
│                         ↓                                         │
│  3. USER CLICKS "Создать поля"                                   │
│     → Program dynamically creates N rows of input fields        │
│                         ↓                                         │
│  4. USER FILLS COORDINATES FOR EACH POINT                        │
│     Point 1: X₁, Y₁, Z₁, α₁, β₁, γ₁                             │
│     Point 2: X₂, Y₂, Z₂, α₂, β₂, γ₂                             │
│     Point 3: X₃, Y₃, Z₃, α₃, β₃, γ₃                             │
│                         ↓                                         │
│  5. USER CLICKS "Сохранить все точки"                            │
│     → Program saves all data to a text file                      │
│                         ↓                                         │
│  6. MATLAB READS THE FILE                                        │
│     → Calculates trajectory (dynamics, velocities, etc.)        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 Two Input Modes Explained

### Mode 1: Cartesian Coordinates

```
┌─────────────────────────────────────────────────────────────────┐
│                    CARTESIAN MODE                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   INPUT: X, Y, Z, Alpha, Beta, Gamma                           │
│                                                                  │
│   PURPOSE:                                                       │
│   • X, Y, Z     = Position of the end effector (tool tip)      │
│   • Alpha, Beta, Gamma = Orientation (rotation angles)         │
│                                                                  │
│   WHEN TO USE:                                                   │
│   When you know WHERE you want the tool to be in space          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Mode 2: Generalized Coordinates (Q1-Q5)

```
┌─────────────────────────────────────────────────────────────────┐
│                   GENERALIZED MODE                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   INPUT: Q1, Q2, Q3, Q4, Q5                                    │
│                                                                  │
│   PURPOSE:                                                       │
│   • These are JOINT ANGLES or actuator positions               │
│   • 5 values because mechanism has 5 motors                    │
│                                                                  │
│   WHEN TO USE:                                                   │
│   When you know exactly how each joint should be positioned     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🗂️ File Output Format

### Cartesian Mode Output (`coordinates.txt`)

```csv
Point,X,Y,Z,Alpha,Beta,Gamma,Time
1,10,10,5,0,0,0,2
2,20,15,8,10,5,0,2
3,30,20,10,20,10,0,2
```

### Generalized Mode Output (`generalized_coordinates.txt`)

```csv
Point,Q1,Q2,Q3,Q4,Q5,Time
1,15,25,30,10,5,2
2,30,40,45,20,15,2
3,45,55,60,30,25,2
```

---

## 📐 Visual Layout of the GUI

```
┌─────────────────────────────────────────────────────────────────────┐
│  Параметры траектории                                                │
├─────────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │ ТИП ВВОДА                                                    │    │
│  │ ○ Декартовы координаты    ○ Обобщенные координаты (Q1-Q5)   │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │ КОЛИЧЕСТВО КООРДИНАТНЫХ СИСТЕМ                               │    │
│  │ Количество точек (N): [___]  [Создать поля]                  │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │ КООРДИНАТНЫЕ СИСТЕМЫ (точки траектории)                      │    │
│  │ ┌────────┬─────┬─────┬─────┬───────┬──────┬───────┐          │    │
│  │ │ Точка  │ X   │ Y   │ Z   │ Alpha │ Beta │ Gamma │          │    │
│  │ ├────────┼─────┼─────┼─────┼───────┼──────┼───────┤          │    │
│  │ │Система1│[__] │[__] │[__] │ [__]  │ [__] │ [__]  │          │    │
│  │ │Система2│[__] │[__] │[__] │ [__]  │ [__] │ [__]  │          │    │
│  │ │Система3│[__] │[__] │[__] │ [__]  │ [__] │ [__]  │          │    │
│  │ └────────┴─────┴─────┴─────┴───────┴──────┴───────┘          │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │ ПАРАМЕТРЫ ВРЕМЕНИ                                             │    │
│  │ Время между точками (с): [___]                                │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │ [СОХРАНИТЬ ВСЕ ТОЧКИ]                                         │    │
│  └─────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 💻 Complete Code

<details>
<summary><b>📁 Click to expand: trajectory_gui.py (Full Code)</b></summary>

```python
import tkinter as tk
from tkinter import ttk
import os

class TrajectoryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Параметры траектории")
        self.root.geometry("1100x750")
        
        # Store all point entries for BOTH modes
        self.points_data_cartesian = []
        self.points_data_generalized = []
        
        # === SECTION 1: Mode Selection ===
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
        
        # === SECTION 2: Number of Points ===
        n_points_frame = ttk.LabelFrame(root, text="Количество координатных систем")
        n_points_frame.pack(padx=10, pady=10, fill="x")
        
        ttk.Label(n_points_frame, text="Количество точек (N):").pack(side=tk.LEFT, padx=5, pady=5)
        self.n_points_entry = ttk.Entry(n_points_frame, width=10)
        self.n_points_entry.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.generate_btn = ttk.Button(n_points_frame, text="Создать поля", command=self.generate_fields)
        self.generate_btn.pack(side=tk.LEFT, padx=10, pady=5)
        
        # === SECTION 3: Dynamic Points Frame ===
        self.points_frame = ttk.LabelFrame(root, text="Координатные системы (точки траектории)")
        self.points_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        # === SECTION 4: Time Settings ===
        time_frame = ttk.LabelFrame(root, text="Параметры времени")
        time_frame.pack(padx=10, pady=10, fill="x")
        
        ttk.Label(time_frame, text="Время между точками (с):").grid(row=0, column=0, padx=5, pady=5)
        self.time_entry = ttk.Entry(time_frame, width=10)
        self.time_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # === SECTION 5: Save Button ===
        self.save_btn = ttk.Button(root, text="Сохранить все точки", command=self.save_all_points)
        self.save_btn.pack(padx=10, pady=10)
        
        # Initial state
        self.save_btn.config(state='disabled')
        self.current_mode = "coordinates"
    
    def switch_mode(self):
        """Switch between Cartesian and Generalized modes"""
        self.current_mode = self.input_mode.get()
        if hasattr(self, 'n_points_entry') and self.n_points_entry.get():
            self.generate_fields()
    
    def generate_fields(self):
        """Create input fields for each point based on selected mode"""
        
        for widget in self.points_frame.winfo_children():
            widget.destroy()
        
        self.points_data_cartesian = []
        self.points_data_generalized = []
        
        try:
            n = int(self.n_points_entry.get())
        except ValueError:
            n = 0
        
        if n <= 0:
            return
        
        if self.current_mode == "coordinates":
            headers = ["Точка", "X", "Y", "Z", "Alpha", "Beta", "Gamma"]
        else:
            headers = ["Точка", "Q1", "Q2", "Q3", "Q4", "Q5"]
        
        for col, header in enumerate(headers):
            ttk.Label(self.points_frame, text=header, font=('Arial', 10, 'bold')).grid(
                row=0, column=col, padx=5, pady=10)
        
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
        """Save all coordinate systems to file based on mode"""
        
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


if __name__ == "__main__":
    root = tk.Tk()
    app = TrajectoryGUI(root)
    root.mainloop()
```

</details>

---

## 🚀 How to Run

```bash
# Save the code as trajectory_gui.py
# Then run:
python3 trajectory_gui.py
```

---

## 📝 Summary

| Feature | Description |
|---------|-------------|
| **Input Modes** | Cartesian (X,Y,Z,α,β,γ) OR Generalized (Q1-Q5) |
| **Multiple Points** | User defines N waypoints |
| **Dynamic Fields** | Fields created automatically based on N |
| **Time Parameter** | Time between consecutive points |
| **Output Format** | CSV text file for MATLAB |

---

## 🔄 System Integration

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   PYTHON    │───▶│    TEXT     │───▶│   MATLAB    │
│     GUI     │    │    FILE     │    │  TRAJECTORY │
└─────────────┘    └─────────────┘    └─────────────┘
```

This GUI serves as the **front-end interface** for your trajectory planning system, making it easy to input multiple waypoints that will later be processed by MATLAB for dynamics calculations and trajectory optimization.
```

## Improvements made:

| Element | What was added |
|---------|----------------|
| **Separators** | `---` between major sections |
| **ASCII boxes** | Clean borders for mode explanations |
| **Collapsible code** | `<details><summary>` tag for the full code |
| **Tables** | For features and summary |
| **Flow diagram** | ASCII flowchart at the end |
| **Better headings** | Emojis + bold text |
| **Code blocks** | With language specification (`python`, `csv`, `bash`) |

Just **copy and paste** this into your `README.md` – it will look professional and well-structured on GitHub! ✅
