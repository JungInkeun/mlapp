from django.shortcuts import render
from excel_upload.forms import ExcelUploadForm
from excel_upload.models import BikeDataExcel
from excel_upload.utils import predict_bike_count
import pandas as pd

# Create your views here.
def upload_page(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            df = pd.read_excel(excel_file)  # 엑셀 파일을 pandas DataFrame으로 읽기

            # DataFrame의 내용을 모델에 저장하거나 계산에 활용
            for index, row in df.iterrows():
                season = row['season']
                workingday = row['workingday']
                weather = row['weather']
                month = row['month']
                
                print(season, workingday, weather, month)
            # BikeData 모델에 저장하거나 계산 수행
            instance = BikeDataExcel(season=season, workingday=workingday, weather=weather, month=month)
            instance.save()
            
            if instance.predict_count:
                predict_count = instance.predict_count
                print(predict_count)
            else:
                predict_count = "^^"
                
            return render(request, "upload/upload.html", {"form":form, "predict_count":predict_count})
    else:
        form = ExcelUploadForm()

    context = {"form":form}

    return render(request, 'upload/upload.html', context)