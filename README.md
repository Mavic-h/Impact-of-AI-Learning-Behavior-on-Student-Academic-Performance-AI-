# Impact of AI Learning Behavior on Student Academic Performance  
### Methods used
**Category A**
- Facet Chart
- Linear Regression
- Logistic Regression
**Category B**
- Lasso Regression
### Business objective
This project examines how learning behavior and AI usage patterns are associated with student performance, identifies at-risk students, and extracts the most important variables for educational intervention.  
### Key patterns to discuss
1. Traditional learning factors such as attendance, concept understanding, and study consistency are expected to remain strong predictors of performance.  
2. AI usage itself may not be the main issue; dependency and substitution-oriented usage are more important.  
3. The at-risk model can support early-warning intervention for education managers.  
4. Lasso helps narrow managerial focus to a smaller set of high-impact indicators.  

# 📘 AI + Education: Does AI Improve Learning?

> **“AI won’t replace humans — but humans with AI will replace humans without AI.”**  
> — Harvard Business Review

---

## 📌 Project Overview

This project investigates a critical question:

> **Does AI usage actually improve student learning outcomes?**

With the rapid adoption of AI tools in education, students increasingly rely on AI for studying, coding, note-taking, and exam preparation. However, the effectiveness of such usage remains unclear.

This project uses **data-driven analysis and machine learning models** to explore:

- The relationship between AI usage and academic performance  
- The impact of different AI usage behaviors  
- Whether AI improves or harms learning outcomes  

---

## 🎯 Key Findings

### 🔹 1. AI Usage ≠ Better Performance  
- No significant difference in average scores between AI users and non-users  
- AI adoption is high, but performance improvement is inconsistent  

---

### 🔹 2. Learning Fundamentals Drive Success  
- Strong predictors:
  - `last_exam_score`  
  - `assignment_scores_avg`  
  - `concept_understanding_score`  

👉 Academic performance is primarily driven by **learning ability**, not AI usage  

---

### 🔹 3. AI Can Both Help and Harm  
- **Supportive usage** (e.g., learning, explanation) → positive  
- **Substitutive usage** (e.g., copying answers) → negative  

---

### 🔹 4. Over-Reliance on AI is Risky  
- High `ai_generated_content_percentage` →  
  - lower scores  
  - higher failure risk  

---

## 🔥 Core Insight

> **AI is not a substitute for learning — it is a multiplier of learning behavior**

---

## 📊 Dataset

- 📁 Source: Kaggle – *Student Performance & Academic Trends Dataset*  
- 📈 Size:
  - 8,000 rows  
  - 26 features  

### Key Variables

| Category | Features |
|----------|--------|
| AI Behavior | `ai_usage_time`, `ai_prompts_per_week`, `ai_generated_content_percentage` |
| Learning Behavior | `study_hours_per_day`, `study_consistency_index`, `attendance_percentage` |
| Performance | `final_score`, `passed`, `last_exam_score` |

---

## ⚙️ Methodology

### 1️⃣ Exploratory Data Analysis (EDA)
- Distribution analysis (scores, AI usage)
- Correlation heatmaps
- Outlier detection (boxplots)

---

### 2️⃣ Feature Engineering
- AI usage grouping (Low / Medium / High)
- AI usage style (Supportive / Substitutive / Mixed)

---

### 3️⃣ Modeling

#### 📌 Linear Regression
- Predict `final_score`

#### 📌 Logistic Regression
- Predict `passed` / `at_risk`

#### 📌 Lasso Regression
- Feature selection  
- Identify key drivers of performance  

---

### 4️⃣ Evaluation Metrics

- Accuracy  
- Precision / Recall / F1-score  
- ROC-AUC  

---

## 📈 Key Visualizations

- Correlation heatmap (learning vs AI variables)  
- Boxplots (AI usage vs performance)  
- Interaction heatmaps (usage style × performance)  
- Lasso feature importance  

---

## 🧠 Business Insights

### 🎓 For Universities
- Develop AI usage guidelines  
- Integrate AI into structured learning  
- Introduce AI literacy & ethics education  

---

### 👨‍🎓 For Students
- Shift from **passive usage → active learning**  
- Use AI for:
  - explanation  
  - practice  
  - feedback  

---

### 🏢 For EdTech

Inspired by this project:

**CogniPal.AI – AI-powered learning system**

- AI usage monitoring  
- Personalized learning recommendations  
- Behavior-driven tutoring  

---

## 🚀 Strategic Insight

> The future of education is not AI tools —  
> but AI-powered learning systems

---

---

## 🛠️ Tech Stack

- Python  
- Pandas / NumPy  
- Matplotlib / Seaborn  
- Scikit-learn  

---


