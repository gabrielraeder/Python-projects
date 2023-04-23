echo "Installing virtual environment..."
python3 -m venv .venv

echo "activating virtual environment..."
source .venv/bin/activate

echo "Installing dependencies..."
python3 -m pip install -r dev-requirements.txt

echo "Starting mongodb container..."
docker-compose up -d

echo "Starting application..."
cd src && uvicorn main:app --reload