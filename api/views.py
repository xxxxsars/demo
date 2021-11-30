from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pkg.common import *


# Create your views here.
@api_view(["POST"])
def save_image(request):
    resp_json = {"message": "", "image": "", "result": ""}

    if request.method == "POST":
        base64_img = request.data.get("image")
        product_id = request.data.get("product_id")

        try:
            # TODO save to db
            img_np = base64_to_np(base64_img)
            gray_img = Image.fromarray(cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)).convert("L")
            gray_base64_img = img_to_base64(gray_img).decode("utf-8")

        except Exception as e:
            resp_json["message"] = f"Saving image had error:{e}"
            resp_json["result"] = "failure"
            return JsonResponse(resp_json, status=417)

        resp_json["message"] = f"Saving image successfully."
        resp_json["result"] = "success"
        resp_json["image"] = gray_base64_img
        return JsonResponse(resp_json, status=200)
