from flask import Flask, render_template, request, redirect, url_for, session, flash
import time
import sys
import os
# Import database modules only if available
try:
    import mysql.connector
    import matplotlib.pyplot as plt
    from werkzeug.security import generate_password_hash, check_password_hash
    DATABASE_AVAILABLE = True
except ImportError:
    DATABASE_AVAILABLE = False

app = Flask(__name__)
app.secret_key = 'ebillingsystem_secret_key'

# Database connection - only used if database modules are available
def get_db_connection():
    if not DATABASE_AVAILABLE:
        return None
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Update with your MySQL password
            database="EBS"
        )
        return conn
    except:
        return None

# Initialize database and tables - only used if database modules are available
def initialize_database():
    if not DATABASE_AVAILABLE:
        print("Database modules not available. Running in demo mode.")
        return
    
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""  # Update with your MySQL password
        )
        cursor = conn.cursor()
        
        # Create database if not exists
        cursor.execute("CREATE DATABASE IF NOT EXISTS EBS;")
        conn.commit()
        
        # Connect to the EBS database
        conn.database = "EBS"
        
        # Create tables
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS newcustomer
        (Accountno INT NOT NULL PRIMARY KEY,
        Bankname VARCHAR(35),
        Name VARCHAR(35),
        Address VARCHAR(100),
        contact INT NOT NULL)
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS signup
        (username VARCHAR(35) PRIMARY KEY,
        _pass VARCHAR(100),
        confirmpass VARCHAR(100))
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS transaction
        (accountno INT,
        unit INT,
        todays VARCHAR(25),
        amtwithoutvat INT,
        vat FLOAT(12,2),
        amtwithvat INT,
        PAID VARCHAR(25),
        FOREIGN KEY(accountno) REFERENCES newcustomer(accountno))
        """)
        
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Database initialization error: {e}")
        print("Running in demo mode.")

# Initialize database when app starts
with app.app_context():
    initialize_database()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if not DATABASE_AVAILABLE:
            # Demo mode - accept any login
            session['logged_in'] = True
            session['username'] = username
            flash('Demo mode: Login successful')
            return redirect(url_for('dashboard'))
        
        conn = get_db_connection()
        if conn is None:
            # Demo mode - accept any login
            session['logged_in'] = True
            session['username'] = username
            flash('Demo mode: Login successful')
            return redirect(url_for('dashboard'))
            
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM signup WHERE username = %s", (username,))
            user = cursor.fetchone()
            
            if user and user['_pass'] == password:  # In a real app, use check_password_hash
                session['logged_in'] = True
                session['username'] = username
                flash('Login successful')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid username or password')
                return redirect(url_for('login'))
            cursor.close()
        except Exception as e:
            flash(f'Error: {e}. Using demo mode.')
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('dashboard'))
        finally:
            if conn:
                conn.close()
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if password != confirm_password:
            flash('Passwords do not match')
            return redirect(url_for('signup'))
        
        if not DATABASE_AVAILABLE:
            # Demo mode - accept any signup
            flash('Demo mode: Account created successfully')
            return redirect(url_for('login'))
        
        conn = get_db_connection()
        if not conn:
            flash('Database connection error. Using demo mode.')
            flash('Demo mode: Account created successfully')
            return redirect(url_for('login'))
            
        cursor = conn.cursor()
        
        try:
            cursor.execute("INSERT INTO signup VALUES (%s, %s, %s)", 
                          (username, password, confirm_password))  # In a real app, hash the password
            conn.commit()
            flash('Account created successfully')
            return redirect(url_for('login'))
        except Exception as err:
            flash(f'Error: {err}. Using demo mode.')
            flash('Demo mode: Account created successfully')
            return redirect(url_for('login'))
        finally:
            cursor.close()
            conn.close()
    
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    return render_template('dashboard.html')

@app.route('/new_customer', methods=['GET', 'POST'])
def new_customer():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        account_no = request.form['account_no']
        bank_name = request.form['bank_name']
        name = request.form['name']
        address = request.form['address']
        contact = request.form['contact']
        
        conn = get_db_connection()
        if conn is None:
            # In demo mode, just show success message without database operations
            flash('Demo Mode: Customer would be added in normal operation')
            return redirect(url_for('dashboard'))
        
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO newcustomer VALUES (%s, %s, %s, %s, %s)", 
                          (account_no, bank_name, name, address, contact))
            conn.commit()
            cursor.close()
            flash('Customer added successfully')
            return redirect(url_for('dashboard'))
        except Exception as err:
            flash(f'Error: {err}')
        finally:
            if conn:
                conn.close()
    
    return render_template('new_customer.html')

@app.route('/delete_customer', methods=['GET', 'POST'])
def delete_customer():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        account_no = request.form['account_no']
        
        conn = get_db_connection()
        if conn is None:
            # In demo mode, just show success message without database operations
            flash('Demo Mode: Customer would be deleted in normal operation')
            return redirect(url_for('dashboard'))
        
        try:
            cursor = conn.cursor()
            # First delete related transactions
            cursor.execute("DELETE FROM transaction WHERE accountno = %s", (account_no,))
            # Then delete the customer
            cursor.execute("DELETE FROM newcustomer WHERE Accountno = %s", (account_no,))
            conn.commit()
            cursor.close()
            flash('Customer deleted successfully')
            return redirect(url_for('dashboard'))
        except Exception as err:
            flash(f'Error: {err}')
        finally:
            if conn:
                conn.close()
    
    return render_template('delete_customer.html')

@app.route('/transaction', methods=['GET', 'POST'])
def transaction():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        account_no = request.form['account_no']
        unit = request.form['unit']
        date = request.form['date']
        
        # Calculate amounts
        amt_without_vat = int(unit) * 10  # Assuming rate is 10
        vat = amt_without_vat * 0.05  # 5% VAT
        amt_with_vat = amt_without_vat + vat
        paid = request.form.get('paid', 'No')
        
        conn = get_db_connection()
        if conn is None:
            # In demo mode, just show success message without database operations
            flash('Demo Mode: Transaction would be recorded in normal operation')
            return redirect(url_for('dashboard'))
        
        try:
            cursor = conn.cursor()
            # Check if account exists
            cursor.execute("SELECT * FROM newcustomer WHERE Accountno = %s", (account_no,))
            if cursor.fetchone():
                cursor.execute("INSERT INTO transaction VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                              (account_no, unit, date, amt_without_vat, vat, amt_with_vat, paid))
                conn.commit()
                flash('Transaction recorded successfully')
                return redirect(url_for('dashboard'))
            else:
                flash('Account number does not exist')
            cursor.close()
        except Exception as err:
            flash(f'Error: {err}')
        finally:
            if conn:
                conn.close()
    
    return render_template('transaction.html')

@app.route('/view_customer_details', methods=['GET', 'POST'])
def view_customer_details():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    customers = []
    transactions = []
    search_attempted = False
    
    if request.method == 'POST':
        account_no = request.form.get('account_no')
        search_attempted = True
        
        conn = get_db_connection()
        if conn is None:
            # In demo mode, provide sample data
            if account_no:
                flash('Demo Mode: Showing sample customer data')
                customers = [
                    {'Accountno': account_no, 'Bankname': 'Sample Bank', 'Name': 'Demo Customer', 
                     'Address': '123 Demo Street', 'Contact': '555-1234'}
                ]
                transactions = [
                    {'accountno': account_no, 'unit': 100, 'todays': '2023-01-01', 
                     'amtwithoutVAT': 1000, 'vat': 50, 'amtwithvat': 1050, 'paid': 'Yes'}
                ]
            else:
                # Show multiple sample customers for "View All"
                customers = [
                    {'Accountno': '1001', 'Bankname': 'Sample Bank', 'Name': 'Demo Customer 1', 
                     'Address': '123 Demo Street', 'Contact': '555-1234'},
                    {'Accountno': '1002', 'Bankname': 'Test Bank', 'Name': 'Demo Customer 2', 
                     'Address': '456 Test Avenue', 'Contact': '555-5678'}
                ]
            return render_template('view_customer_details.html', customers=customers, 
                                  transactions=transactions, search_attempted=search_attempted)
        
        try:
            cursor = conn.cursor(dictionary=True)
            if account_no:
                # Get specific customer
                cursor.execute("SELECT * FROM newcustomer WHERE Accountno = %s", (account_no,))
                customers = cursor.fetchall()
                
                # Get their transactions
                cursor.execute("SELECT * FROM transaction WHERE accountno = %s", (account_no,))
                transactions = cursor.fetchall()
            else:
                # Get all customers
                cursor.execute("SELECT * FROM newcustomer")
                customers = cursor.fetchall()
            cursor.close()
        except Exception as err:
            flash(f'Error: {err}')
        finally:
            if conn:
                conn.close()
    
    return render_template('view_customer_details.html', customers=customers, 
                          transactions=transactions, search_attempted=search_attempted)

@app.route('/graph/<int:account_no>')
def graph(account_no):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT unit, amtwithvat, todays FROM transaction WHERE accountno = %s", (account_no,))
        data = cursor.fetchall()
        
        if data:
            # Create graph directory if it doesn't exist
            graph_dir = os.path.join(app.static_folder, 'graphs')
            os.makedirs(graph_dir, exist_ok=True)
            
            # Create graph
            dates = [row['todays'] for row in data]
            units = [row['unit'] for row in data]
            amounts = [row['amtwithvat'] for row in data]
            
            plt.figure(figsize=(10, 6))
            
            plt.subplot(2, 1, 1)
            plt.bar(dates, units, color='blue')
            plt.title(f'Units Consumed by Account {account_no}')
            plt.xlabel('Date')
            plt.ylabel('Units')
            plt.xticks(rotation=45)
            
            plt.subplot(2, 1, 2)
            plt.bar(dates, amounts, color='green')
            plt.title(f'Amount Paid by Account {account_no}')
            plt.xlabel('Date')
            plt.ylabel('Amount (with VAT)')
            plt.xticks(rotation=45)
            
            plt.tight_layout()
            
            # Save the graph
            graph_path = os.path.join(graph_dir, f'account_{account_no}.png')
            plt.savefig(graph_path)
            
            return render_template('graph.html', account_no=account_no, graph_file=f'graphs/account_{account_no}.png')
        else:
            flash('No transaction data found for this account')
            return redirect(url_for('view_customer_details'))
    except mysql.connector.Error as err:
        flash(f'Error: {err}')
        return redirect(url_for('view_customer_details'))
    finally:
        cursor.close()
        conn.close()

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)