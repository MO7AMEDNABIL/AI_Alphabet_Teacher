import cv2
import time
from ultralytics import YOLO
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = YOLO("best.pt")

@app.route('/detect', methods=['GET', 'POST'])
def detect():
    
    backends = [cv2.CAP_DSHOW, cv2.CAP_ANY, cv2.CAP_MSMF]
    cap = None
    
    for backend in backends:
        cap = cv2.VideoCapture(0, backend)
        if cap.isOpened():
            ret, test_frame = cap.read()
            if ret:
                print(f"Using camera backend: {backend}")
                break
            cap.release()
    
    if not cap or not cap.isOpened():
        return jsonify({"error": "Cannot access camera", "detected_letter": None})
    
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)
    
    
    cv2.namedWindow('Letter Detection Camera', cv2.WINDOW_AUTOSIZE)
    
    best_letter = None
    best_confidence = 0
    start_time = time.time()
    
    print("Camera window opened - show a letter to the camera!")
    print("Press 'q' to quit early")
    
    
    while time.time() - start_time < 5:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame, retrying...")
            time.sleep(0.1)
            continue
            
        
        cv2.imshow('Letter Detection Camera', frame)
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
        results = model.predict(frame, conf=0.8, verbose=False)
        
        if len(results[0].boxes) > 0:
            for box in results[0].boxes:
                letter = model.names[int(box.cls[0])]
                confidence = float(box.conf[0])
                
                
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f'{letter} {confidence:.2f}', (x1, y1-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                
                if confidence > best_confidence:
                    best_confidence = confidence
                    best_letter = letter
                    print(f"Found: {letter} (confidence: {confidence:.2f})")
                
                
                if confidence > 0.85:
                    # Keep window open for 2 more seconds to show result
                    end_time = time.time() + 2
                    while time.time() < end_time:
                        cv2.imshow('Letter Detection Camera', frame)
                        cv2.waitKey(30)
                    
                    cv2.destroyAllWindows()
                    cap.release()
                    return jsonify({
                        "detected_letter": letter,
                        "confidence": confidence
                    })
    
    cv2.destroyAllWindows()
    cap.release()
    
    if best_letter:
        return jsonify({
            "detected_letter": best_letter,
            "confidence": best_confidence
        })
    else:
        return jsonify({
            "detected_letter": None,
            "error": "No letter found"
        })

if __name__ == '__main__':
    print("Starting YOLO server on http://127.0.0.1:5001")
    app.run(host='0.0.0.0', port=5001, debug=True)