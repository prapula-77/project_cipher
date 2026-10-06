# 🦎 Project Cipher: Multi-Mode AI Engine

## 📌 Project Overview

Project Cipher is a multi-mode AI application developed using Python and Streamlit. It demonstrates how a single AI language model can dynamically change its behavior based on different system protocols.

The application provides three different protocols:

* **Protocol Alpha – Reverse Mapping**
* **Protocol Beta – Forward Mapping**
* **Protocol Gamma – Temporal Simulation**

The project is designed to demonstrate dynamic prompt-based behavior in a local/cloud AI system.

---

## 🎯 Objectives

* To develop a multi-mode AI application using Python.
* To demonstrate forward and reverse cipher mapping.
* To demonstrate AI-based historical simulation.
* To understand how system prompts can control AI behavior.
* To create an interactive user interface using Streamlit.

---

## ⚙️ Technologies Used

* Python
* Streamlit
* Google Gemini API
* GitHub
* Large Language Model (LLM)

---

## 🔐 Protocol Alpha – Reverse Mapping

Protocol Alpha converts numerical values into alphabetic characters using the rule:

```text
A = 1
B = 2
C = 3
...
Z = 26
```

### Example

**Input:**

```text
8-5-12-12-15
```

**Output:**

```text
HELLO
```

---

## 🔢 Protocol Beta – Forward Mapping

Protocol Beta performs the reverse operation. It converts words into their corresponding alphabet numbers.

### Example

**Input:**

```text
HELLO
```

**Output:**

```text
8-5-12-12-15
```

Another example:

```text
PYTHON
```

Output:

```text
16-25-20-8-15-14
```

---

## ⏳ Protocol Gamma – Temporal Simulation

Protocol Gamma allows the user to enter a historical year and generates a response based on the historical context of that period.

### Example

**Input:**

```text
1947
```

**Output:**

```text
India has become independent from British rule, and people are celebrating this historic moment. There is great hope and uncertainty about the future.
```

This protocol demonstrates how an AI system can change its perspective based on a specific historical time period.

---

## 🏗️ System Architecture

```text
                USER
                  ↓
          Streamlit Interface
                  ↓
          Select System Protocol
                  ↓
       ┌──────────┼──────────┐
       ↓          ↓          ↓
    Alpha       Beta       Gamma
       ↓          ↓          ↓
   Number →     Word →    Historical
     Word       Number      Year
       └──────────┼──────────┘
                  ↓
             System Prompt
                  ↓
              AI Model
                  ↓
                Output
```

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd project-cipher
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Add the required API key

For deployment, configure the API key using Streamlit Secrets.

### 5. Run the application

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```text
project-cipher/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 💡 Key Feature

The main feature of Project Cipher is **dynamic AI behavior switching**.

Instead of creating separate applications for each task, the project uses different system prompts to make the same AI model perform different tasks.

---

## 🔮 Future Scope

* Add more cipher algorithms.
* Add encryption and decryption methods.
* Add more historical periods.
* Add voice input and output.
* Add multilingual support.
* Add additional AI protocols.
* Improve the user interface.
* Support additional AI models.

---

## 📌 Conclusion

Project Cipher demonstrates how a single AI application can perform multiple tasks by dynamically changing its system instructions. The project combines traditional cipher concepts with modern AI and interactive web development to create a flexible multi-mode AI engine.

---

## 👩‍💻 Author

**Prapula Regunta**

AI/ML Student
