import torch


# 将 COCO 格式转换为张量格式
def coco_to_tensor(coco_preds):
    tensor_preds = []
    for pred in coco_preds:
        x, y, w, h = pred['bbox']
        x1 = x
        y1 = y
        x2 = x + w
        y2 = y + h
        score = pred['score']
        class_id = pred['category_id']
        tensor_preds.append([x1, y1, x2, y2, score, class_id])
    return torch.tensor(tensor_preds)