from django import forms
from excel_upload.models import BikeDataExcel

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField(label="엑셀파일 업로드")
    