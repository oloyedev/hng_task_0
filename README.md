

---

````markdown
# 🧠 Backend Wizards — HNG Stage 0 Task

Welcome to my submission for the **HNG Internship Stage 0 Task**, titled **“Dynamic Profile Endpoint with External API Integration.”**  
This project demonstrates the ability to **consume third-party APIs**, **structure clean JSON responses**, and **return dynamic data** using **FastAPI** — a modern, high-performance Python web framework.

---

## 🧩 Overview

The task requires building a single **GET** endpoint `/me` that returns:
- The developer’s **profile information** (name, email, stack)
- A dynamically fetched **cat fact** from an external API
- A **timestamp** that updates in real time
- A **status message** indicating success or failure

The endpoint is powered by the [Cat Facts API](https://catfact.ninja/fact) and hosted on [Railway.app](https://railway.app).

---

## 🎯 Objectives

- ✅ Build a **RESTful API** with FastAPI  
- ✅ Integrate an **external API (Cat Facts)** dynamically  
- ✅ Implement **real-time timestamps (UTC, ISO 8601 format)**  
- ✅ Handle **errors and external API downtime gracefully**  
- ✅ Deploy the project on a **live server (Railway)**  
- ✅ Document setup, configuration, and testing clearly  

---

## ⚙️ Core Functionality

### 🔹 Primary Endpoint
| Method | Endpoint | Description |
|---------|-----------|-------------|
| GET | `/api/me` | Returns the user's profile data, timestamp, and a random cat fact |

### 🔹 Expected JSON Response (on success)
```json
{
  "status": "success",
  "user": {
    "email": "oloyeadz@gmail.com",
    "name": "Olayide Olatunji",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-17T01:14:20.256298Z",
  "fact": "Researchers are unsure exactly how a cat purrs. Most veterinarians believe that a cat purrs by vibrating vocal folds deep in the throat."
}
````

---

## ⚠️ Error Handling

The API includes smart error handling to ensure stability:

| Scenario                  | Response Status | Message                                                   |
| ------------------------- | --------------- | --------------------------------------------------------- |
| External Cat API is down  | `failed`        | `"Sorry, Cat API is not live right now."`                 |
| Unexpected internal error | `failed`        | `"An unexpected error occurred while fetching cat fact."` |

### Example:

```json
{
  "status": "failed",
  "user": {
    "email": "oloyeadz@gmail.com",
    "name": "Olayide Olatunji",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-17T01:14:20.256298Z",
  "error": "Sorry, Cat API is not live right now."
}
```

---

## 🏗️ Project Structure

```
hng_task_0/
│
├── app/
│   ├── __init__.py          # Makes app a Python package
│   ├── main.py              # Application entry point
│   ├── config.py            # Loads environment variables
│   ├── schema.py            # Defines response data models
│   ├── services.py          # Handles external API call logic
│   └── routes/
│       └── profile.py       # Defines /me route
│
├── .env                     # Local environment variables
├── .env.example             # Template for environment setup
├── requirements.txt          # All dependencies
└── README.md
```

---

## 🌍 Environment Variables

Before running, create a `.env` file in your project root with:

```bash
APP_NAME=Backend Wizards Profile API
ENVIRONMENT=production
CAT_API_URL=https://catfact.ninja/fact
REQUEST_TIMEOUT=5
USER_EMAIL=oloyeadz@gmail.com
USER_NAME=Olayide Olatunji
USER_STACK=Python/FastAPI
```

> You may copy `.env.example` and rename it to `.env` for easier configuration.

---

## ⚙️ Installation and Setup

### Step 1. Clone the Repository

```bash
git clone https://github.com/oloyedev/hng_task_0.git
cd hng_task_0
```

### Step 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### Step 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4. Run the Application

```bash
uvicorn app.main:app --reload
```

Then visit:
👉 [http://127.0.0.1:8000/api/me](http://127.0.0.1:8000/api/me)

---

## 🧪 Testing the Endpoint

You can test using **Postman**, **cURL**, or directly from your browser.

### Example with `curl`

```bash
curl -X GET http://127.0.0.1:8000/api/me
```

### Postman Setup

* **Method:** `GET`
* **URL:** `https://your-railway-app-name.up.railway.app/api/me`
* **Headers:**

  * `Content-Type: application/json`
* **Response:** Returns your profile and a dynamic cat fact.

---

## 🌐 Deployment

This API is deployed on **Railway.app**, which automatically detects Python environments and builds using `Uvicorn`.

### Deployment Notes

* Railway uses `Procfile` or "Start Command" for boot.
* Start command:

  ```bash
  uvicorn app.main:app --host 0.0.0.0 --port $PORT
  ```
* You can monitor logs, CPU usage, and memory directly from the Railway dashboard.

### Live API Example

> 🔗 [Railway](https://hngtask0-production-0897.up.railway.app/me)
> *(Replace with your actual generated domain name)*

---


---

## 🧠 Best Practices Implemented

* Configurations handled securely via `.env` file.
* Modular design with **services**, **routes**, and **schemas**.
* Clean and consistent API responses with Pydantic validation.
* Resilient handling of network and timeout issues.
* Production-ready structure for scaling and CI/CD integration.

---

## 🧑‍💻 Author

**👤 Olayide Olatunji**
📧 [oloyeadz@gmail.com](mailto:oloyeadz@gmail.com)
💻 [GitHub: oloyedev](https://github.com/oloyedev)
🐦 [Twitter: @oloyide_](https://x.com/aonnelson)

---

## 🐾 Final Thoughts

This project reflects how a simple REST endpoint can demonstrate:

* Practical **API consumption**
* **Error tolerance**
* **Clean response modeling**
* And **production deployment discipline**

> 🚀 It’s not just about getting a cat fact — it’s about building APIs that stay reliable when the world (or the cat) takes a nap. 😺

---

```


