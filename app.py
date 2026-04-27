from flask import Flask, render_template, jsonify
import pymysql
from config import Config

app = Flask(__name__)


def get_db_connection():
    connection = pymysql.connect(
        host=config.MYSQL_HOST,
        user=config.MYSQL_USER,
        password=config.MYSQL_PASSWORD,
        database=config.MYSQL_DB,
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection


@app.route("/")
@app.route("/dashboard")
def dashboard():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) as count FROM film")
            film_count = cursor.fetchone()
            cursor.execute("SELECT COUNT(*) as count FROM actor")
            actor_count = cursor.fetchone()
            cursor.execute("SELECT COUNT(*) as count FROM customer")
            customer_count = cursor.fetchone()
            cursor.execute("SELECT COUNT(*) as count FROM rental")
            rental_count = cursor.fetchone()
        conn.close()
        return render_template(
            "dashboard.html",
            film_count=film_count["count"],
            actor_count=actor_count["count"],
            customer_count=customer_count["count"],
            rental_count=rental_count["count"],
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/health")
def health():
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify({"status": "healthy"}), 200
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500


@app.route("/films")
def films():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT film_id, title, description, release_year FROM film LIMIT 50"
        )
        films = cursor.fetchall()
    conn.close()
    return render_template("films.html", films=films)


@app.route("/actors")
def actors():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT actor_id, first_name, last_name FROM actor")
        actors = cursor.fetchall()
    conn.close()
    return render_template("actors.html", actors=actors)


@app.route("/customers")
def customers():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT customer_id, first_name, last_name, email FROM customer LIMIT 50"
        )
        customers = cursor.fetchall()
    conn.close()
    return render_template("customers.html", customers=customers)


@app.route("/rentals")
def rentals():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT rental_id, rental_date, customer_id, inventory_id FROM rental LIMIT 50"
        )
        rentals = cursor.fetchall()
    conn.close()
    return render_template("rentals.html", rentals=rentals)


@app.route("/staff")
def staff():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT staff_id, first_name, last_name, email FROM staff")
        staff = cursor.fetchall()
    conn.close()
    return render_template("staff.html", staff=staff)


@app.route("/inventory")
def inventory():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT inventory_id, film_id, store_id FROM inventory LIMIT 50")
        inventory = cursor.fetchall()
    conn.close()
    return render_template("inventory.html", inventory=inventory)


@app.route("/stores")
def stores():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT store_id, manager_staff_id, address_id FROM store")
        stores = cursor.fetchall()
    conn.close()
    return render_template("stores.html", stores=stores)


@app.route("/reports")
def reports():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT category.name, COUNT(film.film_id) as count FROM film JOIN film_category ON film.film_id = film_category.film_id JOIN category ON film_category.category_id = category.category_id GROUP BY category.name"
        )
        categories = cursor.fetchall()
    conn.close()
    return render_template("reports.html", categories=categories)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
