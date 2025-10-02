# ⚡ Electricity Billing System (EBS)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/MySQL-8.0-orange?logo=mysql&logoColor=white" />
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-green?logo=plotly&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Working-brightgreen" />
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

> A **Console-based Electricity Billing System** made with `Python + MySQL`, featuring over 800 lines of code with ASCII printing, user login/signup, customer management, transaction handling, and bill visualization with graphs. Inspired by my dad's expertise, it uses several Python extensions for efficient billing management. While basic, it provides a solid foundation for backend development and database integration.


---

## 🌟 Features
- 👤 **User Authentication** – Signup, login, delete account  
- 🧾 **Customer Management** – Add, view, update, delete customer details  
- 💰 **Transaction System** – Create bills, apply fines, record payments  
- 📊 **Graphical Insights** (Matplotlib)
  - Bill trends over time  
  - Units vs Amount comparison  
  - Paid vs Unpaid pie chart  
- 💾 **Database Integration** with MySQL  

---

## 📂 Project Structure
- 📦 electricity-billing-system
  - ┣ 📜 electricity_billing.py # Main project file
  - ┣ 📜 requirements.txt # Dependencies
  - ┣ 📜 README.md # Project documentation
  - ┗ 📂 screenshots # Sample outputs / graph images


---

## ⚙️ Installation

### 1️⃣ Clone the Repo
bash
git clone https://github.com/<your-username>/electricity-billing-system.git
cd electricity-billing-system

---

### 2️⃣ Install Dependencies
pip install -r requirements.txt

### 3️⃣ Setup MySQL Database
create database ele;
use ele;

Tables (signup, newcustomer, transaction) will be auto-created when you run the script.

### 4️⃣ Run the Project
python electricity_billing.py

---

### 📊 Graph Menu (New!)

When logged in, users can view multiple graph options:
- 📈 Bill Trend (Line Graph)
- 📊 Units vs Amount (Bar Chart)
- 🥧 Payment Status (Pie Chart)

---

<p align="center"> <img src="screenshots/graph_trend.png" width="400"/> <img src="screenshots/graph_bar.png" width="400"/> <img src="screenshots/graph_pie.png" width="400"/> </p>
### 🛠️ Tech Stack
<p align="left"> <img src="https://skillicons.dev/icons?i=python,mysql,git" height="40" /> </p>

---

### 🚀 Future Improvements
- 🔐 Encrypt user passwords (hashing)
- 👨‍💼 Admin dashboard with multiple customer analytics
- 🌐 Web-based UI with Flask/Django

---

### 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss.

### 📜 License
This project is licensed under the MIT License.

<p align="center">⭐ If you like this project, give it a star on GitHub! ⭐</p> ```
