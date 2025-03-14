# **Assignment Summary: Neural Network-Based Checkered Grid Evaluation System**  

## **Objective**  

To design a **perceptron-based system** that evaluates a **2×2 black-and-white checkered grid** and determines whether the grid is **bright or dark** based on a **heuristic evaluation function**. The system should be **adaptable**, allowing modification of evaluation rules.

---

## **1. Problem Definition**

- The system will analyze a **2×2 grid**, where each square is either **black (1)** or **white (0)**.  
- The **heuristic evaluation** rule determines brightness based on the number of black boxes.  

### **Initial Heuristic**

✔ **Bright** → 0 or 1 black squares.  
✔ **Dark** → 2, 3, or 4 black squares.  

### **Adaptability Requirement**

- The system should allow **dynamic changes** to the evaluation rule, e.g.,  
  - "2 black squares still count as bright."  
  - "At least 3 white squares define brightness."

---

## **2. Neural Network Model: Perceptron Approach**  

### **Inputs**

- A **4-input perceptron** representing each grid cell as **\( x_1, x_2, x_3, x_4 \)**.  
- Each input **\( x_i \) is 1 for black and 0 for white**.

### **Weights and Bias**

- The perceptron will **learn** an optimal weight vector \( W = [w_1, w_2, w_3, w_4] \).  
- A **bias term** \( b \) ensures flexibility in classification.

### **Activation Function**

- A **step function** determines if the grid is **bright or dark**.  

\[
f(z) =
\begin{cases}
\text{Bright (1)}, & \text{if } z < \theta \\
\text{Dark (0)}, & \text{if } z \geq \theta
\end{cases}
\]
where  
\[
z = w_1x_1 + w_2x_2 + w_3x_3 + w_4x_4 + b
\]

- \( \theta \) (threshold) **can be adjusted** to modify brightness rules.

---

## **3. Training Process**  

### **Dataset Creation (Supervised Learning)**

- Generate **all possible 2×2 grid patterns** (16 combinations).  
- Label each combination as **bright (1) or dark (0)** based on the heuristic.  

### **Perceptron Learning Algorithm**

1. **Initialize weights** and bias randomly.  
2. **Compute weighted sum** \( z \).  
3. **Apply step activation function**.  
4. **Compare output with actual label**.  
5. **Update weights using perceptron rule**:  
   \[
   w_i = w_i + \eta (y_{\text{true}} - y_{\text{predicted}}) x_i
   \]
6. **Repeat until convergence**.

---

## **4. Adaptability Mechanism**

- Introduce **dynamic thresholding** to tweak classification rules.  
- Use a **tunable weight adjustment function** instead of fixed perceptron logic.  
- Allow **user-defined rules** (e.g., via UI or config file).

---

## **5. Implementation Considerations**

✔ **Programming Language**: Python (NumPy, TensorFlow/PyTorch for neural implementation).  
✔ **Visualization**: Matplotlib to display grid evaluations.  
✔ **Future Expansion**: Extend to larger grids (e.g., 3×3, 4×4).  

---

### **Conclusion**

The system will classify a **2×2 checkered grid** as **bright or dark** based on a **perceptron** model. It will be **adaptable**, allowing changes to brightness rules via threshold tuning and weight adjustments.
