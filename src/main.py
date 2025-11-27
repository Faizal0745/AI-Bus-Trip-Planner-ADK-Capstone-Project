from config import API_KEY, DATA_PATH
import json

def load_data():
    with open(DATA_PATH) as f:
        return json.load(f)

def plan_trip(source, destination):
    return {"status": "success", "message": "Planning logic will be added with Gemini API"}

if __name__ == "__main__":
    print("AI Bus Trip Planner is ready.")
