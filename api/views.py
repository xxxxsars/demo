from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from pkg.common import *
from api.models import Predict_log
from api.serializers import PredictLogSerializer


# Create your views here.
@api_view(["POST"])
def save_image(request):
    resp_json = {"message": "", "image": "", "result": ""}

    if request.method == "POST":
        base64_img = request.data.get("image")
        product_id = request.data.get("product_id")

        try:
            img_np = base64_to_np(base64_img)
            gray_img = Image.fromarray(cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)).convert("L")
            gray_base64_img = img_to_base64(gray_img).decode("utf-8")

            if Predict_log.objects.filter(production_id=product_id).exists():
                raise ValueError("Your production id has been existed.")

            Predict_log.objects.create(production_id=product_id,
                                       raw_image=base64_img,
                                       gray_image=gray_base64_img)

        except Exception as e:
            resp_json["message"] = f"Saving image had error:{e}"
            resp_json["result"] = "failure"
            return JsonResponse(resp_json, status=417)

        resp_json["message"] = f"Saving image successfully."
        resp_json["result"] = "success"
        resp_json["image"] = gray_base64_img
        return JsonResponse(resp_json, status=200)


class PredictLogViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Predict_log.objects.all()
        serializer = PredictLogSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Predict_log.objects.all()
        log = get_object_or_404(queryset, pk=pk)
        serializer = PredictLogSerializer(log)
        return Response(serializer.data)
