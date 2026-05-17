import cv2
from ultralytics import YOLO

model = YOLO(r"F:\Programacao\FruitDetecter\models\best.pt")
cap = cv2.VideoCapture(0)

nutrition = {
    "Apple": {"calorias": 52},
    "Banana": {"calorias": 89},
    "Grape": {"calorias": 69},
    "Orange": {"calorias": 47},
    "Pineapple": {"calorias": 50},
    "Watermelon": {"calorias": 30}
}

info = {
    "Apple": "Vitamina C | Fibras",
    "Banana": "Potassio | Energia",
    "Grape": "Antioxidantes",
    "Orange": "Vitamina C",
    "Pineapple": "Digestao",
    "Watermelon": "Hidratacao"
}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.5)

    total_calorias = 0

    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        conf = float(box.conf[0])

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        # 🔥 cor por classe (mais bonito)
        color = (0, 255, 0)

        # caixa
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

        # ==========================
        # TEXTO PRINCIPAL
        # ==========================
        title = f"{label} {conf:.2f}"

        cv2.putText(frame, title,
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, color, 2)

        # ==========================
        # INFO EXTRA (ABAIXO)
        # ==========================
        desc = info.get(label, "")
        kcal = nutrition.get(label, {}).get("calorias", 0)

        y_text = y2 + 20

        cv2.putText(frame, desc,
                    (x1, y_text),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (200,200,200), 1)

        y_text += 18

        cv2.putText(frame, f"{kcal} kcal",
                    (x1, y_text),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0,165,255), 2)

        total_calorias += kcal

    # ==========================
    # HUD TOTAL (TOPO)
    # ==========================
    cv2.rectangle(frame, (0, 0), (300, 60), (0,0,0), -1)

    cv2.putText(frame,
                f"TOTAL: {total_calorias} kcal",
                (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0,0,255),
                3)

    cv2.imshow("AI Nutrition 🍎", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()