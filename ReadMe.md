## Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/Additions-Intelligence/adi_lightweight.git
cd adi_lightweight
```

### 2. Create & Activate Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```


### 4. Run the Application
From the root directory (project):
```sh
uvicorn app.main:app --reload
```

The application will run at **`http://127.0.0.1:8000/docs`**


Additional Intelligence App APIs **`http://127.0.0.1:8000/docs`**

---
